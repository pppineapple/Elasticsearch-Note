## ElasticSearch API 

### ElasticSearch API CURD操作
#### 索引初始化


```
# 给索引index_init设置分片数量和副本数量
curl -H 'Content-Type: application/json' -XPUT 'http://10.211.55.4:9200/index_init/' -d '{
	"settings":{
		"index":{
			"number_of_shards":5,
			"number_of_replicas":1
		}
	}
}'
# 返回信息
{"acknowledged":true,"shards_acknowledged":true,"index":"index_init"}
```

注：还有许多设置项：

* blocks.read_only : true  表示只读
* blocks.read : true       表示禁止读操作
* blocks.write : true      表示禁止写操作
* blocks.metadata : true   表示禁止对metadata操作

```
# 可以通过get假设带参数的_settings来获取索引的所有配置信息。
curl -get 'http://10.211.55.4:9200/index_init/_settings'
# 返回信息
{"index_init":{"settings":{"index":{"creation_date":"1575199420204","number_of_shards":"5","number_of_replicas":"1","uuid":"6AbwOwewSci2l3htMeMhgg","version":{"created":"6050499"},"provided_name":"index_init"}}}}
```

注：

* 获取所有索引配置: `curl -get 'http://10.211.55.4:9200/_all/_settings`
* 获取多个索引配置: `curl -get 'http://10.211.55.4:9200/index_init,index1/_settings'`

#### 创建索引

```
# 创建索引 index_create，并且插入一条数据
curl -H 'Content-Type: application/json' -XPUT 'http://10.211.55.4:9200/index_create/_doc' -d '{
	"title": "elasticsearch the definitive guide",
	"author": {
		"first": "clinton gormley",
		"second": "zachary tong"
	},
	"publish_date": "2015-04-19",
	"price": "39.99"
}'
# 返回信息
{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```

#### 查找文档内容
```
# 通过文档的_id属性查找文档
curl -H 'Content-Type: application/json' -XGET 'http://10.211.55.4:9200/index_create/_doc/JYhNwW4BAbgFEXME8uv_'
# 返回信息
{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":1,"found":true,"_source":{"title": "elasticsearch the definitive guide","author": {"first": "clinton gormley","second": "zachary tong"},"publish_date": "2015-04-19","price": "39.99"}}

# 通过_source获取指定字段
curl -H 'Content-Type: application/json' -XGET 'http://10.211.55.4:9200/index_create/_doc/JYhNwW4BAbgFEXME8uv_/?_source=title,price'
# 返回信息
{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":1,"found":true,"_source":{"price":"39.99","title":"elasticsearch the definitive guide"}}
```

#### 更新文档内容

```
# 通过文档_id覆盖更新
curl -H 'Content-Type: application/json' -XPUT 'http://10.211.55.4:9200/index_create/_doc/JYhNwW4BAbgFEXME8uv_' -d '{
	"title": "elasticsearch the definitive guide",
	"author": {
		"first": "clinton gormley",
		"second": "zachary tong"
	},
	"publish_date": "2015-04-19",
	"price": "59.99"
}'
# 返回信息，此处的version值变为2
{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":2,"result":"updated","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1}

# 通过_update API单独更新你想要更新的字段
curl -H 'Content-Type: application/json' -XPOST 'http://10.211.55.4:9200/index_create/_doc/JYhNwW4BAbgFEXME8uv_/_update' -d '{
	"doc": {
		"price": "39.99"
	}
	
}'
# 返回信息，此处已经是第三次修改了，version值为3
{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":3,"result":"updated","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":2,"_primary_term":1}
```

#### 删除文档

```
# 通过_id删除索引中指定的文档
curl -H 'Content-Type: application/json' -XDELETE 'http://10.211.55.4:9200/index_create/_doc/JYhNwW4BAbgFEXME8uv_/'

# 返回信息{"_index":"index_create","_type":"_doc","_id":"JYhNwW4BAbgFEXME8uv_","_version":4,"result":"deleted","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":3,"_primary_term":1}
```

#### 删除索引

```
curl -H 'Content-Type: application/json' -XDELETE 'http://10.211.55.4:9200/index_create'
# 返回信息
{"acknowledged":true}
```