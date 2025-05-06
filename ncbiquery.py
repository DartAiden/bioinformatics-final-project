import requests
import pandas as pd
import time
import random

def query(q, returntype):
    headers = {
        "User-Agent": "adartley123@gmail.com"
    }
    urlq = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nucleotide&id={q}&retmode=json&apikey=985d19c2caa6e79cb923755e5042829cc30"
    for attempt in range(5):
        try:
            response = requests.get(urlq, headers=headers)
            response.raise_for_status()
            data = response.json()
            uid = data["result"]["uids"][0]
            return data['result'][uid][returntype]
        except Exception as e:
            print(f"Attempt {attempt+1} failed for {q}: {e}")
            time.sleep(5 + random.uniform(0, 2))
    return None

blastdf = pd.read_csv(r"C:\Users\adart\Documents\bioinformatics-final-project\tblastn results.csv", index_col=False)
blastdf = blastdf[["query id", "subject id"]]

seq_lines = open(r"C:\Users\adart\Documents\bioinformatics-final-project\filtered.fasta").readlines()
seqdb = {}
temp = []
header = None
for line in seq_lines:
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

grouped = blastdf.groupby("query id")
for query_id, group in grouped:
    for _, row in group.iterrows():
        subject_id = row["subject id"]
        organism = query(subject_id, "organism")
        if organism and "phix" not in organism.lower() and "phi x" not in organism.lower():
            orgos.append(organism)
            accessions.append(subject_id)
            origs.append(query_id)
            seqs_out.append(seqdb[query_id])
            time.sleep(0.5)
            break  

outdf = pd.DataFrame({
    "original": origs,
    "organism": orgos,
    "accession": accessions,
    "sequence": seqs_out
})
outdf.to_csv("tblastn_search.csv", index=False)