keys={'F1','F2','F3','F4','F5'}
print(keys)
keys.add('F9')
print(keys)
keys1={1,2,3,4,5}
keys.update(keys1)
print(keys1)
keys1.discard(4)
print(keys1)
for key in keys:
    print(key)
print(list(keys))
print(tuple(keys))
print(keys.union(keys1))
print(keys.intersection(keys1))
