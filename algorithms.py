import random

# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubblesort(window, tk, data):
  # iteration counter
  iterations = 0
  # boolean for if swaps occurred
  swapped = True
  # end of traversal counter
  end = len(data)-1
  # while there has been a swap
  while swapped:
    swapped = False
    # traverse the list from 0 to where you ended last time (end)
    for i in range(end):
      # increment iterations
      iterations += 1
      # check if elements are out of order (current element is bigger than the next element)
      if data[i] > data[i+1]:
        # swap
        data[i], data[i+1] = data[i+1], data[i]
        swapped = True
        # redraw graph
        window.draw_graph(data, [i ,i+1])
        tk.update()
    # decrement the end as everything after it is already in order
    end -= 1

  return iterations

# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selectionsort(window, tk, data):
  # iteration counter
  iterations = 0
  # traverse all elements
  for i in range(len(data)-1):
    # set location of minimum to ith element
    min = i
    # traverse from i+1 to end of list as everything before is already in order
    for j in range(i+1, len(data)):
      # increment iterations
      iterations += 1
      # if current element is smaller than the minimum element, set location of min to current element
      if data[j] < data[min]:
        min = j
    # swap min element with first found element
    data[i], data[min] = data[min], data[i]
    # redraw graph
    window.draw_graph(data, [i, min])
    tk.update()

  return iterations

# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def insertionsort(window, tk, data):
  # iteration counter
  iterations = 0
  # traverse 1 through end of list
  for i in range(1, len(data)):
    # current element
    cur = data[i]
    j = i-1
    # move elements of list that are greater than the current element up one position
    while j >= 0 and cur < data[j]:
      # increment iterations
      iterations += 1
      data[j+1] = data[j]
      # redraw graph
      window.draw_graph(data, [j+1, j])
      tk.update()
      j -= 1
    # put current element in proper position
    data[j+1] = cur
    # redraw graph
    window.draw_graph(data, [j+1, i])
    tk.update()

  return iterations

# Iterative Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def mergesort(window, tk, data, low=0, high=34):
  # temp list with same values as data
  temp = [data[i] for i in range(35)]
  # iteration counter
  iterations = 0
  m = 1
  # divide array into blocks of size m
  while m <= high - low:
    # for m = 1, i = 0, 2, 4, 6, 8
    # for m = 2, i = 0, 4, 8
    # for m = 3, i = 0, 8
    for i in range(low, high, 2*m):
      # increment iterations
      iterations += 1
      # left, mid, right
      left = i
      mid = i + m - 1
      right = min(i + 2*m - 1, high)

      iterations += merge(window, tk, data, temp, left, mid, right)

    m *= 2

  return iterations

# Helper method for Iterative Merge Sort
def merge(window, tk, data, temp, left, mid, right):
  # iteration counter
  iterations = 0
  k, i, j = left, left, mid + 1

  # traverse while there are elements in left and right side
  while i <= mid and j <= right:
    # redraw graph
    window.draw_graph(data, [i, j])
    tk.update()
    # compare left and right side and store smaller value into temp list
    if data[i] < data[j]:
      temp[k] = data[i]
      i += 1
    else:
      temp[k] = data[j]
      j += 1
    k += 1
    # increment iterations
    iterations += 1

  # add remaining elements to list
  while i < 34 and i <= mid:
    # redraw graph
    window.draw_graph(data, [i])
    tk.update()
    # increment iterations
    iterations += 1
    temp[k] = data[i]
    i += 1
    k += 1

  # copy from temp list to original data array
  for i in range(left, right+1):
    data[i] = temp[i]

  # redraw graph
  window.draw_graph(data)
  tk.update()

  return iterations

'''
# Recursive Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def mergesort(window, tk, data, start=0, end=35, level=1, iterations=0):
  # base case: only one element in the list
  if len(data) == 1:
    return iterations, data

  # calculate middle
  middle = len(data)//2
  # recursively call left side
  its, left = mergesort(window, tk, data[:middle], start, middle, level+1)
  iterations += its
  # recursively call right side
  its, right = mergesort(window, tk, data[middle:], middle, end, level+1)
  iterations += its

  # merge left and right
  its, merged_data = merge(window, tk, left, right)
  iterations += its
  if level != 1:
    return iterations, merged_data
  else:
    data = merged_data
    window.draw_graph(data)
    tk.update()
    return iterations

# Helper method for Recursive Merge Sort
def merge(window, tk, left, right):
  # iteration counter
  iterations = 0
  data = []

  # traverse while there are elements in left and right side
  while len(left) > 0 and len(right) > 0:
    # increment iterations
    iterations += 1
    # redraw graph
    window.draw_graph(window.data, [left[0], right[0]])
    tk.update()
    # compare left and right side and store smaller value into temp list
    if left[0] < right[0]:
      data.append(left[0])
      left.pop(0)
    else:
      data.append(right[0])
      right.pop(0)

  # add any remaining elements
  if len(left) == 0:
    data.extend(right)
  else:
    data.extend(left)

  return iterations, data
'''

# Shell Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def shellsort(window, tk, data):
  # iteration counter
  iterations = 0
  # big gap
  gap = len(data)//2

  # gapped insertion sort
  # The first gap elements a[0..gap-1] are already in gapped order keep adding one more element until the entire array is gap sorted
  while gap > 0:
    for i in range(gap, len(data)):
      # increment iterations
      iterations += 1
      # current element
      cur = data[i]

      # shift earlier gap-sorted elements up until the correct
      # location for a[i] is found
      j = i
      while j >= gap and data[j-gap] > cur:
        data[j] = data[j-gap]
        # redraw graph
        window.draw_graph(data, [j, j-gap])
        tk.update()
        j -= gap

      # put current element in its correct location
      data[j] = cur
      # redraw graph
      window.draw_graph(data, [j, i])
      tk.update()

    # make gap smaller
    gap //= 2

  return iterations

# Quick Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def quicksort(window, tk, data, low, high, iterations=0):
  if low < high:
    # partitioning index, so that data[pi] is in the correct place
    pi, its = partition(window, tk, data, low, high)
    iterations += its
    # sort elements before and after partition
    iterations += quicksort(window, tk, data, low, pi-1)
    iterations += quicksort(window, tk, data, pi+1, high)

  return iterations

# Helper method for Quick Sort
def partition(window, tk, data, low, high):
  # iteration counter
  iterations = 0
  # pivot
  pivot = data[high]
  # index of smaller element
  i = low-1

  for j in range(low, high):
    # increment iterations
    iterations += 1
    # if current element is smaller than the pivot
    if data[j] < pivot:
      # increment index of smaller element
      i += 1
      # swap
      data[i], data[j] = data[j], data[i]
      # redraw graph
      window.draw_graph(data, [i, j])
      tk.update()
  data[i+1], data[high] = data[high], data[i+1]
  # redraw graph
  window.draw_graph(data, [i+1, high])
  tk.update()

  return (i+1), iterations

# Heap Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def heapsort(window, tk, data):
  # iteration counter
  iterations = 0

  # build a maxheap
  for i in range(len(data)//2-1, -1, -1):
    # increment iterations
    iterations += 1
    heapify(window, tk, data, len(data), i)

  # extract elements one by one
  for i in range(len(data)-1, 0, -1):
    # increment iterations
    iterations += 1
    # swap
    data[i], data[0] = data[0], data[i]
    # redraw graph
    window.draw_graph(data, [0, i])
    tk.update()
    heapify(window, tk, data, i, 0)

  return iterations

# Helper method for Heap Sort
def heapify(window, tk, data, n, i):
  # largest is the root
  largest = i
  # left
  l = 2 * i + 1
  # right
  r = 2 * i + 2

  # if left child exists and is greater than root
  if l < n and data[i] < data[l]:
    largest = l
  # if right child exists and is greater than root
  if r < n and data[largest] < data[r]:
    largest = r
  # change root if necessary
  if largest != i:
    data[i], data[largest] = data[largest], data[i]
    # redraw graph
    window.draw_graph(data, [i, largest])
    tk.update()

    # heapify root
    heapify(window, tk, data, n, largest)

# Comb Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def combsort(window, tk, data):
  # iteration counter
  iterations = 0
  # initialize gap
  gap = len(data)
  # boolean for if swaps have been made
  swapped = True

  # keeps running while gap is more than 1 or last iteration had a swap
  while gap != 1 or swapped:
    swapped = False
    # get next gap
    gap = getNextGap(gap)

  # compare all elements with current c\gap
    for i in range(len(data)-gap):
      # increment iterations
      iterations += 1
      # compare ith and ith+gap elements
      if data[i] > data[i+gap]:
        # swap
        data[i], data[i+gap] = data[i+gap], data[i]
        # redraw graph
        window.draw_graph(data, [i, i+gap])
        tk.update()
        swapped = True

  return iterations

# Helper method for Comb Sort
def getNextGap(gap):
  # shrink gap factor by 1.3
  gap = int(gap/1.3)
  if gap < 1:
    return 1
  return gap

# Cocktail Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def cocktailsort(window, tk, data):
  # iteration counter
  iterations = 0
  # boolean for if swaps have been made
  swapped = True
  # start of traversal
  start = 0
  # end of traversal
  end = len(data) - 1

  # while swaps have occurred
  while swapped:
    # reset swapped to False
    swapped = False

    # traverse left to right like bubble sort
    for i in range(start, end):
      # increment iterations
      iterations += 1
      # compare elements - ith and ith+1
      if data[i] > data[i+1]:
        # swap
        data[i], data[i+1] = data[i+1], data[i]
        # redraw graph
        window.draw_graph(data, [i, i+1])
        tk.update()
        swapped = True

    # if no swaps occurred, list is already sorted, so break out of loop
    if not swapped:
      break

    # reset swapped to False
    swapped = False
    # decrement end as everything after it is in the right place
    end -= 1

    # traverse right to left
    for i in range(end, start, -1):
      # increment iterations
      iterations += 1
      # compare elements - ith and ith-1
      if data[i] < data[i-1]:
        # swap
        data[i], data[i-1] = data[i-1], data[i]
        # redraw graph
        window.draw_graph(data, [i, i-1])
        tk.update()
        swapped = True

    # increment start as everything before it is in the right place
    start += 1

  return iterations

# Monkey Sort
# Time Complexity: O(infinity)
# Space Complexity: O(n)
def monkeysort(data):
  # if data is not sorted, generate a permutation of the data
  while not is_sorted(data):
    random.shuffle(data)

  return data

# Helper method for Monkey Sort
def is_sorted(data):
  # traverse through all elements
  for i in range(len(data)-1):
    # if ith and ith+1 elements are out place, list is not sorted, so return False
    if data[i] > data[i+1]:
      return False

  return True

# Generate a list of numbers 1-35 in random order
def generate_data():
  # initialize data to 1-35
  data = [i for i in range(1, 36)]
  # shuffle the order of elements
  random.shuffle(data)

  return data
