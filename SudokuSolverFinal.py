import tkinter as tk

Sudoku = [[0] * 9 for _ in range(9)]


def increment_num(x, y):
    global Sudoku
    Sudoku[y][x] = (Sudoku[y][x] + 1) % 10
    label = grid[y][x]
    label.config(text=Sudoku[y][x])
    # aktualizuje pole


def Mozne(x, y, num):

    for i in range(0, 9):
        if Sudoku[y][i] == num and i != x:
            return False
    # kontrola sloupcu

    for i in range(0, 9):
        if Sudoku[i][x] == num and i != y:
            return False
    # kontroluje radu

    xB = (x // 3) * 3  # x : 3 a zaokrouhli na nejblizsi cislo, pak x/3 * 3
    yB = (y // 3) * 3
    for X in range(xB, xB + 3):
        for Y in range(yB, yB + 3):
            if Sudoku[Y][X] == num:
                return False
    return True

# hledá číslo num na  pozicích x a y, porovnává, jestli se tam objevuje



def zavritokno():
    root.destroy()



def AnsweredSudoku():
    solved_window = tk.Tk()
    solved_window.title("Solved Sudoku")
    for y in range(9):
        for x in range(9):
            label = tk.Label(solved_window, text=Sudoku[y][x], font=("Comic Sans", 16), width=5, height=2, bg="yellow",
                             relief="solid", borderwidth=2)
            label.grid(row=y, column=x)


    close = tk.Button(solved_window, text="Close", command=solved_window.destroy)
    close.grid(row=9, column=4, pady=10)

    solved_window.mainloop()


def Solve():
    global Sudoku
    for y in range(9):
        for x in range(9):
            if Sudoku[y][x] == 0:
                for num in range(1, 10):
                    if Mozne(x, y, num):
                        Sudoku[y][x] = num
                        # update the label text
                        label = grid[y][x]
                        label.config(text=Sudoku[y][x])
                        root.update()  # update the GUI
                        Solve()
                        Sudoku[y][x] = 0
                return

    for y in range(9):
        for x in range(9):
            label = grid[y][x]
            label.config(text=Sudoku[y][x])
    root.withdraw()
    AnsweredSudoku()


root = tk.Tk()
root.title("Sudoku")

grid = [[None] * 9 for _ in range(9)]
for y in range(9):
    for x in range(9):
        label = tk.Label(root, text=Sudoku[y][x], font=("Comic Sans", 16), width=5, height=2, bg="lightgray",
                         relief="solid", borderwidth=2)
        label.grid(row=y, column=x)
        label.bind("<Button-1>", lambda event, x=x, y=y: increment_num(x, y))
        grid[y][x] = label

solve_button = tk.Button(root, text="Solve", command=Solve)
solve_button.grid(row=9, column=4, pady=10)

close_button = tk.Button(root, text="Close", command=zavritokno)
close_button.grid(row=9, column=5, pady=10)

root.mainloop()



