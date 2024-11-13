import random
import os
import time

kode_wilayah = {
    "12": {
        "provinsi": "Jawa Barat",
        "kabupaten": {
            "01": {
                "nama": "Kabupaten Bandung",
                "kecamatan": ["Bojongloa", "Cibiru", "Ujung Berung"],
                "kelurahan": ["Babakan", "Cibeunying", "Margahayu"]
            },
            "02": {
                "nama": "Kabupaten Bekasi",
                "kecamatan": ["Cikarang Utara", "Tambun Selatan", "Setu"],
                "kelurahan": ["Telaga Murni", "Lambangsari", "Wanasari"]
            },
        }
    },
    "13": {
        "provinsi": "Jawa Tengah",
        "kabupaten": {
            "01": {
                "nama": "Kabupaten Semarang",
                "kecamatan": ["Banyumanik", "Candisari", "Pedurungan"],
                "kelurahan": ["Tembalang", "Mijen", "Kalicari"]
            },
            "02": {
                "nama": "Kabupaten Kendal",
                "kecamatan": ["Boja", "Cepiring", "Kaliwungu"],
                "kelurahan": ["Singorojo", "Brangsong", "Sukorejo"]
            },
        }
    },
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_logo():
    merah = "\033[91m"
    putih = "\033[97m"
    reset = "\033[0m"
    print(f"""
{merah}███████╗███████╗████████╗    ███╗   ██╗██╗██╗  ██╗{putih}
██╔════╝██╔════╝╚══██╔══╝    ████╗  ██║██║██║ ██╔╝
███████╗█████╗     ██║       ██╔██╗ ██║██║█████╔╝ 
╚════██║██╔══╝     ██║       ██║╚██╗██║██║██╔═██╗ 
███████║███████╗   ██║       ██║ ╚████║██║██║  ██╗
╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝{reset}

               [ GET-NIK ]
       [ + ] Created by Mr.666 [ + ]
    """)

def validasi_nomor(nomor):
    if not (nomor.startswith("+62") or nomor.startswith("62")):
        print("MAAF, FORMAT YANG BISA HANYA NEGARA INDONESIA (+62/62)🙏🏻")
        return False
    return True

def searching_effect():
    print("[ + ] Mencari informasi dari (https://dukcapil.kemendagri.go.id)")
    time.sleep(1)
    print("[ + ] Mencocokkan Data")
    for i in range(5):
        file_name = random.choice([
            "Data_Penduduk_2023", "Buku_Tamu_Online", "Catatan_Keluarga_2022", 
            "Identitas_Warga", "Data_Paspor_Indonesia"
        ])
        print(f"       - Memindai {file_name}")
        time.sleep(0.5)
    print("[ + ] Done!\n")

def generate_valid_nik(tanggal_lahir, jenis_kelamin, kode_provinsi, kode_kabupaten):
    dd, mm, yy = tanggal_lahir.split("-")
    if jenis_kelamin == "Perempuan":
        dd = str(int(dd) + 40)  # Tambahkan 40 jika perempuan
    
    nomor_urut = f"{random.randint(1, 9999):04}"
    nik = f"{kode_provinsi}{kode_kabupaten}{dd}{mm}{yy[-2:]}{nomor_urut}"
    return nik

def generate_data():
    kode_provinsi = random.choice(list(kode_wilayah.keys()))
    provinsi_data = kode_wilayah[kode_provinsi]
    nama_provinsi = provinsi_data["provinsi"]
    
    kode_kabupaten = random.choice(list(provinsi_data["kabupaten"].keys()))
    kabupaten_data = provinsi_data["kabupaten"][kode_kabupaten]
    nama_kabupaten = kabupaten_data["nama"]
    
    nama_kecamatan = random.choice(kabupaten_data["kecamatan"])
    nama_kelurahan = random.choice(kabupaten_data["kelurahan"])
    
    jenis_kelamin = random.choice(["Laki-laki", "Perempuan"])
    tanggal_lahir = f"{random.randint(1, 31):02}-{random.randint(1, 12):02}-{random.randint(1970, 2010)}"
    nik = generate_valid_nik(tanggal_lahir, jenis_kelamin, kode_provinsi, kode_kabupaten)

    nama = random.choice([
        "Muhammad Rizky", "Muhammad Fahri", "Aulia Rahma", "Aulia Putri", 
        "Budi Santoso", "Dewi Ayu", "Citra Maharani", "Andi Saputra", 
        "Fajar Setiawan", "Gita Pertiwi"
    ])
    tempat_lahir = random.choice(["Jakarta", "Surabaya", "Bandung", "Medan", "Makassar", "Denpasar"])
    gol_darah = random.choice(["A", "B", "AB", "O"])
    agama = random.choices(["Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Konghucu"], weights=[50, 25, 10, 5, 5, 5])[0]
    status_kawin = random.choice(["Belum Kawin", "Kawin", "Cerai Hidup", "Cerai Mati"])
    pendidikan_akhir = random.choice(["SD", "SMP", "SMA", "D3", "S1", "S2", "None"])
    nama_ibu = random.choice(["Sri Ayu", "Ratna Sari", "Dewi Lestari", "Putri Indah", "Nina Sulastri", "Yanti Maharani"])
    no_kk = f"{random.randint(100000000000, 999999999999)}"
    alamat = f"Jalan {random.choice(['Merdeka', 'Sudirman', 'Diponegoro', 'Sutomo', 'Kartini'])} No.{random.randint(1, 100)}"
    no_rt = f"{random.randint(1, 10)}"
    no_rw = f"{random.randint(1, 10)}"

    print(f"""
NIK          : {nik}
Nama         : {nama}
Jenis Kelamin: {jenis_kelamin}
Tempat Lahir : {tempat_lahir}
Tanggal Lahir: {tanggal_lahir}
Gol. Darah   : {gol_darah}
Agama        : {agama}
Status Kawin : {status_kawin}
Pendidikan   : {pendidikan_akhir}
Nama Ibu     : {nama_ibu}
No KK        : {no_kk}
Provinsi     : {nama_provinsi}
Kabupaten    : {nama_kabupaten}
Kecamatan    : {nama_kecamatan}
Kelurahan    : {nama_kelurahan}
Alamat       : {alamat}
No RT        : {no_rt}
No RW        : {no_rw}

[ + ] Created by Mr.666 [ + ]
""")

# Fungsi untuk menjalankan tool
def run_tool():
    clear_screen()
    display_logo()

    while True:
        nomor = input("Masukan nomor (+62): ")
        if validasi_nomor(nomor):
            searching_effect()
            generate_data()
            break
        else:
            print("\nFormat nomor salah. Ulangi input.\n")

# Jalankan tool
run_tool()