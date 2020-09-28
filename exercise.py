# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# if color == 'green':
#     print('Go!')
# elif color == 'yellow':
#     print('Slow down!')
# elif color == 'red':
#     print('Stop!')
# else:
#     print('Bogus!')

hours  = int(input('Enter hours worked:'))

rate = 10

overtime = int((hours - 40) * (1.5 * rate))

paycheck = 0

if hours <= 40:
    paycheck += (int(hours * rate))
else:
    paycheck += (int((hours * rate) + (overtime)))

print(f'Pay: {paycheck}')