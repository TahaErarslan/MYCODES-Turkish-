#Taha ERARSLAN 19010011066
print("PROGRAMI BAŞLATTIKTAN SONRA 4-5 SANIYE BEKLEYINIZ ACILMAZSA TEKRAR BASLATINIZ.")

import random
import gc #Bellek Boşaltmak için kullanılan bir kütüphane


def oyun_modu_1(): #Oyun Modu Gizli
    m=int(input("mxm boyutu giriniz (En az 10x10) m = "))
    gemi_kor= []
    ship11=[]
    ship1=[]
    ship2=[]
    ship3=[]
    gemi_boy=[1,2,3,4]
    a=0
    count=0
    for i in gemi_boy: #Gemiler
        
        if i==1:
            gemi1 =random.randint(0,m-2)
            gemi_1=random.randint(0,m-2)
            gemi=(gemi1,gemi_1)
            gemi_kor += [gemi]
            ship11+=[gemi]
        if i==2:
            while True:
                if(a==0):
                    gemi2=random.randint(0,m-2)
                    gemi_2=random.randint(0,m-2)
                c=gemi_2+a
                d=gemi2+a
                if(c<m):
                    gemi1=(gemi2,gemi_2+a)
                else:
                    gemi1=(gemi2+a,gemi_2)
                if(d>m) and (c>m):
                    gemi1=(gemi2,gemi_2-a)
                elif gemi1 not in gemi_kor:
                    gemi_kor+=[gemi1]
                    ship1+=[gemi1]
                    a=a+1
                if a==2:
                    a=0
                    c=0
                    d=0
                    break
                
        if i==3:
            while True:
                if(a==0):
                    gemi3=random.randint(0,m-2)
                    gemi_3=random.randint(0,m-2)
                c=gemi_3+a
                d=gemi3+a
                if(c<m):
                    gemi2=(gemi3,gemi_3+a)
                else:
                    gemi2=(gemi3+a,gemi_3)
                if(d>m) and (c>m):
                    gemi2=(gemi3,gemi_3-a)
                elif gemi2 not in gemi_kor:
                    gemi_kor+=[gemi2]
                    ship2+=[gemi2]
                    a=a+1
                if a==3:
                    a=0
                    c=0
                    d=0
                    break
                              
        if i==4:
            while True:
                if(a==0):
                    gemi4=random.randint(0,m-2)
                    gemi_4=random.randint(0,m-2)
                c=gemi_4+a
                d=gemi4+a
                if(c<m):
                    gemi3=(gemi4,gemi_4+a)
                else:
                    gemi3=(gemi4+a,gemi_4)
                if(d>m) and (c>m):
                    gemi3=(gemi4,gemi_4-a)
                elif gemi3 not in gemi_kor:
                    gemi_kor+=[gemi3]
                    ship3+=[gemi3]
                    a=a+1
                if a==4:
                    a=0
                    c=0
                    d=0
                    break    
            
    
    oyun_alani =[] #Oyun Alanı
    for i in range(m):
        row = ["?"]*m
        oyun_alani.append(row)
        
        
    for i in oyun_alani:
        print(i)
    
    gemi_sayisi = 4
    deneme =m*m//3
    atis=0
    while deneme: #Oynanış
        
        sutun = int(input("Sutun numarasi giriniz 1-{} : " .format(m)))
        satir = int(input("Satir numarasi giriniz 1-{} : ".format(m)))
                 
        if satir not in range(1,m+1) or sutun not in range(1,m+1):
            print("\nNumaralar 1-{} arasinda olmalidir".format(m))
            for i in oyun_alani:
                print(i)
            continue            
        satir = satir - 1
        sutun = sutun - 1
        if oyun_alani[sutun][satir] == "*" or oyun_alani[sutun][satir] == "X":
            print("\nBuraya zaten ates ettiniz!\n")
            for i in oyun_alani:
                print(i)
            print(f"Deneme hakki: {deneme} | Kalan gemi sayisi: {gemi_sayisi} | Atis sayisi : {atis}")
            continue
        elif (sutun,satir) in gemi_kor:
            if (sutun,satir)in ship11:
                print("\nTebrikler bir gemi batirdiniz\n")
                oyun_alani[sutun][satir] = "X"
                gemi_sayisi -= 1
                deneme-= 1
                atis+=1
            elif (sutun,satir) in ship1:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                deneme-= 1
                atis+=1
                oyun_alani[sutun][satir] = "X"
                if count==2:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            elif (sutun,satir)in ship2:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                deneme-= 1
                atis+=1
                oyun_alani[sutun][satir] = "X"
                if count==3:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            elif (sutun,satir) in ship3:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                oyun_alani[sutun][satir] = "X"
                deneme-= 1
                atis+=1
                if count==4:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            if gemi_sayisi==0:
                print("Tebrikler Tum gemileri batirdiniz ve Oyunu Kazandiniz. ")
                print("Toplam Puan = {}".format(deneme-atis-1))
                gc.collect() #Bellek Boşaltma
                break
        else:
            print("\nMaalesef isabet edemediniz\n")
            oyun_alani[sutun][satir] = "*"
            deneme-= 1
            atis+=1
        for i in oyun_alani:
            print(i)
    
        print(f"Deneme hakki: {deneme} | Kalan gemi sayisi: {gemi_sayisi} | Atis sayisi : {atis}")
    
        if deneme==0:
            print("Oyun bitti. Kaybettiniz")
            gc.collect() #Bellek Boşaltma
            break

                
 
def oyun_modu_2(): #Oyun Modu Gizli Değil
    m=int(input("mxm boyutu giriniz (En az 10x10) m= "))
    gemi_kor= []
    ship11=[]
    ship1=[]
    ship2=[]
    ship3=[]
    gemi_boy=[1,2,3,4]
    a=0
    count=0
    for i in gemi_boy: #Gemiler
        
        if i==1:
            gemi1 =random.randint(0,m-2)
            gemi_1=random.randint(0,m-2)
            gemi=(gemi1,gemi_1)
            gemi_kor += [gemi]
            ship11+=[gemi]
        if i==2:
            while True:
                if(a==0):
                    gemi2=random.randint(0,m-2)
                    gemi_2=random.randint(0,m-2)
                c=gemi_2+a
                d=gemi2+a
                if(c<m):
                    gemi1=(gemi2,gemi_2+a)
                else:
                    gemi1=(gemi2+a,gemi_2)
                if(d>m) and (c>m):
                    gemi1=(gemi2,gemi_2-a)
                elif gemi1 not in gemi_kor:
                    gemi_kor+=[gemi1]
                    ship1+=[gemi1]
                    a=a+1
                if a==2:
                    a=0
                    c=0
                    d=0
                    break
                
        if i==3:
            while True:
                if(a==0):
                    gemi3=random.randint(0,m-2)
                    gemi_3=random.randint(0,m-2)
                c=gemi_3+a
                d=gemi3+a
                if(c<m):
                    gemi2=(gemi3,gemi_3+a)
                else:
                    gemi2=(gemi3+a,gemi_3)
                if(d>m) and (c>m):
                    gemi2=(gemi3,gemi_3-a)
                elif gemi2 not in gemi_kor:
                    gemi_kor+=[gemi2]
                    ship2+=[gemi2]
                    a=a+1
                if a==3:
                    a=0
                    c=0
                    d=0
                    break
                              
        if i==4:
            while True:
                if(a==0):
                    gemi4=random.randint(0,m-2)
                    gemi_4=random.randint(0,m-2)
                c=gemi_4+a
                d=gemi4+a
                if(c<m):
                    gemi3=(gemi4,gemi_4+a)
                else:
                    gemi3=(gemi4+a,gemi_4)
                if(d>m) and (c>m):
                    gemi3=(gemi4,gemi_4-a)
                elif gemi3 not in gemi_kor:
                    gemi_kor+=[gemi3]
                    ship3+=[gemi3]
                    a=a+1
                if a==4:
                    a=0
                    c=0
                    d=0
                    break    
            
    
    oyun_alani =[] #Oyun Alanı
    for i in range(m):
        row = ["?"]*m
        oyun_alani.append(row)
    
    for (a,b) in gemi_kor:
        oyun_alani[a][b]="S"
    
    for i in oyun_alani:
        print(i)
    
    gemi_sayisi = 4
    deneme =m*m//3
    atis=0
    while deneme: #Oynanış
        
        sutun = int(input("Sutun numarasi giriniz 1-{} : " .format(m)))
        satir = int(input("Satir numarasi giriniz 1-{} : ".format(m)))
                
        if satir not in range(1,m+1) or sutun not in range(1,m+1):
            print("\nNumaralar 1-{} arasinda olmalidir".format(m))
            for i in oyun_alani:
                print(i)
            continue            
        satir = satir - 1
        sutun = sutun - 1
        if oyun_alani[sutun][satir] == "*" or oyun_alani[sutun][satir] == "X":
            print("\nBuraya zaten ates ettiniz!\n")
            for i in oyun_alani:
                print(i)
            print(f"Deneme hakki: {deneme} | Kalan gemi sayisi: {gemi_sayisi} | Atis sayisi : {atis}")
            continue
        elif (sutun,satir) in gemi_kor:
            if (sutun,satir)in ship11:
                print("\nTebrikler bir gemi batirdiniz\n")
                oyun_alani[sutun][satir] = "X"
                gemi_sayisi -= 1
                deneme-= 1
                atis+=1
            elif (sutun,satir) in ship1:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                deneme-= 1
                atis+=1
                oyun_alani[sutun][satir] = "X"
                if count==2:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            elif (sutun,satir)in ship2:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                deneme-= 1
                atis+=1
                oyun_alani[sutun][satir] = "X"
                if count==3:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            elif (sutun,satir) in ship3:
                count+=1
                print("\nTebrikler bir gemi vurdunuz\n")
                oyun_alani[sutun][satir] = "X"
                deneme-= 1
                atis+=1
                if count==4:
                    print("\nTebrikler bir gemi batirdiniz\n")
                    count=0
                    gemi_sayisi -= 1
            if gemi_sayisi==0:
                print("Tebrikler Tum gemileri batirdiniz ve Oyunu Kazandiniz. ")
                print("Toplam Puan = {}".format(deneme-atis-1))
                gc.collect() #Bellek Boşaltma
                break
        else:
            print("\nMaalesef isabet edemediniz\n")
            oyun_alani[sutun][satir] = "*"
            deneme-= 1
            atis+=1
        for i in oyun_alani:
            print(i)
    
        print(f"Deneme hakki: {deneme} | Kalan gemi sayisi: {gemi_sayisi} | Atis sayisi : {atis}")
    
        if deneme==0:
            print("Oyun bitti. Kaybettiniz")
            gc.collect() #Bellek Boşaltma
            break

def oyun_modu(): #Oyun Modu Menüsü
    oyun_modu=input("Oyun Modunu Giriniz \n (1)-Gizli mod:Gemiler Görünür Değil.\n (2) - Açık Mod: Gemiler Görünür. \n Giriş = " )
    if oyun_modu=="1":
        oyun_modu_1()
        return
    elif oyun_modu=="2":
        oyun_modu_2()
        return
oyun_modu()

#Yeniden Oynama Menüsü
yeniden_oyna=input("Yeniden Oynamak istermisiniz (E)EVET : (H)HAYIR =  ").upper()
    
if yeniden_oyna=="E":
    oyun_modu()
    gc.collect() #Bellek Boşaltma
else:
    exit
