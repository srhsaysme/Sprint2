from GameWindow import *

def main():
    x = GameWindow()
    x.headerFrame.grid(row = 0, column = 1)
    x.redFrame.grid(row = 1, column = 0)
    x.gridFrame.grid(row = 1, column = 1)
    x.blueFrame.grid(row = 1, column = 2)
    x.scoreFrame.grid(row = 2, column = 1)
    x.charEntryFrame.grid(row = 3, column = 1)
    x.window.mainloop()

if __name__ == "__main__":
    main()