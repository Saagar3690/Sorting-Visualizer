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

  # initialize UI and draw the graphs
  def __initUI(self):
    self.parent.title('Sorting Visualizer')
    self.grid(row=self.row, column=self.col)
    # canvas for the board to be drawn
    self.canvas = Canvas(self, bg=self.color, width=WIDTH, height=HEIGHT)
    self.canvas.pack(fill=BOTH, side=TOP)
    # generate data
    self.data = algorithms.generate_data()
    # draw the graph
    self.draw_graph(self.data)
    # algorithm label
    label = Label(self, text=self.algorithm)
    label.pack()
    # start button
    start = Button(self, text='Start', command=self.__run_algorithm, bd=30)
    start.pack()

  def __run_algorithm(self):
    # time start
    start = time.time()
    # call algorithm function
    if self.algorithm != 'Quick Sort':
      iterations = self.algorithmCall(self, self.parent, self.data)
    else:
      iterations = self.algorithmCall(self, self.parent, self.data, 0, len(self.data)-1)
    # total time for algorithm to run
    totalTime = time.time() - start
    # update title to total time and number of iterations
    self.parent.title('Algorithm: %s\t\tTime: %fs\t\tIterations: %d' % (self.algorithm, totalTime, iterations))
    # after 4 seconds...
    self.after(4000)
    # clear the graph
    self.draw_graph(self.data, done=True)
    # generate new data
    self.data = algorithms.generate_data()
    # draw new graph
    self.draw_graph(self.data)
    # reset title
    self.parent.title('Sorting Visualizer')

  def draw_graph(self, data, cur=[], done=False):
    # clear previous version of graph
    self.canvas.delete('all')
    # for all elements in graph
    for i in range(35):
      # if the algorithm has already run, show the graph being cleared and a new graph being generated
      if done:
        self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, fill='black', outline='white')
        self.parent.update()
        self.after(30)
      else:
        # make current bar in graph white if it is one of the bars whose position was just swapped, else add a normal bar
        if i in cur:
          self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, fill='white', outline='black')
        else:
          self.canvas.create_rectangle(8*i + MARGIN * 3, HEIGHT - 8 * data[i], 8*(i+1) + MARGIN * 3, HEIGHT, outline='black')
