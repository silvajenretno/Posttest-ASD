import os
import time
os.system("cls")

def partisi(l, bawah, atas) :
    pivot = l[bawah]
    sbg_batas = bawah+1
    for a in range (bawah+1, atas) :
        if l[a] < pivot :
            l[sbg_batas], l[a] = l[a], l[sbg_batas]
            sbg_batas += 1
    l[sbg_batas-1], l[bawah] = l[bawah], l[sbg_batas-1]
    return sbg_batas

def quicksort(l, bawah, atas) :
    if atas <= bawah :
        return
    b = partisi(l, bawah, atas)
    quicksort(l, bawah, b-1)
    quicksort(l, b, atas)
    return l

def searching(isi, x, n) :
    fibo2 = 0
    fibo1 = 1
    fibo = fibo2 + fibo1
    while (fibo < n):
        fibo2 = fibo1
        fibo2 = fibo
        fibo = fibo2 + fibo1
    offset = -1
    while (fibo > 1) :
        i = min(offset + fibo2, n-1)
        if (isi[i] < x) :
            fibo = fibo1
            fibo1 = fibo2
            fibo2 = fibo - fibo1
            offset = i
        elif (isi[i] > x) :
            fibo = fibo2
            fibo1 = fibo1 - fibo2
            fibo2 = fibo - fibo1
        else :
            return i
    if (fibo1 and isi[n-1] == x) :
        return n-1
    return -1

def search() :
    print("Ketika ingin mencari kata zaki maka hasilnya : ")
    for z in range(len(data2)):
        if type(data2[z]) == list :
            isi = searching(data[z], "zaki", len(data[z]))
            time.sleep(2)
            print("Zaki berada di array index ke - ", z, "kolom", isi)
        else :
            if data2[z] == x :
                time.sleep(2)
                print("zaki berada di array index ke - ", z)

data = ["daiva", "zaki", ["wahyu", "zaki"], "shafa", ["zaki", "aji", "wahyu"], "zaki"]
data2 =[]
data3 ={}
x = "zaki"

def sorting() :
    print("""
===================================================================================
^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ 
""")
    print("=^.^= Sebelum Diurutkan =^.^=\n", data)
    for i in range(len(data)) :
        if type(data[i]) != str:
            data3[i] = data[i]
        else :
            data2.append(data[i])
            quicksort(data2,0,len(data2))
    print("""
===================================================================================
^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^ ^.^
""")
    for a in data3:
        quicksort(data3[a],0,len(data3[a]))
        data2.insert(a,data3[a])
    print("=^.^= Setelah Diurutkan =^.^=\n", data2)
    print("")


sorting()
search()