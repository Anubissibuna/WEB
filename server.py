import tkinter as tk
import threading
import random
from socket import *


class Randomaizer:
    # Иницииализация приложения сервера
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Random Number')
        self.win.geometry("500x500+150+50")
        self.win.config(bg='#D8BFD8')

        self.setup()
        self.start()

    # Логика работы сервера
    def _server_run(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(("127.0.0.1", 12345))
        server.listen()

        user, addr = server.accept()
        # Отображение изменений серверного окна после клиентского запроса
        while True:
            data = user.recv(1)
            if not data:
                break
            self.update_data()

    # Создание рамки приложения
    def setup(self):
        self.frame = tk.Frame(self.win, background='#D8BFD8')
        self.frame.pack(fill=tk.BOTH, expand=True)

    def start(self):
        new_thread = threading.Thread(target=self._server_run)
        new_thread.start()

    # Реакция сервера на нажатие кнопки из клиентского приложения
    def update_data(self):
        text = tk.Label(self.win, width=9, height=4,
                        background='#D8BFD8', text=random.randint(1, 100), font="Times 35")
        text.place(relx=0.5, rely=0.5, anchor='center')

    def run(app):

        app.win.mainloop()


if __name__ == "__main__":
    app = Randomaizer()
    app.run()
