# Praktikum-ke-8
Latihan 1
Penjelasan Utama:
1. Penanganan ValueError (Input Non-Angka):

Menggunakan loop while True dan try-except ValueError saat meminta angka1 dan angka2.

Jika float(input) gagal, blok except ValueError akan mencetak pesan dan loop akan berulang, meminta input lagi sampai valid.

2. Penanganan Operator Tidak Valid (Custom raise Exception):

Setelah mendapatkan input, kode memeriksa apakah operator termasuk dalam ('+', '-', '*', '/').

Jika tidak, perintah raise Exception(...) digunakan untuk memunculkan pesan error kustom. Exception ini ditangkap oleh blok except Exception as e: di akhir.

3. Penanganan ZeroDivisionError (Pembagian dengan Nol):

Di dalam blok elif operator == '/':

Ada pemeriksaan kondisional if angka2 == 0:.

Jika angka2 adalah nol, kita secara eksplisit menggunakan raise ZeroDivisionError(...) untuk memicu error pembagian dengan nol.

Error ini ditangkap oleh blok except ZeroDivisionError as e: yang mencetak pesan kesalahan spesifik.

Struktur ini memastikan bahwa program dapat berjalan tanpa crash meskipun pengguna memasukkan input yang salah atau memicu kondisi perhitungan yang tidak valid.

Latihan 2 LOOPING
Konsep yang Digunakan
Looping (for item in nilai_list): Iterasi dilakukan pada setiap elemen dalam list.

try Block: Di sinilah kode yang berpotensi menimbulkan error (yaitu float(item)) diletakkan.

except ValueError: Jika float(item) gagal karena item bukan merupakan representasi angka yang valid (seperti 'A' atau 'B'), blok ini akan dieksekusi. Ini mencegah program crash.

continue: Setelah mendeteksi dan melaporkan data yang tidak valid, continue akan langsung melompat ke iterasi berikutnya, memastikan item yang tidak valid dilewati.

Apakah Anda ingin mencoba menjalankan fungsi ini dengan list nilai yang berbeda?
