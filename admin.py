from termcolor import colored
import inquirer
from crud import tambah_konser, lihat_konser, edit_konser, hapus_konser, diagram_konser
import os


def menu_admin(username):
    while True:
        print(colored(f"\n=== MENU ADMIN ({username}) ===", "cyan", attrs=["bold"]))

        pertanyaan = [
            inquirer.List(
                "pilihan",
                message=colored("Pilih Opsi di bawah ini:", "cyan", attrs=["bold"]),
                choices=[
                    "1. Tambah Konser",
                    "2. Lihat Konser",
                    "3. Edit Konser",
                    "4. Hapus Konser",
                    "5. Lihat statistik penjualan",
                    "0. Logout",
                ],
            ),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        pilihan = jawaban["pilihan"][0] 

        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tambah_konser()
        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            lihat_konser()
        elif pilihan == "3":
            os.system("cls" if os.name == "nt" else "clear")
            edit_konser()
        elif pilihan == "4":
            os.system("cls" if os.name == "nt" else "clear")
            hapus_konser()
        elif pilihan == "5":
            os.system("cls" if os.name == "nt" else "clear")
            diagram_konser()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print(" Pilihan tidak valid!")