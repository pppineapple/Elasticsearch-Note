
import requests

# 创建非结构化索引
esurl = "http://localhost:9200/"
headers = {"Content-Type": "application/json"}


query_body = {
    "settings": {
        "index": {
            "number_of_shards": "2",
            "number_of_replicas": "0"
        }
    }
}


indexname_list = ["test_2019.12.{0:0>2d}".format(i) for i in range(1, 32)]
for indexname in indexname_list:
    index_exists_res = requests.head(esurl+indexname)
    if index_exists_res.status_code == 200:
        print "index {0} has been created".format(indexname)
    else:
        index_create_res = requests.put(esurl+indexname, json=query_body, headers=headers)
        if index_create_res.status_code == 200:
            print "index {0} created successfully".format(indexname)
        else:
            print "index {0} created unsuccessfully".format(indexname)