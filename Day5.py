print("Part 1:",
max(ids := [sum(2**i * (1 if b in 'BR' else 0) for i, b in enumerate(s.strip()[::-1])) for s in open('Inputday5.txt')]),
"Part 2:",
next(s+1 for s in ids if s+1 not in ids and s+2 in ids))I
