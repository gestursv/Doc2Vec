#!/usr/local/bin/python3
# -*- coding: UTF8 -*-

import random
import os
from gensim.models import Doc2Vec

model = Doc2Vec.load('doc2vec3.model') #hér er hlaðið inn módelskrá af diski


#próf A

#velja skjalsheiti random úr foldernum sem var notaður til þess að þjálfa með
LemmurLabels = [d for d in os.listdir("lemmafolder") if d.endswith('lemmur.txt')]
selected_doc = random.choice(LemmurLabels)
print ('Valið skjal er ' + selected_doc)

#búa til breytu fyrir skjalsheitið og sækja texta
sel_doc_all = []
doc_text = open('lemmafolder/' + selected_doc, 'r', encoding = 'utf8', errors = 'ignore')
for line in doc_text:
    if not line.startswith('\x00'):
        sel_doc_lemmas = line.strip()
        sel_doc_all.append(sel_doc_lemmas)

#keyra infer_vector, s.s. endurreikna vektorgildi fyrir skjalið sem valið var
selected_doc_vec = model.infer_vector(sel_doc_all, epochs=20)

# finna líkustu 10 skjölin
similars = model.docvecs.most_similar(positive=[selected_doc_vec])
print (similars)

#próf B

#velja skjalsheiti random úr foldernum sem var notaður til þess að þjálfa með
LemmurLabels = [d for d in os.listdir("ithrlemmafolder") if d.endswith('lemmur.txt')]
selected_doc = random.choice(LemmurLabels)
print ('Valið skjal sem er íþróttafrétt er ' + selected_doc)

#búa til breytu fyrir skjalsheitið og sækja texta
sel_doc_all = []
doc_text = open('ithrlemmafolder/' + selected_doc, 'r', encoding = 'utf8', errors = 'ignore')
for line in doc_text:
    if not line.startswith('\x00'):
        sel_doc_lemmas = line.strip()
        sel_doc_all.append(sel_doc_lemmas)

#keyra infer_vector, s.s. endurreikna vektorgildi fyrir skjalið sem valið var
selected_doc_vec = model.infer_vector(sel_doc_all, epochs=20)

# finna líkustu 10 skjölin
similars = model.docvecs.most_similar(positive=[selected_doc_vec])
print (similars)
