from Ant import Ant
from alg_ants_langton import Alg_Ants_Langton
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import random


def create_board(n, m):
    board = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        board.append(row)
    return board


def display_board(board):
    for row in board:
        print(row)


def draw_on_canvas(board, ants):
    # rysowanie na płótnie ruchu mrówek
    d = canvas.winfo_width()/len(board)
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            for idx, ant in enumerate(ants):
                if board[i][j] == idx+1:
                    canvas.create_rectangle(i*d, j*d, i*d + d, j*d + d, fill=ant.color, outline=ant.color)
    # wyświtlenie aktualnych współrzędnych mórwek
    for ant in ants:
        x, y = ant.current_coord
        canvas.create_oval(x * d, y * d, x * d + d, y * d + d, fill=ant.color, outline="white")


def clear_canvas():
    canvas.delete("all")


def run_ants_langton(n, number_ants, iterations):
    board = create_board(n, n)
    ants = [Ant(n) for i in range(number_ants)]
    antsLangton = Alg_Ants_Langton()
    board = antsLangton.alg(board, ants, iterations)
    clear_canvas()
    draw_on_canvas(board, ants)


# def rgb_color(rgb):
#    return '#%02x%02x%02x' % rgb
#
#
# def create_colors(number_ants):
#     colors = []
#     for c in range(number_ants):
#         r, g, b = (random.randrange(255), random.randrange(255), random.randrange(255))
#         colors.append(rgb_color((r, g, b)))
#     return colors


def submit():
    try:
        # pobranie od uzytkownika wartości
        n = int(entry_board_size.get())
        iterations = int(entry_iterations.get())
        number_ants = int(entry_numer_ants.get())

        # wykonaj algorytm
        run_ants_langton(n, number_ants, iterations)
        label_message.config(text="", fg="red")
    except:
        label_message.config(text="ERROR: Coś poszło nie tak!!\nSprawdź czy wszytkie wprowadzone wartości są liczbami.", fg="red")

# --- ustawienia dla symulacji


print("Koniec")

window_width = 700
window_height = 500

window = tk.Tk()
window.geometry("700x550")

# ----------------- legend ----------------------------

legend = tk.Frame(window, width=100, bg="black", height=window_height)
legend.grid(row=0, column=0, sticky="n")

legend_label = tk.Label(legend, text="legenda")
legend_label.grid(row=0, column=0, sticky="n")

# ----------------- canvas ----------------------------

canvas = tk.Canvas(window, width=window_height, height=window_height, bg="white")
canvas.grid(row=0, column=1)


# ----------------- settings ----------------------------

settings = tk.Frame(window, width=100, height=window_height)
settings.grid(row=0, column=2, sticky="n")

settings_label = tk.Label(settings, text="ustawienia")
settings_label.grid(row=0, column=0, sticky="we")

separator = ttk.Separator(settings, orient='horizontal')
separator.grid(row=1, column=0,  sticky="we", pady=3)


entry_label1 = tk.Label(settings, text="l. mrówek")
entry_label1.grid(row=2, column=0, sticky="w", pady=[10, 0])

entryText_number_ants = tk.StringVar()
entry_numer_ants = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5, textvariable=entryText_number_ants)
entryText_number_ants.set("3")
entry_numer_ants.grid(row=3, column=0, sticky="we")

entry_label2 = tk.Label(settings, text="l. iteracji")
entry_label2.grid(row=4, column=0, sticky="w",  pady=[10, 0])

entryText_iterations = tk.StringVar()
entry_iterations = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5, textvariable=entryText_iterations)
entryText_iterations.set("11000")
entry_iterations.grid(row=5, column=0, sticky="we")

entry_label3 = tk.Label(settings, text="nxn")
entry_label3.grid(row=6, column=0, sticky="w",  pady=[10, 0])

entryText_board_size = tk.StringVar()
entry_board_size = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5, textvariable=entryText_board_size)
entryText_board_size.set("100")
entry_board_size.grid(row=7, column=0, sticky="we")

btn_save = tk.Button(settings, text="Zapisz", fg="black", command=submit)
btn_save.grid(row=8, column=0, sticky="we", pady=[10, 0])

# ------------------ info ------------------------------------------

label_message = tk.Label(window, text="nxn(px)")
label_message.grid(row=1, column=0, columnspan=3, sticky="we")


window.mainloop()

# for i in range(n):
#     for j in range(n):
#         for idx, ant in enumerate(ants):
#             if board[i][j] == idx+1:
#                 plt.plot(i, j, "."+colors[idx], alpha=0.7)
#
# for ant in ants:
#     plt.plot(ant.current_coord[0], ant.current_coord[1], ".b")
#
# plt.axis([0, n, 0, n])
# plt.show()
#display_board(board)
    # print("------------------------------------------------")
