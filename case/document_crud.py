#!/usr/bin/env python
import os
import requests
import json
import unittest

class ElasticCRUD(unittest.TestCase):
    def setUp(self):
        self.es_ip = os.environ['ES_IP']
        self.index_ = "school"
        self.type_ = "student"
        self.url = 'http://%s:9200/%s/%s/'%(self.es_ip, self.index_, self.type_)
        print self.url
    def create_Index(self,data):
        print "===create_Index"
        print "post to %s with data --%s--"%(self.url, json.dumps(data))
        r = requests.post(self.url, data = json.dumps(data))
        assert r.status_code == 201
        print "response: %s"%(r.text)
        return r.json()["_id"]
    def read_Get(self, id_):
        print "===read_Get"
        url = self.url + id_ + "?filter_path=_source"
        print "get from %s"%(url)
        r = requests.get(url)
        print "response: %s"%(r.text)
        return r.json()["_source"]
    def update_Update(self,id_, data):
        print "===update_Update"
        url = self.url + id_
        print "put to %s with data --%s--"%(url, json.dumps(data))
        r = requests.put(url, data = json.dumps(data))
        print r.text

    def test_crud(self):
        d1 = {'name' : 'Lily', 'born' : 1997 }
        #create
        id_ = self.create_Index(d1)
        #get
	d2 = self.read_Get(id_)
        print d1
        print d2
        assert d1 == d2
        #update 
        d2["born"] = 1998
        self.update_Update(id_, d2)
        d3 = self.read_Get(id_)
        assert d1 != d3


if __name__ == '__main__':
    unittest.main()
