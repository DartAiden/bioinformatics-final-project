seqs = ''.join(open('combined.fasta','r').readlines())
seqs = seqs.split('>')
uniques = []
uniqueseqs = set()
for a in seqs:
    if a not in uniqueseqs:
        uniques.append(a)
        uniqueseqs.add(a)
combined = open('filtered.fasta','w')
temp = '>'.join(uniques)
temp = '>' + temp
combined.write(temp)
combined.close()