# membuat sebuah definisi fungsi dengan nama funsinya adalah fibonacci 2
def fibonacci2(panjang) :
    # membuat tipe data list pada objek hasil
    hasil = []
    # assignment nilai a = 0, dan b = 2
    a,b = 0,1
    
    # selama nilai a < panjang maka lakukan perulangan
    while a < panjang :
        # menambahkan nilai ke dalam objek list hasil
        hasil.append(a)
        # nilai b di assignment ke variabel a,
        a, b = b, a+b
    # mengembalikan nilai hasil
    return hasil

tes = fibonacci2(5)
print(tes);