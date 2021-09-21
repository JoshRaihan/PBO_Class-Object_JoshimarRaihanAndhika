class BangunDatar:
    Segitiga=None
    JajarGenjang = None

BD=BangunDatar()
Segitiga=None
JajarGenjang=None

rows = 5

for i in range(rows + 1, 0, -1):

    for j in range(0, i - 1):

        print("*", end= "")
    print()

print("Jajar Genjang")
n= int (input("Masukan n:"))
i= 1
a= n
while (1<=n):
    print(" "*(n-1),"*" * a)
    n=n-1