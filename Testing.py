from tkinter import *

def print_value(row, col):
    print (find_in_grid(root, row, col).cget())


def find_in_grid(frame, row, column):
    for children in frame.children.values():
        info = children.grid_info()
        #note that rows and column numbers are stored as string
        if info['row'] == str(row) and info['column'] == str(column):
            return children
    return None

root = Tk()

height = 5
width = 1
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="", width=100)
        b.grid(row=i, column=j)

height = 5
width = 1
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Button(root, text="print value", command=lambda i=i,j=j: print_value(i,j), width=10)
        b.grid(row=i, column=j+1)


mainloop()
