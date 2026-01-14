f = open('24_18186.txt').readline()
s = 'BCDFGH'
vowels = 'AE'
prev_index = 0
curr_index = 0
max_len = float('-inf')
curr_index_exist = False
for i in range(len(f) - 2):
    if f[i] in s and f[i + 1] in s and f[i + 2] in vowels:
        if curr_index_exist:
            prev_index = curr_index
            curr_index = i
            max_len = max(curr_index - prev_index + 3, max_len)
        else:
            curr_index = i
            curr_index_exist = True


print(prev_index, curr_index, max_len)