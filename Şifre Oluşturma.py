# -*- coding: utf-8 -*-

tarih=input('DOGUM YILINIZI GIRINIZ : ')
sifre=input('SIFRE GIRINIZ : ')
sayac=0
sayac1=0
sayac2=0
print('---Herhangi bir UYARI almazsaniz sifreniz basariyla olusturulmus demektir---')
if len(sifre)>7 and len(sifre)<13:
    
#SAYI ILE BASLAMA BITME   
    for i in range(10):
        if sifre.startswith(str(i)):
            print("UYARI : Sifre sayi ile baslayamaz")
            break
        if sifre.endswith(str(i)):
            print("UYARI : Sifre sayi ile bitemez")
            break
#BUYUK HARF KUCUK HARF  
    for s in sifre:
        if(s.isupper()==True):
            sayac=1
        if(s.islower()==True):
            sayac1=1
    if(sayac==0):
        print('UYARI : Sifre en az 1 buyuk harf karakteri icermelidir')
    if(sayac1==0):
        print('UYARI : Sifre en az 1 kucuk harf karakteri icermelidir') 
#BOSLUK KARAKTERI  
    count=sifre.count(' ')
    if count!=0:
        print('UYARI : Sifre bosluk iceremez')
#ALFANUMERIK ICERME  
    elif sifre.isalnum()==True:
        print('UYARI : En az 1 tane alfanumerik olmayan karakter icermelidir')
#TEKRAR EDEN KARAKTER 
    tekrar = {}
    for j in sifre:
          if j in tekrar:
               tekrar[j] += 1
          else:
               tekrar[j] = 1
    for k in tekrar:
         if tekrar[k] > 1:
              print('UYARI : Sifre icinde tekrarlaryan karakter bulunmamalidir')
              break
#DOGUM TARIHI ICERME
    if(sifre.count(tarih)==1):
        print('UYARI : Sifre dogum yilinizi icermemelidir')
#SAYI ICERME
    for h in sifre:
        if(h.isdecimal()==True):
            sayac2=1
    if(sayac2==0):
        print('UYARI : Sifre en az 1 tane sayi icermelidir')

else: print("UYARI : Parola en az 8,en cok 12 karakterden olusmalidir")