#open file and convert into a list
import sys

file = sys.argv[1]

seq = open(file)
contents = seq.readlines()
seq.close()

#read the sequence lines
seq1 = contents[1].strip("\n")
seq2 = contents[3].strip("\n")

#turn string to a list of characters
sepseq1 = [x for x in seq1]
sepseq2 = [x for x in seq2]

#do alignment
alignment = []
for x,y in zip(sepseq1,sepseq2):
    if x == y:
        alignment.append("|")
    else:
        alignment.append(" ")
alignment = "".join(alignment)

print(seq1)
print(alignment)
print(seq2)