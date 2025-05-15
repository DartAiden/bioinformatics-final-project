import pandas as pd
protresults = pd.read_csv(r'feats\blastp_search.csv')
hitdb = {}
for _,i in protresults.iterrows():
    hitdb[i["original"]] = i["accession"]

hitfeats = pd.read_csv(r'feats\hitfeats.csv')
queryfeats = pd.read_csv(r'feats\queryfeats.csv')

for i in hitdb.keys():
    temp = hitfeats.loc[hitfeats["Query"] == i]
    for j in temp:
    
