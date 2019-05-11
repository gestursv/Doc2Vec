#!/usr/local/bin/python3
# -*- coding: UTF8 -*-

import os #til að geta lesið úr skrárkerfinu
import re #til að geta hreinsað til í skránum
from gensim.models import Doc2Vec # því það er það sem við ætlum að nota

import logging #svo hægt sé að fylgjast með framganginum
import etree3 #svo ég geti kallað í fall og lesið í XML-ið

import etree3 #til þess að lesa úr XML-inu
import DocIterator #sem er forritið sem við mótum til þess að geta byggt upp safnið, með því að ítra skrárnar

#gerum folder (ef það er ekki til
if not os.path.isdir('lemmafolder'):
    os.mkdir ('lemmafolder')
 
#gerum folder (ef það er ekki til
if not os.path.isdir('ithrlemmafolder'):
    os.mkdir ('ithrlemmafolder')

#etree3.get_doc('xml') #kallar í stubbinn sem sækir lemmurar í XML-ið. Það er rétt að gæta að því að stöðva keyrsluna þegar nægt efni er komið í möppurnar tvær.
# Að örðum kosti verður þar allt of mikið efni til að vinna úr. Þegar nægt er komið af greinum ætti að vera hægt að "rem-a" út etree3.doc

#Hér hefst Gensimhlutinn
LemmurLabels = [d for d in os.listdir("lemmafolder") if d.endswith('lemmur.txt')] #sæki heiti hverrar skráar, sem geymir lemmur greinanna

#Hleð innihaldi skjala
LemmurData = []
for doc in LemmurLabels:
    with open('lemmafolder/' + doc, 'r', encoding = 'utf8', errors = 'ignore') as eachfile:
        for line in eachfile:
            if not line.startswith('\x00'):
                lemmas = line.strip()
                LemmurData.append(lemmas)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO) #loggurinn settur inn

it = DocIterator.Dociter(LemmurData, LemmurLabels) #innihald módelsins búið til
model = Doc2Vec(vector_size=100, min_count=5, workers=4, epochs=20) #módelið byggt upp

model.build_vocab(it) #orðabókin útbúin

model.train(it, epochs=model.epochs, total_examples=346241) #hér ætti að setja inn fjölda dæmasvo hægt sé að fylgjast me framgangi
#en ég fann ekki leið til þess að telja þau öðru vísi en að byrja keyrsluna.

model.save('doc2vec2.model') #nafnið á módelinu sem maður vistar. Því má síðan breyta