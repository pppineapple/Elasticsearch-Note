# Elasticsearch API
在实际的工作中，通常都是使用基于HTTP协议，以JSON为数据交互格式RESTful API，与Elasticsearch进行通信。所以对于python来说，可以使用request库来低啊用ES的API，实现你想要的操作。

* ES官网的API文档目录 [REST APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)
* ES官网的Index相关API文档 [Index APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)

目前，该代码库中保存的是我自己编写的需要用到脚本示例:

|script name| purpose |
|----|-----|
|[RESTfulAPI.py](https://github.com/pppineapple/Elasticsearch-Note/blob/master/RESTfulAPI/DeleteIndex.py)| A simple demo
|[CreatedIndex.py](https://github.com/pppineapple/Elasticsearch-Note/blob/master/RESTfulAPI/CreateIndex.py)| Creating index if not existed
|[DeleteIndex.py](https://github.com/pppineapple/Elasticsearch-Note/blob/master/RESTfulAPI/DeleteIndex.py)| Deleting index a week ago by customized keyword