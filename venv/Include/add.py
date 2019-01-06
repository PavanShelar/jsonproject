import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
   # w=w.upper()
    if w in data:
       return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
         #return "Did you mean %s Instead ?"%get_close_matches(w.data.key())[0]
         a=input("Did you mean %s Instead ?"%get_close_matches(w,data.keys())[0])
         if a=="Y":
            return data[get_close_matches(w,data.keys())[0]]
         elif a=="N":
            return"no found"
    else:
         return "keyword not found"
word=input("search:")
print(translate(word))
output=translate(word)
if type(word)==list:
    for item in output:
        print(item)
    else:
        print(output)