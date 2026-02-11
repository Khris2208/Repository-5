import time
import random
import json
import os
from datetime import datetime

class Senjata:
    """Class untuk merepresentasikan senjata dalam game"""
    def __init__(self, nama, damage_min, damage_max, mana_cost, level_diperlukan, deskripsi):
        self.nama = nama
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.mana_cost = mana_cost
        self.level_diperlukan = level_diperlukan  # Berapa kristal yang diperlukan
        self.deskripsi = deskripsi
        self.aktif = False
    
    def hitung_damage(self):
        """Hitung damage acak antara min dan max"""
        return random.randint(self.damage_min, self.damage_max)
    
    def __str__(self):
        return f"{self.nama} (Dmg: {self.damage_min}-{self.damage_max}, Mana: {self.mana_cost}, Level: {self.level_diperlukan})"

# Database senjata yang dapat ditemukan
DATABASE_SENJATA = {
    "pedang_kayu": Senjata(
        "Pedang Kayu",
        damage_min=8, damage_max=12,
        mana_cost=5,
        level_diperlukan=0,
        deskripsi="Senjata pemula, mudah digunakan tapi kurang kuat"
    ),
    "pedang_besi": Senjata(
        "Pedang Besi",
        damage_min=15, damage_max=22,
        mana_cost=10,
        level_diperlukan=1,
        deskripsi="Senjata standar, solid dan handal dalam pertarungan"
    ),
    "pedang_ajaib": Senjata(
        "Pedang Ajaib",
        damage_min=20, damage_max=30,
        mana_cost=15,
        level_diperlukan=2,
        deskripsi="Senjata berenergi magis, meningkatkan kekuatan serangan"
    ),
    "pedang_cahaya": Senjata(
        "Pedang Cahaya",
        damage_min=25, damage_max=35,
        mana_cost=20,
        level_diperlukan=3,
        deskripsi="Senjata yang memancarkan cahaya putih, sangat ampuh"
    ),
    "pedang_petir": Senjata(
        "Pedang Petir",
        damage_min=28, damage_max=38,
        mana_cost=25,
        level_diperlukan=4,
        deskripsi="Senjata beralirankan energi petir, serangan mematikan"
    ),
    "pedang_naga": Senjata(
        "Pedang Naga",
        damage_min=35, damage_max=50,
        mana_cost=30,
        level_diperlukan=5,
        deskripsi="Senjata paling kuat, dipercayakan oleh para naga kuno"
    )
}

class SistemLogin:
    """Sistem Login dan Registrasi untuk game dengan penyimpanan file"""
    def __init__(self):
        # File penyimpanan data
        self.file_akun = "akun_pengguna.json"
        self.file_histori = "histori_pengguna.json"
        
        # Database pengguna dengan username dan password
        self.akun_terdaftar = {}
        self.histori_login = {}
        
        # Muat data dari file jika ada
        self.muat_akun()
        self.muat_histori()
    
    def muat_akun(self):
        """Muat data akun dari file JSON"""
        if os.path.exists(self.file_akun):
            try:
                with open(self.file_akun, 'r') as f:
                    self.akun_terdaftar = json.load(f)
                print("[📁] Data akun berhasil dimuat dari file.")
            except:
                print("[⚠️] Gagal membaca file akun. Memulai database baru.")
                self.akun_terdaftar = {}
        else:
            self.akun_terdaftar = {}
    
    def muat_histori(self):
        """Muat data histori dari file JSON"""
        if os.path.exists(self.file_histori):
            try:
                with open(self.file_histori, 'r') as f:
                    self.histori_login = json.load(f)
            except:
                self.histori_login = {}
        else:
            self.histori_login = {}
    
    def simpan_akun(self):
        """Simpan data akun ke file JSON"""
        try:
            with open(self.file_akun, 'w') as f:
                json.dump(self.akun_terdaftar, f, indent=4)
        except Exception as e:
            print(f"[❌] Gagal menyimpan akun: {e}")
    
    def simpan_histori(self):
        """Simpan data histori ke file JSON"""
        try:
            with open(self.file_histori, 'w') as f:
                json.dump(self.histori_login, f, indent=4)
        except Exception as e:
            print(f"[❌] Gagal menyimpan histori: {e}")
    
    def registrasi(self):
        """Proses registrasi akun baru"""
        print("\n" + "="*50)
        print("📝 REGISTRASI AKUN BARU")
        print("="*50)
        
        username = input("Masukkan username: ").strip()
        
        if username in self.akun_terdaftar:
            print("❌ Username sudah terdaftar! Gunakan username lain.")
            return False
        
        password = input("Masukkan password: ").strip()
        
        if len(password) < 4:
            print("❌ Password minimal 4 karakter!")
            return False
        
        self.akun_terdaftar[username] = password
        self.simpan_akun()  # Simpan ke file
        
        # Inisialisasi histori untuk akun baru
        if username not in self.histori_login:
            self.histori_login[username] = {
                "tanggal_dibuat": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_login": 0,
                "riwayat_login": [],
                "statistik_game": []
            }
        self.simpan_histori()  # Simpan histori ke file
        
        print(f"✓ Akun '{username}' berhasil dibuat! Selamat datang!")
        return True
    
    def login(self):
        """Proses login akun"""
        print("\n" + "="*50)
        print("🔐 LOGIN AKUN")
        print("="*50)
        
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        
        if username in self.akun_terdaftar and self.akun_terdaftar[username] == password:
            print(f"✓ Selamat datang kembali, {username}! 👋")
            
            # Catat login ke histori
            if username in self.histori_login:
                self.histori_login[username]["total_login"] += 1
                self.histori_login[username]["riwayat_login"].append(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            self.simpan_histori()  # Simpan histori update
            
            return username
        else:
            print("❌ Username atau password salah!")
            return None
    
    def lihat_statistik(self, username):
        """Tampilkan statistik pengguna"""
        if username in self.histori_login:
            data = self.histori_login[username]
            print("\n" + "="*50)
            print(f"📊 STATISTIK PEMAIN: {username}")
            print("="*50)
            print(f"📅 Tanggal Dibuat: {data['tanggal_dibuat']}")
            print(f"🔢 Total Login: {data['total_login']} kali")
            
            if data['riwayat_login']:
                print(f"⏰ Login Terakhir: {data['riwayat_login'][-1]}")
            
            if data['statistik_game']:
                print(f"\n📈 Statistik Game:")
                for stat in data['statistik_game'][-5:]:  # Tampilkan 5 permainan terakhir
                    print(f"  - {stat['tanggal']}: Level {stat['kesulitan']} | "
                          f"HP Akhir: {stat['hp_akhir']}/{stat['hp_max']} | "
                          f"Kristal: {stat['kristal']}/7")
            print("="*50)
    
    def menu_utama_login(self):
        """Menu utama untuk login dan registrasi"""
        while True:
            print("\n" + "╔" + "="*48 + "╗")
            print("║" + "  🎮 MENU UTAMA - TAMAN MISTERI  ".center(50) + "║")
            print("╚" + "="*48 + "╝")
            print("\n1. Login")
            print("2. Registrasi")
            print("3. Lihat Statistik")
            print("4. Keluar Game")
            
            pilihan = input("\nPilihan (1-4): ")
            
            if pilihan == "1":
                username = self.login()
                if username:
                    return username
            elif pilihan == "2":
                self.registrasi()
            elif pilihan == "3":
                username = input("Masukkan username: ").strip()
                self.lihat_statistik(username)
            elif pilihan == "4":
                print("\nTerima kasih telah bermain! 👋")
                exit()
            else:
                print("❌ Pilihan tidak valid!")

class Pemain:
    def __init__(self, nama, tingkat_kesulitan="normal"):
        self.nama = nama
        self.tingkat_kesulitan = tingkat_kesulitan
        
        # Waktu mulai game
        self.waktu_mulai = datetime.now()
        
        # HP berdasarkan tingkat kesulitan
        if tingkat_kesulitan == "mudah":
            self.hp = 150
            self.max_hp = 150
            self.mana = 100
            self.max_mana = 100
        elif tingkat_kesulitan == "sulit":
            self.hp = 60
            self.max_hp = 60
            self.mana = 80
            self.max_mana = 80
            self.enemy_damage_multiplier = 1.3
        else:  # normal
            self.hp = 100
            self.max_hp = 100
            self.mana = 90
            self.max_mana = 90
            self.enemy_damage_multiplier = 1.0
            
        self.inventaris = []
        self.misteri_terpecahkan = 0
        self.lokasi_sekarang = "gerbang"
        self.lokasi_dikunjungi = set()
        self.pertempuran_menang = 0
        self.kesalahan_total = 0
        
        # Sistem Senjata
        self.senjata_pemilik = {}  # {kode_senjata: Senjata object}
        self.senjata_aktif = None  # Senjata yang sedang digunakan
        self.senjata_level_tertinggi = 0  # Level senjata tertinggi yang ditemukan
        
        # Penjaga Gerbang yang sudah dikalahkan
        self.penjaga_dikalahkan = set()  # {nama_penjaga}
        
        # Tracking Pemulihan HP
        self.pemulihan_hp_digunakan = 0  # Berapa kali sudah menggunakan pemulihan
        self.max_pemulihan_hp = 5  # Berapa kali maksimal bisa digunakan per game
        
        # Status effect
        self.keracunan = False
        self.terkunci = False
        self.boost_attack = 0
        self.boost_defense = 0
        
    def ambil_item(self, item):
        self.inventaris.append(item)
        print(f"✓ Kamu mengambil: {item}")
        
    def gunakan_item(self, item):
        if item in self.inventaris:
            self.inventaris.remove(item)
            return True
        return False
    
    def gunakan_mana(self, cost):
        """Gunakan mana untuk skill spesial"""
        if self.mana >= cost:
            self.mana -= cost
            return True
        return False
    
    def regenerasi_mana(self, jumlah=20):
        """Regenerasi mana setiap turn"""
        self.mana = min(self.mana + jumlah, self.max_mana)
    
    def tambah_senjata(self, kode_senjata, senjata_obj):
        """Tambah senjata ke inventaris pemain"""
        self.senjata_pemilik[kode_senjata] = senjata_obj
        
        # Update level senjata tertinggi
        if senjata_obj.level_diperlukan > self.senjata_level_tertinggi:
            self.senjata_level_tertinggi = senjata_obj.level_diperlukan
        
        # Otomatis gunakan senjata pertama atau yang lebih baik
        if self.senjata_aktif is None or senjata_obj.level_diperlukan > self.senjata_aktif.level_diperlukan:
            self.gunakan_senjata(kode_senjata)
            return True
        return False
    
    def gunakan_senjata(self, kode_senjata):
        """Gunakan senjata tertentu"""
        if kode_senjata in self.senjata_pemilik:
            self.senjata_aktif = self.senjata_pemilik[kode_senjata]
            return True
        return False
    
    def lihat_senjata(self):
        """Tampilkan senjata yang dimiliki"""
        print("\n⚔️ ══════ SENJATA YANG DIMILIKI ══════")
        if not self.senjata_pemilik:
            print("Kamu belum memiliki senjata apapun!")
            return
        
        for i, (kode, senjata) in enumerate(self.senjata_pemilik.items(), 1):
            status = " (AKTIF)" if self.senjata_aktif == senjata else ""
            print(f"{i}. {senjata.nama}{status}")
            print(f"   Damage: {senjata.damage_min}-{senjata.damage_max} | Mana: {senjata.mana_cost} | Level: {senjata.level_diperlukan}")
            print(f"   {senjata.deskripsi}")
        
        print("\n" + "─"*40)
    
    def lihat_status(self):
        print(f"\n═══ STATUS PEMAIN ═══")
        print(f"Nama: {self.nama}")
        print(f"Tingkat Kesulitan: {self.tingkat_kesulitan.upper()} ⚔️")
        print(f"HP: {self.hp}/{self.max_hp} ❤️")
        print(f"Misteri Terpecahkan: {self.misteri_terpecahkan}/6 🔍")
        print(f"Inventaris: {', '.join(self.inventaris) if self.inventaris else 'Kosong'}")
        print(f"Lokasi: {self.lokasi_sekarang}\n")

def cerita_pembukaan(pemain):
    print("\n" + "="*60)
    print("🌙 MISTERI TAMAN YANG TERLUPAKAN - CERITA UTAMA 🌙")
    print("="*60)
    time.sleep(0.5)
    
    print(f"\nSelamat datang, {pemain.nama}!")
    print("\n" + "─"*60)
    print("CERITA:")
    print("─"*60)
    
    print("""
500 tahun yang lalu, Taman Misteri adalah tempat paling indah di dunia.
Raja Kuno dan Ratu Mistis memimpin dengan bijak. Namun, seorang penyihir jahat
bernama Malachar datang dan meracuni taman dengan kutukan gelap.

Raja Kuno mengumpulkan 6 Penjaga Dimensi untuk melindungi taman:
  🌺 Peri Bunga - Penjaga Keindahan (mudah dipahami)
  🌲 Werewolf Hutan - Penjaga Kekuatan (tantangan biasa)
  💧 Hantu Danau - Penjaga Kebijaksanaan (tantangan biasa)
  💻 Sage Coding - Penjaga Logika (tantangan sedang)
  📚 Pustakawan Kuno - Penjaga Pengetahuan (tantangan sedang)
  ⛩️ Pendeta Kuil - Penjaga Keseimbangan (tantangan sulit)
  🐞 Debug Hunter - Penjaga Kesempurnaan (tantangan sulit)
  🏔️ Naga Purba - Penjaga Harta Utama (sangat sulit)

Setiap penjaga menyimpan Kristal Energi Dimensi. Ketika 6 kristal berkumpul,
kutukan akan terangkat dan portal ke Ruang Harta Karun akan terbuka.

MISI MU: Temui setiap penjaga, mengerti maksud mereka, dan kumpulkan kristal mereka.
    """)
    
    print("─"*60)
    print(f"Kamu akan memulai petualangan di Level: {pemain.tingkat_kesulitan.upper()}")
    print(f"HP Awal: {pemain.hp}/{pemain.max_hp}")
    print("─"*60)
    print("\nGerbang taman terbuka dengan cahaya ungu mistis...")
    print("Energi kuno terasa mengelilingimu...")
    input("\nTekan ENTER untuk mulai petualangan...")


def tantangan_pemulihan_hp(pemain):
    """
    Sistem pemulihan HP dengan berbagai tantangan.
    Pemain harus menyelesaikan tantangan untuk mendapatkan HP kembali.
    """
    print("\n" + "="*60)
    print("💚 RUANG PEMULIHAN MISTERIUS 💚")
    print("="*60)
    
    # Pengecekan cooldown/batasan penggunaan
    if pemain.pemulihan_hp_digunakan >= pemain.max_pemulihan_hp:
        print("\n❌ AKSES DITOLAK!")
        print(f"Kamu sudah menggunakan fasilitas pemulihan {pemain.pemulihan_hp_digunakan} kali.")
        print(f"Maksimum pemulihan per permainan adalah {pemain.max_pemulihan_hp} kali.")
        print("\nSosok mistis berbicara:")
        print('"Energi pemulihan telah habis. Kamu harus menyelesaikan petualanganmu'
              ' dengan kekuatanmu sendiri."')
        input("\nTekan ENTER untuk kembali ke gerbang...")
        return
    
    sisa_pemulihan = pemain.max_pemulihan_hp - pemain.pemulihan_hp_digunakan
    print(f"\n✨ Sisa Kesempatan Pemulihan: {sisa_pemulihan}/{pemain.max_pemulihan_hp}")
    
    print("\nKamu memasuki ruangan bercahaya yang penuh energi pemulihan...")
    print("Seorang sosok mistis muncul dari kesembilan arah.\n")
    
    print("Sosok Mistis berbicara:")
    print('"Setiap petualang membutuhkan istirahat. Namun aku tidak memberi hadiah'
          ' dengan gratis."')
    print('"Selesaikan tantanganku, dan energi pemulihan akan mengalir ke dalam tubuhmu."\n')
    
    print("="*60)
    print("PILIH JENIS TANTANGAN:")

    print("="*60)
    print("1. 🧩 RIDDLE MISTIS (Puzzle logika)")
    print("2. 🧮 MATH CHALLENGE (Tantangan matematika)")
    print("3. 🎯 MEMORY GAME (Permainan memori)")
    print("4. ❌ Batal")
    
    pilihan = input("\nPilihan (1-4): ").strip()
    
    if pilihan == "4":
        print("\nKamu membatalkan pemulihan dan meninggalkan ruangan.")
        return
    
    berhasil = False
    
    if pilihan == "1":
        # RIDDLE MISTIS
        berhasil = tantangan_riddle(pemain)
    elif pilihan == "2":
        # MATH CHALLENGE
        berhasil = tantangan_matematika(pemain)
    elif pilihan == "3":
        # MEMORY GAME
        berhasil = tantangan_memori(pemain)
    else:
        print("❌ Pilihan tidak valid!")
        return
    
    # Tambah counter penggunaan
    pemain.pemulihan_hp_digunakan += 1
    
    if berhasil:
        # Hitung pemulihan berdasarkan tingkat kesulitan
        if pemain.tingkat_kesulitan == "mudah":
            pemulihan = int(pemain.max_hp * 0.5)  # 50% HP
        elif pemain.tingkat_kesulitan == "sulit":
            pemulihan = int(pemain.max_hp * 0.3)  # 30% HP
        else:  # normal
            pemulihan = int(pemain.max_hp * 0.4)  # 40% HP
        
        pemain.hp = min(pemain.hp + pemulihan, pemain.max_hp)
        
        print("\n" + "✨"*30)
        print("✨ TANTANGAN BERHASIL! ✨")
        print("✨"*30)
        print(f"Energi pemulihan menyala terang dari kaki hingga kepala!")
        print(f"HP Pemulihan: +{pemulihan}")
        print(f"HP Sekarang: {pemain.hp}/{pemain.max_hp}")
        sisa = pemain.max_pemulihan_hp - pemain.pemulihan_hp_digunakan
        print(f"Sisa kesempatan: {sisa}/{pemain.max_pemulihan_hp}")
        print("="*60)
    else:
        print("\n" + "❌"*30)
        print("❌ TANTANGAN GAGAL! ❌")
        print("❌"*30)
        print("Energi pemulihan gagal mengalir ke tubuhmu.")
        print("Kamu harus mencoba lagi nanti dengan hati lebih fokus.")
        print("="*60)
    
    input("\nTekan ENTER untuk kembali ke gerbang...")


def tantangan_riddle(pemain):
    """Tantangan riddle/puzzle untuk pemulihan HP"""
    riddles = [
        {
            "pertanyaan": "Aku memiliki kota tapi tidak ada rumah? Hutan tapi tidak ada pohon? Air tapi tidak ada ikan? Apa aku?",
            "jawaban": ["peta", "map"],
            "hint": "Sesuatu yang menunjukkan lokasi"
        },
        {
            "pertanyaan": "Aku memiliki wajah dan dua tangan tetapi tidak memiliki lengan atau kaki? Apa aku?",
            "jawaban": ["jam", "clock", "waktu"],
            "hint": "Sesuatu yang mengukur waktu"
        },
        {
            "pertanyaan": "Semakin banyak kamu mengambil, semakin banyak tersisa. Apa aku?",
            "jawaban": ["jejak", "footsteps", "langkah kaki"],
            "hint": "Sesuatu yang ditinggalkan saat berjalan"
        }
    ]
    
    riddle = random.choice(riddles)
    
    print("\n" + "🧩"*30)
    print("\n🧩 RIDDLE MISTIS 🧩")
    print("="*60)
    print(f"Pertanyaan: {riddle['pertanyaan']}")
    print(f"Hint: {riddle['hint']}")
    print("="*60)
    
    jawaban_pemain = input("\nJawabanmu: ").strip().lower()
    
    jawaban_benar = any(jawaban_pemain == j.lower() for j in riddle['jawaban'])
    
    if jawaban_benar:
        print(f"\n✓ BENAR! Jawabannya adalah: {riddle['jawaban'][0]}")
        return True
    else:
        print(f"\n✗ SALAH! Jawaban yang benar adalah: {riddle['jawaban'][0]}")
        return False


def tantangan_matematika(pemain):
    """Tantangan matematika untuk pemulihan HP"""
    print("\n" + "🧮"*30)
    print("\n🧮 MATH CHALLENGE 🧮")
    print("="*60)
    print("Selesaikan 2 dari 3 soal matematika dengan benar!\n")
    
    benar = 0
    total = 3
    
    soal = [
        {
            "pertanyaan": "Berapa hasil dari 7 × 8 - 12 + 4?",
            "jawaban": 48,
            "opsi": ["36", "48", "60", "72"]
        },
        {
            "pertanyaan": "Jika x + 5 = 20, berapakah nilai x?",
            "jawaban": 15,
            "opsi": ["10", "15", "20", "25"]
        },
        {
            "pertanyaan": "Berapa percentage dari 25% dari 200?",
            "jawaban": 50,
            "opsi": ["30", "40", "50", "60"]
        }
    ]
    
    random.shuffle(soal)
    
    for i, s in enumerate(soal, 1):
        print(f"Soal {i}/3: {s['pertanyaan']}")
        for j, opsi in enumerate(s['opsi'], 1):
            print(f"  {j}. {opsi}")
        
        jawaban = input("Jawaban (1-4): ").strip()
        
        try:
            index = int(jawaban) - 1
            if 0 <= index < len(s['opsi']):
                if int(s['opsi'][index]) == s['jawaban']:
                    print("✓ BENAR!\n")
                    benar += 1
                else:
                    print(f"✗ SALAH! Jawaban yang benar adalah {s['jawaban']}\n")
            else:
                print("❌ Input tidak valid!\n")
        except:
            print("❌ Input tidak valid!\n")
    
    print("="*60)
    print(f"HASIL: {benar}/3 soal benar")
    print("="*60)
    
    if benar >= 2:
        print("✓ Kamu lulus math challenge!")
        return True
    else:
        print("✗ Kamu tidak lulus math challenge.")
        return False


def tantangan_memori(pemain):
    """Tantangan memory game untuk pemulihan HP"""
    print("\n" + "🎯"*30)
    print("\n🎯 MEMORY GAME 🎯")
    print("="*60)
    print("Ingat pola angka dan tuliskan kembali!\n")
    
    # Buat sequence random
    sequence = [random.randint(1, 4) for _ in range(5)]
    
    print("Perhatikan pola angka ini selama 5 detik:")
    print("="*60)
    time.sleep(1)
    
    # Tampilkan pola
    for num in sequence:
        print(f"  {num}", end="", flush=True)
        time.sleep(0.5)
    
    print("\n" + "="*60)
    time.sleep(2)
    
    # Clear screen effect
    print("\n[Pola telah disembunyikan. Silakan ketik urutan angka yang kamu ingat]\n")
    time.sleep(1)
    
    jawaban = input("Urutan angka (pisahkan dengan spasi): ").strip().split()
    
    # Convert ke integer
    try:
        jawaban = [int(x) for x in jawaban]
    except:
        print("❌ Input tidak valid!")
        return False
    
    if jawaban == sequence:
        print("\n✓ BENAR! Kamu mengingat pola dengan sempurna!")
        return True
    else:
        print(f"\n✗ SALAH! Pola yang benar adalah: {sequence}")
        print(f"Jawaban mu: {jawaban}")
        return False


def lokasi_gerbang(pemain):
    print("\n🏰 GERBANG TAMAN 🏰")
    print("─" * 50)
    print("Kamu berdiri di depan gerbang besar berusia ratusan tahun.")
    print("Patung singa kuno menjaga kedua sisinya.")
    print(f"Status: Level {pemain.tingkat_kesulitan.upper()} | HP: {pemain.hp}/{pemain.max_hp}")
    print("\n" + "="*50)
    print("📍 DAFTAR LOKASI (Diurutkan Berdasarkan Tingkat Kesulitan)")
    print("="*50)
    print("\n🟢 MUDAH")
    print("1. 🌺 Taman Bunga Pesona (tenggara)")
    
    print("\n🟡 NORMAL")
    print("2. 🌲 Hutan Gelap (timur)")
    print("3. 💧 Danau Misterius (barat)")
    
    print("\n🟠 SEDANG")
    print("4. 💻 Lembah Coding (selatan)")
    print("5. 📚 Perpustakaan Kuno (tengah)")
    
    print("\n🔴 SULIT")
    print("6. ⛩️ Kuil Kuno (utara)")
    print("7. 🐞 Gunung Bug (barat daya)")
    
    print("\n🔥 SANGAT SULIT")
    print("8. 🏔️ Gua Naga Purba (timur laut)")
    
    print("\n⚔️ FASILITAS SPESIAL")
    print("9. 🗡️ Ruang Senjata (Carilah senjata berdasarkan kristal)")
    print("10. � Ruang Pemulihan HP (Tantang dirimu untuk pemulihan)")
    print("11. 📊 Lihat Status & Senjata")
    print("12. Keluar Game")
    
    pilihan = input("\nPilihan (1-12): ")
    
    # Menggunakan if-else untuk mengarahkan ke jalur yang dipilih (berdasarkan urutan level)
    if pilihan == "1":
        taman_bunga_pesona(pemain)
    elif pilihan == "2":
        semak_hutan_gelap(pemain)
    elif pilihan == "3":
        danau_misterius(pemain)
    elif pilihan == "4":
        lembah_coding(pemain)
    elif pilihan == "5":
        perpustakaan_kuno(pemain)
    elif pilihan == "6":
        kuil_kuno(pemain)
    elif pilihan == "7":
        gunung_bug(pemain)
    elif pilihan == "8":
        gua_naga_purba(pemain)
    elif pilihan == "9":
        ruang_senjata(pemain)
    elif pilihan == "10":
        tantangan_pemulihan_hp(pemain)
    elif pilihan == "11":
        pemain.lihat_status()
        pemain.lihat_senjata()
        lokasi_gerbang(pemain)
    elif pilihan == "12":
        print("\nTerima kasih telah bermain! 👋")
        return False
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        lokasi_gerbang(pemain)
    
    return True

def ruang_senjata(pemain):
    """
    Ruang Senjata - Lokasi khusus untuk mencari senjata
    Senjata dapat ditemukan berdasarkan jumlah kristal yang dikumpulkan
    """
    print("\n" + "="*70)
    print("🗡️ RUANG SENJATA KUNO 🗡️")
    print("="*70)
    print("Ruangan gelap berisi rak-rak berisi senjata berusia berabad-abad...")
    print("Cahaya mistis bersinar dari setiap sudut.")
    print("─"*70)
    
    print(f"\n📊 STATISTIK KRISTAL MU: {pemain.misteri_terpecahkan}/7 Kristal")
    print(f"⚔️ Senjata Pemilik: {len(pemain.senjata_pemilik)}")
    if pemain.senjata_aktif:
        print(f"Senjata Aktif: {pemain.senjata_aktif.nama}")
    else:
        print("Belum ada senjata aktif")
    
    # Tentukan senjata mana yang bisa diakses berdasarkan kristal
    senjata_tersedia = []
    
    if pemain.misteri_terpecahkan >= 0:
        senjata_tersedia.append(("pedang_kayu", DATABASE_SENJATA["pedang_kayu"], "Tersedia tanpa kristal"))
    if pemain.misteri_terpecahkan >= 1:
        senjata_tersedia.append(("pedang_besi", DATABASE_SENJATA["pedang_besi"], "Memerlukan 1 Kristal"))
    if pemain.misteri_terpecahkan >= 2:
        senjata_tersedia.append(("pedang_ajaib", DATABASE_SENJATA["pedang_ajaib"], "Memerlukan 2 Kristal"))
    if pemain.misteri_terpecahkan >= 3:
        senjata_tersedia.append(("pedang_cahaya", DATABASE_SENJATA["pedang_cahaya"], "Memerlukan 3 Kristal"))
    if pemain.misteri_terpecahkan >= 4:
        senjata_tersedia.append(("pedang_petir", DATABASE_SENJATA["pedang_petir"], "Memerlukan 4 Kristal"))
    if pemain.misteri_terpecahkan >= 5:
        senjata_tersedia.append(("pedang_naga", DATABASE_SENJATA["pedang_naga"], "Memerlukan 5 Kristal - SENJATA LEGENDARIS!"))
    
    print("="*70)
    print("⚔️ SENJATA YANG DAPAT DIAKSES:")
    print("="*70)
    
    for i, (kode, senjata, status) in enumerate(senjata_tersedia, 1):
        print(f"\n{i}. {senjata.nama}")
        print(f"   • Damage: {senjata.damage_min}-{senjata.damage_max}")
        print(f"   • Mana Cost: {senjata.mana_cost}")
        print(f"   • Status: {status}")
        print(f"   • {senjata.deskripsi}")
    
    if len(senjata_tersedia) == 0:
        print("❌ Tidak ada senjata yang bisa diakses.")
        print("Carilah kristal lebih banyak untuk membuka senjata!")
    else:
        print("\n" + "="*70)
        pilihan = input(f"\nPilih senjata (1-{len(senjata_tersedia)}) atau 0 untuk kembali: ")
        
        try:
            pilihan_int = int(pilihan)
            if pilihan_int == 0:
                lokasi_gerbang(pemain)
                return
            elif 1 <= pilihan_int <= len(senjata_tersedia):
                kode_senjata, senjata_obj, _ = senjata_tersedia[pilihan_int - 1]
                
                # Cek apakah sudah dimiliki
                if kode_senjata in pemain.senjata_pemilik:
                    print(f"\nℹ️ Kamu sudah memiliki {senjata_obj.nama}!")
                    print("Gunakan opsi lain untuk berganti senjata.")
                else:
                    # Dapatkan senjata
                    print(f"\n✨ Kamu menemukan {senjata_obj.nama}!")
                    print(f"{senjata_obj.deskripsi}")
                    print("Senjata ini bersinar dengan energi magis...")
                    time.sleep(1)
                    
                    # Tambah senjata dan gunakan
                    pemain.tambah_senjata(kode_senjata, senjata_obj)
                    print(f"⚔️ {senjata_obj.nama} sekarang menjadi senjata aktif mu!")
                    print(f"Damage: {senjata_obj.damage_min}-{senjata_obj.damage_max}")
                
                input("\nTekan ENTER untuk kembali ke gerbang...")
                lokasi_gerbang(pemain)
            else:
                print("❌ Pilihan tidak valid!")
                ruang_senjata(pemain)
        except:
            print("❌ Input tidak valid!")
            ruang_senjata(pemain)
\n\ndef semak_hutan_gelap(pemain):
    # PERTARUNGAN PENJAGA GERBANG
    penjaga_menang = pertarungan_penjaga_gerbang(
        pemain=pemain,
        nama_penjaga="Werewolf Junior",
        deskripsi_penjaga="Seekor werewolf muda dengan tubuh bercat abu-abu berdiri menjaga pintu hutan.",
        hp_penjaga=50,
        damage_penjaga=12,
        level_lokasi="NORMAL"
    )
    
    if not penjaga_menang:
        print("\n❌ Werewolf tidak membiarkanmu masuk ke Hutan Gelap.")
        return
    
    print("\n" + "="*60)
    print("🌲 HUTAN GELAP - LOKASI NORMAL 🌲")
    print("="*60)
    print("Penjaga: Werewolf Hutan (Penjaga Kekuatan)")
    print("="*60)
    
    print("Pohon-pohon tinggi memblokir cahaya matahari.")
    print("Kegelapan menyelimuti sekelilingmu... terdengar suara binatang berbahaya!")
    
    print("\nKarena matahari mulai terbenam, aura penjaga Hutan mulai terekspos...")
    print("Seekor Werewolf keluar dengan mata bersinar merah!")
    
    print("\n" + "─"*60)
    print("WEREWOLF HUTAN berbicara dengan suara yang berat:")
    print("─"*60)
    print("""
'Aku adalah Werewolf Hutan, Penjaga Kekuatan. Aku adalah simbol
dari kekuatan yang dibutuhkan untuk melindungi taman dari malapetaka.

Kutukan Malachar membuat kami menjadi penjaga yang ketat dan tegas.
Untuk membuktikan kekuatanmu, aku akan menguji kemampuanmu!'
    """)
    
    print("\nAda 3 jalan di depanmu:")
    print("1. Jalan ke kanan (terlihat cahaya)")
    print("2. Jalan ke kiri (terdengar air mengalir)")
    print("3. Kembali ke gerbang")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        bertemu_monster_hutan(pemain)
    elif pilihan == "2":
        misteri_pohon_tua(pemain)
    elif pilihan == "3":
        pemain.lokasi_sekarang = "gerbang"
    else:
        print("Pilihan tidak valid!")
        semak_hutan_gelap(pemain)


def bertemu_monster_hutan(pemain):
    print("\n👹 PERTARUNGAN BOSS: WEREWOLF HUTAN 👹")
    print("═" * 50)
    print("Seekor Werewolf legendaris dengan mata merah menyala!")
    print("Dia adalah penjaga Hutan yang telah menunggu musuh sejati...")
    time.sleep(1)
    
    # Boss stats
    boss_hp = 80 if pemain.tingkat_kesulitan == "mudah" else (60 if pemain.tingkat_kesulitan == "sulit" else 70)
    boss_max_hp = boss_hp
    
    print("\n┌─ STRATEGI PERTARUNGAN ─┐")
    print("1. ⚔️  SERANGAN BIASA (Damage: 15-20, Mana: 0)")
    print("2. 🔥 SERANGAN KHUSUS (Damage: 30-40, Mana: 30)")
    print("3. 🛡️  PERTAHANAN (Reduce damage 50%, Mana: 20)")
    print("4. 💚 PENYEMBUHAN (Heal: 25, Mana: 35)")
    print("5. 🏃 MELARIKAN DIRI (50% berhasil)")
    print("└────────────────────────┘")
    
    pertarungan_berlangsung = True
    giliran_pemain = True
    damage_multiplier = 1.3 if pemain.tingkat_kesulitan == "sulit" else 1.0
    
    while pertarungan_berlangsung:
        print(f"\n┌─ STATUS ─────────┐")
        print(f"│ Pemain HP:  {pemain.hp}/{pemain.max_hp} ({int(pemain.hp/pemain.max_hp*100)}%)")
        print(f"│ Mana:       {pemain.mana}/{pemain.max_mana}")
        print(f"│ Werewolf: {boss_hp}/{boss_max_hp} ({int(boss_hp/boss_max_hp*100)}%)")
        print(f"└────────────────────┘")
        
        if giliran_pemain:
            pilihan = input("\nPilahan aksi (1-5): ")
            
            if pilihan == "1":  # Serangan biasa
                # Gunakan bonus damage dari senjata jika ada
                if pemain.senjata_aktif:
                    damage = pemain.senjata_aktif.hitung_damage()
                    desc_senjata = f" dengan {pemain.senjata_aktif.nama}"
                else:
                    damage = random.randint(15, 20)
                    desc_senjata = ""
                
                boss_hp -= damage
                print(f"⚔️  Kamu menyerang{desc_senjata}! Damage: {damage}")
                pemain.regenerasi_mana(5)
                
            elif pilihan == "2":  # Serangan khusus
                # Serangan khusus menggunakan mana lebih banyak untuk senjata
                mana_cost = 30
                if pemain.senjata_aktif and pemain.senjata_aktif.mana_cost > 0:
                    mana_cost = pemain.senjata_aktif.mana_cost + 20
                
                if pemain.gunakan_mana(mana_cost):
                    if random.random() > 0.3:  # 70% hit rate
                        base_damage = random.randint(30, 40)
                        if pemain.senjata_aktif:
                            # Senjata memberikan bonus damage
                            base_damage += pemain.senjata_aktif.damage_max // 2
                        damage = int(base_damage * damage_multiplier)
                        boss_hp -= damage
                        senjata_desc = f" {pemain.senjata_aktif.nama}" if pemain.senjata_aktif else ""
                        print(f"🔥 COMBO SERANGAN{senjata_desc}! Damage KRITIS: {damage}!")
                    else:
                        print("🔥 Serangan khususmu meleset!")
                    pemain.regenerasi_mana(10)
                else:
                    print(f"❌ Mana tidak cukup! Mana minimum {mana_cost} dibutuhkan.")
                    continue
                    
            elif pilihan == "3":  # Pertahanan
                if pemain.gunakan_mana(20):
                    print("🛡️  Kamu mengambil posisi pertahanan!")
                    pemain.boost_defense = 1
                    pemain.regenerasi_mana(15)
                else:
                    print("❌ Mana tidak cukup!")
                    continue
                    
            elif pilihan == "4":  # Penyembuhan
                if pemain.gunakan_mana(35):
                    heal = 25
                    pemain.hp = min(pemain.hp + heal, pemain.max_hp)
                    print(f"💚 Kamu menyembuhkan diri! HP +{heal}")
                    pemain.regenerasi_mana(10)
                else:
                    print("❌ Mana tidak cukup!")
                    continue
                    
            elif pilihan == "5":  # Lari
                if random.random() > 0.5:
                    print("✓ Kamu berhasil melarikan diri dari pertarungan!")
                    return
                else:
                    print("✗ Werewolf meninggalkan rasa malu saat kamu coba lari!")
                    boss_hp -= 5  # Damage saat lari gagal
                    
            else:
                print("❌ Pilihan tidak valid!")
                continue
            
            # Serangan boss
            if boss_hp > 0:
                time.sleep(1)
                boss_damage = random.randint(12, 18)
                
                if pemain.boost_defense > 0:
                    boss_damage = int(boss_damage * 0.5)
                    print(f"😤 Werewolf menyerang! Damage: {boss_damage} (pertahanan aktif)")
                    pemain.boost_defense = 0
                else:
                    print(f"😤 Werewolf menyerang! Damage: {boss_damage}")
                
                boss_damage = int(boss_damage * damage_multiplier)
                pemain.hp -= boss_damage
                
                if pemain.hp <= 0:
                    print(f"\n💀 Kamu kalah! Werewolf mengakhiri pertarunganmu...")
                    game_over_kalah(pemain)
                    return
        
        # Cek kemenangan
        if boss_hp <= 0:
            print("\n" + "="*50)
            print("⭐ KEMENANGAN! ⭐")
            print("Werewolf terjatuh dan menatapmu dengan hormat...")
            print("Cahaya putih membungkus tubuhnya...")
            print("'Akhirnya... ada yang kuat dalam misteri ini'")
            print("Dia meninggalkan kristal bercahaya: Kristal Energi Kekuatan")
            print("="*50)
            pemain.ambil_item("Kristal Energi Kekuatan")
            pemain.misteri_terpecahkan += 1
            pemain.pertempuran_menang += 1
            pemain.hp = min(pemain.hp + 30, pemain.max_hp)
            print(f"✓ HP dipulihkan! HP sekarang: {pemain.hp}")
            pertarungan_berlangsung = False

    print("2. Jelajahi lebih jauh")
    
    pilihan2 = input("\nPilihan (1-2): ")
    if pilihan2 == "1":
        pemain.lokasi_sekarang = "gerbang"
    else:
        semak_hutan_gelap(pemain)

def misteri_pohon_tua(pemain):
    print("\n" + "─"*60)
    print("🌳 POHON TUA - UJIAN PENJAGA KEKUATAN 🌳")
    print("─"*60)
    
    print("Kamu menemukan pohon raksasa dengan akar yang melilit tanah.")
    print("Patung batu di bawahnya berbicara dengan mata bersinar!")
    
    print("\n'Aku adalah pohon pengetahuan Hutan Gelap.'")
    print("'Werewolf Hutan menguji kebijakan melalui teka-teki ini:'")
    print("\n🔍 TEKA-TEKI: 'Saya memiliki kota tapi tanpa rumah. Saya memiliki air tapi tanpa ikan.'")
    print("'Saya memiliki jalan tapi tanpa mobil. Apa aku?'")
    
    print("\nJawaban:")
    print("1. Peta")
    print("2. Cermin")
    print("3. Foto")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        print("\n✓ BENAR! Pohon itu bergerak dan membukakan jalan!")
        print("Patung berubah menjadi cahaya emas...")
        print("\nWerewolf Hutan muncul hadir dengan senyum:")
        print("'Kamu telah membuktikan bahwa kebijakan seimbang dengan kekuatan!'")
        print("'Kristal Energi Kekuatan milikku adalah milikmu sekarang.' 💎✨")
        pemain.ambil_item("Kristal Energi Kekuatan")
        pemain.misteri_terpecahkan += 1
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
    else:
        print("\n✗ SALAH! Pohon itu marah dan mengeluarkan gas beracun!")
        pemain.hp -= 20
        print(f"HP berkurang 20 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"


def danau_misterius(pemain):
    # PERTARUNGAN PENJAGA GERBANG
    penjaga_menang = pertarungan_penjaga_gerbang(
        pemain=pemain,
        nama_penjaga="Roh Danau Gerbang",
        deskripsi_penjaga="Sosok transparan berbentuk manusia muncul dari air danau.",
        hp_penjaga=50,
        damage_penjaga=11,
        level_lokasi="NORMAL"
    )
    
    if not penjaga_menang:
        print("\n❌ Roh danau mencegahmu untuk memasuki danau.")
        return
    
    print("\n" + "="*60)
    print("💧 DANAU MISTERIUS - LOKASI NORMAL 💧")
    print("="*60)
    print("Penjaga: Hantu Danau (Penjaga Kebijaksanaan)")
    print("="*60)
    
    print("Air danau bersinar dengan cahaya biru yang aneh.")
    print("Ada perahu tua di tepi danau...")
    print("Namun ada sesuatu yang bergerak di dalam air!")
    
    print("\nKabut mistis mulai muncul di atas danau...")
    print("Sebuah bayangan manusia terlihat di permukaan air!")
    
    print("\nApa yang akan kamu lakukan?")
    print("1. Naik perahu dan seberangi danau")
    print("2. Renang melintasi danau")
    print("3. Cari barang di sekitar danau")
    print("4. Kembali ke gerbang")
    
    pilihan = input("\nPilihan (1-4): ")
    
    if pilihan == "1":
        perahu_berhantu(pemain)
    elif pilihan == "2":
        print("\n🌊 Kamu mulai renang...")
        print("Tiba-tiba sesuatu menangkap kakimu!")
        print("Seekor Naga Air keluar dari kedalaman!")
        pemain.hp -= 40
        print(f"✗ Naga menyerangmu! HP berkurang 40 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    elif pilihan == "3":
        print("\nKamu mencari di sekitar danau...")
        print("Ditemukan: Pedang Ajaib yang tersembunyi di rumput!")
        pemain.ambil_item("pedang ajaib")
        print("⚔️ Senjata yang sempurna untuk menghadapi monster!")
    elif pilihan == "4":
        pemain.lokasi_sekarang = "gerbang"
    else:
        print("Pilihan tidak valid!")
        danau_misterius(pemain)


def perahu_berhantu(pemain):
    print("\n" + "─"*60)
    print("👻 PERAHU BERHANTU - UJIAN PENJAGA KEBIJAKSANAAN 👻")
    print("─"*60)
    
    print("Kamu menaiki perahu dan mulai mendayung...")
    print("Tiba-tiba, kabut tebal menyelimuti danau...")
    print("Cahaya ungu terang dari dalam air!")
    
    print("\n'Hantu Danau' muncul dengan suara yang lembut namun tegas:")
    
    print("\n" + "─"*60)
    print("HANTU DANAU (Penjaga Kebijaksanaan) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Hantu Danau, Penjaga Kebijaksanaan. Dulu aku adalah pendeta
yang bijaksana. Malachar mengubah bijaksanaku menjadi pengakhir.

Saat ini aku hanya tinggal menunggu seseorang cukup bijak untuk
melampaui jebakan pikiran saya. Teka-teki ini telah menunggu 500 tahun...'
    """)
    
    print("\n🔍 TEKA-TEKI: 'Saya naik ketika hujan, turun ketika cerah. Apa aku?'")
    
    print("\nJawaban:")
    print("1. Ember air")
    print("2. Payung")
    print("3. Pita")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "2":
        print("\n✓ BENAR! Hantu menghilang dengan tenang...")
        print("Cahaya putih menerangi danau dan meninggalkan cahaya indah.")
        print("\nHantu Danau kembali hadir dengan suara damai:")
        print("'Akhirnya, kebijaksanaan kembali ke taman ini.'")
        print("'Kristal Energi Kebijaksanaan adalah milikmu.' 💎✨")
        pemain.ambil_item("Kristal Energi Kebijaksanaan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += 15
        print(f"HP pulih +15 (sekarang: {pemain.hp})")
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
    else:
        print(f"\n✗ SALAH! Hantu marah dan menenggelamkan perahu!")
        print("Kamu jatuh ke danau!")
        pemain.hp -= 35
        print(f"HP berkurang 35 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"


def kuil_kuno(pemain):
    # PERTARUNGAN PENJAGA GERBANG
    penjaga_menang = pertarungan_penjaga_gerbang(
        pemain=pemain,
        nama_penjaga="Pendeta Perak",
        deskripsi_penjaga="Seorang pendeta bertubuuh kokoh dengan jubah perak berdiri menjaga kuil.",
        hp_penjaga=70,
        damage_penjaga=16,
        level_lokasi="SULIT"
    )
    
    if not penjaga_menang:
        print("\n❌ Pendeta Kuil tidak membiarkanmu masuk ke dalam kuil.")
        return
    
    print("\n" + "="*60)
    print("⛩️ KUIL KUNO - LOKASI SULIT ⛩️")
    print("="*60)
    print("Penjaga: Pendeta Kuil (Penjaga Keseimbangan)")
    print("="*60)
    
    print("Kamu menemukan kuil berusia berabad-abad dengan arca-arca aneh.")
    print("Sebuah pintu besar tertutup rapat di tengah kuil...")
    print("Aura merah dan biru bersinar dari dalam!")
    
    print("\nSeorang Pendeta dengan mata yang dalam menatapmu...")
    
    print("\n" + "─"*60)
    print("PENDETA KUIL (Penjaga Keseimbangan) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Pendeta Kuil, Penjaga Keseimbangan. Aku menjaga keseimbangan
antara cahaya dan kegelapan, baik dan jahat dalam taman ini.

Malachar menggoyahkan keseimbangan dengan kutukan gelap. Untuk mengembalikan
keseimbangan, aku perlu uji coba yang lebih ketat. Tunjukkan bahwa kamu
memahami keseimbangan sejati!'
    """)
    
    print("\nArea kuil:")
    print("1. Ruang Altar (utara) - Ujian Keseimbangan")
    print("2. Gua Tersembunyi (timur) - Pertarungan Naga Kuil")
    print("3. Ruang Harta Karun (butuh 6 kristal)")
    print("4. Kembali ke gerbang")
    
    pilihan = input("\nPilihan (1-4): ")
    
    if pilihan == "1":
        ruang_altar(pemain)
    elif pilihan == "2":
        gua_tersembunyi(pemain)
    elif pilihan == "3":
        if pemain.misteri_terpecahkan >= 6:
            ruang_harta_karun_final(pemain)
        else:
            print("\n⛓️ Pintu tidak terbuka! Kamu perlu 6 kristal energi dulu!")
            print(f"Saat ini kamu baru punya {pemain.misteri_terpecahkan}/6 kristal")
            kuil_kuno(pemain)
    elif pilihan == "4":
        pemain.lokasi_sekarang = "gerbang"
    else:
        print("Pilihan tidak valid!")
        kuil_kuno(pemain)


def ruang_altar(pemain):
    print("\n" + "─"*60)
    print("🕯️ RUANG ALTAR - UJIAN KESEIMBANGAN 🕯️")
    print("─"*60)
    
    print("Ruangan penuh dengan lilin bernyala di sebelah kiri dan kanan.")
    print("Sebuah tulisan di dinding menampilkan angka-angka: 2 + 3 + 5 = ?")
    print("Pendeta berbisik: 'Keseimbangan berarti mencari harmoni angka-angka.'")
    
    print("\n🔍 Pertanyaan: Berapa hasil dari 2 + 3 + 5?")
    
    jawaban = input("\nJawaban Anda (angka): ")
    
    if jawaban == "10":
        print("\n✓ BENAR! Lantai mulai bergetar dengan harmoni...")
        print("Cahaya putih dan hitam bersatu menjadi emas!")
        print("\nPendeta Kuil muncul dengan tersenyum:")
        print("'Keseimbangan telah kembali. Terima kristal keseimbanganku.' 💎✨")
        pemain.ambil_item("Kristal Energi Keseimbangan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += 20
        print(f"HP pulih +20 (sekarang: {pemain.hp})")
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
    else:
        print("\n✗ SALAH! Altar mengeluarkan serangan cahaya dan gelap!")
        pemain.hp -= 15
        print(f"HP berkurang 15 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk melanjutkan...")
    kuil_kuno(pemain)

def gua_tersembunyi(pemain):
    print("\n" + "─"*60)
    print("🐉 GUA TERSEMBUNYI - SARANG NAGA KUIL 🐉")
    print("─"*60)
    print("Gua gelap ini penuh dengan fosil dan batu-batuan aneh.")
    print("Cahaya merah terang dari sudut gua!")
    print("\nDi sudut gua, ada Naga Kuil yang sangat tua dan sagap!")
    
    print("\n" + "─"*60)
    print("Pendeta Kuil berbisik kepada sosok Naga:")
    print("─"*60)
    print("""
'Naga Kuil, kamu adalah simbol dari pertarungan yang menetap.
Malachar membuat kamu penjaga yang gelisah. Sekarang ada seseorang yang datang
untuk memahami makna sebenarnya. Ujilah mereka!'
    """)
    
    print("\nApa yang kamu lakukan?")
    print("1. Hadapi Naga Kuil dalam pertarungan langsung")
    print("2. Coba diplomasi dengan Naga")
    print("3. Cari harta tersembunyi")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        print("\nKamu menantang Naga Kuil dalam pertarungan sengit!")
        pertarungan_naga(pemain)
    elif pilihan == "2":
        print("\nKamu berbicara dengan lembut kepada Naga...")
        print("Naga melirik dengan mata yang dalam...")
        print("'Akhirnya, seseorang yang mengerti saya....'")
        print("\nNaga memberikan Kristal Energi Perlindungan! 💎✨")
        pemain.ambil_item("Kristal Energi Perlindungan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += 30
        print(f"HP pulih +30 (sekarang: {pemain.hp})")
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
        print("\nNaga kembali tidur dengan damai di gua ini...")
    elif pilihan == "3":
        print("\nKamu mencari di bawah batu besar...")
        print("Ditemukan: Senjata Kuno! Ini mungkin berguna nanti...")
        pemain.ambil_item("Senjata Kuno")
    
    input("\nTekan ENTER untuk melanjutkan...")
    kuil_kuno(pemain)


def pertarungan_naga(pemain):
    print("\n" + "="*60)
    print("🐉 PERTARUNGAN NAGA KUIL! 🐉")
    print("="*60)
    
    if "pedang ajaib" in pemain.inventaris or "Senjata Kuno" in pemain.inventaris:
        print("Kamu mengeluarkan senjata ajaib!")
        print("Naga dan kamu bertarung sengit...")
        time.sleep(1)
        
        if random.random() > 0.3:
            print("⚔️ Dengan gerakan cepat, kamu mengalahkan Naga Kuil!")
            print("Naga itu jatuh dengan elegan, tubuhnya berubah menjadi cahaya emas...")
            print("Kristal Energi Perlindungan jatuh dari langit 💎✨")
            pemain.ambil_item("Kristal Energi Perlindungan")
            pemain.misteri_terpecahkan += 1
            pemain.hp += 20
            print(f"HP pulih +20 (sekarang: {pemain.hp})")
            print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
            return
        else:
            print("✗ Naga terlalu kuat! Kamu terluka parah!")
            pemain.hp -= 30
    else:
        print("✗ Tanpa senjata, kamu tidak bisa mengalahkan naga!")
        pemain.hp -= 45
    
    print(f"HP berkurang, sisa HP: {pemain.hp}")
    if pemain.hp <= 0:
        game_over_kalah(pemain)
        return

def ruang_harta_karun(pemain):
    print("\n" + "="*50)
    print("💰 RUANG HARTA KARUN TERAKHIR 💰")
    print("="*50)
    print("\nPintu dengan hieroglif membuka dengan suara gemuruh...")
    print("Cahaya emas memenuhi ruangan...")
    print("\n🏆 SELAMAT! KAM TELAH MEMECAHKAN SEMUA MISTERI! 🏆")
    
    print("\nDi tengah ruangan ada:")
    print("✓ Medali Emas")
    print("✓ Permata Ungu")
    print("✓ Kristal Biru")
    print("✓ Batu Merah Panas")
    print("✓ Kalung Batu Biru Langit")
    print("✓ Mahkota Permata Naga")
    
    print("\nGate taman terbuka lebar...")
    print("Semua monster dan jebakan kehilangan kekuatan magis mereka...")
    print(f"\n{pemain.nama}, kamu adalah PEMENANG! 🎉")
    print("Kamu berhasil keluar dari Taman Misteri dengan membawa harta karun!")
    print(f"HP Akhir: {pemain.hp}/{pemain.max_hp}")
    print("\n" + "="*50)
    print("TERIMA KASIH TELAH BERMAIN!")
    print("="*50)

def pertarungan_penjaga_gerbang(pemain, nama_penjaga, deskripsi_penjaga, hp_penjaga, damage_penjaga, level_lokasi):
    """
    Sistem pertarungan dengan penjaga gerbang untuk setiap level.
    Penjaga harus dikalahkan untuk masuk ke lokasi.
    
    Args:
        pemain: Object Pemain
        nama_penjaga: Nama penjaga gerbang
        deskripsi_penjaga: Deskripsi penampilan penjaga
        hp_penjaga: HP penjaga
        damage_penjaga: Damage per attack penjaga
        level_lokasi: Tingkat kesulitan lokasi ('mudah', 'normal', 'sulit' dst)
    
    Returns:
        bool: True jika pemain menang, False jika kalah
    """
    
    # Jika sudah dikalahkan, langsung izinkan masuk
    if nama_penjaga in pemain.penjaga_dikalahkan:
        print(f"\n✓ Penjaga {nama_penjaga} mengenali kamu dan membiarkan laluan.")
        return True
    
    print("\n" + "="*60)
    print(f"⚔️  PENJAGA GERBANG: {nama_penjaga.upper()} ⚔️")
    print("="*60)
    print(f"Deskripsi: {deskripsi_penjaga}")
    print(f"Level: {level_lokasi}")
    time.sleep(2)
    
    # Stats penjaga
    boss_hp = hp_penjaga
    boss_max_hp = hp_penjaga
    pemain_damage_multiplier = 1.3 if pemain.tingkat_kesulitan == "sulit" else 1.0
    penjaga_damage_multiplier = 1.4 if pemain.tingkat_kesulitan == "sulit" else 1.0
    
    pertarungan_berlangsung = True
    giliran = 0
    
    print(f"\n{nama_penjaga} berbicara: 'Kamu tidak bisa masuk tanpa izin!'")
    print("Dia siap untuk bertarung...\n")
    time.sleep(1)
    
    print("┌─ OPSI PERTARUNGAN ─┐")
    print("1. ⚔️  Serangan Biasa")
    print("2. 🔥 Serangan Kuat (Mana)")
    print("3. 🛡️  Pertahanan")
    print("4. 💚 Penyembuhan")
    print("5. 🏃 Mundur")
    print("└────────────────────┘\n")
    
    while pertarungan_berlangsung:
        print(f"\n┌─ STATUS ──────────────┐")
        print(f"│ Pemain HP:  {pemain.hp}/{pemain.max_hp}")
        print(f"│ Mana:       {pemain.mana}/{pemain.max_mana}")
        print(f"│ {nama_penjaga}: {boss_hp}/{boss_max_hp}")
        print(f"└────────────────────────┘")
        
        pilihan = input("\nPilihan aksi (1-5): ").strip()
        
        if pilihan == "1":  # Serangan biasa
            damage = random.randint(10, 18)
            damage = int(damage * pemain_damage_multiplier)
            boss_hp -= damage
            print(f"⚔️  Kamu menyerang! Damage: {damage}")
            
        elif pilihan == "2":  # Serangan kuat
            if pemain.gunakan_mana(25):
                if random.random() > 0.25:  # 75% hit
                    damage = random.randint(25, 35)
                    damage = int(damage * pemain_damage_multiplier)
                    boss_hp -= damage
                    print(f"🔥 Serangan kuat! Damage: {damage}!")
                else:
                    print("🔥 Serangan meleset!")
            else:
                print("❌ Mana tidak cukup (butuh 25)!")
                continue
                
        elif pilihan == "3":  # Pertahanan
            if pemain.gunakan_mana(15):
                pemain.boost_defense = 1
                print("🛡️  Kamu dalam posisi pertahanan! Damage berkurang 50%")
            else:
                print("❌ Mana tidak cukup (butuh 15)!")
                continue
                
        elif pilihan == "4":  # Penyembuhan
            if pemain.gunakan_mana(30):
                heal = 20
                pemain.hp = min(pemain.hp + heal, pemain.max_hp)
                print(f"💚 Kamu menyembuhkan diri! HP +{heal}")
            else:
                print("❌ Mana tidak cukup (butuh 30)!")
                continue
                
        elif pilihan == "5":  # Mundur
            if random.random() > 0.5:  # 50% success
                print(f"✓ Kamu berhasil mundur dari {nama_penjaga}.")
                print("(Kamu bisa coba lagi nanti)")
                return False
            else:
                print(f"✗ {nama_penjaga} memblokir jalanmu!")
                
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        # Regenerasi mana
        pemain.regenerasi_mana(5)
        
        # Serangan penjaga
        if boss_hp > 0:
            time.sleep(1)
            penjaga_damage = random.randint(12, damage_penjaga)
            
            if pemain.boost_defense > 0:
                penjaga_damage = int(penjaga_damage * 0.5)
                print(f"😤 {nama_penjaga} menyerang! Damage: {penjaga_damage} (pertahanan aktif)")
                pemain.boost_defense = 0
            else:
                print(f"😤 {nama_penjaga} menyerang! Damage: {penjaga_damage}")
            
            penjaga_damage = int(penjaga_damage * penjaga_damage_multiplier)
            pemain.hp -= penjaga_damage
            
            if pemain.hp <= 0:
                print(f"\n💀 Kamu kalah dari {nama_penjaga}!")
                print("Penjaga tidak membiarkanmu masuk...")
                return False
        
        # Cek kemenangan
        if boss_hp <= 0:
            print("\n" + "="*60)
            print(f"⭐ KEMENANGAN! ⭐")
            print(f"Kamu berhasil mengalahkan {nama_penjaga}!")
            print("="*60)
            print(f"{nama_penjaga} kalah dan membiarkanmu masuk ke lokasi ini.")
            pemain.penjaga_dikalahkan.add(nama_penjaga)
            pemain.pertempuran_menang += 1
            
            # Bonus HP kecil setelah menang
            bonus_hp = 15
            pemain.hp = min(pemain.hp + bonus_hp, pemain.max_hp)
            print(f"Bonus HP +{bonus_hp} (sekarang: {pemain.hp})")
            pertarungan_berlangsung = False
            return True
    
    return False

def game_over_kalah(pemain):
    print("\n" + "="*50)
    print("💀 GAME OVER 💀")
    print("="*50)
    print(f"\nHp {pemain.nama} habis...")
    print("Kamu kalah dalam petualangan di Taman Misteri...")
    print(f"Misteri yang berhasil dipecahkan: {pemain.misteri_terpecahkan}/3")
    print("\nCoba lagi lebih hati-hati! 👻")
    print("="*50)

def lembah_coding(pemain):
    """
    Lembah Coding - Jalur dengan tantangan logika dan programming
    Penjaga: Sage Coding (Penjaga Logika)
    """
    print("\n" + "="*60)
    print("💻 LEMBAH CODING - LOKASI SEDANG 💻")
    print("="*60)
    print("Penjaga: Sage Coding (Penjaga Logika)")
    print("="*60)
    
    print("Kamu memasuki lembah yang dipenuhi dengan rune-rune aneh.")
    print("Setiap rune menyala dengan cahaya biru, menampilkan kode magis!")
    
    print("\nSeorang pria dengan pakaian tahun 2000-an muncul dari portal digital!")
    
    print("\n" + "─"*60)
    print("SAGE CODING (Penjaga Logika) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Sage Coding, Penjaga Logika. Aku adalah manifestasi dari
pembuat taman yang menggunakan logika untuk melindungi dari kutukan.

Untuk menguji apakah logikamu cukup kuat, aku akan memberikan 3 tantangan.
Tunjukkan bahwa kamu memahami hukum-hukum fundamental dari dunia digital!'
    """)
    
    tantangan_selesai = 0
    
    while tantangan_selesai < 3:
        print(f"\n📊 Tantangan {tantangan_selesai + 1}/3")
        print("─" * 40)
        
        if tantangan_selesai == 0:
            # Tantangan 1: Loop Python
            print("TANTANGAN 1: PERULANGAN MAGIS")
            print("Kode di bawah ini akan menghasilkan output apa?")
            print("\nfor i in range(1, 4):")
            print("    print(i * i)")
            print("\n1. 1 2 3")
            print("2. 1 4 9")
            print("3. 3 6 9")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "2":
                print("\n✓ BENAR! Logika perulangan Anda sempurna!")
                pemain.hp += 10
                print(f"HP pulih +10 (sekarang: {pemain.hp})")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Logika yang salah menyebabkan ledakan energi!")
                pemain.hp -= 15
                print(f"HP berkurang 15 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif tantangan_selesai == 1:
            # Tantangan 2: Conditional Logic
            print("TANTANGAN 2: LOGIKA BERSYARAT")
            print("Kode di bawah ini akan menghasilkan output apa?")
            print("\nangka = 5")
            print("if angka > 3 and angka < 10:")
            print("    print('BENAR')")
            print("else:")
            print("    print('SALAH')")
            print("\n1. SALAH")
            print("2. BENAR")
            print("3. Tidak ada output")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "2":
                print("\n✓ BENAR! Kondisi logika Anda sempurna!")
                pemain.ambil_item("Kristal Energi Logika")
                pemain.misteri_terpecahkan += 1
                print(f"Kristal Energi Logika diterima! 💎✨")
                print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Kondisi yang keliru memicu ledakan!")
                pemain.hp -= 12
                print(f"HP berkurang 12 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif tantangan_selesai == 2:
            # Tantangan 3: Array/List
            print("TANTANGAN 3: MANIPULASI DATA")
            print("Kode di bawah ini akan menghasilkan output apa?")
            print("\nlista = [1, 2, 3, 4, 5]")
            print("print(sum(lista))")
            print("\n1. 12")
            print("2. 15")
            print("3. 123456")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "2":
                print("\n✓ BENAR! Kamu Master Logika Sejati!")
                pemain.hp += 20
                print(f"HP pulih +20 (sekarang: {pemain.hp})")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Kesalahan perhitungan fatal!")
                pemain.hp -= 10
                print(f"HP berkurang 10 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
    
    print("\n" + "="*40)
    print("✨ SELAMAT! Lembah Coding dikuasai! ✨")
    print("Sage Coding memberikan salam kehormatan:")
    print("'Logikamu bersinar terang seperti kode sempurna.'")
    print("='="*40)
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"


def gunung_bug(pemain):
    """
    Gunung Bug - Jalur dengan tantangan debugging dan perbaikan kode
    Penjaga: Debug Hunter (Penjaga Kesempurnaan)
    """
    print("\n" + "="*60)
    print("🐞 GUNUNG BUG - LOKASI SULIT 🐞")
    print("="*60)
    print("Penjaga: Debug Hunter (Penjaga Kesempurnaan)")
    print("="*60)
    
    print("Kamu mendaki gunung tinggi yang dipenuhi dengan makhluk-makhluk aneh...")
    print("Setiap makhluk adalah representasi dari sebuah BUG dalam program!")
    
    print("\nSeorang Debug Hunter mendekatimu dengan pose waspada...")
    
    print("\n" + "─"*60)
    print("DEBUG HUNTER (Penjaga Kesempurnaan) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Debug Hunter, Penjaga Kesempurnaan. Aku adalah manifestasi
dari kesalahan yang diperbaiki dan kesempurnaan yang dicapai.

Malachar meninggalkan beberapa bug dalam struktur taman. Aku yang berjaga
agar bug-bug tersebut tidak menyebabkan kehancuran total. Tunjukkan bahwa
kamu bisa memperbaiki kesalahan-kesalahan kritis!'
    """)
    
    bug_terperbaiki = 0
    
    while bug_terperbaiki < 3:
        print(f"\n🐛 Bug ke-{bug_terperbaiki + 1}/3")
        print("─" * 40)
        
        if bug_terperbaiki == 0:
            # Bug 1
            print("BUG #1: SYNTAX ERROR")
            print("Kode di bawah ini memiliki error. Apa yang salah?")
            print("\nprint('Halo Dunia'")
            print("\n1. Kurang tanda tutup kurung ')'")
            print("2. Tanda quote tidak cocok")
            print("3. Nama variabel salah")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "1":
                print("\n✓ BENAR! Bug dibereskan! Makhluk bug menjadi cahaya!")
                pemain.hp += 5
                print(f"HP pulih +5 (sekarang: {pemain.hp})")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Bug membuat serangan balik!")
                pemain.hp -= 20
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif bug_terperbaiki == 1:
            # Bug 2
            print("BUG #2: LOGIC ERROR")
            print("Program ini seharusnya menampilkan angka genap dari 1-10.")
            print("Tapi ada bug dalam logikanya. Apa yang salah?")
            print("\nfor i in range(1, 11):")
            print("    if i % 2 == 1:")
            print("        print(i)")
            print("\n1. Kondisi seharusnya 'i % 2 != 1'")
            print("2. Kondisi seharusnya 'i % 2 == 0'")
            print("3. Range seharusnya range(2, 10)")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "2":
                print("\n✓ BENAR! Logika diperbaiki! Bug hilang!")
                print("Debug Hunter memberikan Kristal Energi Kesempurnaan! 💎✨")
                pemain.ambil_item("Kristal Energi Kesempurnaan")
                pemain.misteri_terpecahkan += 1
                pemain.hp += 15
                print(f"HP pulih +15 (sekarang: {pemain.hp})")
                print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Logika yang keliru memicu ledakan!")
                pemain.hp -= 18
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif bug_terperbaiki == 2:
            # Bug 3
            print("BUG #3: VARIABLE UNDEFINED ERROR")
            print("Program ini error saat dijalankan. Mengapa?")
            print("\nangka = '5'")
            print("hasil = angka + 10")
            print("print(hasil)")
            print("\n1. Variabel 'hasil' belum didefinisikan")
            print("2. Tidak bisa menambah string dengan integer")
            print("3. Variabel 'angka' tidak boleh string")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "2":
                print("\n✓ BENAR! Semua bug dibasmi! Kesempurnaan tercapai!")
                pemain.hp += 15
                print(f"HP pulih +15 (sekarang: {pemain.hp})")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Bug terakhir menyerang dengan ganas!")
                pemain.hp -= 25
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
    
    print("\n" + "="*40)
    print("🏆 SELAMAT! Gunung Bug dikuasai! 🏆")
    print("Debug Hunter memberikan salam hormat kepadamu...")
    print("'Kamu adalah Debug Master sejati!'")
    print("="*40)
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"

def gua_naga_purba(pemain):
    # PERTARUNGAN PENJAGA GERBANG
    penjaga_menang = pertarungan_penjaga_gerbang(
        pemain=pemain,
        nama_penjaga="Naga Gerbang",
        deskripsi_penjaga="Naga kecil berwarna merah tua menjaga gerbang gua dengan pertarungan sengit.",
        hp_penjaga=90,
        damage_penjaga=20,
        level_lokasi="SANGAT SULIT"
    )
    
    if not penjaga_menang:
        print("\n❌ Naga Gerbang tidak membiarkanmu masuk ke Gua Naga Purba.")
        return
    
    """
    Gua Naga Purba - Lokasi SANGAT SULIT - Pertarungan Final BOSS
    Penjaga: Naga Purba (Manifestasi dari Kutukan Malachar)
    """
    print("\n" + "="*60)
    print("🐉 GUA NAGA PURBA - BRAWL BOS SUPER SULIT 🐉")
    print("="*60)
    print("Penjaga Terakhir: Naga Purba (Inti Kutukan Malachar)")
    print("="*60)
    
    print("Kamu memasuki gua yang sangat gelap dan berbau sulfur.")
    print("Batu-batu raksasa dengan goresan cakar naga terlihat di mana-mana!")
    print("Suara gemuruh seperti pertarungan kuno yang tak pernah berakhir...")
    time.sleep(1)
    
    print("\nTiba-tiba, cahaya merah membara menerangi gua!")
    print("Naga Purba dengan tubuh setara dengan bukit keluar dari kedalaman!")
    time.sleep(1)
    
    print("\n" + "─"*60)
    print("NAGA PURBA berbicara dengan suara yang mengguncang dunia:")
    print("─"*60)
    print("""
'Aku adalah Naga Purba, inti dari kutukan Malachar!
Selama 500 tahun aku dipaksa menahan beban kegelapan ini.
Kamu telah sampai ke sini... berarti kamu layak mendapatkan kesempatan.'
    """)
    time.sleep(1)
    
    # Boss stats
    boss_hp = 150 if pemain.tingkat_kesulitan != "sulit" else 180
    boss_max_hp = boss_hp
    boss_stage = 1  # Fase 1 dari 2
    
    # Multiplier tingkat kesulitan
    damage_multiplier = 1.4 if pemain.tingkat_kesulitan == "sulit" else 1.0
    
    pertarungan_berlangsung = True
    giliran = 0
    pemain_super_hits = 0
    
    print("\n┌─ OPSI PERTARUNGAN NAGA PURBA ─┐")
    print("1. ⚔️  SERANGAN BIASA (Damage: 15-25)")
    print("2. 🔥 LEDAKAN MAGIS (Damage: 35-50, Mana: 40)")
    print("3. 🛡️  PERTAHANAN MAGICAL (Reduce 60%, Mana: 30)")
    print("4. 💚 MENYEMBUHKAN (HP: 30, Mana: 40)")
    print("5. ⭐ SUPER HIT (Random besar, Mana: 50)")
    print("6. 🏃 MUNDUR (30% berhasil)")
    print("└──────────────────────────────┘")
    
    while pertarungan_berlangsung:
        print(f"\n┌─ FASE {boss_stage} STATUS ──────────┐")
        print(f"│ Pemain HP:  {pemain.hp}/{pemain.max_hp}")
        print(f"│ Mana:       {pemain.mana}/{pemain.max_mana}")
        print(f"│ Naga HP:    {boss_hp}/{boss_max_hp} ({int(boss_hp/boss_max_hp*100)}%)")
        print(f"└───────────────────────────────┘")
        
        # Boss phase 2 (50% health)
        if boss_hp < boss_max_hp * 0.5 and boss_stage == 1:
            boss_stage = 2
            print("\n🔥 NAGA PURBA MEMASUKI FASE KEDUA! 🔥")
            print("Serangannya menjadi dua kali lebih kuat!")
            time.sleep(2)
        
        pilihan = input("\nPilihan aksi (1-6): ")
        
        if pilihan == "1":  # Serangan biasa
            # Gunakan bonus damage dari senjata jika ada
            if pemain.senjata_aktif:
                damage = pemain.senjata_aktif.hitung_damage()
                desc_senjata = f" dengan {pemain.senjata_aktif.nama}"
            else:
                damage = random.randint(15, 25)
                desc_senjata = ""
            
            boss_hp -= damage
            print(f"⚔️  Kamu menyerang{desc_senjata}! Damage: {damage}")
            
        elif pilihan == "2":  # Ledakan Magis
            mana_cost = 40
            if pemain.senjata_aktif and pemain.senjata_aktif.mana_cost > 0:
                mana_cost = pemain.senjata_aktif.mana_cost + 25
            
            if pemain.gunakan_mana(mana_cost):
                base_damage = random.randint(35, 50)
                if pemain.senjata_aktif:
                    base_damage += pemain.senjata_aktif.damage_max // 2
                damage = int(base_damage * damage_multiplier)
                if random.random() > 0.25:  # 75% hit
                    boss_hp -= damage
                    senjata_desc = f" {pemain.senjata_aktif.nama}" if pemain.senjata_aktif else ""
                    print(f"🔥 LEDAKAN MAGIS{senjata_desc}! CRITICAL HIT - Damage: {damage}!")
                else:
                    print("🔥 Ledakan magis meleset dari target yang gesit!")
            else:
                print(f"❌ Mana tidak cukup (butuh {mana_cost})!")
                continue
                
        elif pilihan == "3":  # Pertahanan Magical
            if pemain.gunakan_mana(30):
                pemain.boost_defense = 2  # 60% reduction
                print("🛡️  Kamu membuat perlindungan magical! Damage berkurang 60%!")
            else:
                print("❌ Mana tidak cukup (butuh 30)!")
                continue
                
        elif pilihan == "4":  # Penyembuhan
            if pemain.gunakan_mana(40):
                heal = 30
                pemain.hp = min(pemain.hp + heal, pemain.max_hp)
                print(f"💚 Kamu menyembuhkan diri! HP +{heal}")
            else:
                print("❌ Mana tidak cukup (butuh 40)!")
                continue
                
        elif pilihan == "5":  # Super Hit
            mana_cost = 50
            if pemain.senjata_aktif and pemain.senjata_aktif.mana_cost > 0:
                mana_cost = pemain.senjata_aktif.mana_cost + 30
            
            if pemain.gunakan_mana(mana_cost):
                if random.random() > 0.4:  # 60% hit rate
                    base_damage = random.randint(60, 90)
                    if pemain.senjata_aktif:
                        base_damage += pemain.senjata_aktif.damage_max
                    boss_hp -= base_damage
                    pemain_super_hits += 1
                    senjata_desc = f" {pemain.senjata_aktif.nama}" if pemain.senjata_aktif else ""
                    print(f"⭐ SUPER HIT{senjata_desc}! Damage MASSIF: {base_damage}!")
                else:
                    print("⭐ Super hit gagal! Naga menghindar dengan tangkas!")
            else:
                print(f"❌ Mana tidak cukup (butuh {mana_cost})!")
                continue
                
        elif pilihan == "6":  # Mundur
            if random.random() > 0.7:  # 30% success
                print("✓ Kamu berhasil mundur dari pertarungan!")
                print("Namun, kamu harus kembali untuk menyelesaikan ini...")
                return
            else:
                print("✗ Naga memblokir jalan keluarmu!")
                boss_hp += 10  # Boost for failed escape
                
        else:
            print("❌ Pilihan tidak valid!")
            continue
        
        # Regenerasi mana pemain
        pemain.regenerasi_mana(8)
        
        # Serangan Naga
        if boss_hp > 0:
            giliran += 1
            time.sleep(1)
            
            # Serangan berbeda di fase 2
            if boss_stage == 1:
                naga_damage = random.randint(18, 28)
                naga_attack = random.choice(["Cakar perkasa", "Napas api naga", "Ekor pukul"])
            else:
                naga_damage = random.randint(25, 40)
                naga_attack = random.choice(["Serangan triple Cakar", "Ledakan napas api super", "Pukulan Ekor yang mengguncang"])
            
            if pemain.boost_defense > 0:
                naga_damage = int(naga_damage * 0.4)
                print(f"🛡️ {naga_attack}! Damage: {naga_damage} (Pertahanan aktif!)")
                pemain.boost_defense = 0
            else:
                print(f"😤 {naga_attack}! Damage: {naga_damage}")
            
            naga_damage = int(naga_damage * damage_multiplier)
            pemain.hp -= naga_damage
            
            if pemain.hp <= 0:
                print(f"\n💀 Kamu kalah! HP habis dalam pertarungan dengan Naga Purba...")
                game_over_kalah(pemain)
                return
        
        # Cek kemenangan
        if boss_hp <= 0:
            print("\n" + "="*60)
            print("⭐ KEMENANGAN BESAR! ⭐")
            print("="*60)
            print("Naga Purba terjatuh dengan gemuruh yang menggetarkan bumi...")
            print("Cahaya putih membanjiri seluruh gua...")
            print("Tubuh Naga Purba bersinar dan berubah menjadi seorang pria bijak...")
            print(f"\nKau telah mengalahkan bos dengan {pemain_super_hits} super hits!")
            print("\n'Terima kasih... aku akhirnya bebas dari kutukan ini.'")
            print("'500 tahun penderitaan... dan kamu yang membebaskanku.'")
            print("\nKristal Energi Pemecah Kutukan terbentuk dengan cahaya emas! 💎✨")
            print("="*60)
            
            pemain.ambil_item("Kristal Energi Pemecah Kutukan")
            pemain.misteri_terpecahkan += 1
            pemain.pertempuran_menang += 1
            
            # Massive HP restore
            pemain.hp = min(pemain.hp + 60, pemain.max_hp)
            print(f"\n✓ Kamu menerima healing besar! HP sekarang: {pemain.hp}/{pemain.max_hp}")
            pertarungan_berlangsung = False
    
    print("\n" + "="*60)
    print("✨ KUTUKAN AKHIRNYA RONTOK! ✨")
    print("="*60)
    print("Cahaya emas menyinar dari setiap sudut taman magis...")
    print("Naga Purba (kini kembali manusia) tersenyum dengan damai...")
    print("'Selesaikan misimu. Dunia akan terbebas karena keberanianmu.'")
    print("\nSebuah portal cahaya terbentuk di depanmu...")
    print("Arah menuju: RUANG HARTA KARUN TERAKHIR")
    print("="*60)
    
    input("\nTekan ENTER untuk memasuki portal akhir...")
    ruang_harta_karun_final(pemain)


def taman_bunga_pesona(pemain):
    """
    Taman Bunga Pesona - Lokasi MUDAH - Pengenalan Cerita
    Penjaga: Peri Bunga (Penjaga Keindahan)
    """
    # PERTARUNGAN PENJAGA GERBANG
    penjaga_menang = pertarungan_penjaga_gerbang(
        pemain=pemain,
        nama_penjaga="Peri Bunga Gerbang",
        deskripsi_penjaga="Peri bersayap indah dengan cahaya emas terlihat di depan pintu masuk.",
        hp_penjaga=40,
        damage_penjaga=8,
        level_lokasi="MUDAH"
    )
    
    if not penjaga_menang:
        print("\n❌ Kamu tidak bisa memasuki Taman Bunga Pesona tanpa mengalahkan penjaganya.")
        return
    
    print("\n" + "="*60)
    print("🌺 TAMAN BUNGA PESONA - LOKASI MUDAH 🌺")
    print("="*60)
    print("Penjaga: Peri Bunga (Penjaga Keindahan)")
    print("="*60)
    
    print("\nKamu memasuki taman yang indah penuh dengan bunga-bunga berwarna cerah.")
    print("Aroma bunga yang menenangkan memenuhi setiap aspek pikiranmu.")
    print("\nTiba-tiba, cahaya terang bersinar dari pertengahan taman...")
    print("Seorang peri bunga muncul, dengan sayap yang berpencar warna-warni!")
    
    print("\n" + "─"*60)
    print("PERI BUNGA berbicara dengan lembut:")
    print("─"*60)
    print("""
'Selamat datang, pemberani. Aku adalah Peri Bunga, Penjaga Keindahan.
Aku dipilih oleh Raja Kuno untuk melindungi taman dari kutukan Malachar.

500 tahun kami menunggu seseorang yang cukup kuat untuk memecahkan kutukan.
Tugasku yang pertama adalah menguji apakah hatimu murni dan penuh apresiasi.

Jika kamu bisa mengumpulkan 5 bunga istimewa dari taman ini,
aku akan memberikan Kristal Energi Keindahan - salah satu dari 6 kristal 
yang diperlukan untuk mengangkat kutukan!'
    """)
    
    bunga_dikumpulkan = 0
    bunga_nama = ["Bunga Matahari Emas", "Bunga Mawar Merah Darah", 
                  "Bunga Teratai Putih", "Bunga Lavender Ungu", "Bunga Lotus Sakral"]
    
    for i, bunga in enumerate(bunga_nama, 1):
        print(f"\n🌸 Bunga #{i}: {bunga}")
        print("Lokasi bunga ini sangat tersembunyi. Mau mencarinya?")
        
        pilihan = input("Lanjut? (y/n): ").lower()
        
        if pilihan == 'y':
            # Kemungkinan tinggi untuk mudah
            if random.random() > 0.2:
                print(f"✓ Kamu menemukan {bunga}!")
                pemain.ambil_item(bunga)
                bunga_dikumpulkan += 1
            else:
                print(f"✗ Bunga itu terlalu indah, kamu hanya bisa menghafal lokasinya...")
        
        if i == 5 and bunga_dikumpulkan == 5:
            print("\n" + "="*60)
            print("🎁 SELAMAT! Kamu mengumpulkan semua 5 bunga!")
            print("="*60)
            print("Peri Bunga memberikan cahaya emas yang hangat...")
            print("'Terima kasih, pemberani. Hatimu memang murni!' ")
            print("Peri memberikan Kristal Energi Keindahan! 💎✨")
            pemain.ambil_item("Kristal Energi Keindahan")
            pemain.misteri_terpecahkan += 1
            pemain.hp += 30
            print(f"HP Anda pulih sepenuhnya! (+30, sekarang: {pemain.hp})")
            print("\n'Pergilah sekarang. 5 penjaga lainnya menunggu uji cobamu.'")
            break
        elif i == 5:
            print(f"\nKamu hanya dapat mengumpulkan {bunga_dikumpulkan}/5 bunga.")
            print("Peri memberikan hadiah kecil sebagai tanda kasih...")
            pemain.ambil_item("Kristal Keindahan Taman")
            pemain.hp += 20
            print("'Mungkin cobalah lagi nanti, atau lanjut ke penjaga berikutnya.'")
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"


def perpustakaan_kuno(pemain):
    """
    Perpustakaan Kuno - Lokasi SEDANG dengan tantangan pengetahuan
    Penjaga: Pustakawan Kuno (Penjaga Pengetahuan)
    """
    print("\n" + "="*60)
    print("📚 PERPUSTAKAAN KUNO - TANTANGAN INTELEKTUAL 📚")
    print("="*60)
    print("Penjaga: Pustakawan Kuno (Penjaga Pengetahuan)")
    print("="*60)
    
    print("Kamu memasuki perpustakaan raksasa dengan buku-buku berusia berabad-abad.")
    print("Debu membang di udara, cahaya matahari menebus celah-celah jendela kuno.")
    time.sleep(1)
    
    print("\nSeorang Pustakawan Tua dengan mata bijak mendekatimu dari balik rak buku!")
    
    print("\n" + "─"*60)
    print("PUSTAKAWAN KUNO (Penjaga Pengetahuan) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Pustakawan Kuno, Penjaga Pengetahuan. Selama 500 tahun,
aku menjaga pengetahuan dunia di dalam buku-buku ini.

Malachar menginginkan untuk menghapus semua pengetahuan, namun aku berhasil
menyembunyikan sebagian. Sekarang aku menguji apakah kamu cukup cerdas
untuk layak membawa pengetahuan ini keluar dari taman!

Siapkan diri. Ada 4 pertanyaan dengan tingkat kesulitan TINGGI.
Kamu harus menjawab setidaknya 3 dengan benar untuk lulus!'
    """)
    time.sleep(1)
    
    benar_terjawab = 0
    salah_total = 0
    
    pertanyaan = [
        {
            "q": "Berapakah kombinasi dari 10 pilih 3? (C(10,3))",
            "pilihan": ["30", "45", "60", "120"],
            "jawab": "2",  # 120
            "penjelasan": "Kombinasi C(10,3) = 10!/(3!*7!) = 120"
        },
        {
            "q": "Siapa penulis novel 'Laskar Pelangi' dan tahun publikasinya?",
            "pilihan": ["Pramoedya (1985)", "Andrea Hirata (2008)", "Sutan Syamir (2000)", "Sukarno (1950)"],
            "jawab": "1",  # Andrea Hirata (2008)
            "penjelasan": "Laskar Pelangi ditulis oleh Andrea Hirata dan dipublikasikan tahun 2005"
        },
        {
            "q": "Manakah diantara berikut yang BUKAN termasuk asam amino esensial?",
            "pilihan": ["Valin", "Leucin", "Glutamat", "Isoleucin"],
            "jawab": "2",  # Glutamat bukan esensial
            "penjelasan": "Glutamat memang asam amino, tapi tidak esensial (tubuh bisa memproduksinya)"
        },
        {
            "q": "Dalam periode 1900-2024, berapa kali Indonesia telah mengalami pergantian konstitusi utama?",
            "pilihan": ["2 kali", "3 kali", "4 kali", "5 kali"],
            "jawab": "2",  # 4 kali (UUD 1945, Konstitusi RIS 1949, UUD Sementara 1950, kembali UUD 1945)
            "penjelasan": "Indonesia telah memiliki 4 konstitusi: UUD 1945, Konstitusi RIS, UUD Sementara, dan kembali UUD 1945"
        }
    ]
    
    print("Tidak ada waktu untuk berpikir lama - Pustakawan akan menguji dirimu!\n")
    
    for i, item in enumerate(pertanyaan, 1):
        print(f"\n{'='*50}")
        print(f"❓ PERTANYAAN {i}/4 - Tingkat Kesulitan: TINGGI")
        print(f"{'='*50}")
        print(f"{item['q']}")
        print("\nOpsi Jawaban:")
        for j, pilihan in enumerate(item['pilihan']):
            print(f"  {j}. {pilihan}")
        
        # Hanya 30 detik untuk jawab
        try:
            jawaban = input("\nJawaban Anda (0-3): ").strip()
            
            if jawaban == item['jawab']:
                print(f"✓ BENAR! {item['penjelasan']}")
                benar_terjawab += 1
                print("Buku berkobar dengan cahaya emas yang indah.")
            else:
                print(f"✗ SALAH!")
                print(f"   Jawaban yang benar adalah: {item['pilihan'][int(item['jawab'])]}")
                print(f"   {item['penjelasan']}")
                salah_total += 1
                
                # Damage yang lebih besar untuk difficulty sulit
                damage = 15 if pemain.tingkat_kesulitan == "normal" else 20
                pemain.hp -= damage
                print(f"HP berkurang {damage} (sekarang: {pemain.hp})")
                
                if pemain.hp <= 0:
                    print("\n💀 Kamu terlalu lemah dalam pengetahuan untuk melanjutkan...")
                    game_over_kalah(pemain)
                    return
        except:
            print("❌ Input tidak valid! Pertanyaan dijawab salah.")
            salah_total += 1
            pemain.hp -= 15
            if pemain.hp <= 0:
                game_over_kalah(pemain)
                return
        
        time.sleep(1)
    
    print("\n" + "="*60)
    print(f"HASIL AKHIR: {benar_terjawab}/4 jawaban BENAR")
    print("="*60)
    
    if benar_terjawab >= 3:
        print("\n✓ LULUS UJIAN PENGETAHUAN!")
        print("Pustakawan Kuno memberikan Kristal Energi Pengetahuan dengan hormat!")
        print("'Kamu telah menunjukkan kebijaksanaan yang luar biasa.'")
        print("'Pengetahuan sejati adalah kekuatan terbesar di dunia.'")
        pemain.ambil_item("Kristal Energi Pengetahuan")
        pemain.misteri_terpecahkan += 1
        
        # Bonus HP berdasarkan score
        bonus_hp = 25 + (benar_terjawab - 3) * 15
        pemain.hp = min(pemain.hp + bonus_hp, pemain.max_hp)
        print(f"✓ HP Anda pulih (+{bonus_hp}, sekarang: {pemain.hp})")
        print(f"✓ Misteri terpecahkan: {pemain.misteri_terpecahkan}/7")
    else:
        print("\nPustakawan memberikan buku panduan sederhana...")
        pemain.ambil_item("Buku Panduan Sederhana")
        print("'Datanglah lagi ketika kamu lebih siap.'")
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"


def ruang_harta_karun_final(pemain):
    """
    Ruang Harta Karun Final - ENDING CERITA - Semua makna bersatu
    """
    print("\n" + "="*70)
    print("💰 RUANG HARTA KARUN TERAKHIR - ENDING CERITA 💰")
    print("="*70)
    
    print("\nPortal cahaya membawamu ke ruangan yang megah dan mistis...")
    print("Pintu dengan hieroglif kuno membuka dengan suara gemuruh yang dahsyat...")
    print("Cahaya emas murni memenuhi seluruh ruangan...")
    print("Aura mistis mengelilingi semua objek berharga...")
    
    print("\n" + "─"*70)
    print("Kamu melihat bayangan Raja Kuno dan Ratu Mistis muncul!")
    print("─"*70)
    
    print("""
RAJA KUNO berbicara dengan tenang:
'500 tahun yang lalu, kami mempercayakan taman kepada penjaga dimensi.
Mereka menjaga bukan hanya fasilitas fisik, namun esensi taman itu sendiri.

Kamu telah memahami makna sejati dari setiap penjaga:
- Peri Bunga mengajarkan pentingnya keindahan dalam dunia
- Werewolf Hutan mengajarkan kekuatan tanpa kehilangan kebijaksanaan  
- Hantu Danau mengajarkan pentingnya kebijaksanaan
- Sage Coding mengajarkan logika sebagai dasar kehidupan
- Pustakawan Kuno menjaga pengetahuan untuk generasi mendatang
- Pendeta Kuil mempertahankan keseimbangan antara baik dan jahat
- Debug Hunter menjaga kesempurnaan dalam setiap detail

Dan yang terpenting, KAMU telah belajar bahwa penghancuran kutukan
membutuhkan lebih dari kekerasan - dibutuhkan pemahaman dan belas kasih.
    """)
    
    print("\n" + "─"*70)
    print("RATU MISTIS melanjutkan:")
    print("─"*70)
    
    print("""
'Harta karun sejati bukan emas atau permata. Harta karun sejati adalah
cahaya yang sekarang kamu bawa - kesadaran akan keindahan, kekuatan,
kebijaksanaan, logika, pengetahuan, keseimbangan, dan kesempurnaan.

Dengan 7 kristal energi, taman kini bebas!
Kutukan Malachar telah lenyap. Makhluk-makhluk terjebak kini terbebas.
Taman akan dipulihkan menjadi tempat indah yang pernah kami ciptakan.
    """)
    
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + "🏆 SELAMAT! KAMU TELAH MENYELAMATKAN TAMAN MISTERI! 🏆".center(70) + "║")
    print("╚" + "="*68 + "╝")
    
    print(f"\n✨ {pemain.nama}, kamu adalah PEMENANG dan PENYELAMAT SEJATI! ✨")
    
    print("\n" + "─"*70)
    print("STATISTIK AKHIR PETUALANGAN:")
    print("─"*70)
    print(f"Tingkat Kesulitan: {pemain.tingkat_kesulitan.upper()} ⚔️")
    print(f"HP Akhir: {pemain.hp}/{pemain.max_hp} ❤️")
    print(f"Kristal Energi Dikumpulkan: {pemain.misteri_terpecahkan}/7 💎")
    print(f"Total Barang: {len(pemain.inventaris)} item")
    
    print("\n" + "─"*70)
    print("ITEM BERHARGA YANG DIKUMPULKAN:")
    print("─"*70)
    
    if pemain.inventaris:
        for i, item in enumerate(pemain.inventaris, 1):
            print(f"{i}. ✓ {item}")
    
    print("\n" + "─"*70)
    print("PESAN TERAKHIR DARI PENJAGA-PENJAGA:")
    print("─"*70)
    
    messages = [
        "🌺 Peri Bunga: 'Keindahan akan selalu bersinar di hati yang murni.'",
        "🌲 Werewolf Hutan: 'Kekuatan sejati adalah melindungi yang lemah.'",
        "💧 Hantu Danau: 'Kebijaksanaan adalah harta yang tidak pernah usang.'",
        "💻 Sage Coding: 'Logika adalah bahasa universal semua makhluk.'",
        "📚 Pustakawan Kuno: 'Pengetahuan adalah cahaya yang tidak pernah padam.'",
        "⛩️ Pendeta Kuil: 'Keseimbangan adalah jalan menuju kedamaian abadi.'",
        "🐞 Debug Hunter: 'Kesempurnaan dicapai melalui pembelajaran berkelanjutan.'",
        "🐉 Naga Purba: 'Terima kasih telah membebaskan kami dari kesakitan.'"
    ]
    
    for msg in messages:
        print(msg)
    
    print("\n" + "="*70)
    print("🌍 TAMAN MISTERI KEMBALI BERSINAR DENGAN CAHAYA INDAH 🌍")
    print("="*70)
    
    if pemain.tingkat_kesulitan == "sulit":
        print("\n⚔️ Mode Sulit Diselesaikan! Kamu adalah Juara Sejati! ⚔️")
    elif pemain.tingkat_kesulitan == "mudah":
        print("\n😊 Perjalananmu penuh pembelajaran dan keindahan!")
    else:
        print("\n⚖️ Keseimbangan sempurna antara tantangan dan pencapaian!")
    
    print("\n" + "="*70)
    print("🎮 TERIMA KASIH TELAH BERMAIN 'MISTERI TAMAN YANG TERLUPAKAN' 🎮")
    print("="*70)
    print("Sampai jumpa di petualangan berikutnya! 👋\n")
    
    input("Tekan ENTER untuk keluar dari game...")

def simpan_statistik_game(pemain, username, login_system, status_akhir):
    """
    Simpan statistik akhir game ke histori pengguna
    status_akhir: 'menang' atau 'kalah'
    """
    if username in login_system.histori_login:
        stat_game = {
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status_akhir,
            "kesulitan": pemain.tingkat_kesulitan,
            "hp_akhir": pemain.hp,
            "hp_max": pemain.max_hp,
            "kristal": pemain.misteri_terpecahkan,
            "total_item": len(pemain.inventaris),
            "pertempuran_menang": pemain.pertempuran_menang,
            "durasi_game": str(datetime.now() - pemain.waktu_mulai)
        }
        login_system.histori_login[username]["statistik_game"].append(stat_game)
        login_system.simpan_histori()
        print(f"\n[💾] Statistik game berhasil disimpan!")

def game_utama():
    # Inisialisasi sistem login
    login_system = SistemLogin()
    
    # Menu login dan registrasi
    username_pemain = login_system.menu_utama_login()
    
    # Tampilkan header game
    print("\n" + "╔" + "="*48 + "╗")
    print("║" + " "*48 + "║")
    print("║" + "  🌙 PETUALANGAN TAMAN MISTERI FANTASI 🌙  ".center(48) + "║")
    print("║" + " "*48 + "║")
    print("╚" + "="*48 + "╝")
    
    print(f"\nHalo {username_pemain}! Selamat datang di petualangan!")
    nama = input("Siapa nama karakter Anda? ")
    
    # Menu pemilihan tingkat kesulitan
    print("\n" + "="*50)
    print("⚔️ PILIH TINGKAT KESULITAN ⚔️")
    print("="*50)
    print("1. 😊 MUDAH - HP: 150 (Cocok untuk pemula)")
    print("2. ⚖️ NORMAL - HP: 100 (Standar, seimbang)")
    print("3. 😈 SULIT - HP: 60 (Untuk yang cari tantangan)")
    
    tingkat_input = input("\nPilihan Anda (1-3): ")
    
    if tingkat_input == "1":
        tingkat_kesulitan = "mudah"
    elif tingkat_input == "3":
        tingkat_kesulitan = "sulit"
    else:
        tingkat_kesulitan = "normal"
    
    print(f"\nKamu memilih mode: {tingkat_kesulitan.upper()}! 🎮")
    
    pemain = Pemain(nama, tingkat_kesulitan)
    cerita_pembukaan(pemain)
    
    pemain.lokasi_sekarang = "gerbang"
    
    try:
        while pemain.hp > 0:
            if lokasi_gerbang(pemain) == False:
                simpan_statistik_game(pemain, username_pemain, login_system, "kalah")
                break
            
            if pemain.misteri_terpecahkan >= 6 and pemain.lokasi_sekarang == "gerbang":
                print("\n✨ Kamu merasa semua misteri taman telah terpecahkan! ✨")
                print("Gerbang utama bersinar dengan cahaya putih...")
                ruang_harta_karun_final(pemain)
                simpan_statistik_game(pemain, username_pemain, login_system, "menang")
                break
        
        # Jika pemain kehabisan HP, simpan sebagai kalah
        if pemain.hp <= 0:
            simpan_statistik_game(pemain, username_pemain, login_system, "kalah")
    
    except KeyboardInterrupt:
        print("\n\n[⚠️] Game dihentikan oleh pemain.")
        simpan_statistik_game(pemain, username_pemain, login_system, "dihentikan")


if __name__ == "__main__":
    game_utama()