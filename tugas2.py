
def buatMatriks3kali3():
    matriks = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        nilai = [int(k) for k in input(f"Masukkan elemen matriks baris {i+1}:").split()]
        for j in range(0,3):
            matriks[i][j] = nilai[j]
    return matriks

def penjumlahan(matriks1, matriks2):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j]
    return hasil

def pengurangan(matriks1, matriks2):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] - matriks2[i][j]
    return hasil

def perkalian(matriks1, matriks2):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]
    return hasil

def pemeriksaanMatriksSatuan(matriks):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    count = 0
    for i in range(3):
        for j in range(3):
            if matriks[i][j] == 1 or matriks[i][j] == 0:
                hasil[i][j] = 1
            else:
                hasil[i][j] = 0
    for i in range(3):
        for j in range(3):
            if hasil[i][j] == 1:
                count += 1
            if count == 9:
                return True
    return False

def menuOpsi():
    print("Silakan pilih operasi yang diinginkan:")
    print("1. Penjumlahan")
    print("2. Pengurangan") 
    print("3. Perkalian")
    print("4. Pemeriksaan matriks satuan")
    pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))
    while pilihan not in [1,2,3,4]:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))
    match pilihan:
        case 1:
            hasil_penjumlahan = penjumlahan(matriks1, matriks2)
            print("Hasil penjumlahan matriks1 dan matriks2 adalah:", hasil_penjumlahan)
        case 2:
            hasil_pengurangan = pengurangan(matriks1, matriks2)
            print("Hasil pengurangan matriks1 dan matriks2 adalah:", hasil_pengurangan)
        case 3:
            hasil_perkalian = perkalian(matriks1, matriks2)
            print("Hasil perkalian matriks1 dan matriks2 adalah:", hasil_perkalian)
        case 4:
            if pemeriksaanMatriksSatuan(matriks1):
                print("Matriks1 adalah matriks satuan.")
            else:
                print("Matriks1 bukan matriks satuan.")
            if pemeriksaanMatriksSatuan(matriks2):
                print("Matriks2 adalah matriks satuan.")
            else:
                print("Matriks2 bukan matriks satuan.")


if __name__ == "__main__":
    print("Selamat datang di kalkulator matriks 3x3")
    print("Masukkan elemen matriks1 dan matriks2 terlebih dahulu")
    print("###################################")
    matriks1 = buatMatriks3kali3()
    print("ini adalah matriks1 Anda: ",matriks1)
    matriks2 = buatMatriks3kali3()
    print("ini adalah matriks2 Anda",matriks2)
    print("###################################")
    menuOpsi()