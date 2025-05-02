a = open('set_2.fasta','r').readlines()
b = open('set_7.fasta','r').readlines()

for i in range(len(a)):
    if a[i] != b[i]:
        print(a[i])
        print(b[i])