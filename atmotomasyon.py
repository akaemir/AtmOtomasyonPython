print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nX ATM hoşgeldiniz\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para çekme
4. Borç sorgulama

Atm'den "exit" yazarak ayrılabilirsiniz.

""")

bakiye = 1000
limit = 2000
fark=0

while True:
    işlem = input("İşlemi giriniz:")
    #debug = """bakiye {} limit {} fark {} """.format(bakiye,limit,fark)
    #print(debug)
    if (işlem == "exit"):
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} ".format(bakiye),end="TL\n")
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar:"))
        bakiye += miktar
        fark-=miktar
        if(bakiye>=0):
                limit=2000
        else:
            limit+=miktar
        
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0 ):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} ".format(bakiye),end="TL\n")
            borc = input("Borç ister misiniz? - evet yada hayır : ")
            if (borc=="evet" and miktar<=limit):
                fark=miktar-bakiye
                if(bakiye>=0):
                    limit-=fark
                if(bakiye<0):
                    limit-=miktar
                bakiye-=miktar
                print("Borç aldınız kalan limitiniz: {} ".format(limit),end="TL\n")
            elif(bakiye-miktar<limit):
                print("Yetersiz limit, ancak şu kadar para çekebilirsiniz {} ".format(limit),end="TL\n")
            else:
                print("İşlem yapılmadı...")
            continue
        bakiye-=miktar
    elif(işlem=="4"):
        if (fark>0):
            print("Borcunuz {} ".format(fark),end="TL\nBorcunuzu ödemek için para yatırabilirsiniz...\n")
        else:
            print("Bankamıza ait mevduat hesabı borcunuz yoktur.") 
        pass
        continue
        

    else:
        print("Lütfen geçerli bir işlem giriniz.")