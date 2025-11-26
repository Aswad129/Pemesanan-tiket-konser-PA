import csv
import time
import sys
from termcolor import colored

USER_FILE = "users.csv"


def load_animation(text="loading"):
    animasi = [
        "[■□□□□□□□□□]",
        "[■■□□□□□□□□]",
        "[■■■□□□□□□□]",
        "[■■■■□□□□□□]",
        "[■■■■■□□□□□]",
        "[■■■■■■□□□□]",
        "[■■■■■■■□□□]",
        "[■■■■■■■■□□]",
        "[■■■■■■■■■□]",
        "[■■■■■■■■■■]",
    ]

    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(
            "\r" + colored(f"{text} {animasi[i % len(animasi)]}", "yellow")
        )
        sys.stdout.flush()
        print("\r", end="")


def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    load_animation("Memeriksa data...")

    try:
        with open(USER_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for u in reader:
                if u["username"] == username and u["password"] == password:
                    print(colored(f" Login berhasil sebagai {u['role'].upper()}!", "green"))
                    return username, u["role"]
    except FileNotFoundError:
        pass

    print(colored("Login gagal! Username atau password salah.", "red"))
    return None, None


def register():
    print("\n=== REGISTER ===")
    username = input("Username baru: ").strip()
    password = input("Password: ").strip()
    load_animation("Memproses registrasi...")

    # Cek username sudah ada
    try:
        with open(USER_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for u in reader:
                if (
                    u["username"].lower() == username.lower()
                ):  # cek tanpa case sensitive
                    print(colored("Username sudah digunakan! Coba nama lain.", "red"))
                    return
    except FileNotFoundError:
        pass

    # user baru
    with open(USER_FILE, mode="a", newline="", encoding="utf-8") as file:
        fieldnames = ["username", "password", "role"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:  
            writer.writeheader()

        writer.writerow({"username": username, "password": password, "role": "user"})

    print(colored(" Registrasi berhasil!", "green"))