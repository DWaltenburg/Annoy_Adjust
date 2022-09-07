from tkinter import *

on = True


def set_off():
    on = False
    print("off")


def set_on():
    on = True
    print("on")


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Annoying Sound Mixer")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

        onButton = Button(self, text="On", command=set_on)
        onButton.place(x=100, y=100)

        offButton = Button(self, text="Off", command=set_off)
        offButton.place(x=300, y=100)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
