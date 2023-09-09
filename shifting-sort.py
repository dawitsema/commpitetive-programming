def shifting_sort(a):
  """
  Sorts the given array using no more than n cyclic shifts.

  Args:
    a: The array to sort.

  Returns:
    A list of cyclic shifts that can be used to sort the array.
  """
  n = len(a)

  # Initialize the sorted array.
  sorted_a = [None] * n

  # Initialize the queue of unsorted elements.
  queue = []
  for i in range(n):
    queue.append(i)

  # Iterate until the queue is empty.
  while queue:
    # Get the next unsorted element.
    i = queue.pop(0)

    # Find the smallest element in the sorted array that is greater than a[i].
    j = 0
    while sorted_a[j] is None or sorted_a[j] <= a[i]:
      j += 1

    # If such an element exists, then shift the sorted array to make room for a[i].
    if j < n:
      # Shift the elements from sorted_a[j] to sorted_a[i - 1] one position to the right.
      for k in range(i - 1, j, -1):
        sorted_a[k + 1] = sorted_a[k]

      # Insert a[i] into sorted_a[j].
      sorted_a[j] = a[i]

    # Add the elements after a[i] to the queue.
    for k in range(i + 1, n):
      queue.append(k)

  # Return the cyclic shifts that were used to sort the array.
  return [(i, j, d) for i, j in enumerate(sorted_a) if a[i] != j]

def main():
  """
  The main function.
  """
  t = int(input())

  for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cyclic_shifts = shifting_sort(a)

    print(len(cyclic_shifts))
    for i, j, d in cyclic_shifts:
      print(i, j, d)

if __name__ == '__main__':
  main()
