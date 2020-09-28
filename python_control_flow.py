 EXERCISE 1

letter = input('Please enter a letter from the alphabet: ')

lower_letter = letter.lower()

vowels = ['a', 'e', 'i', 'o', 'u']


if lower_letter == 'a' or lower_letter == 'e' or lower_letter == 'i' or lower_letter == 'o' or lower_letter == 'u':
    print(f'The letter {lower_letter} is a vowel')
else: 
    print(f'The letter {lower_letter} is a consonant')

EXERCISE 2


def check():
    phrase_word = input('Please enter a word or phrase: ')
    length = len(phrase_word)
    if phrase_word != 'quit':
        print(f'What you entered is {length} characters long')
        check()
    else:
        return

check()

EXERCISE 3

years = int(input("Input your dog's age in human years: "))

def dog_years(years):
    first_two = float(years * 10)
    remaining = float(20 + ((years - 2) *7))
    if years <= 2:
        print(f'Your dog is {first_two} years old in dog years.')
    else:
        print(f'Your dog is {remaining} years on in dog years.')

dog_years(years)

EXERISE 4

a = int(input('Enter length A of your triangle: '))
b = int(input('Enter length B of your triangle: '))
c = int(input('Enter length C of your triangle: '))

if a + b + c == 180:
    if a == b == c:
        print(f'this is an equilateral triangle with sides of {a}, {b}, and {c}')
    elif a == b or b == c or c == a:
        print(f'this is an isosceles triangle with sides of {a}, {b}, and {c}')
    else:
        print(f'this is a scalene triangle with sides of {a}, {b}, and {c}')
else:
    print('this is not a triangle')

EXERCISE 5

nterms = 50
n1, n2 = 0, 1
count = 0
   
while count < nterms:
    print(f'term: {count} / number: {n1}')
    num = n1 + n2
    n1 = n2
    n2 = num
    count += 1

EXERCISE 6

month = input(('Enter the month of the year (Jan - Dec): ').lower())

day = int(input('Enter the day of the month: '))

if month == 'dec' and day >= 21 or month == 'jan' or month == 'feb' or month == 'mar' and day <= 19:
    print(f'{month} {day} is in Winter')
elif month == 'mar' and day >= 20 or month == 'apr' or month == 'may' or month == 'jun' and day <= 20:
    print(f'{month} {day} is in Spring')
elif month == 'jun' and day >= 21 or month == 'jul' or month == 'aug' or month == 'sep' and day <= 21:
    print(f'{month} {day} is in Summer')
elif month == 'sep' and day >= 22 or month == 'oct' or month == 'nov' or month == 'dec' and day <= 20:
    print(f'{month} {day} is in Autumn')


