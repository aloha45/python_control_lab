pyg = 'ay'

original = input('Please enter a word: ')

if len(original) > 0 and original.isalpha():
    print(original)
else: 
    print('empty')

word = original.lower()

first = word[0]

pyg_word = word[1:len(word)] + first + pyg

print(f'Now it is: {pyg_word}')