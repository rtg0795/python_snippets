import tkinter


class myApplication:
    def __init__(self, root):
        self.root = root
        self.initialisation()

    def initialisation(self):
        tkinter.Label(self.root, text='Hello World!').grid(row=0, column=0)


def main():
    root = tkinter.Tk()
    root.title('My Application')
    app = myApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()