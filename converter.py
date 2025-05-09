from Bio import SeqIO

records = []
for record in SeqIO.parse("viral_genomes_stav_align.fas", "fasta"):
    record.annotations["molecule_type"] = "DNA"  # or "RNA" or "protein"
    records.append(record)

count = SeqIO.write(records, "out.nexus", "nexus")
print(f"{count} records written to out.nexus")
