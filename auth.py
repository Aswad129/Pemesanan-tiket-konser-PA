import csv

USER_FILE = "users.csv"

def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    try:
        with open(USER_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for u in reader:
                if u["username"] == username and u["password"] == password:
                    print(f" Login berhasil sebagai {u['role'].upper()}!")
                    return username, u["role"]
    except FileNotFoundError:
        pass

    print(" Login gagal! Username atau password salah.")
    return None, None

def register():
    print("\n=== REGISTER ===")
    username = input("Username baru: ")
    password = input("Password: ")

    # Cek username sudah ada
    try:
        with open(USER_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for u in reader:
                if u["username"] == username:
                    print(" Username sudah digunakan!!!")
                    return
    except FileNotFoundError:
        pass

    # Tambah data baru
    with open(USER_FILE, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ["username", "password", "role"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:  # tulis header kalau file kosong
            writer.writeheader()
        writer.writerow({"username": username, "password": password, "role": "user"})

    print(" Registrasi berhasil!")