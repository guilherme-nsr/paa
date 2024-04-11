def merge_sort(array):

  print_separator()
  print(f'merge_sort({array})')

  if len(array) <= 1: # caso base
    print("caso base")
    return array

  # dividir
  mid_index = calc_mid_index(array)
  left, right = divide(array, mid_index)

  # conquistar
  left = merge_sort(left)
  right = merge_sort(right)

  # combinar
  return merge(left, right)

def merge(left, right):

  print_separator()
  print(f'merge({left}, {right})')

  result = []
  left_index, right_index = 0, 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1

    else:
      result.append(right[right_index])
      right_index += 1

  result.extend(left[left_index:])
  result.extend(right[right_index:])

  print('result: ', result)

  return result

def print_separator():
  print("--------------------------------------")

def calc_mid_index(array):
  mid_index = (len(array) + 1) // 2

  return mid_index

def divide(array, mid_index):
  left = array[:mid_index]
  right = array[mid_index:]

  return left, right

def main():
  array = [2, 1, 4, 5, 3, 6]
  ordered_array = merge_sort(array)

  print_separator()
  print("main()")
  print("ordered_array: ", ordered_array)

if __name__ == '__main__':
  main()