#coding:utf8
#可以通过 “bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic my-topic --from-beginning”
#查看消费者信息

from kafka import KafkaProducer
from kafka.errors import KafkaError
import msgpack
import json

producer = KafkaProducer(bootstrap_servers=['192.168.2.101:9092'])
future = producer.send('my-topic', b'knight')   ##创建my-topic(就是一个topic),并发送信息
record_metadata = future.get(timeout=10)



# producer.send('my-topic', key=b'foo', value=b'bar1144331')
# producer = KafkaProducer(value_serializer=msgpack.dumps)
# producer.send('msgpack-topic', {'key': 'value'})
# producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
# for _ in range(100):
#     producer.send('my-topic', b'msg')
# producer.flush()
# producer = KafkaProducer(retries=5)