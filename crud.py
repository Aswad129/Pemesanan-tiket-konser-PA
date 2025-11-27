import csv
from prettytable import PrettyTable
import pyfiglet
from termcolor import colored
import matplotlib.pyplot as plt


CONCERT_FILE = "concerts.csv"


def header_konser():
    header = pyfiglet.figlet_format("DAFTAR KONSER", font="slant")
    print(colored(header, "cyan"))

def format_rupiah(angka):
    angka = int(angka)
    return f"Rp {angka:,.0f}".replace(",", ".") + ",-"

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
        fieldnames = ["id", "nama", "tanggal", "lokasi", "harga", "stok", "terjual"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(concerts)


def tambah_konser():
    concerts = baca_konser()
    print("\n=== Tambah Konser ===")
    nama = input("Nama konser: ")
    tanggal = input("Tanggal (dd-mm-yyyy): ")
    lokasi = input("Lokasi: ")
    harga = input("Harga tiket: ")
    stok = input("Jumlah tiket: ")

    konser_id = str(len(concerts) + 1)

    concerts.append(
        {
            "id": konser_id,
            "nama": nama,
            "tanggal": tanggal,
            "lokasi": lokasi,
            "harga": harga,
            "stok": stok,
            "terjual": "0",
        }
    )

    simpan_konser(concerts)
    print(colored("Konser berhasil ditambahkan!", "green"))


def lihat_konser():
    concerts = baca_konser()
    if not concerts:
        print(colored("Belum ada konser yang di tambahkan", "red"))
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama Konser", "Tanggal", "Lokasi", "Harga", "Stok"]
    

    for c in concerts:
        harga_format = format_rupiah(c["harga"])
        table.add_row(
            [c["id"], c["nama"], c["tanggal"], c["lokasi"], harga_format, c["stok"]]
        )

    header_konser()
    print(colored(table, "green"))



def edit_konser():
    concerts = baca_konser()
    lihat_konser()
    konser_id = input("Masukkan ID konser yang ingin diedit: ")

    for c in concerts:
        if c["id"] == konser_id:
            c["nama"] = input(f"Nama ({c['nama']}): ") or c["nama"]
            c["tanggal"] = input(f"Tanggal ({c['tanggal']}): ") or c["tanggal"]
            c["lokasi"] = input(f"Lokasi ({c['lokasi']}): ") or c["lokasi"]
            c["harga"] = input(f"Harga ({c['harga']}): ") or c["harga"]
            c["stok"] = input(f"Stok ({c['stok']}): ") or c["stok"]

            simpan_konser(concerts)
            print("Data konser berhasil diperbarui!")
            return

    print(colored("ID konser tidak ditemukan.", "red"))


def hapus_konser():
    concerts = baca_konser()
    lihat_konser()
    konser_id = input("Masukkan ID konser yang ingin dihapus: ")

    new_list = [c for c in concerts if c["id"] != konser_id]
    simpan_konser(new_list)
    print(colored("Konser berhasil dihapus!", "green"))


def diagram_konser():
    concerts = baca_konser()
    if not concerts:
        print(colored("Belum ada data konser yang di tambahkan", "red"))
        return

    nama_konser = [c.get("nama", "-") for c in concerts]
    terjual = [int(c.get("terjual", 0) or 0) for c in concerts]

    plt.figure(figsize=(10, 5))
    plt.bar(nama_konser, terjual)
    plt.title("Statistik Tiket Konser yang Terjual")
    plt.xlabel("Nama Konser")
    plt.ylabel("Tiket Terjual")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()