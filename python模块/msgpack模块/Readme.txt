小数据的情况下，JSON在低端CPU上性能表现不佳，在高端CPU上的表现跟msgpack接近。
大数据的情况下，msgpack的性能比JSON快5-6倍。
PS. 如果是涉及大量序列化运算的应用，建议选择高频的CPU。

参考链接:
http://rfyiamcool.blog.51cto.com/1030776/1303868/
