import socket
import tkinter as tk
from socket import *


class DarkSoulsApp:
    # Инициализация приложения клиента + подключение к серверу
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Die?')
        self.win.geometry("256x256+400+300")
        self.win.config(bg='#D8BFD8')

        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 12345))

        self.setup()

    # Кнопка в приложении
    def setup(self):
        btn = tk.Button(self.win, background='#D8BFD8', width=4, height=2, text='Die?', font="Times 35",
                        command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        btn.focus()

    # Кликабельность
    def click(self):
        self.client.send(bytes("\00", 'ascii'))

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    app = DarkSoulsApp()
    app.run()
