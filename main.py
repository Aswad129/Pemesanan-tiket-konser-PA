import os 
from user import menu_user
from auth import register, login


def menu_utama():
    print("=== Menu Utama ===")
    print("1. REGISTER")
    print("2. LOGIN")
    print("3. EXIT")

    pilihan = input("Pilih opsi (1-3): ")

    if pilihan == "1":
        register() 
    elif pilihan == "2":
        username, role = login()
        if role == "admin":
            print(f"Selamat datang, Admin {username}!")
        elif role == "user":
           print(f"Selamat datang, User {username}!")
    elif pilihan == "3":
        print("Keluar dari program.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_utama()

if __name__ == "__main__":
    menu_utama()