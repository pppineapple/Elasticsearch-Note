import requests
import datetime

esurl = "http://localhost:9200/"
headers = {"Content-Type": "application/json"}

# Query all of indices which match the key_word
# indexname: key_word + date
key_word = "test_"

indices_get_res = requests.get(esurl+'_cat/indices')
indices_iwanted = []
for row in indices_get_res.content.split('\n'):
    if row != "":
        print indexname
        indexname = row.split(' ')[2]
        if key_word in indexname:
            print indexname
            indices_iwanted.append(indexname)

# Delete indices a week ago
for indexname in indices_iwanted:
    index_date = indexname.split(key_word)[-1]
    index_day = datetime.datetime.strptime(index_date, "%Y.%m.%d")
    today = datetime.datetime.today()
    if (today - index_day).days > 7:
        index_delete_res = requests.delete(esurl + indexname)
        if index_delete_res.status_code == 200:
            print 'index {0} deleted successfully'.format(indexname)
        else:
            print 'index {0} deleted unsuccessfully'.format(indexname)
