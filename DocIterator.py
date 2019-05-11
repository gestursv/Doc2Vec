#!/usr/local/bin/python3
# -*- coding: UTF8 -*-

from gensim.models.doc2vec import TaggedDocument as LabeledSentence
from gensim import utils

class Dociter(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list

    def __iter__(self):
        for doc in enumerate(self.doc_list):
            yield LabeledSentence(words=doc,tags=self.labels_list)
