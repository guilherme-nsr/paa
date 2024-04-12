INFINITY = float('inf')

def merge_sort_cormen(array, p, r):
  if p >= r:
    return

  q = (p+r) // 2 # dividir
  
  merge_sort_cormen(array, p, q) # conquistar
  merge_sort_cormen(array, q+1, r) # conquistar
  merge(array, p, q, r) # combinar

def merge(array, p, q, r):
  n1 = q - p + 1
  n2 = r - q

  left = [array[p+i] for i in range(n1)]
  left.append(INFINITY)

  right = [array[q+i+1] for i in range(n2)]
  right.append(INFINITY)

  i, j, k = 0, 0, p

  while k <= r:
    if left[i] <= right[j]:
      array[k] = left[i]
      i = i + 1
    else:
      array[k] = right[j]
      j = j + 1
    k = k + 1

def main():
  array = [-3, 2, 1, 0, -2, 3, -1]
  print(f'array: {array}')

  p = 0
  r = len(array) - 1

  merge_sort_cormen(array, p, r)
  print(f'ordered array: {array}')

if __name__ == '__main__':
  main()