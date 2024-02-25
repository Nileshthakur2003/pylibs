import urllib
import json
 
from urllib.request import urlopen

globaldata_ = []


def load_data(phrase):
    word = phrase
    try:
        
        html = urlopen("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
        contents = html.read()
        decoded_string = contents.decode('utf-8')
        resp_object = json.loads(decoded_string)
                
    except :
        return False
    
    globaldata_=resp_object
    return True

def raw_data(phrase):
    word = phrase
    try:
    
        html = urlopen("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
        contents = html.read()
        decoded_string = contents.decode('utf-8')
        resp_object = json.loads(decoded_string)
            
    except :
        return [{"error":"True"}]

    
    return resp_object

def getWord():
    if(globaldata_!=[]):
        return globaldata_[0]["word"]
    else:
        return False

def getPhonetic():
    if(globaldata_!=[]):
        return globaldata_[0]["phonetic"]
    else:
        return False

def getPhonetics():
    if(globaldata_!=[]):
        return globaldata_[0]["phonetics"]
    else:
        return False

def getMeanings():
    if(globaldata_!=[]):
        return globaldata_[0]["meanings"]
    else:
        return False
        
def getOrigin():
    if(globaldata_!=[]):
        return globaldata_[0]["origin"]
    else:
        return False


