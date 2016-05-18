#!/usr/bin/python
###############################################################################
""" Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string ss of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of
# times that the symbols 'A', 'C', 'G', and 'T' occur in ss."""
###############################################################################
# Open a file
f = open("rosalind_dna.txt", "r")
print "Name of the file: ", f.name

str = f.read();
print "Read String is : ", str

G_list = []
C_list = []
A_list = []
T_list = []

for i in str:
    if (i == 'G'):
        G_list.append(i)
    elif (i == 'C'):
        C_list.append(i)
    elif (i == 'A'):
        A_list.append(i)
    elif (i == 'T'):
        T_list.append(i)

print len(A_list)
print len(C_list)
print len(G_list)
print len(T_list)

####################################################################################
# Alternate solutions given by other users
def qt(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")

count = qt(str)
print count

####################################################################################

# Close opend file
f.close()

