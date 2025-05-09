import pandas as pd
df = pd.read_csv('blastp_search.csv')
seqs = open('seqs.fasta','w')
for _,i in df.iterrows():
    seqs.write(i['accession'])
    seqs.write('\n')