#!/usr/local/bin/python3
# -*- coding: UTF8 -*-

import re
import os
from xml.etree import ElementTree as ET
import filefetcher


# tek lista af minningargreinum inn
with open("mogginn/minningargreinar.txt", "r") as m_files:
    minningargreinar_list = []
    for line in m_files:
        minningargreinar_list.append(line.strip())

#tek lista af íþróttafréttum inn til samanburðar
with open("mogginn/ithrottir.txt", "r") as i_files:
    ithrottir_list = []
    for line in i_files:
        ithrottir_list.append(line.strip())


def get_doc(xml):
    Fjoldi_greina = 0
    listOfFiles = filefetcher.getListOfFiles('mbl')
    for file in listOfFiles:
        file_name = (file.rsplit('/',1)[1])
        if file_name in minningargreinar_list:
            #Sæki xml
            Fjoldi_greina +=1
            while Fjoldi_greina < 2000:
                with open(file, 'rt') as f:
                        #Parsa allt tréð
                        tree = ET.parse(f)
                        #Set rótina þar sem skjalið byrjar (ekki hausinn
                        root = tree.getroot()[1]
                        #Næ í orðin í tréð
                        e = root.findall(".//")

                        #Skilgreini skrár fyrir orð og lemmur úr Morgunblaði
                        flemma = open ("lemmafolder/" + file_name[:11] + ".lemmur.txt","w+")
                        
                        for i in e:
                            #næ í orðin
                            word = str(i.text)
                            #sæki attrib
                            var = i.attrib  
                            #tengi orð og lemmu, þótt ég hafi orðið strax sér, því ég vil geta losað mig við "lemmur" ekki orða.
                            t = str(var)
                            add = str (word + " " + t+"\n")
                            if re.search(r'^[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+',add):
                                add = add.replace('{', '')
                                add = add.replace('}', '')
                                add_lemma = add.split(': \'', 1)[1]
                                add_lemma = add_lemma.split('\',',1)[0]
                                flemma.write (add_lemma+"\n")

        if file_name in ithrottir_list:
                #Sæki xml
                with open(file, 'rt') as f:
                        #Parsa allt tréð
                        tree = ET.parse(f)
                        #Set rótina þar sem skjalið byrjar (ekki hausinn
                        root = tree.getroot()[1]
                        #Næ í orðin í tréð
                        e = root.findall(".//")

                        #Skilgreini skrár fyrir orð og lemmur úr Morgunblaði
                        flemma = open ("ithrlemmafolder/" + file_name[:11] + ".lemmur.txt","w+")
                        
                        for i in e:
                            #næ í orðin
                            word = str(i.text)
                            #sæki attrib
                            var = i.attrib  
                            #tengi orð og lemmu, þótt ég hafi orðið strax sér, því ég vil geta losað mig við "lemmur" ekki orða.
                            t = str(var)
                            add = str (word + " " + t+"\n")
                            if re.search(r'^[A-Za-zÞÆÖÐÚÁÍÓÉþæöðúáíóé]+',add):
                                add = add.replace('{', '')
                                add = add.replace('}', '')
                                add_lemma = add.split(': \'', 1)[1]
                                add_lemma = add_lemma.split('\',',1)[0]
                                flemma.write (add_lemma+"\n")
