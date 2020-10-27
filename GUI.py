from tkinter import Label, Button, RAISED, Entry
import tkinter as tk
root = tk.Tk()


root.geometry("670x200")
buttons = [['MC', 'M+', 'M-', 'MR'],
          ['C' , '\u221a', 'x\u00b2', '+' ],
          ['7' , '8' , '9' , '-' ],
          ['4' , '5' , '6' , '*' ],
          ['1' , '2' , '3' , '/' ],
          ['0' , '.' , '+-', '=' ]]


for r in range (1,7):
    for c in range (2,6):
        w = Label(root, relief = RAISED, padx = 10, text = buttons[r-1][c-2])
        w.grid(row = r, column = c)



def show_entry_fields():
    print("Loan Amount: %s\nInterest Rate: %s\nLoan Terms" % (e1.get(), e2.get()))

   # mortgage = tk.Tk()

w =    tk.Label(root, 
         text="Loan Amount").grid(row=0)
w =    tk.Label(root, 
         text="Interest Rate").grid(row=1)
w =    tk.Label(root, 
         text="Loan Terms").grid(row=2)


e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e4 = tk.Entry(root)
e5 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=0, column=2,columnspan=4)

tk.Button(root, 
          text='Computer Mortgage', 
          command=root.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                   pady=4)




root.mainloop()
