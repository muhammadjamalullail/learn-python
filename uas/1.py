print()

print(3*"=", "Program nilai input paling besar", 3*"=")
nilai_A = int(input("masukan nilai A = "))
nilai_B = int(input("masukan nilai B = "))
nilai_C = int(input("masukan nilai C = "))

if nilai_A > nilai_B and nilai_A > nilai_C :
    print("Nilai A adalah yang terbesar")
elif nilai_B > nilai_A and nilai_B > nilai_C :
    print("Nilai B adalah yang terbesar")
else :
    print("Nilai C adalah yang terbesar")

print()