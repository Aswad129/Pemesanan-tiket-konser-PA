from InquirerPy import inquirer

def main ():
    while True:
        print("SELAMAT DATANG DI PROGRAM KAMI")
        print("\n==== SISTEM PEMESANAN TIKET KONSER ====")

        pilihan = inquirer.select(
            message="Pilih menu utama:",
            choices=[
                "🔐 Login",
                "📝 Register",
                "🚪 Keluar"
            ],
            default="🔐 Login"
        ).execute()
        # print("1. REGISTER")
        # print("2. LOGIN")
        # print("3. EXIT")
        # try :
        #     pilihan = int(input("Masukkan pilihan Anda (1/2/3): "))
        # except ValueError:
        #     print("Input tidak valid. Silakan masukkan angka 1, 2, atau 3.")
        #     continue

        # if pilihan == 1:
        

        # else if pilihan == 2:


        # else if pilihan == 3:

        # else:
        #     print("Pilihan tidak valid. Silakan coba lagi.")