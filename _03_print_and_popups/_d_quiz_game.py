from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    c=0
    # ASK A QUESTION AND CHECK THE ANSWER
    j=simpledialog.askstring('ask a question and check the answer', 'are you human')
    #      // 2.  Ask the user a question 

    #      // 3.  Use an if statement to check if their answer is correct
    if j == 'yes':
        c=c+1
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    j=simpledialog.askstring('rabit', 'do you like hot dogs')
    if j == 'yes':
        c=c+1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo('sea', 'your final score is' + str(c))
    # Run the window's .mainloop() method
    window.mainloop()
