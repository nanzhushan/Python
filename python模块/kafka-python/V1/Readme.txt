两个模块都可以:

http://kafka-python.readthedocs.io/en/latest/usage.html#kafkaproducer

http://orchome.com/6

序列化使用msgpack：

pip install msgpack-python


(2)消费者查看命令:
[root@localhost kafka_2.11-0.9.0.0]# bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic my-topic --from-beginning


(3)RocketMQ 与 Kafka对比
https://github.com/alibaba/RocketMQ/wiki/rmq_vs_kafka
