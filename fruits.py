prices = {
  'banana': 4,
  'apple': 2,
  'orange': 1.5,
  'pear': 3
  }

stock = {
  'banana': 4,
  'apple': 5,
  'orange': 6,
  'pear': 7
}

for price in prices:
  print(f'{price}')
  print(f'Price: {prices[price]}')
  print(f'Stock: {stock}')
total = 0
for price in prices:
  inventory = prices[price] * stock[price]
  total += inventory
print(f'Total: {total}')