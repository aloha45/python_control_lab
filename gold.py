inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashells', 'strange berry', 'lint']

print(inventory)

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

print(inventory)
