from termcolor import colored
import inquirer
from crud import tambah_konser, lihat_konser, edit_konser, hapus_konser, diagram_konser


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
        pilihan = jawaban["pilihan"][0]  # ambil nomor pilihan saja

        if pilihan == "1":
            tambah_konser()
        elif pilihan == "2":
            lihat_konser()
        elif pilihan == "3":
            edit_konser()
        elif pilihan == "4":
            hapus_konser()
        elif pilihan == "5":
            diagram_konser()
        elif pilihan == "0":
            break
        else:
            print(" Pilihan tidak valid!")