from tkinter import *
import algorithms
import time

MARGIN = 5
SIDE = 33
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class UI(Frame):
  def __init__(self, parent, algorithm, algorithmCall, row, col, color, data=[]):
    self.parent = parent
    self.algorithm = algorithm
    self.algorithmCall = algorithmCall
    Frame.__init__(self, parent)
    self.row, self.col = row, col
    self.color = color
    self.data = data
    self.__initUI()

  # initialize UI and draw the board
  def __initUI(self):
    self.parent.title('Sorting Visualizer')
    self.grid(row=self.row, column=self.col)
    # canvas for the board to be drawn
    self.canvas = Canvas(self, bg=self.color, width=WIDTH, height=HEIGHT)
    self.canvas.pack(fill=BOTH, side=TOP)
    self.data = algorithms.generate_data()
    self.draw_graph(self.data)
    label = Label(self, text=self.algorithm)
    label.pack()
    start = Button(self, text='Start', command=self.__run_algorithm, bd=30)
    start.pack()

  def __run_algorithm(self):
    start = time.time()
    if self.algorithm != 'Quick Sort':
      iterations = self.algorithmCall(self, self.parent, self.data)
    else:
      iterations = self.algorithmCall(self, self.parent, self.data, 0, len(self.data)-1)
    totalTime = time.time() - start
    self.parent.title('Algorithm: %s\t\tTime: %fs\t\tIterations: %d' % (self.algorithm, totalTime, iterations))
    self.after(4000)
    self.draw_graph(self.data, done=True)
    self.data = algorithms.generate_data()
    self.draw_graph(self.data)
    self.parent.title('Sorting Visualizer')

  def draw_graph(self, data, cur=[], done=False):
    self.canvas.delete('all')
    for i in range(35):
      if done:
        self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, fill='black', outline='white')
        self.parent.update()
        self.after(30)
      else:
        if i in cur:
          self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, fill='white', outline='black')
        else:
          self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, outline='black')

  '''# redraw the board after the value of a cell changes
  def redraw(self, board, row, col, iterations=0, time=0):
    # time and iterations
    self.parent.title('Time: %fs\tIterations: %d' % (time, iterations))
    # reset canvas
    self.canvas.delete('all')
    # redraw the board
    self.__draw_board(board, row, col)

  # draw the board
  def __draw_board(self, board, row=-1, col=-1):
    self.__draw_cells(row, col)
    self.__draw_grid()
    self.__draw_values(board)

  # draw the grid
  def __draw_grid(self):
    # 10 lines
    for i in range(10):
      # black for main lines that separate board into 3x3, gray for other sublines
      color = "black" if i % 3 == 0 else "gray"

      # Horizontal Lines
      x0 = MARGIN
      y0 = MARGIN + i * SIDE
      x1 = WIDTH - MARGIN
      self.canvas.create_line(x0, y0, x1, y0, fill=color)

      # Vertical Lines
      x0 = MARGIN + i * SIDE
      y0 = MARGIN
      y1 = HEIGHT - MARGIN
      self.canvas.create_line(x0, y0, x0, y1, fill=color)

  # draw the cells
  def __draw_cells(self, row=-1, col=-1):
    # column
    for i in range(9):
      # row
      for j in range(9):
        x0 = MARGIN + i * SIDE
        y0 = MARGIN + j * SIDE
        x1 = MARGIN + (i+1) * SIDE
        y1 = MARGIN + (j+1) * SIDE
        if col != i or row != j:
          # all other cells
          self.canvas.create_rectangle(x0, y0, x1, y1, outline='gray')
        else:
          # current cell
          self.canvas.create_rectangle(x0, y0, x1, y1, outline='red', width=3)

  # draw the values in the cells
  def __draw_values(self, board):
    # delete the values the solver generated
    self.canvas.delete('numbers')
    # row
    for i in range(9):
      # column
      for j in range(9):
        # center of cell
        x = MARGIN + j * SIDE + SIDE / 2
        y = MARGIN + i * SIDE + SIDE / 2
        # temporary variable for current coordinates
        tmp = [i, j]
        # if current coordinates is  part of the clues (the given values at the beginning), color of values of clues is black
        if not tmp in self.clues:
          # if current cell's value is not empty (0), color of the values are gray
          if board[i][j] != 0:
            self.canvas.create_text(x, y, text=board[i][j], tags='numbers', fill='gray')
        else:
          self.canvas.create_text(x, y, text=board[i][j], tags='clues', fill='black')'''
