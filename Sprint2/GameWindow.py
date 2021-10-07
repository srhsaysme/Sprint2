import tkinter as tk
import unittest as ut

class GameWindow:
    #Window setup
    window = tk.Tk()
    window.title("SOS Game")
    window.geometry("1000x600")

    #Sets up frames within window.
    headerFrame = tk.Frame(window)
    redFrame = tk.Frame(window)
    blueFrame = tk.Frame(window)
    gridFrame = tk.Frame(window)
    scoreFrame = tk.Frame(window)
    charEntryFrame = tk.Frame(window)

    redScoreLabel = tk.Label(scoreFrame, width = 3)
    blueScoreLabel = tk.Label(scoreFrame, width = 3)
    turnLabel = tk.Label(scoreFrame)
    announceLabel = tk.Label(scoreFrame)

    redSButton = tk.Radiobutton(redFrame, pady = 3, text = "S")
    redOButton = tk.Radiobutton(redFrame, pady = 3, text = "O")
    blueSButton = tk.Radiobutton(blueFrame, pady = 3, text = "S")
    blueOButton = tk.Radiobutton(blueFrame, pady = 3, text = "O")

    simpleButton = tk.Radiobutton(charEntryFrame, text = "Simple Game")
    complexButton = tk.Radiobutton(charEntryFrame, text = "Complex Game")

    xEntry = tk.Entry(charEntryFrame, width = 10)
    yEntry = tk.Entry(charEntryFrame, width = 10)

    redComputerBox = tk.Checkbutton(redFrame, text = "Computer")
    blueComputerBox = tk.Checkbutton(blueFrame, text = "Computer")

    addCharButton = tk.Button(charEntryFrame, text = "Add character")
    newGameButton = tk.Button(charEntryFrame, text = "New Game")

    #Label placements.
    tk.Label(headerFrame, text = "SOS Game").pack(fill = 'x')
    tk.Label(headerFrame, text = "By Stephen Holman").pack(fill = 'x')

    tk.Label(redFrame, text = "Red Player", pady = 15).pack()
    redSButton.pack()
    redOButton.pack()
    redComputerBox.pack(pady = 10)

    tk.Label(blueFrame, text = "Blue Player", pady = 15).pack()
    blueSButton.pack()
    blueOButton.pack()
    blueComputerBox.pack(pady = 10)

    tk.Label(scoreFrame, text = "Red Score: ").pack(side = 'left')
    redScoreLabel.pack(side = 'left')
    blueScoreLabel.pack(side = 'right')
    tk.Label(scoreFrame, text = "Blue Score: ").pack(side = 'right')
    announceLabel.pack()
    turnLabel.pack()

    tk.Label(charEntryFrame, text = "X value:").grid(row = 0, column = 0)
    xEntry.grid(row = 0, column = 1)
    tk.Label(charEntryFrame, text = "Y value:").grid(row = 0, column = 2)
    yEntry.grid(row = 0, column = 3)
    addCharButton.grid(row = 1, column = 0, columnspan = 4, pady = 10)
    tk.Label(charEntryFrame, text = "Game Type:").grid(row = 2, column = 0)
    simpleButton.grid(row = 2, column = 1)
    complexButton.grid(row = 2, column = 2)
    newGameButton.grid(row = 2, column = 3)

    #Playing Field placements.
    labelGrid = []
    for y in range(0, 8):
        tempGrid = []
        for x in range(0, 8):
            tempGrid.append(tk.Label(gridFrame, text = " ", height = 1, width = 1, padx = 5, relief = "ridge").grid(row = y, column = x))
        labelGrid.append(tempGrid)

    headerFrame.grid(row = 0, column = 1)
    redFrame.grid(row = 1, column = 0)
    gridFrame.grid(row = 1, column = 1)
    blueFrame.grid(row = 1, column = 2)
    scoreFrame.grid(row = 2, column = 1)
    charEntryFrame.grid(row = 3, column = 1)
    window.mainloop()