def cycleToChromosome(cycle):
    cycle = cycle[1:-1].split(" ")
    cycle = [int(x) for x in cycle]
    chr = [i for i in range(1, int(len(cycle)/2) +1)]
    for j in range(0, int(len(cycle)/2)):
        if(cycle[2*j] > cycle[2*j + 1]):
            chr[j] = -chr[j]
    return chr

cycInput = "(1 2 3 4 5 6 7 8 9 10 12 11 13 14 15 16 17 18 20 19 21 22 24 23 26 25 27 28 30 29 31 32 34 33 35 36 38 37 39 40 42 41 44 43 45 46 48 47 49 50 52 51 54 53 56 55 57 58 59 60 62 61 64 63 66 65 67 68 69 70 72 71 73 74 75 76 78 77 80 79 81 82 84 83 85 86 87 88 89 90 92 91 94 93 95 96 98 97 99 100 101 102 104 103 106 105 108 107 109 110 112 111 113 114 116 115 117 118 120 119 122 121 124 123 126 125 127 128 129 130)"

print("(", end="")
for i in cycleToChromosome(cycInput):
    if(i > 0):
        print("+", end="")
    if i == cycleToChromosome(cycInput)[-1]:
        print(i, end="")
    else:
        print(i, end=" ")
print(")")
