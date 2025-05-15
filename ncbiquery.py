import requests
import pandas as pd
import time
import random

def query(q, returntype):
    headers = {
        "User-Agent": "xxx.com"
    }
    urlq = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=protein&id={q}&retmode=json&apikey=xxx"
    for attempt in range(5):
        try:
            response = requests.get(urlq, headers=headers) #Fetch profile from NCBI
            response.raise_for_status() #Return error if there is one 
            data = response.json() #Convert to JSON
            uid = data["result"]["uids"][0] 
            return data['result'][uid][returntype] #Extract protein
        except Exception as e:
            print(f"Attempt {attempt+1} failed for {q}: {e}") #Try again if there is an error
            time.sleep(5 + random.uniform(0, 2))
    return None #Or return none

blastdf = pd.read_csv(r"1HZXNT1J013-Alignment-HitTable.csv", index_col=False) #Open BLAST
blastdf = blastdf[["query id", "subject id"]] #Extract relevant info

seq_lines = open(r"C:\Users\adart\Documents\bioinformatics-final-project\filtered.fasta").readlines() #Open existing seqs
seqdb = {}
temp = [] 
header = None
for line in seq_lines: #Create dictionary that has the original sequence hashed to the header
    line = line.strip()
    if line.startswith(">"):
        if header:
            seqdb[header] = ''.join(temp)
        header = line[1:]
        temp = []
    else:
        temp.append(line)
if header:
    seqdb[header] = ''.join(temp)

orgos = []
accessions = []
origs = []
seqs_out = []

grouped = blastdf.groupby("query id") #Create database that has 
for query_id, group in grouped:
    for _, row in group.iterrows(): #Group them by gene and hits
        subject_id = row["subject id"]  #Pull one with greatest homology
        organism = query(subject_id, "organism")
        if organism and "phix" not in organism.lower() and "phi x" not in organism.lower(): #Discard if it is Phi X and proceed onto next
            orgos.append(organism) #Add to dataframe
            accessions.append(subject_id)
            origs.append(query_id)
            seqs_out.append(seqdb[query_id])
            time.sleep(0.5) #Avoid being rate-limited
            break  

outdf = pd.DataFrame({
    "original": origs, #Create dataframe
    "organism": orgos,
    "accession": accessions,
    "sequence": seqs_out
})
outdf.to_csv("blastp_search.csv", index=False)