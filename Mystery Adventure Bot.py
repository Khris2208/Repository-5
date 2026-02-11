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
        elif tingkat_kesulitan == "sulit":
            self.hp = 70
            self.max_hp = 70
        else:  # normal
            self.hp = 100
            self.max_hp = 100
            
        self.inventaris = []
        self.misteri_terpecahkan = 0
        self.lokasi_sekarang = "gerbang"
        self.lokasi_dikunjungi = set()
        
    def ambil_item(self, item):
        self.inventaris.append(item)
        print(f"✓ Kamu mengambil: {item}")
        
    def gunakan_item(self, item):
        if item in self.inventaris:
            self.inventaris.remove(item)
            return True
        return False
    
    def lihat_status(self):
        print(f"\n═══ STATUS PEMAIN ═══")
        print(f"Nama: {self.nama}")
        print(f"Tingkat Kesulitan: {self.tingkat_kesulitan.upper()} ⚔️")
        print(f"HP: {self.hp}/{self.max_hp} ❤️")
        print(f"Misteri Terpecahkan: {self.misteri_terpecahkan}/6 🔍")
        print(f"Inventaris: {', '.join(self.inventaris) if self.inventaris else 'Kosong'}")
        print(f"Lokasi: {self.lokasi_sekarang}\n")

def cerita_pembukaan(pemain):
    print("\n" + "="*50)
    print("🌙 MISTERI TAMAN YANG TERLUPAKAN 🌙")
    print("="*50)
    time.sleep(0.5)
    
    print(f"\nSelamat datang, {pemain.nama}!")
    print("\nKamu menemukan dirimu di depan sebuah taman kuno yang penuh misteri.")
    print("Legenda mengatakan bahwa taman ini menyimpan harta karun besar...")
    print("Namun taman ini juga dipenuhi dengan monster berbahaya dan jebakan mematikan.")
    print("\nMisi Mu: Pecahkan 3 misteri utama untuk menemukan harta dan keluar dari taman ini!")
    print("\nGate taman terbuka perlahan mengeluarkan kabut gelap...")
    input("\nTekan ENTER untuk melanjutkan...")

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
    print("\n🌲 HUTAN GELAP 🌲")
    print("─" * 40)
    print("Pohon-pohon tinggi memblokir cahaya matahari.")
    print("Kegelapan menyelimuti sekelilingmu... terdengar suara binatang berbahaya!")
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
    print("\n🌳 POHON TUA BERBICARA 🌳")
    print("─" * 40)
    print("Kamu menemukan pohon raksasa dengan akar yang melilit tanah.")
    print("Patung batu di bawahnya berbicara dengan mata bersinar!")
    print("\n'Aku adalah penjaga hutan selama 500 tahun.'")
    print("'Untuk melewatiku, jawab teka-teki ini:'")
    print("\n🔍 TEKA-TEKI: 'Saya memiliki kota tapi tanpa rumah. Saya memiliki air tapi tanpa ikan.'")
    print("'Saya memiliki jalan tapi tanpa mobil. Apa aku?'")
    
    print("\nJawaban:")
    print("1. Peta")
    print("2. Cermin")
    print("3. Foto")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        print("\n✓ BENAR! Pohon itu bergerak dan membukakan jalan!")
        print("Patung berubah menjadi cahaya, meninggalkan kristal biru 💎")
        pemain.ambil_item("Kristal Biru")
        pemain.misteri_terpecahkan += 1
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
    else:
        print("\n✗ SALAH! Pohon itu marah dan mengeluarkan gas beracun!")
        pemain.hp -= 20
        print(f"HP berkurang 20 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk melanjutkan...")
    pemain.lokasi_sekarang = "gerbang"

def danau_misterius(pemain):
    print("\n💧 DANAU MISTERIUS 💧")
    print("─" * 40)
    print("Air danau bersinar dengan cahaya biru yang aneh.")
    print("Ada perahu tua di tepi danau...")
    print("Namun ada sesuatu yang bergerak di dalam air!")
    
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
    print("\n👻 PERAHU BERHANTU 👻")
    print("─" * 40)
    print("Kamu menaiki perahu dan mulai mendayung...")
    print("Tiba-tiba, kabut tebal menyelimuti danau...")
    print("Nampak bayangan manusia di depan!")
    
    print("\n'Hantu Danau' berbisik...")
    print("'Untuk keluar dari danau ini, kamu harus memecahkan teka-tekit saya...'")
    print("\n🔍 TEKA-TEKI: 'Saya naik ketika hujan, turun ketika cerah. Apa aku?'")
    
    print("\nJawaban:")
    print("1. Ember air")
    print("2. Payung")
    print("3. Pita")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "2":
        print("\n✓ BENAR! Hantu menghilang dengan senyuman...")
        print("Cahaya putih menerangi danau dan meninggalkan Permata Ungu 💜")
        pemain.ambil_item("Permata Ungu")
        pemain.misteri_terpecahkan += 1
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
    else:
        print("\n✗ SALAH! Hantu marah dan menenggelamkan perahu!")
        print("Kamu jatuh ke danau!")
        pemain.hp -= 35
        print(f"HP berkurang 35 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk melanjutkan...")
    pemain.lokasi_sekarang = "gerbang"

def kuil_kuno(pemain):
    print("\n⛩️ KUIL KUNO ⛩️")
    print("─" * 40)
    print("Kamu menemukan kuil berusia berabad-abad dengan arca-arca aneh.")
    print("Sebuah pintu besar tertutup rapat di tengah kuil...")
    print("Ada tulisan misterius di dinding: 'Temukan 3 batu ajaib untuk buka pintu'")
    
    print("\nArea kuil:")
    print("1. Ruang Altar (utara)")
    print("2. Gua Tersembunyi (timur)")
    print("3. Ruang Harta Karun (butuh 3 batu ajaib)")
    print("4. Kembali ke gerbang")
    
    pilihan = input("\nPilihan (1-4): ")
    
    if pilihan == "1":
        ruang_altar(pemain)
    elif pilihan == "2":
        gua_tersembunyi(pemain)
    elif pilihan == "3":
        if pemain.misteri_terpecahkan >= 3:
            ruang_harta_karun(pemain)
        else:
            print("\n⛓️ Pintu tidak terbuka! Kamu perlu 3 batu ajaib dulu!")
            print(f"Saat ini kamu baru punya {pemain.misteri_terpecahkan}/3")
            kuil_kuno(pemain)
    elif pilihan == "4":
        pemain.lokasi_sekarang = "gerbang"
    else:
        print("Pilihan tidak valid!")
        kuil_kuno(pemain)

def ruang_altar(pemain):
    print("\n🕯️ RUANG ALTAR 🕯️")
    print("─" * 40)
    print("Ruangan penuh dengan lilin bernyala dan beberapa altar emas.")
    print("Sebuah tulisan di dinding menampilkan angka-angka: 2 + 3 + 5 = ?")
    print("Jika benar, harta akan terbuka...")
    
    jawaban = input("\nJawaban Anda (angka): ")
    
    if jawaban == "10":
        print("\n✓ BENAR! Lantai mulai bergetar...")
        print("Sebuah peti harta muncul! Di dalamnya ada Batu Merah Panas 🔴")
        pemain.ambil_item("Batu Merah Panas")
        pemain.misteri_terpecahkan += 1
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
    else:
        print("\n✗ SALAH! Altar mengemeluarkan api!")
        pemain.hp -= 15
        print(f"HP berkurang 15 (sekarang: {pemain.hp})")
        if pemain.hp <= 0:
            game_over_kalah(pemain)
            return
    
    input("\nTekan ENTER untuk melanjutkan...")
    kuil_kuno(pemain)

def gua_tersembunyi(pemain):
    print("\n🍖 GUA BERISI FOSIL 🔨")
    print("─" * 40)
    print("Gua gelap ini penuh dengan fosil dan batu-batuan aneh.")
    print("LED cahaya lampu biofosforescen menembus kegelapan.")
    print("\nDi sudut gua, ada naga tidur... atau apakah sudah mati?")
    
    print("\nApa yang kamu lakukan?")
    print("1. Ambil fosil berharga dari gua")
    print("2. Bangunkan naga (BERBAHAYA!)")
    print("3. Cari harta tersembunyi")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        print("\nKamu mengambil beberapa fosil berharga...")
        print("Naga terbangun! GROAAARRR!!!")
        pertarungan_naga(pemain)
    elif pilihan == "2":
        print("\nKamu memukul naga dengan batu!")
        print("NAGA BANGUN DAN SANGAT MARAH!!!")
        pertarungan_naga(pemain)
    elif pilihan == "3":
        print("\nDi bawah batu besar ada kalung emas dengan batu biru! 💙")
        pemain.ambil_item("Kalung Batu Biru Langit")
        pemain.misteri_terpecahkan += 1
        print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
        print("\nTapi naga mulai bergerak...")
        print("Kamu cepat-cepat lari keluar gua!")
    
    input("\nTekan ENTER untuk melanjutkan...")
    kuil_kuno(pemain)

def pertarungan_naga(pemain):
    print("\n🐉 PERTARUNGAN NAGA! 🐉")
    print("─" * 40)
    
    if "pedang ajaib" in pemain.inventaris:
        print("Kamu mengeluarkan pedang ajaib!")
        print("Naga dan kamu bertarung sengit...")
        time.sleep(1)
        
        if random.random() > 0.3:
            print("⚔️ Dengan gerakan cepat, kamu mengalahkan naga!")
            print("Naga itu runtuh dan berubah menjadi cahaya...")
            print("Sebuah mahkota permata jatuh dari langit 👑")
            pemain.ambil_item("Mahkota Permata Naga")
            pemain.misteri_terpecahkan += 1
            print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
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
    """
    print("\n💻 LEMBAH CODING 💻")
    print("─" * 40)
    print("Kamu memasuki lembah yang dipenuhi dengan rune-rune aneh.")
    print("Setiap rune menyala dengan cahaya biru, menampilkan kode magis!")
    print("Seorang Sage Teknologi muncul dari dalam asap digital...")
    print("\n'Selamat datang, pemberani! Ini adalah tempat di mana logika dan sihir bersatu.'")
    print("'Untuk melewati lembah ini, kamu harus menyelesaikan 3 tantangan coding!'")
    
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
                print("\n✓ BENAR! Kamu memahami kuasa perulangan!")
                print("Cahaya biru menerangi dinding, kuartal pertama terbuka!")
                pemain.hp += 10
                print(f"HP Anda pulih! (+10, sekarang: {pemain.hp})")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Rune menyerang! Kesalahan logika fatal!")
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
                print("\n✓ BENAR! Logika kondisionalmu sempurna!")
                print("Cahaya emas menerangi area baru! Kristal Logika muncul!")
                pemain.ambil_item("Kristal Logika")
                pemain.misteri_terpecahkan += 1
                print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Kondisi yang salah memicu jebakan!")
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
                print("\n✓ BENAR! Kamu adalah Master Coding Sejati!")
                print("Ledakan cahaya digital mengisi lembah!")
                print("Sage Teknologi memberikan Medali Algoritma Emas! 🥇")
                pemain.ambil_item("Medali Algoritma Emas")
                pemain.hp += 20
                print(f"HP Anda pulih! (+20, sekarang: {pemain.hp})")
                tantangan_selesai += 1
            else:
                print("\n✗ SALAH! Kesalahan perhitungan data!")
                pemain.hp -= 10
                print(f"HP berkurang 10 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
    
    print("\n" + "="*40)
    print("✨ SELAMAT! Kamu telah menguasai Lembah Coding! ✨")
    print("Sage memberikan pesan: 'Teruslah belajar, sewaktu ada bug...'")
    print("="*40)
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"

def gunung_bug(pemain):
    """
    Gunung Bug - Jalur dengan tantangan debugging dan perbaikan kode
    """
    print("\n🐞 GUNUNG BUG 🐞")
    print("─" * 40)
    print("Kamu mendaki gunung tinggi yang dipenuhi dengan makhluk-makhluk aneh...")
    print("Setiap makhluk adalah representasi dari sebuah BUG dalam program!")
    print("Mereka menganggukan kepala dengan keras, menyesal akan kesalahan mereka...")
    print("\nSeorang Debug Hunter mendekatimu dengan pose waspada...")
    print("\n'Halo! Aku adalah Debug Hunter. Di sini, kamu harus memperbaiki BUG.'")
    print("'Jika berhasil, kamu akan mendapat reward. Jika gagal, mereka akan menyerangmu!'")
    
    bug_terperbaiki = 0
    
    while bug_terperbaiki < 3:
        print(f"\n🐛 Bug ke-{bug_terperbaiki + 1}/3")
        print("─" * 40)
        
        if bug_terperbaiki == 0:
            # Bug 1: Typo/Syntax Error
            print("BUG #1: SYNTAX ERROR")
            print("Kode di bawah ini memiliki error. Apa yang salah?")
            print("\nprint('Halo Dunia'")
            print("\n1. Kurang tanda tutup kurung ')'")
            print("2. Tanda quote tidak cocok")
            print("3. Nama variabel salah")
            jawaban = input("\nJawaban Anda (1-3): ")
            
            if jawaban == "1":
                print("\n✓ BENAR! Bug dibereskan! Makhluk bug berubah menjadi cahaya!")
                print("Sebuah Debug Badge muncul! 🎖️")
                pemain.ambil_item("Debug Badge Level 1")
                pemain.hp += 5
                print(f"HP Anda pulih! (+5, sekarang: {pemain.hp})")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Bug membuat serangan balik!")
                pemain.hp -= 20
                print(f"HP berkurang 20 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif bug_terperbaiki == 1:
            # Bug 2: Logic Error
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
                print("Aura merah mengelilingi makhluk, lalu menghilang...")
                print("Debug Badge Level 2 muncul! 🎖️")
                pemain.ambil_item("Debug Badge Level 2")
                pemain.misteri_terpecahkan += 1
                print(f"Misteri terpecahkan: {pemain.misteri_terpecahkan}/3")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Logika yang keliru memicu ledakan!")
                pemain.hp -= 18
                print(f"HP berkurang 18 (sekarang: {pemain.hp})")
                if pemain.hp <= 0:
                    game_over_kalah(pemain)
                    return
        
        elif bug_terperbaiki == 2:
            # Bug 3: Variable/Type Error
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
                print("\n✓ BENAR! Tipe data dibetulkan!")
                print("Semua bug di gunung ini menjadi emas murni...")
                print("Debug Badge Level 3 - MAHKOTA DEBUG muncul! 👑")
                pemain.ambil_item("Mahkota Debug Master")
                pemain.hp += 15
                print(f"HP Anda pulih! (+15, sekarang: {pemain.hp})")
                bug_terperbaiki += 1
            else:
                print("\n✗ SALAH! Bug terakhir menyerang dengan ganas!")
                pemain.hp -= 25
                print(f"HP berkurang 25 (sekarang: {pemain.hp})")
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
    Gua Naga Purba - Lokasi SANGAT SULIT dengan harta karun terbesar
    """
    print("\n🐉 GUA NAGA PURBA (SANGAT SULIT) 🐉")
    print("─" * 50)
    print("Kamu memasuki gua yang sangat gelap dan berbau sulfur.")
    print("Batu-batu raksasa dengan goresan cakar naga terlihat di mana-mana!")
    print("Suara gemuruh seperti pertarungan kuno terdengar dari dalam gua...")
    
    # Multiplier tingkat kesulitan
    if pemain.tingkat_kesulitan == "sulit":
        damage = 40
        reward_hp = 25
    else:
        damage = 30
        reward_hp = 35
    
    print("\n" + "="*50)
    print("⚔️ PERTARUNGAN DENGAN NAGA PURBA! ⚔️")
    print("="*50)
    
    print("\nNaga Purba muncul dengan napas api yang membara!")
    print("Dia adalah makhluk paling berbahaya di taman ini!")
    
    print("\nApa yang akan kamu lakukan?")
    print("1. Serang dengan semua kekuatan")
    print("2. Gunakan taktik defensif")
    print("3. Coba negosiasi")
    
    pilihan = input("\nPilihan (1-3): ")
    
    if pilihan == "1":
        if random.random() > 0.4:
            print("\n⚔️ Ledakan pertarungan yang luar biasa!")
            print("Kamu berhasil mengalahkan Naga Purba!")
            print("Harta karun berupa Mahkota Platinum muncul! 👑")
            pemain.ambil_item("Mahkota Platinum")
            pemain.misteri_terpecahkan += 1
            pemain.hp += reward_hp
            print(f"HP Anda pulih! (+{reward_hp}, sekarang: {pemain.hp})")
        else:
            print("\n✗ Naga Purba terlalu kuat! Serangannya sangat dahsyat!")
            pemain.hp -= damage
            print(f"HP berkurang {damage} (sekarang: {pemain.hp})")
    elif pilihan == "2":
        print("\nKamu mempertahankan posisi dan menunggu waktu yang tepat...")
        if random.random() > 0.5:
            print("Naga itu lelah dan memberikan kesempatan emas!")
            print("Kamu berhasil mengalahkan Naga Purba dengan bijak!")
            print("Permata Naga Purba jatuh ke tanganmu! 💎")
            pemain.ambil_item("Permata Naga Purba")
            pemain.misteri_terpecahkan += 1
            pemain.hp += reward_hp
        else:
            print("Naga itu masih terlalu agresif!")
            pemain.hp -= (damage - 10)
            print(f"HP berkurang {damage - 10} (sekarang: {pemain.hp})")
    elif pilihan == "3":
        print("\nKamu memandang mata naga dengan penuh keyakinan...")
        print("Naga melirik, seolah mengerti maksudmu...")
        print("Sebuah suara dalam berbicara: 'Kamu adalah manusia yang berbeda.'")
        print("Naga memberikan Kristal Kebijaksanaan! 🔮")
        pemain.ambil_item("Kristal Kebijaksanaan")
        pemain.misteri_terpecahkan += 1
        pemain.hp += (reward_hp + 10)
        print(f"HP Anda pulih! (+{reward_hp + 10}, sekarang: {pemain.hp})")
    
    if pemain.hp <= 0:
        game_over_kalah(pemain)
        return
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"

def taman_bunga_pesona(pemain):
    """
    Taman Bunga Pesona - Lokasi MUDAH dengan cerita romantis
    """
    print("\n🌺 TAMAN BUNGA PESONA (MUDAH) 🌺")
    print("─" * 50)
    print("Kamu memasuki taman yang indah penuh dengan bunga-bunga berwarna cerah.")
    print("Aroma bunga yang menenangkan memenuhi setiap aspek pikiranmu.")
    print("Seorang peri bunga muncul dan tersenyum ramah kepadamu...")
    
    print("\n'Selamat datang di Taman Bunga Pesona!'")
    print("'Aku adalah Peri Bunga, penjaga taman ini.'")
    print("'Jika kamu dapat mengumpulkan 5 bunga istimewa, aku akan memberikan hadiah.'")
    
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
            print("\n" + "="*50)
            print("🎁 SELAMAT! Kamu mengumpulkan semua 5 bunga!")
            print("="*50)
            print("Peri Bunga memberikan Mahkota Bunga Kekal! 👑")
            pemain.ambil_item("Mahkota Bunga Kekal")
            pemain.misteri_terpecahkan += 1
            pemain.hp += 30
            print(f"HP Anda pulih sepenuhnya! (+30, sekarang: {pemain.hp})")
            break
        elif i == 5:
            print(f"\nKamu hanya dapat mengumpulkan {bunga_dikumpulkan}/5 bunga.")
            print("Peri memberikan hadiah kecil sebagai tanda kasih...")
            pemain.ambil_item("Kristal Keindahan Taman")
            pemain.hp += 20
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"

def perpustakaan_kuno(pemain):
    """
    Perpustakaan Kuno - Lokasi SEDANG dengan tantangan pengetahuan
    """
    print("\n📚 PERPUSTAKAAN KUNO (SEDANG) 📚")
    print("─" * 50)
    print("Kamu memasuki perpustakaan raksasa dengan buku-buku berusia berabad-abad.")
    print("Debu membang di udara, cahaya matahari menebus celah-celah jendela kuno.")
    print("Seorang Pustakawan Tua mendekatimu dari balik rak buku yang tinggi...")
    
    print("\n'Selamat datang di Perpustakaan Kuno!'")
    print("'Di sini tersimpan pengetahuan dunia. Tapi hanya yang cerdas yang bisa keluar.'")
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
        print("Pustakawan memberikan Grimoire Pengetahuan Kuno!")
        pemain.ambil_item("Grimoire Pengetahuan Kuno")
        pemain.misteri_terpecahkan += 1
        pemain.hp += 25
        print(f"HP Anda pulih! (+25, sekarang: {pemain.hp})")
    else:
        print("Pustakawan memberikan buku panduan sederhana...")
        pemain.ambil_item("Buku Panduan Sederhana")
    
    input("\nTekan ENTER untuk kembali ke gerbang...")
    pemain.lokasi_sekarang = "gerbang"

def ruang_harta_karun_final(pemain):
    """
    Ruang Harta Karun Final - Ending game untuk 6 misteri terpecahkan
    """
    print("\n" + "="*60)
    print("💰 RUANG HARTA KARUN TERAKHIR - ENDING 💰")
    print("="*60)
    
    print("\nPintu dengan hieroglif membuka dengan suara gemuruh yang dahsyat...")
    print("Cahaya emas murni memenuhi seluruh ruangan...")
    print("Aura mistis mengelilingi semua objek berharga...")
    
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + "🏆 SELAMAT! KAMU TELAH MEMENANGKAN PETUALANGAN! 🏆".center(60) + "║")
    print("╚" + "="*58 + "╝")
    
    print(f"\n{pemain.nama}, kamu adalah PEMENANG SEJATI! 🎉")
    print(f"Tingkat Kesulitan: {pemain.tingkat_kesulitan.upper()}")
    print(f"HP Akhir: {pemain.hp}/{pemain.max_hp}")
    print(f"Misteri Terpecahkan: {pemain.misteri_terpecahkan}/6")
    
    print("\n" + "─"*60)
    print("HARTA KARUN YANG DIKUMPULKAN:")
    print("─"*60)
    
    if pemain.inventaris:
        for i, item in enumerate(pemain.inventaris, 1):
            print(f"{i}. ✓ {item}")
    
    print("\n" + "─"*60)
    print("PESAN DARI PENJAGA TAMAN:")
    print("─"*60)
    
    if pemain.tingkat_kesulitan == "sulit":
        print("\n⚔️ 'Kamu yang berani menghadapi segala tantangan!")
        print("Keberanianmu mencerminkan jiwa seorang prajurit sejati.'")
    elif pemain.tingkat_kesulitan == "mudah":
        print("\n😊 'Perjalananmu indah dan penuh pembelajaran.")
        print("Setiap perjalanan memulai dari langkah yang nyaman.'")
    else:
        print("\n⚖️ 'Kamu telah melewati ujian dengan sempurna!")
        print("Keseimbangan antara keberanian dan kebijaksanaan adalah kunci.'")
    
    print("\nSemua monster dan jebakan hilang dalam cahaya emas...")
    print("Taman Misteri kembali ke kebalikan aslunya...")
    print("Kamu keluar dari taman dengan harta karun dan pengalaman berharga!")
    
    print("\n" + "="*60)
    print("🎮 TERIMA KASIH TELAH BERMAIN 'MISTERI TAMAN' 🎮")
    print("="*60)
    print("Sampai jumpa di petualangan berikutnya! 👋\n")

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