alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabet_dict = {}
for i in range(0,26):
    alphabet_dict[alphabet[i]] = i+1

str_input = input()

for s in str_input:
    print(alphabet_dict[s],end=' ')
