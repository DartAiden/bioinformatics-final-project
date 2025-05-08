import requests
import pandas as pd
import time
import random
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "xxx.com"
ids = []
ps = open("found_proteins.fasta",'w')
df = pd.read_csv('blastp_search.csv')
for _, a in df.iterrows():
    ids.append(a['accession'])
print(ids)
handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")   
for seq in SeqIO.parse(handle, "fasta"):
    temp = ">" + seq.id + seq.description + '\n'
    ps.write(temp)
    temp = str(seq.seq) + '\n'
    ps.write(temp)

ps.close()