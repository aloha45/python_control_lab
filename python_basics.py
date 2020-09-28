# print('hello')

# greet = 'hayyyy'

# print(len(greet))

# quote = 'to be or not to be'

# print(quote.upper())

# print(quote.find('be'))

# print(quote.replace('be', 'me'))

# .append changes the list in place
#  doesn't produce a value
# adds only one thing

# .extend([]) adds multiple things

# .pop() -- returns whatever you just removed--the value of the index

# .remove() -- takes any value in the list

# pop removes by index, remove removes by value

# .clear() removes everything in lists

# .join() -- puts things together

# [::-1] --reverses a list, but creates a new list first

# list unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

# print(d)

# Dictionary aka dict

my_list = [
    {
        'a' : [1,2,3],
        'b' : 'hello',
        'c' : True,
    },
    {
        'a' : [4,5,6],
        'b' : 'goodbye',
        'c' : False,
    },
]

print(my_list[0]['a'][2])

user = {
    'basket': [],
    'greet': 'hello'
}

print(user.get('greet', 'wrong party bro'))