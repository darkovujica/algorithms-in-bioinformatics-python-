def BreakOnGenomeGraph(GenomeGraph, i, I, j, J):
     if (i,I) in GenomeGraph:
         GenomeGraph.remove((i,I))
     else:
         if (I,i) in GenomeGraph:
             GenomeGraph.remove((I, i))
     if (j,J) in GenomeGraph:
         GenomeGraph.remove((j,J))
     else:
         if (J,j) in GenomeGraph:
             GenomeGraph.remove((J, j))
     GenomeGraph.append((i,j))
     GenomeGraph.append((I,J))
     return GenomeGraph


#f = open("C:\\Users\\DARKO\\Downloads\\rosalind_ba6j.txt", "r")
#inlines = f.read().splitlines()
x = '''(1, 3), (4, 6), (5, 8), (7, 9), (10, 11), (12, 13), (14, 15), (16, 18), (17, 20), (19, 22), (21, 23), (24, 25), (26, 27), (28, 30), (29, 31), (32, 33), (34, 35), (36, 37), (38, 40), (39, 42), (41, 43), (44, 45), (46, 47), (48, 50), (49, 51), (52, 54), (53, 56), (55, 58), (57, 60), (59, 62), (61, 64), (63, 66), (65, 67), (68, 69), (70, 72), (71, 74), (73, 76), (75, 77), (78, 80), (79, 81), (82, 83), (84, 85), (86, 88), (87, 90), (89, 91), (92, 93), (94, 95), (96, 98), (97, 99), (100, 101), (102, 103), (104, 106), (105, 108), (107, 110), (109, 111), (112, 114), (113, 115), (116, 118), (117, 119), (120, 121), (122, 123), (124, 126), (125, 127), (128, 2)
102, 103, 107, 110'''
inlines = x.split("\n")
edges = inlines[0]
edges = edges[1:-1]
p = edges.split("), (")
for i in range(len(p)):
     a = p[i].split(", ")
     p[i] = (int(a[0]), int(a[1]))
indices = inlines[1].split(", ")
for i in range(len(indices)):
     indices[i] = int(indices[i])
#print(p)
res = BreakOnGenomeGraph(p, indices[0], indices[1], indices[2], indices[3])
for i in range(len(res)):
     res[i] = str(res[i])
res = ", ".join(res)
print(res)
