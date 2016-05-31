import uuid
    from pymongo import MongoClient

    #两地址
    CONN_ADDR1 = 'demotest-1.mongodb.tbc3.newtest.rdstest.aliyun-inc.com:27017'
    CONN_ADDR2 = 'demotest-2.mongodb.tbc3.newtest.rdstest.aliyun-inc.com:27017'
    REPLICAT_SET = 'mgset-1441984463'

    username = 'demouser'
    password = '123456'


    #获取mongoclient
    client = MongoClient([CONN_ADDR1, CONN_ADDR2], replicaSet=REPLICAT_SET)

    #授权. 这里的user基于admin数据库授权
    client.admin.authenticate(username, password)

    #使用test数据库的collection:testColl做例子, 插入doc, 然后根据DEMO名查找
    demo_name = 'python-' + str(uuid.uuid1())
    print 'demo_name:', demo_name
    doc = dict(DEMO=demo_name, MESG="Hello AliCloudDB For MongoDB")
    doc_id = client.test.testColl.insert(doc)
    print 'doc_id:', doc_id

    for d in client.test.testColl.find(dict(DEMO=demo_name)):
        print 'find documents:', d