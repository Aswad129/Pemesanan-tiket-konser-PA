import csv
from prettytable import PrettyTable
from crud import lihat_konser
from termcolor import colored
import inquirer

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

    # tampilkan konser dalam prettytable
    lihat_konser()

    # input tambahan customer
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
                total = harga * jumlah
                simpan_konser(concerts)

                # simpan tiket
                with open(TICKET_FILE, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [username, nama_customer, konser_id, nama_konser, jumlah, total]
                    )

                print("\n=== STRUK PEMBELIAN ===")
                print(f"Nama Customer : {nama_customer}")
                print(f"Konser        : {nama_konser}")
                print(f"Jumlah        : {jumlah}")
                print(f"Total Bayar   : Rp {total}")
                return

            else:
                print(" Stok tidak cukup!")
                return

    print(" ID konser tidak ditemukan.")


def lihat_tiket(username):
    print("\n=== TIKET YANG ANDA PESAN ===")

    table = PrettyTable()
    table.field_names = ["Nama Customer", "Konser", "Jumlah Tiket", "Total Bayar"]

    try:
        with open(TICKET_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            found = False

            for row in reader:
                if len(row) < 6:
                    continue

                usr, nama_customer, konser_id, nama_konser, qty, total = row

                if usr == username:
                    found = True
                    table.add_row([nama_customer, nama_konser, qty, total])

            if found:
                print(table)
            else:
                print("Anda belum memesan tiket.")
    except FileNotFoundError:
        print("Belum ada tiket tercatat.")