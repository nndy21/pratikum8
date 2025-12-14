def hitung_rata_rata_aman(nilai_list):
    """
    Menghitung rata-rata nilai angka dari sebuah list yang mungkin berisi non-angka.
    Data non-angka akan dilewati menggunakan try-except.
    """
    total_nilai = 0
    jumlah_nilai_valid = 0

    print("--- Proses Iterasi dan Validasi Data ---")
    
    # Melakukan iterasi pada setiap item dalam list
    for item in nilai_list:
        try:
            # Mencoba mengkonversi item menjadi float (angka)
            nilai = float(item)
            
            # Jika konversi berhasil, item adalah angka yang valid
            total_nilai += nilai
            jumlah_nilai_valid += 1
            print(f"✅ Data valid ditemukan: {item}")

        except ValueError:
            # Jika konversi gagal (misalnya item adalah 'A' atau 'B'),
            # ValueError akan terangkat, dan program akan masuk ke blok except.
            # Perintah 'pass' atau kode di sini akan mengeksekusi aksi
            # melewati item ini tanpa menghentikan program.
            print(f"⚠️ Data tidak valid dilewati: '{item}' (Bukan angka)")
            # Lanjutkan ke iterasi berikutnya (skip item ini)
            continue
    
    print("-" * 35)

    # Menghitung rata-rata dari data yang valid
    if jumlah_nilai_valid > 0:
        rata_rata = total_nilai / jumlah_nilai_valid
        
        print(f"✨ Hasil Perhitungan Akhir ✨")
        print(f"Total Nilai Valid: {total_nilai}")
        print(f"Jumlah Data Valid: {jumlah_nilai_valid}")
        print(f"Rata-Rata Nilai: {rata_rata:.2f}") # Menampilkan 2 angka di belakang koma
    else:
        print("🛑 Tidak ada data nilai angka yang valid ditemukan dalam list.")

# Data mahasiswa yang diberikan
nilai = [80, 90, 'A', 70, 100, 'B', '95.5']

# Panggil fungsi
hitung_rata_rata_aman(nilai)