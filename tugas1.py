

def hitung_rerata(array):
    sumarray = 0
    for i in range(len(array)):
        sumarray += array[i]
    return sumarray / len(array)

def hitung_nilai_max(array, n):
    maximum = -9999
    for i in range(n):
        if (array[i]>maximum):
            maximum = array[i]
    return maximum

def hitung_nilai_min(array,n):
    minimum = 9999
    for i in range(n):
        if (array[i]<minimum):
            minimum = array[i]
    return minimum

def sorting_alg(array,n):
    for i in range(n):
        temp = array[i]
        j=i-1
        while j>=0 and temp>array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp
    return array


def hitung_nilai_median(array):
    array.sort()
    n = len(array)
    if n % 2 == 0:
        median = (array[n // 2 - 1] + array[n // 2]) / 2
    else:
        median = array[n // 2]
    return median

if __name__ == "__main__":
    key = True
    n = int(input("Masukkan bilangan bulat positif: "))
    arrayList = [0 for i in range(n)]
    while key:
        if n <= 5:
            print("Bilangan kurang dari atau sama dengan 25")
            n = int(input("Masukkan bilangan bulat positif: "))
            arrayList = [0 for i in range(n)]
        else:
            for i in range(n):
                nilai = int(input("Masukkan bilangan bulat: "))
                arrayList[i] = nilai
            key = False
        

    print("Rata-rata:", hitung_rerata(arrayList))
    print("Nilai maksimum:", hitung_nilai_max(arrayList,n))
    print("Nilai minimum:", hitung_nilai_min(arrayList,n))
    print("Nilai median:", hitung_nilai_median(arrayList))
    print("Top 10 nilai", sorting_alg(arrayList,n))