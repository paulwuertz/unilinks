# -*- coding: utf-8 -*-
import json
import os

def readJSON(file):
    data=[]
    with open("data/"+file+".json", encoding='utf-8') as data_file:
        data+=json.loads(data_file.read())
    return data


file="et"
www="data/"+file+"/"

et=readJSON("et.gs")+readJSON("et.hs")

for modul in et:
    os.makedirs(www+modul["name"], exist_ok=True)
    open(www+modul["name"]+"/index.md", 'a').close()
    os.makedirs(www+modul["name"]+"/Vorlesung", exist_ok=True)
    os.makedirs(www+modul["name"]+"/Übungen", exist_ok=True)
    os.makedirs(www+modul["name"]+"/Prüfung", exist_ok=True)
    if "praktikum" in modul and modul["praktikum"]:
        os.makedirs(www+modul["name"]+"/Praktikum", exist_ok=True)