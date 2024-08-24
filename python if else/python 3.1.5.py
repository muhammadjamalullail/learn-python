print("menentukan nilai terkecil");
nilai1 = int(input("masukan nilai 1 = "));
nilai2 = int(input("masukan nilai 2 = "));
nilai3 = int(input("masukan nilai 3 = "));
print("\n");

if nilai1 < nilai2 and nilai1 < nilai3 :
    print("maka nilai 1 lebih kecil");
elif nilai2 < nilai1 and nilai2 < nilai3 :
    print("maka nilai 2 lebih kecil");
elif nilai3 < nilai1 and nilai3 < nilai2 :
    print("maka nilai 3 lebih kecil");
else : 
    print("tidak ada nilai");
