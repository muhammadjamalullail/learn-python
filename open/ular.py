# try :
#     text = open("halo.txt", "r")
#     print(text.read())
# except :
#     print("terjadi error : tidak ada file bernama halo.txt")
# from math import nan

# input = int(input("masukan angka : "));
# hasil = nan;
# try :
#     hasil = 10/input;   
# except :
#     print("input tidak boleh 0")

# print(f"hasilnya adalah {hasil}")


# from math import nan

# while(True) :
#     angka = int(input("masukan angka pembagi :"))
#     try :
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#     except :
#         print("pembagi nol, silahkan masukan input lagi!!")

#     done = input("lanjutkan y/n? ")
#     if done == "n" and done == "N" :
#         break 

# print("akhir dari program")


while(True) :
    try :
        with open("data.txt", "r") as name:
            print(name.read())  
        break
    except :
        print("file data.txt tidak ditemukan, membuat file baru")
        with open("data.txt", "w", encoding="utf-8") as name :
            name.write("file baru \nMuhammad Jamalullail\nFitriansyah")
        break

print("akhir dari program")