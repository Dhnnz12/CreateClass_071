class persegipanjang:
    # Mendefinisikan kelas `persegipanjang` untuk objek persegi panjang

    def __init__(lah, panjang, lebar):
        # Konstruktor kelas dengan parameter `panjang` dan `lebar`
        lah.panjang = panjang  # Menginisialisasi atribut panjang
        lah.lebar = lebar      # Menginisialisasi atribut lebar

    def keliling(lah):
        # Metode untuk menghitung keliling persegi panjang
        return (lah.panjang + lah.lebar) * 2  # Rumus keliling = (panjang + lebar) * 2

    def luas(lah):
        # Metode untuk menghitung luas persegi panjang
        return lah.panjang * lah.lebar  # Rumus luas = panjang * lebar

    def __str__(lah):
        # Metode untuk mengembalikan representasi string dari objek
        return f"Panjangnya {lah.panjang} cm, dan Lebarnya {lah.lebar} cm"
    
try:
    # Blok try untuk menangani kesalahan input
    panjang = float(input("Masukkan panjang = "))  # Meminta input panjang dari pengguna
    lebar = float(input("Masukan lebar = "))       # Meminta input lebar dari pengguna

    if panjang <= 0 or lebar <= 0:
        # Memeriksa apakah panjang dan lebar bernilai positif
        print("Nilainya harus positif yah")
    else:
        # Jika nilai valid, membuat objek `persegipanjang` dengan panjang dan lebar yang dimasukkan
        pergipanjang = persegipanjang(panjang, lebar)
        
        print(pergipanjang)  # Menampilkan panjang dan lebar menggunakan metode `__str__`
        
        # Menampilkan keliling menggunakan metode `keliling`
        print("keliling = ", pergipanjang.keliling(), "cm")
        
        # Menampilkan luas menggunakan metode `luas`
        print("Luas = ", pergipanjang.luas(), "cm^2")

except ValueError:
    # Menangani kesalahan jika input tidak dapat diubah menjadi float
    print("Error nganbs")  # Menampilkan pesan kesalahan
