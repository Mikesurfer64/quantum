"""punnet_square.py"""

#Reference: W3 tutorials and geekforgeeks tutorials
# Create a punnett square which represents a 4x4 matrix of values determining dominant/recessive traits of allelles.

import numpy as py 
from pprint import pprint
from fractions import Fraction

# Let color = 1 be Yellow and color = 0 be green (y)
# Let shape = 1 be Round (R) and shape = 0 be wrinkled (r)
# Let the digits each declare a color or a shape '10' = Yy (color) '10' = Rr so '1010' would be the string 'YyRr'

#Input color for parent 1
x1 = "10" 
#Input shape for parent 1
y1 = "10"

parent_1_genotype = {'Color': 'x1', 'Shape': 'y1'}

# Gametes of Parents: 

parent_1_gametes = [{'Color': x1[:1], 'Shape': y1[:1]}, 
                    {'Color': x1[:1], 'Shape': y1[1:2]},
                    {'Color': x1[1:2], 'Shape': y1[:1]}, 
                    {'Color': x1[1:2], 'Shape': y1[1:2]},  
]

#Input color for parent 2
x2 = "10"
#Input shape for parent 2
y2 = "10"

parent_2_genotype = {'Color': 'x2', 'Shape': 'y2'}

parent_2_gametes = [{'Color': x2[:1], 'Shape': y2[:1]}, 
                    {'Color': x2[:1], 'Shape': y2[1:2]},
                    {'Color': x2[1:2], 'Shape': y2[:1]}, 
                    {'Color': x2[1:2], 'Shape': y2[1:2]},  
]

print("Possible Gametes of Parent 1")

print("\n\n".join(map(str, parent_1_gametes)))

print("Possible Gametes of Parent 2")

print("\n\n".join(map(str, parent_2_gametes)))

#a's are for colors

a11=''.join([x1[:1],x2[:1]])
a12=''.join([x1[:1],x2[1:2]])
a13=''.join([x1[1:2],x2[:1]])
a14=''.join([x1[1:2],x2[1:2]])

L1=[a11,a12,a13,a14]

#b's are for shape
                            #key given that x=y=10
b11=''.join([y1[:1],y2[:1]]) #11
b12=''.join([y1[:1],y2[1:2]]) #10
b13=''.join([y1[1:2],y2[:1]]) #01
b14=''.join([y2[1:2],y2[1:2]]) #00

L2=[b11,b12,b13,b14]

import numpy as np

#height, width = 4, 4 another possible method using np.array instead of my rudimentary method
#num = [a11, a12, a13, a14, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#array = np.array(num).reshape((height, width))
#print(array)


punnet_square_results = [{'Color': a11, 'Shape': b11}, #row 1 start
                    {'Color': a11, 'Shape': b12},
                    {'Color': a12,'Shape': b11}, 
                    {'Color': a12, 'Shape': b12}, # row 1 end
                    {'Color': a11, 'Shape': b13}, #row 2 start
                    {'Color': a11, 'Shape': b14},
                    {'Color': a12,'Shape': b13}, 
                    {'Color': a12, 'Shape': b14}, #row 2 end
                    {'Color': a13, 'Shape': b11}, #row 3 start
                    {'Color': a13, 'Shape': b12},
                    {'Color': a14,'Shape': b11}, 
                    {'Color': a14, 'Shape': b12}, #row 3 end
                    {'Color': a13, 'Shape': b13}, # row 4 start
                    {'Color': a13, 'Shape': b14},
                    {'Color': a14,'Shape': b13}, 
                    {'Color': a14, 'Shape': b14},      
]

#pprint(np.array(punnet_square_results))
rows = 4
cols = 4

pprint('Punnet Square Results')

for i in range(rows):
    for j in range(cols):
        print(punnet_square_results[i * cols + j], end=' ')
    print()

# Find the phenotype ratios 
print("Phenotype Ratios")

# if color is "00" and shape is "11,10,01" then wrinkled (green)) 
# if color is "11,10,01" and shape is "11,10,01" then round (yellow)
# if color is "11,10,01" and shape is "00" then wrinkled (yellow)
# if color is "00" and shape is "00" then wrinkled (green)

#if L1 == 00:
  #  return "green"
#else "yellow"
    
#if L2 == 00:
  #  return "wrinkled"
##else "round"
    
for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '11', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '11'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '10', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '11'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '01', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '11'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '11', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '10'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '10', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '10'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '01', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '10'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '11', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '01'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '10', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '01'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '01', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '01'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '11', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '00'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '10', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '00'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '01', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': '00'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '00', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': '11'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '00', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': '10'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '00', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': '01'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': '00', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': '00'}
#account for the replacement of round/wrinkling

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Green', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Green', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Green', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Green', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Green', 'Shape': 'Wrinkled'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Yellow', 'Shape': '11'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Yellow', 'Shape': '10'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Yellow', 'Shape': '01'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': 'Round'}

for i in range(len(punnet_square_results)):
    if punnet_square_results[i] == {'Color': 'Yellow', 'Shape': '00'}:
        punnet_square_results[i] = {'Color': 'Yellow', 'Shape': 'Wrinkled'}

pprint(punnet_square_results)

s1 = punnet_square_results.count({'Color': 'Yellow', 'Shape': 'Round'})

s2 = punnet_square_results.count({'Color': 'Yellow', 'Shape': 'Wrinkled'})

s3 = punnet_square_results.count({'Color': 'Green', 'Shape': 'Round'})

s4 = punnet_square_results.count({'Color': 'Green', 'Shape': 'Wrinkled'})

print(f"Yellow and Round", Fraction(s1/16))
print(f"Yellow and Wrinkled", Fraction(s2/16))
print(f"Green and Round", Fraction(s3/16))
print(f"Green and Wrinkled", Fraction(s4/16))
