import tkinter as tk


class Window:

    root = tk.Tk()
    root.title('Main wingow')
    root.geometry('300x300')

class Button(tk.Button):

    def make_button(self):
        btn = Button()
        btn.grid()



class Main:

    a = Window()
    b = Button()
    b.make_button()
    a.root.mainloop()


