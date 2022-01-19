import itertools
import random

m = 0
n = 0
with open('ieeja.txt', 'r') as infile:
    for idx, line in enumerate(infile):
        if idx == 0: m = int(line)
        else: n = int(line)

symbols = list(range(m))*n
generated = list(itertools.permutations(symbols, n))
viable = sorted(list(dict.fromkeys(generated)))

def find_matches(curr, used):
    possibilities = []
    for j in viable:
        if j in used: continue
        elif curr == j: continue
        else:
            if n > 2:
                for k in range(n-2):
                    if curr[k+1] == j[k] and curr[k+2] == j[k+1]:
                        possibilities.append(j)
            else:
                if curr[1] == j[0]:
                    possibilities.append(j)
    return possibilities

def make_loop(seq):
    actual_loop = []
    first = seq[0]
    for i in first: actual_loop.append(i)
    for i in range(1,(m**n) - (n-1)):
        actual_loop.append(seq[i][-1])
    return actual_loop

def find_bruin_loop(used, viable, curr, seq):
    if curr not in used: 
        seq.append(curr)
        used.append(curr)
    possibilities = find_matches(curr, used)
    if len(possibilities) == 0: return seq
    else:
        next = random.choice(possibilities)
        possibilities.remove(next)
        
        seq = find_bruin_loop(used, viable, next, seq)
    if type(seq) == list:
        if(len(seq) == m**n):
            return seq

found = False
while(not found):
    possible_loop = find_bruin_loop([], viable, viable[0], [])
    if type(possible_loop) == list:
        if len(possible_loop) == m**n:
            str_version = ''.join(str(e) for e in make_loop(possible_loop))
            with open('izeja.txt', 'w') as outfile:
                outfile.write(str_version)
            break
