def recursive_binary_search(array, v, p, r):
  print('-------------------------------------------------------')
  print(f'array: {array}\np: {p}\nr: {r}\nsub-array: {array[p:r+1]}')

  if p > r: # caso base
    print(f'i didnt found it')
    return -1

  q = (p+r) // 2
  print(f'q = {q}')

  if v == array[q]:
    print(f'i found it! its index is {q}')
    return q

  if v < array[q]:
    print('im gonna search on the left side')
    return recursive_binary_search(array, v, p, q-1)

  if v > array[q]:
    print('im gonna search on the right side')
    return recursive_binary_search(array, v, q+1, r)

def main():
  array = [1, 2, 3, 4, 5, 6]
  v = 7
  print(f'searching for value {v}')

  p = 0
  r = len(array) - 1

  i = recursive_binary_search(array, v, p, r)

if __name__ == '__main__':
  main()