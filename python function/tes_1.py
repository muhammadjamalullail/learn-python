# membuat sebuah definisi fungsi dengan nama fungsina a adalah fibonacci. fungsi tersebut berisikan argument "panjang"
def fibonacci(panjang):
    # nilai 0 dan 1 di assgiments ke variabel a dan b
    a, b = 0, 1
    # cek kondisi saat nilai a < panjang maka jalankan perintah selanjutnya, sampai kondisi bernilai false
    while a < panjang :
        # tampilkan nilai a dengan format spasi
        print(a, end=" ")
        # nilai b di assignment ke variabel a, nilai a+b diassignment ke variabel b
        a, b = b, a+b
    
#memanggil nama fungsinya    
fibonacci(10)
print()


