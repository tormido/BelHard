import collections

value = [1, 2, 5]
value.sort(reverse=1)
print (value)
result = sorted(value)
for c in result[::] * 5:
    print (c)
var = collections.Counter()