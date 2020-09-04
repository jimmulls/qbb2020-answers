#!/usr/bin/env python3

import sys

##def kmer_matcher(target, query, k = 11):

from fasta_iterator_class import FASTAReader

target = sys.argv[1]
query = sys.argv[2]
k = int(sys.argv[3])


fs = open(query, 'r')
fs2 = open(target, 'r')
##fs3 = open('output.txt', 'w')

##def kcount(subset, dict_name, k =11):

    ##reader = FASTAReader(open(subset))
    ##dict_name = {}

    ##for seq_id, sequence in reader:
        ##for i in range(0, len(sequence) - k +1):
            ##kmer = sequence[i:i +k]
            ##dict_name.setdefault(kmer, 0)
            ##dict_name[kmer] += 1

query_ks={} 

for seq_id, sequence in FASTAReader(fs):

    for i in range(0, len(sequence)- k +1):
        kmer = sequence[i:i+k]
        query_ks.setdefault(kmer, [])
        query_ks[kmer].append(i)


    ##print(seq_id, sequence)
    ##target_seqs[seq_id] = sequence

target_ks={}

for seq_id2, sequence2 in FASTAReader(fs2):

    for i in range(0, len(sequence2)-k +1):
        kmer2 = sequence2[i:i+k]
        target_ks.setdefault(kmer2, {})
        target_ks[kmer2].setdefault(seq_id2,[])
        target_ks[kmer2][seq_id2].append(i)


for key in query_ks:
    if key in target_ks:
        target_name = target_ks[key]
        query_start = query_ks[key]
        k_mer = key
        for key3 in target_name:
            ##fs3.write(str(key3) + '\t' + str((target_name[key3])) + '\t' +
                    ##(str(query_start)) + '\t' + str(k_mer)+ '\n')
            print(str(key3) + '\t' + str((target_name[key3])) + '\t' +
                    (str(query_start)) + '\t' + str(k_mer))




        ##target_ks[kmer2][1]+= 1



fs.close()
fs2.close()
##fs3.close()

if __name__ == "__main__":
    seqs = FASTAReader(sys.stdin)
    for seq_id, sequence in seqs:
        print("{}: {}".format(seq_id, sequence), file=sys.stdout)
