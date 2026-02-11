import time
import random

class SistemLogin:
    """Sistem Login dan Registrasi untuk game"""
    def __init__(self):
        # Database pengguna dengan username dan password
        self.akun_terdaftar = {}
    
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
            return username
        else:
            print("❌ Username atau password salah!")
            return None
    
    def menu_utama_login(self):
        """Menu utama untuk login dan registrasi"""
        while True:
            print("\n" + "╔" + "="*48 + "╗")
            print("║" + "  🎮 MENU UTAMA - TAMAN MISTERI  ".center(50) + "║")
            print("╚" + "="*48 + "╝")
            print("\n1. Login")
            print("2. Registrasi")
            print("3. Keluar Game")
            
            pilihan = input("\nPilihan (1-3): ")
            
            if pilihan == "1":
                username = self.login()
                if username:
                    return username
            elif pilihan == "2":
                self.registrasi()
            elif pilihan == "3":
                print("\nTerima kasih telah bermain! 👋")
                exit()
            else:
                print("❌ Pilihan tidak valid!")

class Pemain:
    def __init__(self, nama, tingkat_kesulitan="normal"):
        self.nama = nama
        self.tingkat_kesulitan = tingkat_kesulitan
        
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
    
    print("\n9. Lihat Status")
    print("10. Keluar Game")
    
    pilihan = input("\nPilihan (1-10): ")
    
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
        pemain.lihat_status()
        lokasi_gerbang(pemain)
    elif pilihan == "10":
        print("\nTerima kasih telah bermain! 👋")
        return False
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        lokasi_gerbang(pemain)
    
    return True

def semak_hutan_gelap(pemain):
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
    print("\n👹 BERTEMU MONSTER HUTAN! 👹")
    print("─" * 40)
    print("Tiba-tiba, seekor Werewolf keluar dari bayangan!")
    print("Matanya bersinar merah... dan dia mengaum keras!")
    
    print("\nApa yang akan kamu lakukan?")
    print("1. Lari secepat mungkin")
    print("2. Hadapi monster (jika punya senjata)")
    print("3. Coba berbicara dengannya")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        if random.random() > 0.5:
            print("\n✓ Kamu berhasil lari! Monster itu marah dan mengejar, tapi kamu lebih cepat!")
            pemain.hp -= 10
            print(f"HP berkurang 10 (sekarang: {pemain.hp})")
        else:
            print("\n✗ Monster menangkapmu! Kamu terluka parah!")
            pemain.hp -= 30
            print(f"HP berkurang 30 (sekarang: {pemain.hp})")
            if pemain.hp <= 0:
                game_over_kalah(pemain)
                return
    
    elif pilihan == "2":
        if "pedang ajaib" in pemain.inventaris:
            print("\n⚔️ PERTARUNGAN! ⚔️")
            print("Kamu mengeluarkan pedang ajaib dan melawan monster!")
            time.sleep(1)
            if random.random() > 0.4:
                print("✓ KEMENANGAN! Monster itu terkapar!");
                print("Sebelum menghilang, monster meninggalkan medali emas 🏅")
                pemain.ambil_item("Medali Emas")
                pemain.misteri_terpecahkan += 1
                print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
            else:
                print("✗ Monster terlalu kuat! Kamu terluka!")
                pemain.hp -= 25
                print(f"HP berkurang 25 (sekarang: {pemain.hp})")
        else:
            print("\n✗ Kamu tidak memiliki senjata! Monster menyerangmu!")
            pemain.hp -= 35
            print(f"HP berkurang 35 (sekarang: {pemain.hp})")
            if pemain.hp <= 0:
                game_over_kalah(pemain)
                return
    
    elif pilihan == "3":
        print("\nMonster menatap matamu... suara dalam berkata...")
        print("'Aku adalah penjaga hutan. Aku menunggu yang dapat memecahkan misteri kami.'")
        print("'Jika kamu bisa mengalahkan Naga di Kuil, aku akan memberikan hadiah.'")
        pemain.ambil_item("Kunci Hutan")
    
    print("\nApa lagi yang ingin kamu lakukan?")
    print("1. Kembali ke gerbang")
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
    """
    Gua Naga Purba - Lokasi SANGAT SULIT - Pertarungan Final
    Penjaga: Naga Purba (Manifestasi dari Kutukan Malachar)
    """
    print("\n" + "="*60)
    print("🐉 GUA NAGA PURBA - LOKASI SANGAT SULIT 🐉")
    print("="*60)
    print("Penjaga Terakhir: Naga Purba (Inti Kutukan Malachar)")
    print("="*60)
    
    print("Kamu memasuki gua yang sangat gelap dan berbau sulfur.")
    print("Batu-batu raksasa dengan goresan cakar naga terlihat di mana-mana!")
    print("Suara gemuruh seperti pertarungan kuno yang tak pernah berakhir...")
    
    print("\nTiba-tiba, cahaya merah membara menerangi gua!")
    print("Naga Purba dengan tubuh setara dengan bukit keluar dari kedalaman!")
    
    print("\n" + "─"*60)
    print("NAGA PURBA berbicara dengan suara yang mengguncang dunia:")
    print("─"*60)
    print("""
'Aku adalah Naga Purba, inti dari kutukan Malachar!
Selama 500 tahun aku dipaksa menahan beban kegelapan ini.
Kamu telah mengumpulkan 6 kristal energi dari para penjaga.

Sekarang, pilihan ada di tanganmu:
1. Melawanku dengan kekuatan brutal
2. Menggunakan kebijaksanaan dan negosiasi
3. Menyatukan kekuatan 6 kristal untuk mengalahkanku'
    """)
    
    # Multiplier tingkat kesulitan
    if pemain.tingkat_kesulitan == "sulit":
        damage = 50
        reward_hp = 35
    else:
        damage = 40
        reward_hp = 45
    
    print("\nApa yang akan kamu lakukan?")
    print("1. Serang dengan semua kekuatan")
    print("2. Gunakan diplomasi dan kebijaksanaan")
    print("3. Satukan kekuatan 6 kristal (jika semua dimiliki)")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        if random.random() > 0.4:
            print("\n⚔️ Pertarungan yang luar biasa dahsyat!")
            print("Kamu berhasil mengalahkan Naga Purba dengan kemenangan mulia!")
            print("Naga itu runtuh dan cahaya putih mulai membanjiri gua...")
            print("Kristal Energi Pemecah Kutukan bersinar terang! 💎✨")
            pemain.ambil_item("Kristal Energi Pemecah Kutukan")
            pemain.misteri_terpecahkan += 1
            pemain.hp += reward_hp
            print(f"HP pulih +{reward_hp} (sekarang: {pemain.hp})")
        else:
            print("\n✗ Naga Purba terlalu kuat! Serangannya melampaui batas!")
            pemain.hp -= damage
            print(f"HP berkurang {damage} (sekarang: {pemain.hp})")
    elif pilihan == "2":
        print("\nKamu berbicara dengan penuh kebijaksanaan...")
        print("'Kamu adalah korban kutukan, bukan penyebabnya.'")
        print("\nNaga Purba merunduk dan air mata cahaya jatuh...")
        print("'Akhirnya, seseorang memahami dengannya. Terima kasih...'")
        print("Kristal Energi Pemecah Kutukan diberikan dengan tenang! 💎✨")
        pemain.ambil_item("Kristal Energi Pemecah Kutukan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += (reward_hp + 20)
        print(f"HP pulih +{reward_hp + 20} (sekarang: {pemain.hp})")
    elif pilihan == "3":
        if pemain.misteri_terpecahkan >= 6:
            print("\nKamu mengeluarkan ke-6 kristal energi!")
            print("Cahaya warna-warni memancar dari kristal-kristal itu...")
            print("Kekuatan semua penjaga bersatu dalam satu cahaya perkasa!")
            print("\nNaga Purba tersengkal oleh kekuatan tersebut...")
            print("Kutukan Malachar mulai rontok!")
            print("Kristal Energi Pemecah Kutukan terbentuk dari kesatuan! 💎✨✨✨")
            pemain.ambil_item("Kristal Energi Pemecah Kutukan")
            pemain.misteri_terpecahkan += 1
            pemain.hp = pemain.max_hp
            print(f"HP penuh! (sekarang: {pemain.hp})")
        else:
            print(f"\nKamu hanya memiliki {pemain.misteri_terpecahkan} kristal dari 6!")
            print("Kamu belum cukup kuat untuk menggunakan strategi ini.")
            print("Naga Purba menyerang dengan gemas!")
            pemain.hp -= 30
            if pemain.hp <= 0:
                game_over_kalah(pemain)
                return
    
    if pemain.hp <= 0:
        game_over_kalah(pemain)
        return
    
    print("\n" + "="*60)
    print("✨ KUTUKAN MULAI RONTOK! ✨")
    print("="*60)
    print("Cahaya emas mulai bersinar dari setiap sudut taman...")
    print("Naga Purba kembali ke bentuk asalnya - seorang pria bijak...")
    print("'Terima kasih. Taman dan kami akhirnya bebas dari kutukan.'")
    print("\nSebuah portal cahaya terbentuk di depanmu...")
    print("'Pergilah, dan selesaikan misimu di Ruang Harta Karun Terakhir!'")
    print("="*60)
    
    input("\nTekan ENTER untuk memasuki portal akhir...")
    ruang_harta_karun_final(pemain)

def taman_bunga_pesona(pemain):
    """
    Taman Bunga Pesona - Lokasi MUDAH - Pengenalan Cerita
    Penjaga: Peri Bunga (Penjaga Keindahan)
    """
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
    print("📚 PERPUSTAKAAN KUNO - LOKASI SEDANG 📚")
    print("="*60)
    print("Penjaga: Pustakawan Kuno (Penjaga Pengetahuan)")
    print("="*60)
    
    print("Kamu memasuki perpustakaan raksasa dengan buku-buku berusia berabad-abad.")
    print("Debu membang di udara, cahaya matahari menebus celah-celah jendela kuno.")
    
    print("\nSeorang Pustakawan Tua dengan mata bijak mendekatimu dari balik rak buku!")
    
    print("\n" + "─"*60)
    print("PUSTAKAWAN KUNO (Penjaga Pengetahuan) berbicara:")
    print("─"*60)
    print("""
'Aku adalah Pustakawan Kuno, Penjaga Pengetahuan. Selama 500 tahun,
aku menjaga pengetahuan dunia di dalam buku-buku ini.

Malachar menginginkan untuk menghapus semua pengetahuan, namun aku berhasil
menyembunyikan sebagian. Sekarang aku menguji apakah kamu cukup cerdas
untuk layak membawa pengetahuan ini keluar dari taman!'
    """)
    
    print("'Jawab 3 pertanyaan trivia, dan hadiah menanti!'")
    
    benar_terjawab = 0
    
    pertanyaan = [
        {
            "q": "Berapa jumlah benua di Bumi?",
            "pilihan": ["5", "6", "7", "8"],
            "jawab": "1"  # Index 1 = 6
        },
        {
            "q": "Siapa penulis 'Laskar Pelangi'?",
            "pilihan": ["Pramoedya Ananta Toer", "Andrea Hirata", "Sutan Syamir", "Habiburrahman El Shirazy"],
            "jawab": "1"  # Index 1 = Andrea Hirata
        },
        {
            "q": "Manakah planet terbesar di tata surya kita?",
            "pilihan": ["Saturnus", "Neptunus", "Jupiter", "Uranus"],
            "jawab": "2"  # Index 2 = Jupiter
        }
    ]
    
    for i, item in enumerate(pertanyaan, 1):
        print(f"\n❓ PERTANYAAN {i}/3")
        print(f"{item['q']}")
        for j, pilihan in enumerate(item['pilihan']):
            print(f"{j}. {pilihan}")
        
        jawaban = input("\nJawaban Anda (0-3): ")
        
        if jawaban == item['jawab']:
            print("✓ BENAR! Buku berkobar dengan cahaya emas.")
            benar_terjawab += 1
        else:
            print(f"✗ SALAH! Jawaban yang benar adalah: {item['pilihan'][int(item['jawab'])]}")
            pemain.hp -= 10
            print(f"HP berkurang 10 (sekarang: {pemain.hp})")
            if pemain.hp <= 0:
                game_over_kalah(pemain)
                return
    
    print("\n" + "="*50)
    print(f"HASIL: {benar_terjawab}/3 jawaban benar!")
    print("="*50)
    
    if benar_terjawab >= 2:
        print("\nPustakawan memberikan Kristal Energi Pengetahuan!")
        print("'Pengetahuan adalah kekuatan yang paling berharga.'")
        pemain.ambil_item("Kristal Energi Pengetahuan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += 25
        print(f"HP Anda pulih! (+25, sekarang: {pemain.hp})")
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/6")
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
    print("3. 😈 SULIT - HP: 70 (Untuk yang cari tantangan)")
    
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
    
    while pemain.hp > 0:
        if lokasi_gerbang(pemain) == False:
            break
        
        if pemain.misteri_terpecahkan >= 6 and pemain.lokasi_sekarang == "gerbang":
            print("\n✨ Kamu merasa semua misteri taman telah terpecahkan! ✨")
            print("Gerbang utama bersinar dengan cahaya putih...")
            ruang_harta_karun_final(pemain)
            break
    
if __name__ == "__main__":
    game_utama()