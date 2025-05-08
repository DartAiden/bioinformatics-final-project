import json
import pandas as pd

with open('interpro.json', 'r') as file:
    data = json.load(file)

signaturecounts = {}
pathwaycounts = {}



results = data["results"]
for i in results:
    matches = i["matches"]
    for j in matches:
        temp = j['signature']['name']
        if temp not in signaturecounts.keys():
            signaturecounts[temp] = 1
        else:
            signaturecounts[temp]+=1
        if j['signature']['entry']:
            for k in j['signature']['entry']["pathwayXRefs"]:
                temp2 = k['name']
                if temp2 not in pathwaycounts.keys():
                    pathwaycounts[temp2] = 1
                else:
                    pathwaycounts[temp2]+=1

signaturedf = pd.DataFrame(
    {
        "Signature" : signaturecounts.keys(),
        "Signature count" : signaturecounts.values()
    }
)

pathwaydf = pd.DataFrame(
    {
        "Pathway" : pathwaycounts.keys(),
        "Pathway count" : pathwaycounts.values()
    }
)
print(pathwaycounts)
#signaturedf.to_csv("signatures.csv", index= False)
pathwaydf.to_csv("pathways.csv", index = False)