from Ant import Ant
from Alg_ants_langton import Alg_Ants_Langton
import tkinter as tk
from tkinter import ttk


class GUI():
    window_width = 700
    window_height = 500
    window = tk.Tk()

    # ----------------- legend ----------------------------
    # legend = tk.Frame(window, width=100, bg="black", height=window_height)
    # legend_label = tk.Label(legend, text="legenda")

    # ----------------- canvas ----------------------------
    canvas = tk.Canvas(window, width=(window_width-200), height=(window_width-200), bg="white")

    # ----------------- settings ----------------------------
    settings = tk.Frame(window, width=200, height=window_height)
    settings_label = tk.Label(settings, text="ustawienia")
    separator1 = ttk.Separator(settings, orient='horizontal')

    # ----------------- entry number ants  ----------------------------
    entry_label1 = tk.Label(settings, text="l. mrówek")
    entryText_number_ants = tk.StringVar()
    entry_number_ants = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5,
                                textvariable=entryText_number_ants)

    # ----------------- entry iterations  ----------------------------
    entry_label2 = tk.Label(settings, text="l. iteracji")
    entryText_iterations = tk.StringVar()
    entry_iterations = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5,
                                textvariable=entryText_iterations)

    # ----------------- entry board size  ----------------------------
    entry_label3 = tk.Label(settings, text="nxn(px)")
    entryText_board_size = tk.StringVar()
    entry_board_size = tk.Entry(settings, font=('Arial', 10), width=15, relief=tk.FLAT, borderwidth=5,
                                textvariable=entryText_board_size)

    # ----------------- radio  --------------------------------------
    radio_var = tk.IntVar()
    radio_label = tk.Label(settings, text="Wizualizacja")
    separator2 = ttk.Separator(settings, orient='horizontal')
    radio_v1 = tk.Radiobutton(settings, text="wynik", variable=radio_var, value=1)
    radio_v2 = tk.Radiobutton(settings, text="kroki", variable=radio_var, value=2)

    # ----------------- btn settings save ----------------------------
    btn_save = tk.Button(settings, text="Start", fg="black")

    # ------------------ info ------------------------------------------
    label_message = tk.Label(window, text="")

    def __init__(self):
        nxm = "%ix%i"%(self.window_width, self.window_height+50)
        self.window.geometry(nxm)
        self.window.title("Mrówki Langtona")

        # ------------- legend - section 1 -------------
        # self.legend.grid(row=0, column=0, sticky="n")
        # self.legend_label.grid(row=0, column=0, sticky="n")

        # ------------- canvas - section 2---------------
        self.canvas.grid(row=0, column=1)

        # -------------- settings - section 3 -----------
        self.settings.grid(row=0, column=2, sticky="n", padx=10)
        self.settings_label.grid(row=0, column=0, sticky="we")
        self.separator1.grid(row=1, column=0, sticky="we", pady=3)
        self.entry_label1.grid(row=2, column=0, sticky="w", pady=[10, 0])
        self.entryText_number_ants.set("3")
        self.entry_number_ants.grid(row=3, column=0, sticky="we")
        self.entry_label2.grid(row=4, column=0, sticky="w", pady=[10, 0])
        self.entryText_iterations.set("11000")
        self.entry_iterations.grid(row=5, column=0, sticky="we")
        self.entry_label3.grid(row=6, column=0, sticky="w", pady=[10, 0])
        self.entryText_board_size.set("100")
        self.entry_board_size.grid(row=7, column=0, sticky="we")
        self.radio_var.set(1)
        self.radio_label.grid(row=9, column=0, sticky="w", pady=[20, 0])
        self.separator2.grid(row=10, column=0, sticky="we", pady=[3, 0])
        self.radio_v1.grid(row=11, column=0, sticky="w", pady=[0, 0])
        self.radio_v2.grid(row=12, column=0, sticky="w", pady=[0, 0])
        self.btn_save.config(command=self.submit)
        self.btn_save.grid(row=13, column=0, sticky="we", pady=[10, 0])
        self.label_message.grid(row=1, column=0, columnspan=3, sticky="we")

    def show(self):
        self.window.mainloop()

    def set_window_size(self, n):
        self.window.geometry("%ix%i"%(n, n-150))
        self.canvas.config(width=(n-200), height=(n-200))

    def draw_on_canvas(self, board, ants):
        # rysowanie na płótnie ruchu mrówek
        d = self.canvas.winfo_width() / len(board)
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                for idx, ant in enumerate(ants):
                    if board[i][j] == idx + 1:
                        self.canvas.create_rectangle(i * d, j * d, i * d + d, j * d + d, fill=ant.color, outline=ant.color)

        # wyświtlenie aktualnych współrzędnych mórwek
        for ant in ants:
            x, y = ant.current_coord
            self.canvas.create_oval(x * d, y * d, x * d + d, y * d + d, fill="blue", outline="white")

    def clear_canvas(self):
        self.canvas.delete("all")

    def run_ants_langton_1(self, n, number_ants, iterations):
        # n - rozmiar planszy
        # number_ants - liczba mrówek na planszy
        ants_langton = Alg_Ants_Langton(n, number_ants)
        board = ants_langton.alg(iterations)
        self.clear_canvas()
        self.draw_on_canvas(board, ants_langton.ants)

    def move_ants(self, ants_langton, iterations, k):
        self.clear_canvas()
        if k == 1:
            board = ants_langton.board
        else:
            board = ants_langton.alg(1)
        self.draw_on_canvas(board, ants_langton.ants)
        self.label_message.config(text="Krok: "+str(k), fg="green")
        if iterations > 1:
            self.canvas.after(500, lambda: self.move_ants(ants_langton, iterations - 1, k+1))

    def run_ants_langton_steps(self, n, number_ants, iterations):
        # n - rozmiar planszy
        # number_ants - liczba mrówek na planszy
        ants_langton = Alg_Ants_Langton(n, number_ants)
        self.move_ants(ants_langton, iterations, 1)

    def submit(self):
        try:
            # pobranie od uzytkownika wartości
            n = int(self.entry_board_size.get())
            iterations = int(self.entry_iterations.get())
            number_ants = int(self.entry_number_ants.get())

            # wykonaj algorytm
            if self.radio_var.get() == 1:
                self.run_ants_langton_1(n, number_ants, iterations)
            else:
                self.run_ants_langton_steps(n, number_ants, iterations)

            self.label_message.config(text="", fg="red")
        except:
            self.label_message.config(
                text="ERROR: Coś poszło nie tak!!\nSprawdź czy wszytkie wprowadzone wartości są liczbami.", fg="red")


