import json
import os, sys
import markdown
from flask import Flask, render_template
from flask_flatpages import FlatPages
import urllib
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

def readJSON(file):
    data=[]
    with open("data/"+file+".json", encoding='utf-8') as data_file:
        data+=json.loads(data_file.read())
    return data

@app.route('/')
def page():
    file="et"
    www="data/"+file+"/"
    
    #if "praktikum" in modul and modul["praktikum"]:
    #    os.makedirs(www+modul["name"]+"/Praktikum", exist_ok=True)    
    
    #content =""
    #content = Markup(markdown.markdown(content))
    #return render_template('index.html', **locals())
    #index=readJSON("index")
    data=readJSON("et.gs")
    data+=readJSON("et.hs")
    
    for modul in data:
        modul["files"]={}
        modul["files"]["Vorlesung"]=[]
        modul["files"]["Übung"]=[]
        modul["files"]["Prüfung"]=[]
        for file in sorted(os.listdir(www+modul["name"]+"/Vorlesung/")):   
            modul["files"]["Vorlesung"]+=[file]
        for file in sorted(os.listdir(www+modul["name"]+"/Übungen/")):   
            modul["files"]["Übung"]+=[file]
        for file in sorted(os.listdir(www+modul["name"]+"/Prüfung/")):   
            modul["files"]["Prüfung"]+=[file]
    
    return render_template('linklist.html', data=data)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)


