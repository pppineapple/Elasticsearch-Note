
import json
import requests

# 创建非结构化索引
esurl = "http://localhost:9200/"
headers = {"Content-Type": "application/json"}
index_name = "haoke/"
data = {
    "settings": {
        "index": {
            "number_of_shards": "2",
            "number_of_replicas": "0"
        }
    }
}
response = requests.post(esurl+index_name, json=data, headers=headers)

