print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nX ATM hoşgeldiniz\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para çekme

Atm'den "exit" yazarak ayrılabilirsiniz.

""")

bakiye = 1000
fark=0

while True:
    işlem = input("İşlemi giriniz:")
    #debug = """bakiye {} fark {} """.format(bakiye,fark)
    #print(debug)
    if (işlem == "exit"):
        print("Yine bekleriz...")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} ".format(bakiye),end="TL\n")
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))
        bakiye += miktar
        fark-=miktar
        
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0 ):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} ".format(bakiye),end="TL\n")
        elif(bakiye-miktar >= 0):
            bakiye-=miktar
        else:
             print("İşlem yapılmadı...")
    else:
        print("Lütfen geçerli bir işlem giriniz.")