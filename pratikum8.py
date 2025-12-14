def kalkulator_aman():
    """
    Program kalkulator sederhana yang menangani:
    1. Input non-angka (ValueError).
    2. Pembagian dengan nol (ZeroDivisionError).
    3. Operator tidak valid (Custom Exception).
    """
    print("--- Kalkulator Aman ---")

    # 1. Input Angka Pertama
    while True:
        try:
            angka1_str = input("Masukkan angka pertama: ")
            # Mengkonversi input ke float. Jika gagal, ValueError akan terangkat.
            angka1 = float(angka1_str)
            break # Keluar dari loop jika konversi berhasil
        except ValueError:
            print("❌ Input tidak valid. Pastikan Anda memasukkan angka.")

    # 2. Input Angka Kedua
    while True:
        try:
            angka2_str = input("Masukkan angka kedua: ")
            # Mengkonversi input ke float. Jika gagal, ValueError akan terangkat.
            angka2 = float(angka2_str)
            break # Keluar dari loop jika konversi berhasil
        except ValueError:
            print("❌ Input tidak valid. Pastikan Anda memasukkan angka.")

    # 3. Input Operator
    operator = input("Masukkan operator (+, -, *, /): ")

    hasil = None

    try:
        # Menangani Operator Tidak Valid (Custom Exception)
        if operator not in ('+', '-', '*', '/'):
            # Jika operator tidak ada di daftar yang diizinkan, raise Exception kustom
            raise Exception(f"Operator tidak valid: '{operator}'. Silakan gunakan +, -, *, atau /.")

        # Melakukan Perhitungan
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            # Menangani Pembagian dengan Nol (ZeroDivisionError)
            if angka2 == 0:
                # Secara eksplisit raise ZeroDivisionError jika angka2 adalah 0.
                # Ini akan ditangkap oleh block 'except ZeroDivisionError' di bawah.
                raise ZeroDivisionError("Tidak dapat melakukan pembagian dengan nol.")
            hasil = angka1 / angka2

    except ZeroDivisionError as e:
        print(f"🛑 Error: {e}")
        return # Menghentikan fungsi jika terjadi ZeroDivisionError

    except Exception as e:
        # Menangkap Exception kustom untuk operator tidak valid
        print(f"🛑 Error Operator: {e}")
        return # Menghentikan fungsi jika terjadi Exception kustom

    # 4. Menampilkan Hasil (jika perhitungan berhasil)
    print("-" * 25)
    print(f"Hasil dari {angka1_str} {operator} {angka2_str} adalah: {hasil}")
    print("-" * 25)

# Panggil fungsi kalkulator
kalkulator_aman()