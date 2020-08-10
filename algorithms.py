import random

def bubblesort(window, tk, data):
  iterations = 0
  swapped = True
  end = len(data)-1
  while swapped:
    swapped = False
    for i in range(end):
      iterations += 1
      if data[i] > data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
        swapped = True
        window.draw_graph(data, [i ,i+1])
        tk.update()
    end -= 1

  return iterations

def selectionsort(window, tk, data):
  iterations = 0
  for i in range(len(data)-1):
    min = i
    for j in range(i+1, len(data)):
      iterations += 1
      if data[j] < data[min]:
        min = j
    data[i], data[min] = data[min], data[i]
    window.draw_graph(data, [i, min])
    tk.update()

  return iterations

def insertionsort(window, tk, data):
  iterations = 0
  for i in range(1, len(data)):
    cur = data[i]
    j = i-1
    while j >= 0 and cur < data[j]:
      iterations += 1
      data[j+1] = data[j]
      window.draw_graph(data, [j+1, j])
      tk.update()
      j -= 1
    data[j+1] = cur
    window.draw_graph(data, [j+1, i])
    tk.update()

  return iterations

# iterative
def mergesort(window, tk, data, low=0, high=34):
  temp = [data[i] for i in range(35)]
  iterations = 0
  m = 1
  while m <= high - low:
    for i in range(low, high, 2*m):
      iterations += 1
      left = i
      mid = i + m - 1
      right = min(i + 2*m - 1, high)

      iterations += merge(window, tk, data, temp, left, mid, right)

    m *= 2

  return iterations

def merge(window, tk, data, temp, left, mid, right):
  iterations = 0
  k, i, j = left, left, mid + 1

  while i <= mid and j <= right:
    window.draw_graph(data, [i, j])
    tk.update()
    if data[i] < data[j]:
      temp[k] = data[i]
      i += 1
    else:
      temp[k] = data[j]
      j += 1
    k += 1
    iterations += 1

  while i < 34 and i <= mid:
    window.draw_graph(data, [i])
    tk.update()
    iterations += 1
    temp[k] = data[i]
    i += 1
    k += 1

  for i in range(left, right+1):
    data[i] = temp[i]

  window.draw_graph(data)
  tk.update()

  return iterations

'''# recursive
def mergesort(window, tk, data, start=0, end=35, level=1, iterations=0):
  if len(data) == 1:
    return iterations, data

  middle = len(data)//2
  its, left = mergesort(window, tk, data[:middle], start, middle, level+1)
  iterations += its
  its, right = mergesort(window, tk, data[middle:], middle, end, level+1)
  iterations += its

  its, merged_data = merge(window, tk, left, right)
  iterations += its
  if level != 1:
    return iterations, merged_data
  else:
    data = merged_data
    window.draw_graph(data)
    tk.update()
    return iterations

def merge(window, tk, left, right):
  iterations = 0
  data = []
  while len(left) > 0 and len(right) > 0:
    iterations += 1
    window.draw_graph(window.data, [left[0], right[0]])
    tk.update()
    if left[0] < right[0]:
      data.append(left[0])
      left.pop(0)
    else:
      data.append(right[0])
      right.pop(0)

  if len(left) == 0:
    data.extend(right)
  else:
    data.extend(left)

  return iterations, data'''

def shellsort(window, tk, data):
  iterations = 0
  gap = len(data)//2

  while gap > 0:
    for i in range(gap, len(data)):
      iterations += 1
      cur = data[i]

      j = i
      while j >= gap and data[j-gap] > cur:
        data[j] = data[j-gap]
        window.draw_graph(data, [j, j-gap])
        tk.update()
        j -= gap

      data[j] = cur
      window.draw_graph(data, [j, i])
      tk.update()
    gap //= 2

  return iterations

def quicksort(window, tk, data, low, high, iterations=0):
  if low < high:
    pi, its = partition(window, tk, data, low, high)
    iterations += its
    iterations += quicksort(window, tk, data, low, pi-1)
    iterations += quicksort(window, tk, data, pi+1, high)

  return iterations

def partition(window, tk, data, low, high):
  iterations = 0
  pivot = data[high]
  i = low-1

  for j in range(low, high):
    iterations += 1
    if data[j] < pivot:
      i += 1
      data[i], data[j] = data[j], data[i]
      window.draw_graph(data, [i, j])
      tk.update()
  data[i+1], data[high] = data[high], data[i+1]
  window.draw_graph(data, [i+1, high])
  tk.update()

  return (i+1), iterations

def heapsort(window, tk, data):
  iterations = 0
  for i in range(len(data)//2-1, -1, -1):
    iterations += 1
    heapify(window, tk, data, len(data), i)

  for i in range(len(data)-1, 0, -1):
    iterations += 1
    data[i], data[0] = data[0], data[i]
    window.draw_graph(data, [0, i])
    tk.update()
    heapify(window, tk, data, i, 0)

  return iterations

def heapify(window, tk, data, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and data[i] < data[l]:
    largest = l
  if r < n and data[largest] < data[r]:
    largest = r
  if largest != i:
    data[i], data[largest] = data[largest], data[i]
    window.draw_graph(data, [i, largest])
    tk.update()

    heapify(window, tk, data, n, largest)

def combsort(window, tk, data):
  iterations = 0
  gap = len(data)
  swapped = True

  while gap != 1 or swapped:
    swapped = False
    gap = getNextGap(gap)

    for i in range(len(data)-gap):
      iterations += 1
      if data[i] > data[i+gap]:
        data[i], data[i+gap] = data[i+gap], data[i]
        window.draw_graph(data, [i, i+gap])
        tk.update()
        swapped = True

  return iterations

def getNextGap(gap):
  gap = int(gap/1.3)
  if gap < 1:
    return 1
  return gap

def cocktailsort(window, tk, data):
  iterations = 0
  swapped = True
  start = 0
  end = len(data) - 1

  while swapped:
    swapped = False

    for i in range(start, end):
      iterations += 1
      if data[i] > data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
        window.draw_graph(data, [i, i+1])
        tk.update()
        swapped = True

    if not swapped:
      break

    swapped = False
    end -= 1

    for i in range(end, start, -1):
      iterations += 1
      if data[i] < data[i-1]:
        data[i], data[i-1] = data[i-1], data[i]
        window.draw_graph(data, [i, i-1])
        tk.update()
        swapped = True

    start += 1

  return iterations

def monkeysort(data):
  while not is_sorted(data):
    random.shuffle(data)

  return data

def is_sorted(data):
  for i in range(len(data)-1):
    if data[i] > data[i+1]:
      return False

  return True

def generate_data():
  data = []
  for i in range(1, 36):
    data.append(i)
  random.shuffle(data)

  return data





'''data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = bubblesort(data_to_be_sorted)
print('Bubble Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = selectionsort(data_to_be_sorted)
print('Selection Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = insertionsort(data_to_be_sorted)
print('Insertion Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = mergesort(data_to_be_sorted)
print('Merge Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = shellsort(data_to_be_sorted)
print('Shell Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = quicksort(data_to_be_sorted, 0, len(data_to_be_sorted)-1)
print('Quick Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = heapsort(data_to_be_sorted)
print('Heap Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = combsort(data_to_be_sorted)
print('Comb Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = cocktailsort(data_to_be_sorted)
print('Cocktail Sort: ' + str(data_sorted))

data_to_be_sorted = []
for i in range(1, 51):
  data_to_be_sorted.append(i)
random.shuffle(data_to_be_sorted)
data_sorted = monkeysort(data_to_be_sorted)
print('Monkey Sort: ' + str(data_sorted))'''
