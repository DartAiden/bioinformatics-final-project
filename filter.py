seqs = ''.join(open('combined.fasta','r').readlines())
seqs = seqs.split('>')[1:]
uniques = []
uniqueseqs = set()
for a in seqs:
    temp = ''.join(a.split('\n')[1:])
    header = a.split('\n')[0]
    if temp not in uniqueseqs:
        uniques.append(a)
        uniqueseqs.add(temp)
    else:
        print(header)
combined = open('filtered.fasta','w')
temp = '>'.join(uniques)
temp = '>' + temp
combined.write(temp)
combined.close()