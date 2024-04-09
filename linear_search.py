def linear_search(collection, element):
  for j in range(len(collection)):
    if collection[j] == element:
      return j
  return None

print(linear_search([2, 4, 1, 0], int(input())))