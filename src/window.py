import tkinter as tk
from tkinter import messagebox
from random import randint


class Window:
    def __init__(self, name, width, height):
        # creating a main window
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        # create cell-buttons
        self.cell_button0 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button0))
        self.cell_button1 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button1))
        self.cell_button2 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button2))

        self.cell_button3 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button3))
        self.cell_button4 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button4))
        self.cell_button5 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button5))

        self.cell_button6 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button6))
        self.cell_button7 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button7))
        self.cell_button8 = tk.Button(self.root, text='  ', command=lambda: self.__click_button(self.cell_button8))

        # dict - {button: (free = 0; human = 1; computer = 2)}
        self.__cell_buttons_dict = {self.cell_button0: 0, self.cell_button1: 0, self.cell_button2: 0,
                                    self.cell_button3: 0, self.cell_button4: 0, self.cell_button5: 0,
                                    self.cell_button6: 0, self.cell_button7: 0, self.cell_button8: 0}

        # creating 'close' button
        self.restart_button = tk.Button(self.root, text='restart', command=self.__reset)

    # method grid buttons to the main window
    def create_buttons(self):
        # grid cell-buttons__
        self.cell_button0.grid(row=0, column=0, sticky='wens')
        self.cell_button1.grid(row=0, column=1, sticky='wens')
        self.cell_button2.grid(row=0, column=2, sticky='wens')

        self.cell_button3.grid(row=1, column=0, sticky='wens')
        self.cell_button4.grid(row=1, column=1, sticky='wens')
        self.cell_button5.grid(row=1, column=2, sticky='wens')

        self.cell_button6.grid(row=2, column=0, sticky='wens')
        self.cell_button7.grid(row=2, column=1, sticky='wens')
        self.cell_button8.grid(row=2, column=2, sticky='wens')

        # grid close button
        self.restart_button.grid(row=3, columnspan=3, sticky='wens')

    # run endless loop of window
    def run_win(self):
        self.root.mainloop()

    # review is button clicked
    def __is_not_clicked(self, btn):
        return self.__cell_buttons_dict[btn] == 0

    # set a value of button and text of it
    def __set_btn_value(self, btn, value):
        self.__cell_buttons_dict[btn] = value
        if value == 1:
            btn['text'] = 'x'
        if value == 2:
            btn['text'] = 'o'

    # property-method return is any free cell in pole for move
    @property
    def __is_free_cells_in_pole(self):
        return 0 in self.__cell_buttons_dict.values()

    # review if someone won
    def __review_win(self, player):
        player_value = None
        if player == 'human':
            player_value = 1
        elif player == 'computer':
            player_value = 2

        buttons_values = tuple(self.__cell_buttons_dict.values())
        is_win_way1 = (buttons_values[0] == buttons_values[1] == buttons_values[2]) \
                      and buttons_values[0] == player_value
        is_win_way2 = (buttons_values[3] == buttons_values[4] == buttons_values[5]) \
                      and buttons_values[3] == player_value
        is_win_way3 = (buttons_values[6] == buttons_values[7] == buttons_values[8]) \
                      and buttons_values[6] == player_value
        is_win_way4 = (buttons_values[0] == buttons_values[3] == buttons_values[6]) \
                      and buttons_values[0] == player_value
        is_win_way5 = (buttons_values[1] == buttons_values[4] == buttons_values[7]) \
                      and buttons_values[1] == player_value
        is_win_way6 = (buttons_values[2] == buttons_values[5] == buttons_values[8]) \
                      and buttons_values[2] == player_value
        is_win_way7 = (buttons_values[0] == buttons_values[4] == buttons_values[8]) \
                      and buttons_values[0] == player_value
        is_win_way8 = (buttons_values[2] == buttons_values[4] == buttons_values[6]) \
                      and buttons_values[2] == player_value
        player_win = is_win_way1 or is_win_way2 or is_win_way3 or is_win_way4 \
                or is_win_way5 or is_win_way6 or is_win_way7 or is_win_way8

        if player_win:
            messagebox.showinfo(message=f'{player} win!\nplease restart game')
            return True
        else:
            return False

    # method make a random computer move
    def __computer_move(self):
        if self.__is_free_cells_in_pole:
            while True:
                index = randint(0, 8)
                btn = tuple(self.__cell_buttons_dict.keys())[index]
                if not self.__is_not_clicked(btn):
                    continue
                self.__set_btn_value(btn, 2)
                break

    def __human_move(self, btn):
        if self.__is_not_clicked(btn):
            self.__set_btn_value(btn, 1)
            return True

    # main game logic
    def __click_button(self, btn):
        if self.__human_move(btn) and not self.__review_win('human'):
            self.__computer_move()
            self.__review_win('computer')

    # restart of game (use in button 'restart_button')
    def __reset(self):
        for btn in self.__cell_buttons_dict.keys():
            btn['text'] = '  '
            self.__set_btn_value(btn, 0)
