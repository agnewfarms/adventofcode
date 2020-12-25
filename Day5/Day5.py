<<<<<<< HEAD
print("Part 1:",
max(ids := [sum(2**i * (1 if b in 'BR' else 0) for i, b in enumerate(s.strip()[::-1])) for s in open('Inputday5.txt')]),
"Part 2:",
=======
print("Part 1:",
max(ids := [sum(2**i * (1 if b in 'BR' else 0) for i, b in enumerate(s.strip()[::-1])) for s in open('Inputday5.txt')]),
"Part 2:",
>>>>>>> db1c44c90b7e7d467049dbdda56832b530541efb
next(s+1 for s in ids if s+1 not in ids and s+2 in ids))