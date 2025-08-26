# Notasi Algoritmik Kalkulator Matriks 3x3

## DEKLARASI
    matriks1, matriks2, hasil : array[0..2, 0..2] of integer
    i, j, k, pilihan, count : integer
    nilai : array of integer

## DESKRIPSI

### Program KalkulatorMatriks3x3
    output("Selamat datang di kalkulator matriks 3x3")
    output("Masukkan elemen matriks1 dan matriks2 terlebih dahulu")
    output("###################################")
    
    matriks1 ← buat_matriks_tiga_kali_tiga()
    output("ini adalah matriks1 Anda: ", matriks1)
    matriks2 ← buat_matriks_tiga_kali_tiga()
    output("ini adalah matriks2 Anda: ", matriks2)
    output("###################################")
    
    menuOpsi()

### Function buat_matriks_tiga_kali_tiga() → array[0..2, 0..2] of integer
    deklarasi:
        matriks : array[0..2, 0..2] of integer
        i, j : integer
        nilai : array of integer
    
    algoritma:
        for i ← 0 to 2 do
            input(nilai) {Masukkan elemen matriks baris ke-(i+1)}
            for j ← 0 to 2 do
                matriks[i,j] ← nilai[j]
        return matriks

### Function penjumlahan(matriks1, matriks2 : array[0..2, 0..2] of integer) → array[0..2, 0..2] of integer
    deklarasi:
        hasil : array[0..2, 0..2] of integer
        i, j : integer
    
    algoritma:
        for i ← 0 to 2 do
            for j ← 0 to 2 do
                hasil[i,j] ← matriks1[i,j] + matriks2[i,j]
        return hasil

### Function pengurangan(matriks1, matriks2 : array[0..2, 0..2] of integer) → array[0..2, 0..2] of integer
    deklarasi:
        hasil : array[0..2, 0..2] of integer
        i, j : integer
    
    algoritma:
        for i ← 0 to 2 do
            for j ← 0 to 2 do
                hasil[i,j] ← matriks1[i,j] - matriks2[i,j]
        return hasil

### Function perkalian(matriks1, matriks2 : array[0..2, 0..2] of integer) → array[0..2, 0..2] of integer
    deklarasi:
        hasil : array[0..2, 0..2] of integer
        i, j, k : integer
    
    algoritma:
        for i ← 0 to 2 do
            for j ← 0 to 2 do
                for k ← 0 to 2 do
                    hasil[i,j] ← hasil[i,j] + (matriks1[i,k] × matriks2[k,j])
        return hasil

### Function pemeriksaanMatriksSatuan(matriks : array[0..2, 0..2] of integer) → boolean
    deklarasi:
        hasil : array[0..2, 0..2] of integer
        i, j, count : integer
    
    algoritma:
        count ← 0
        for i ← 0 to 2 do
            for j ← 0 to 2 do
                if (matriks[i,j] = 1) or (matriks[i,j] = 0) then
                    hasil[i,j] ← 1
                else
                    hasil[i,j] ← 0
        
        for i ← 0 to 2 do
            for j ← 0 to 2 do
                if hasil[i,j] = 1 then
                    count ← count + 1
        
        if count = 9 then
            return true
        else
            return false

### Procedure menuOpsi()
    deklarasi:
        pilihan : integer
    
    algoritma:
        output("Silakan pilih operasi yang diinginkan:")
        output("1. Penjumlahan")
        output("2. Pengurangan")
        output("3. Perkalian")
        output("4. Pemeriksaan matriks satuan")
        
        input(pilihan) {Masukkan pilihan Anda (1/2/3/4)}
        
        while pilihan ∉ [1,2,3,4] do
            output("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
            input(pilihan)
        
        depend on pilihan:
            case 1:
                hasil ← penjumlahan(matriks1, matriks2)
                output("Hasil penjumlahan matriks1 dan matriks2 adalah:", hasil)
            case 2:
                hasil ← pengurangan(matriks1, matriks2)
                output("Hasil pengurangan matriks1 dan matriks2 adalah:", hasil)
            case 3:
                hasil ← perkalian(matriks1, matriks2)
                output("Hasil perkalian matriks1 dan matriks2 adalah:", hasil)
            case 4:
                if pemeriksaanMatriksSatuan(matriks1) then
                    output("Matriks1 adalah matriks satuan.")
                else
                    output("Matriks1 bukan matriks satuan.")
                if pemeriksaanMatriksSatuan(matriks2) then
                    output("Matriks2 adalah matriks satuan.")
                else
                    output("Matriks2 bukan matriks satuan.")