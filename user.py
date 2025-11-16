import csv

CONCERT_FILE = "concerts.csv"
TICKET_FILE = "tickets.csv"      # === FITUR TIKET ===

def menu_user(username):
    while True:
        print(f"\n=== MENU USER ({username}) ===")
        print("1. Lihat konser")
        print("2. Pesan tiket")
        print("3. Lihat tiket yang dipesan")   # === FITUR TIKET ===
        print("0. Logout")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            lihat_konser()
        elif pilihan == "2":
            pesan_tiket(username)               # username diperlukan untuk simpan tiket
        elif pilihan == "3":
            lihat_tiket(username)               # === FITUR TIKET ===
        elif pilihan == "0":
            break

def baca_konser():
    concerts = []
    try:
        with open(CONCERT_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            concerts = list(reader)
    except FileNotFoundError:
        pass
    return concerts

def simpan_konser(concerts):
    with open(CONCERT_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["id", "nama", "tanggal", "lokasi", "harga", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(concerts)

def lihat_konser():
    concerts = baca_konser()
    if not concerts:
        print("Belum ada konser.")
        return
    print("\n=== DAFTAR KONSER ===")
    for c in concerts:
        print(f"{c['id']}. {c['nama']} | {c['tanggal']} | {c['lokasi']} | Harga: {c['harga']} | Stok: {c['stok']}")

# ======================================
#             FITUR PEMBAYARAN
# ======================================
def pesan_tiket(username):
    concerts = baca_konser()
    lihat_konser()
    konser_id = input("Masukkan ID konser: ")
    jumlah = int(input("Jumlah tiket: "))

    for c in concerts:
        if c["id"] == konser_id:
            stok = int(c["stok"])
            if jumlah <= stok:
                c["stok"] = str(stok - jumlah)
                total = jumlah * int(c["harga"])
                simpan_konser(concerts)

                # === SIMPAN TIKET USER ===
                with open(TICKET_FILE, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, konser_id, jumlah, total])

                print(f"✅ Pemesanan berhasil! Total: Rp {total}")
                return
            else:
                print("❌ Stok tidak cukup!")
                return
    print("❌ ID konser tidak ditemukan.")

# ======================================
#           FITUR LIHAT TIKET
# ======================================
def lihat_tiket(username):
    print("\n=== TIKET YANG ANDA PESAN ===")

    try:
        with open(TICKET_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            found = False

            for row in reader:
                if len(row) < 4:
                    continue
                usr, cid, qty, total = row
                if usr == username:
                    found = True
                    print(f"- Konser ID: {cid} | Jumlah: {qty} | Total: Rp {total}")

            if not found:
                print("Anda belum memesan tiket.")
    except FileNotFoundError:
        print("Belum ada tiket tercatat.")