import time
import algorithms
import ui

from tkinter import *

def main():
  root = Tk()
  root.title('Sorting Visualizer')

  # each sorting algorithm component
  bswindow = ui.UI(root, 'Bubble Sort', algorithms.bubblesort, 0, 0, 'red')
  sswindow = ui.UI(root, 'Selection Sort', algorithms.selectionsort, 0, 1, 'orange')
  iswindow = ui.UI(root, 'Insertion Sort', algorithms.insertionsort, 0, 2, 'yellow')
  mswindow = ui.UI(root, 'Merge Sort', algorithms.mergesort, 1, 0, 'green')
  sswindow = ui.UI(root, 'Shell Sort', algorithms.shellsort, 1, 1, 'turquoise')
  qswindow = ui.UI(root, 'Quick Sort', algorithms.quicksort, 1, 2, 'blue')
  hswindow = ui.UI(root, 'Heap Sort', algorithms.heapsort, 2, 0, 'purple')
  cswindow = ui.UI(root, 'Comb Sort', algorithms.combsort, 2, 1, 'violet')
  ctswindow = ui.UI(root, 'Cocktail Sort', algorithms.cocktailsort, 2, 2, 'pink')
  root.mainloop()

# main
if __name__ == '__main__':
  main()
