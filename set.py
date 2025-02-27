s = {1,2,4,5,6,8}
s1 = {1,44,4,55,6,88}

print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
print(s1.difference(s))
print(s1.update(s))