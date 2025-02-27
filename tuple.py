# tup = (1,2,3)

# print(type(tup),tup)

# print(tup[0])

# l=tup
# print(l)

# l = [1,2,3,4]
# t = [3,495]

# lt = l+t
# lt.sort()
# print(lt)

tup = (1,32,432,34,3,3,3,33,3,3,33,4,3,432,)
# res = tup.count(33)
# res = tup.index(33)
res = tup.index(33,8,12)
l=[tup]
l[0]=1000
# tup=(l)
print(tup)