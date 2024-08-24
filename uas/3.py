try:
    fileku = open("data.txt", "r")
    x = fileku.read()
    print(x)
    raise Exception("terjadi exception")
except:
    print("File tidak ditemukan ")
finally:
    fileku.close()
    print("selesai")
