def insertion_sort(collection):
  
  for j in range(1, len(collection)):
    key = collection[j]
    i = j-1
    print("\nkey = ", key)
    print("A = ", collection)

    while i >= 0 and collection[i] > key:
      print("deslocando")
      collection[i+1] = collection[i]
      i = i-1
      print("A = ", collection)

    collection[i+1] = key

collection = [5, 4, 3, 2, 1]
insertion_sort(collection)
print(collection)