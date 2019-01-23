# RedisMsg
redis订阅功能的示例，基于此设计分布式系统
### 参考文档
https://www.cnblogs.com/anpengapple/p/7027979.html<p>
https://segmentfault.com/a/1190000016898228
### 订阅多个频道
```python
pub.subscribe(str)
# 改为
pub.psubscribe([])
```
### 消息订阅的两种方式
方式一使用发布订阅对象的parse_response()方法获取订阅信息<p>
方式二使用发布订阅对象的listen()方法获取订阅信息<p>
listen()方法是对parse_response()方法的封装，加入了阻塞<p>
并将parse_response()返回的结果进行了处理，使结果更加简单。

心跳问题还需解决，在实际运行中再处理

