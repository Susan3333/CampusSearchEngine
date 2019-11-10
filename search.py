from elasticsearch import Elasticsearch

es = Elasticsearch()
dsl = {
    # "_source": {
    #     "includes": "tittle",
    #     "includes": "content",
    # },
    "query": {

        "multi_match": {
            "query": "上海理工大学",
            # "fields": ["tittle"]
        }
    }
}

# result = es.search(index='news', doc_type='campus')
result = es.search(index='news', body=dsl)
# print(result)
for i in range(len(result['hits']['hits'])):
    print(result['hits']['hits'][i]['_score'])
    # print()
    print(result['hits']['hits'][i]['_source']['tittle'])

    # print(result['hits']['hits'][i]['_source']['content'])
