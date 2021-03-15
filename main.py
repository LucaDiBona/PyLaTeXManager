from latexFile import latexFile
running=True
while running:
    command=input("> ") #TODO Replace with reasonable TUI (curses maybe)
    x=latexFile("test.txt")

    if command=="kill":
        running = False