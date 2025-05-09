import pandas as pd

protresults = pd.read_csv(r'feats\blastp_search.csv')
hitfeats = pd.read_csv(r'feats\hitfeats.csv')
queryfeats = pd.read_csv(r'feats\queryfeats.csv')

hitdb = {row["original"]: row["accession"] for _, row in protresults.iterrows()}

shared_motifs = []

for original, hit in hitdb.items():
    query_motifs = queryfeats[queryfeats["Query"] == original]
    hit_motifs = hitfeats[hitfeats["Query"] == hit]

    for _, q_row in query_motifs.iterrows():
        for _, h_row in hit_motifs.iterrows():
            if (
                q_row["Title"].strip().lower() == h_row["Title"].strip().lower()
                and q_row["source domain"] == h_row["source domain"]
            ):
                shared_motifs.append({
                    "Query": original,
                    "Hit": hit,
                    "Motif": q_row["Title"],
                })

shared_df = pd.DataFrame(shared_motifs)
shared_df.to_csv('shared_hits.csv')
