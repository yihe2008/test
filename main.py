print("hello world")


def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  print(arr)


print(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

