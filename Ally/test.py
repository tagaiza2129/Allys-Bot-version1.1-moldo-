import json
import os
import requests
name="jxau"
url="https://emctoolkit.vercel.app/api/aurora/residents/"+name
get=requests.get(url)
os.chdir(os.path.dirname(__file__))
with open("result.json",mode="w",encoding="UTF-8")as f:
    f.write(get.text)
with open("result.json",mode="r",encoding="UTF-8")as f:
    jsn=json.load(f)
print(jsn["name"])