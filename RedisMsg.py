# -*- coding:utf-8 -*-

import redis

redis_url = 'redis://auth:@127.0.0.1:6379'
pool = redis.ConnectionPool.from_url(redis_url)


class RedisMsg:

    def __init__(self, channel='test'):
        self.__conn = redis.Redis(connection_pool=pool)
        self.__channel = channel

    def put_msg(self, msg='test-msg'):
        """
        向指定频道发送msg
        :param msg:
        :return: int
        """
        get_number = self.__conn.publish(self.__channel, msg)
        return get_number

    def get_msg(self):
        """
        订阅获取消息-堵塞式
        :return:
        """
        pub = self.__conn.pubsub()
        pub.subscribe(self.__channel)
        while True:
            try:
                msg = pub.parse_response(block=False, timeout=12)   # 非堵塞
                self.callback(msg)
            except KeyboardInterrupt:
                break

    def callback(self, msg):
        if not msg:
            return
        msg = msg[2]
        if isinstance(msg, bytes):
            msg = msg.decode()
        print(msg)


if __name__ == '__main__':
    test = RedisMsg()
    test.put_msg()
    test.get_msg()




