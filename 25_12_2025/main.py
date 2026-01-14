# HARDCODED_1
# s = 'Hello how are you' * 10000000
#
# counts = []
#
# for x in s:
#     s_add = True
#     for c in counts:
#         if c[0] == x:
#             c[1] += 1
#             s_add = False
#     if s_add:
#         counts.append([x, 1])
#
# print(counts)

# HARDCODED_2
# s = 'Hello how are you' * 100000000
# counts = []
# set_s = set(s)
# for x in set_s:
#     counts.append([x, s.count(x)])
#
# print(counts)



# m = 'Hello how are you' * 1000000
# d = dict()
# for x in m:
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1
#
# print(d)
#
#
# d = dict()
# d['Svetlana'] = 1
# d['Nikita'] = 4
#
# print(d.keys())
# print(d.values())
# print(d)


from collections import Counter
m = 'Hello how are you' * 1000000
print(Counter(m))