import csv
from prettytable import PrettyTable
from crud import lihat_konser, format_rupiah
from termcolor import colored
import inquirer
import os

CONCERT_FILE = "concerts.csv"
TICKET_FILE = (
    "tickets.csv"  
)


def menu_user(username):
    while True:
        print(colored(f"\n=== MENU USER ({username}) ===", "cyan", attrs=["bold"]))

        pertanyaan = [
            inquirer.List(
                "pilihan",
                message=colored("Pilih Opsi di bawah ini:", "cyan"),
                choices=[
                    "1. Lihat Konser",
                    "2. Pesan Tiket",
                    "3. Lihat Tiket Saya",
                    "0. Logout",
                ],
            ),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        pilihan = jawaban["pilihan"][0]  

        if pilihan == "1":
            lihat_konser()
        elif pilihan == "2":
            pesan_tiket(username)
        elif pilihan == "3":
            lihat_tiket(username)
        elif pilihan == "0":
            break

def baca_konser():
    concerts = []
    try:
        with open(CONCERT_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            concerts = list(reader)
    except FileNotFoundError:
        pass
    return concerts


def simpan_konser(concerts):
    with open(CONCERT_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "nama", "tanggal", "lokasi", "harga", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(concerts)


def pesan_tiket(username):
    concerts = baca_konser()

    lihat_konser()

    nama_customer = input("Masukkan nama customer: ")

    konser_id = input("Masukkan ID konser: ")
    jumlah = int(input("Jumlah tiket: "))

    for c in concerts:
        if c["id"] == konser_id:
            stok = int(c["stok"])
            harga = int(c["harga"])
            nama_konser = c["nama"]

            if jumlah <= stok:
                c["stok"] = str(stok - jumlah)
                terjual_lama = int(c.get("terjual", 0))
                c["terjual"] = str(terjual_lama + jumlah)
                total = harga * jumlah
                simpan_konser(concerts)

                # simpan tiket
                file_baru = not os.path.exists(TICKET_FILE)
                with open(TICKET_FILE, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)

                    if file_baru:
                        writer.writerow(
                            [
                                "username",
                                "nama_pelanggan",
                                "nama_konser",
                                "jumlah_tiket",
                                "total",
                            ]
                        )
                    writer.writerow(
                        [username, nama_customer, nama_konser, jumlah, total]
                    )

                print(colored("\n" + "="*35, "green"))
                print(colored("|         STRUK PEMBELIAN         |", "green"))
                print(colored("="*35, "green"))
                print(colored(f"| Nama Customer : {nama_customer:<12}    |", "green"))
                print(colored(f"| Konser        : {nama_konser:<12}    |", "green"))
                print(colored(f"| Jumlah Tiket  : {jumlah:<12}    |", "green"))
                print(colored(f"| Total Bayar   : {format_rupiah(total):<12}    |", "green"))
                print(colored("="*35, "green"))
                return

            else:
                print(colored(" Stok tidak cukup!", "red"))
                return

    print(colored(" ID konser tidak ditemukan.", "red"))


def lihat_tiket(username):
    print(colored("\n================== TIKET YANG ANDA PESAN ==================", "cyan", attrs=["bold"]))

    table = PrettyTable()
    table.field_names = ["Nama Customer", "Konser", "Jumlah Tiket", "Total Bayar"]

    try:
        with open(TICKET_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            found = False

            next(reader, None)

            for row in reader:
                if not row or len(row) < 5:
                    continue

                usr, nama_customer, nama_konser, qty, total = row

                if usr == username:
                    found = True
                    total_format = format_rupiah(total)
                    table.add_row([nama_customer, nama_konser, qty, total_format])

            if found:
                print(colored(table, "green"))
            else:
                print(colored(" Anda belum memesan tiket.", "red"))

    except FileNotFoundError:
        print(colored(" Belum ada tiket tercatat.", "red"))