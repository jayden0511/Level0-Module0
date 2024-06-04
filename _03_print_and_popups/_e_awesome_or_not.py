from tkinter import messagebox, simpledialog, Tk
import random
messagebox.showinfo()
# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    a= random.randint(0, 2)
    # 2. Print your variable to the console
    print(a)
    # 3. Get the user to enter something that they think is awesome
    d=simpledialog.askstring('hat', 'something that they think is awesome')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if a==0:
        messagebox.showinfo('bird', 'tell the user whatever they emtered is awesome')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if a==1:
        messagebox.showinfo('gorilla' 'tell whatever they entered is ok')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if a==2:
        messagebox.showinfo('elephant', 'tell the user whatever they entered is boring')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if a==3:
        messagebox.showinfo('apple', 'invent your own message to give to the user')
    # Run the window's .mainloop() method
    window.mainloop()
