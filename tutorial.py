print("Hello World")

5+5

10.5-2*3

10**2

17.0//3

17%3

5*3+2

type(5)

type(3.5)

12/5

float(12)/5

"This is a codon isn't it?"

print("This is a codon isn't it?")

a=4
a

b=a
b

b=b+3
b

dna = "gatccccccccgggtttccatctaccagcgcgcgctgctsccaaattcagtca"
dna[0]

dna[-1]

dna[-5]

dna[0:3]

dna[:3]

dna[2:]

len(dna)

help(len)

dna.count('c')

dna.count('gc')

dna.upper()

dna

# Where ag is found
dna.find('ag')

# Find the position of ag after position 27
dna.find('ag', 27)

dna.rfind('ag')

help(str)

dna

dna.islower()

dna.isupper()

# Replace character in a string to another
dna.replace('c', 'C')

dna = 'actgctatgctttagatattagaagagagaggcgcgcgcgcgcttttgcgcgcttgcgcgctaatgatgatgc'
dna

no_c=dna.count('c')
no_c

no_g=dna.count('g')
no_g

dna_length=len(dna)
dna_length

gc_percent=(no_c+no_g)*100.0/dna_length
gc_percent

# to make linux command executable chmod a+x gc.py
print(gc_percent)

dna=input("Enter a DNA sequence, please")

dna

my_number=input("Please enter a number")

actual_number=int(my_number)
actual_number

cool_number=int(input("Please enter a number"))

cool_number

# 0-255 characters that map to internal characters and string functions in python
chr(65)

str(65)

print("The DNA sequence's GC content is", gc_percent, "%")

print("The DNA sequence's GC content is %5.3f %%" % gc_percent)

print("%d" % 10.6) #transforms to integer

print("%3d" % 10.6) #3 positions to print

print("%o" % 10) #o for octal %x for hexadecimal

print("%e" % 10.6) #e is scientific notation base 10

print("%s" % dna) #print something as a string

dna="atgctggggact"
dna[:3]
dna

print('>HSBGPG Human bone gla gene\\transcript "BGP"\nGGCAGATTCCCCCTAGA')

val = 1.234567 * 10 ** 6
val

a=1

b=2

c=a+b

a = b

a = c

d=a+c
d

# Lists
gene_expression=['gene', '0.23658', '5.16e-08', '44.6e-09']
print(gene_expression[2])

gene_expression[0]='Lif'
print(gene_expression)

motif='nacatgggg'
motif[0]='a' #strings imupatble data types

gene_expression[-3:]

gene_expression[1:3]=[6.09e-07]
gene_expression

len(gene_expression)

del gene_expression[1]
gene_expression

gene_expression.extend([5.16e-09, 0.000013556])
gene_expression

print(gene_expression.count('Lif'), gene_expression.count('gene'))

gene_expression.reverse()
gene_expression

stack=['a', 'b', 'c', 'd']
stack

stack.append('e')
stack

gene_expression

stack.append(gene_expression)
stack

mylist=[3, 31, 123, 1, 5]
mylist

sorted(mylist)

mylist

# ,sort changes the elements on the list to sort them
mylist.sort()
mylist

mylist=['c', 'g', 'T', 'a', 'A']
mylist

print(sorted(mylist))

# Tuple
t=1,2,3
t

t=(1, 2, 3)
t

# Set lists with no duplicate enteries
brca1={'Annot1', 'Annot2', 'Annot3', 'Annot4', 'Annot5', 'Annot1'} #Duplicated on purpose to show python removed duplicates
brca1

brca2={'Annot6', 'Annot7', 'Annot8', 'Annot9', 'Annot1', 'Annot2'} #Duplicated on purpose to show python removed duplicates
brca2

brca1|brca2 #Union

brca1 & brca2 #common terms

brca1 - brca2 #difference

# Dictionary
TF_motif = {
    'SP1' : 'gggcgg',
    'C/EBP' : 'attgcgcaat',
    'ATF' : 'tgacgtca',
    'c-Myc' : 'cacgtg',
    'Oct-1' : 'atgcaaat'
}
TF_motif

print("The recognition sequence for the ATF transcription factor is %s." % TF_motif['ATF']) # %s is where in the string the function applies

'NF-1' in TF_motif

TF_motif['AP-1']='tgagtca'
TF_motif

TF_motif['AP-1']='tga(g/c)tca'
TF_motif

del TF_motif['SP1']
TF_motif

# you can update using the following update command
TF_motif.update({'SP1': 'gggcgg'})
TF_motif # note how SP1 has changed from what it was earlier

len(TF_motif)

list(TF_motif.keys())

list(TF_motif.values())

list(sorted(TF_motif.keys()))

type([1e-10,(1,2),"BGP",[3]])

splice_site_pairs = ['GT-AG','GC-AG','AT-AC']
splice_site_pairs[:-1]

t = ('a', 'c', 'g', 't')
t.append(('A','C','G','T'))

dna=input("Enter DNA sequence:")

dna_counts={'t':dna.count('t'),'c':dna.count('c'),'g':dna.count('g'),'a':dna.count('a')}
nt=sorted(dna_counts.keys())
print(nt[-1]) #the minus 1 moves from 0 to the last

nt

dna_counts = {
    't':dna.count('t'),'c':dna.count('c'),'g':dna.count('g'),'a':dna.count('a')
}
max_freq=sorted(dna_counts.values())[-1]
max_freq

dna_counts.values()

max_freq=sorted(dna_counts.keys())[-1]
max_freq

someData = { }
someData['cheese'] = 'dairy'
someData['Cheese'] = 'dairy'
someData['Cheese'] = 'Dairy'
someData['cheese'] = 'Dairy'
someData
