import os 
from user import menu_user
from auth import register, login
import time
import sys
from termcolor import colored
import inquirer


def load_animation(text="loading"):
    animasi = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
               "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
               "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(20):
        time.sleep(0.2)
        sys.stdout.write("\r" + colored(f"{text} {animasi[i % len(animasi)]}", 'yellow'))
        sys.stdout.flush()
        print("\r", end="")

def menu_utama():
    print(colored("=== SELAMAT DATANG DI SISTEM PENJUALAN TIKET KONSER ===", "yellow", attrs=["bold"]))


    pertanyaan = [
        inquirer.List(
            'pilihan',
            message="Pilih Opsi di bawah ini:",
            choices=['REGISTER', 'LOGIN', 'EXIT'],
        ),
    ]

    jawaban = inquirer.prompt(pertanyaan)
    pilihan = jawaban['pilihan']

    if pilihan == "REGISTER":
        register() 
        load_animation("memproses registrasi")
    elif pilihan == "LOGIN":
        username, role = login()
        load_animation("memproses login")

        if role == "admin":
            print(f"Selamat datang, Admin {username}!")
        elif role == "user":
           print(f"Selamat datang, User {username}!")
    elif pilihan == "EXIT":
        print("Keluar dari program.")
    else:
        print(colored("Pilihan tidak valid. Silakan coba lagi.", "red"))
        return

if __name__ == "__main__":
    menu_utama()