# class PlayerCharacter:
#     #dunder method
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def run(self):
#         print('run!')
#         return 'done'

# player1 = PlayerCharacter('cory', 32)

# print(player1.name)

# # help(player1)

# player2 = PlayerCharacter('cindy', 31)

# print(player2.run())


# given the class below

# class Cat:
#     species = 'mammals'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the cat object with 3 cats

# cat1 = Cat('cory', 7)
# cat2 = Cat('kailah', 5)
# cat3 = Cat('stavon', 6)

# # find the oldest cat

# cats = [cat1, cat2, cat3]

# sort_cats = sorted(cats, key=lambda cat: cat.age)

# # output 'the oldest cat is (name of cat) it is (age of cat) years old'

# old_cat = sort_cats.pop()

# print(f'the oldest cat is {old_cat.name} and it is {old_cat.age} years old')

# class Dog():
#     dog_id = 1

#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#         self.id = Dog.dog_id
#         Dog.dog_id += 1
    
#     def bark(self):
#         print(f'{self.name} says woof!!!')

#     def __str__(self):
#         return f"Dog ({self.id}) named {self.name} is {self.age} years old"
    
#     @classmethod
#     def get_total_dogs(cls):
#         return cls.dog._id - 1

# dog1 = Dog('JT', 3)
# dog2 = Dog('Elvis', 9)
# dog3 = Dog('Lola', 9)

# print(Dog.get_total_dogs())

# Decorator functions -- super charge our function @

def hello():
    print('hello')

greet = hello

print(greet())

def bye(func):
    return func()

def farewell():
    print('peacing out')

a = bye(farewell)

print(a)

# a decorator function from scratch

def my_decorator(func):
    def wrap_function():
        print('jt is a cute little boy')
        func()
        print('jt is the cutest little boy')
    return wrap_function

@my_decorator
def peace():
    print('later yo')

peace()