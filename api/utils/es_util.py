import elasticsearch
def GetEsConn():
    return elasticsearch.Elasticsearch()