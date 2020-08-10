import time
import algorithms
import ui

from tkinter import *

def main():
  root = Tk()
  root.title('Sorting Visualizer')

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

'''# creates second frame with board
def generate(input):
  # based on input, generate custom or random board of specific level
  if input == 'easy' or input == 'medium' or input == 'hard' or input == 'expert':
    board = game.user_input('r', input)
  else:
    board = game.user_input('c', input)

  # clues (numbers given on board at the start)
  clues = []
  for row in  range(9):
    for col in range(9):
      if board[row][col] != 0:
        clues.append([row, col])

  # create second frame
  top = Toplevel()
  # sudoku ui - the board
  window = ui.UI(top, board, clues)
  # start the solving algorithm
  start_button = Button(top, text="Start", width=10, command=lambda : start(board, window, top))
  start_button.pack()
  # close the second frame and go back to home
  back_button = Button(top, text="Go Back", width=10, command=top.destroy)
  back_button.pack(pady=(0, 10))

# starts the backtracking algorithm
def start(board, window, top):
  # start time
  start = time.time()

  # tracker for when algorithm is finished
  done = False
  while True:
    top.update_idletasks()
    top.update()
    # backtracking algorithm called to solve the board
    game.solve(board, window, top, start)
    # once algorithm finishes, update the time taken and number of iterations
    if not done:
      window.redraw(board, -1, -1, game.iterations, round(time.time() - start, 10))
      done = True'''

# main
if __name__ == '__main__':
  main()
