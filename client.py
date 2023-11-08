import socket
import tkinter as tk
from socket import *


class Randomaizer:
    # Инициализация приложения клиента + подключение к серверу
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Random')
        self.win.geometry("500x500+400+300")
        self.win.config(bg='#D8BFD8')

        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 12345))

        self.setup()

    # Кнопка в приложении
    def setup(self):
        btn = tk.Button(self.win, background='#D8BFD8', width=7, height=3,
                        text='Random', font="Times 35",
                        command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        btn.focus()

    def click(self):
        self.client.send(bytes("\00", 'ascii'))

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    app = Randomaizer()
    app.run()
