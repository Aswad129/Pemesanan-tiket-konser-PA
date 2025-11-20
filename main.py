import os
from user import menu_user
from auth import register, login
from termcolor import colored
import inquirer
from admin import menu_admin
from user import menu_user


def menu_utama():
    print(
        colored(
            "=== SELAMAT DATANG DI SISTEM PENJUALAN TIKET KONSER ===",
            "cyan",
            attrs=["bold"],
        )
    )

    pertanyaan = [
        inquirer.List(
            "pilihan",
            message=colored("Pilih Opsi di bawah ini:", "cyan"),
            choices=["REGISTER", "LOGIN", "EXIT"],
        ),
    ]

    jawaban = inquirer.prompt(pertanyaan)
    pilihan = jawaban["pilihan"]

    if pilihan == "REGISTER":
        register()
    elif pilihan == "LOGIN":
        username, role = login()

        if role == "admin":
            print(f"Selamat datang, Admin {username}!")
            menu_admin(username)

        elif role == "user":
            print(f"Selamat datang, User {username}!")
            menu_user(username)

    elif pilihan == "EXIT":
        print(colored("Keluar dari program.", "green"))
        exit()


if __name__ == "__main__":
    while True:
        menu_utama()
