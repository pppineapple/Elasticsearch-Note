## ES倒排索引

>倒排索引 Inverted index 用来存储在全文搜索下某个单词在一个文档或者一组文档中的存储位置的映射，它是文档检索系统中最常用的数据结构

常规索引：文档 -> 关键词
倒排索引：关键词 -> 文档位置

假设两个文档的内容是：<br>
1. The quick brown fox jumped over the lazy dog.<br>
2. Quick brown foxes leap over lazy dogs in summer.<br>

倒排索引就会现将这两个文档进行分词处理，将去重之后的所有唯一的词放到一个表，和文档组成一个矩阵：

|Term|doc_1|doc_2|
|---|----|----|
|Quick|| <center>O</center> |
|The|	<center>O</center>||	
|brown|	<center>O</center>|	<center>O</center>|
|dog	|<center>O</center>|	|
|dogs		||<center>O</center>|
|fox	|<center>O</center>|	|
|foxes|	|	<center>O</center>|
|in	|	|<center>O</center>|
|jumped|<center>O</center>||	
|lazy	|<center>O</center>	|<center>O</center>|
|leap|		|<center>O</center>|
|over	|<center>O</center>|	|<center>O</center>|
|quick	|<center>O</center>|	|
|summer|		|<center>O</center>|
|the	|<center>O</center>||	

如果需要搜索“brown fox”的文档，只需要找到每个词在哪个文档出现即可。并且还会根据匹配项的个数来判断哪个文档的相关性高，并且可以根据这个对结果来排序。

|Term|doc_1|doc_2|
|---|----|----|
|brown|	<center>O</center>|	<center>O</center>|
|fox	|<center>O</center>|	|
|Total Count| <center>2</center> | <center>1</center>|