from utilities import *
import tkinter as tk

root = tk.Tk(className='sorting visualizer')
root.geometry("800x400")
frame = tk.Frame(root, height=100, width=200, background='lightblue', bd = 2)
frame.pack()
label = tk.Label(frame, font=('Helvetica', 20), text= "Swarm inbound")
label.pack()

root.mainloop()





#list_length = inputListLength()
#num_range_low = inputLowRange()
#num_range_high = inputHighRange()
#unsorted_list = createList(list_length, num_range_low, num_range_high)
#sorted_list = bubbleSort(unsorted_list, list_length)


