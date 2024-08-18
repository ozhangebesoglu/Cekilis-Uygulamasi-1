import random
import time
import os

print('Uygulama Açılıyor Lütfen Bekleyiniz...', end='', flush=True)
time.sleep(3)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')  



kullanicilar = list()
print('****CEKILIS UYGULAMASINA HOSGELDINIZ****')
print('-'*30)

def kullanici_ekle(x):
    print('-'*30)
    print('Kullanıcı Ekleme Ekranına Hosgeldiniz')
    ekle = input('Eklemek istediginiz kullanici adini giriniz: ')
    print('-'*30)
    kullanicilar.append(ekle)
    input('Kullanici eklendi. Ana menuye donmek icin bir tusa basiniz...')
    print('-'*30)

def kullanici_gor(x):
    say = 1 
    print('-'*30)
    for i in x:
        print(str(say) + ' -Kulanici Adi: ' , i)
        say += 1
    input('Ana menuye donmek icin bir tusa basiniz...')
    print('-'*30)

def sec(x):
    print('-'*30)
    say = 1
    kisi_sec = int(input('Kac kisi secilsin: '))
    rastgele_sec = random.sample(x,kisi_sec)

    for i in rastgele_sec:
        print('Rastgele secilen kisi veya kisiler sistemden cekiliyor...')
        time.sleep(3)
        print(str(say) + ' -Kulanici Adi: ' , i)
        say +=1 
    input('Ana menuye donmek icin bir tusa basiniz...')
    print('-'*30)

def salla(x):
    print('-'*30)
    say = 1 
    random.shuffle(x) #karistirma islemi
    for i in x :
        print(str(say) + ' -Kulanici Adi: ' , i)
        say += 1
    input('Karistirma islemi yapildi. Ana menuye donmek icin bir tusa basiniz...')

while True:
    print('-------------MENU-------------')
    print('-'*30)
    secim = int(input('1-Kullanici Ekle\n2-Kullanici Gor\n3-Kullanicilari Karistir\n4-Rastgele Sec\n5-Cikis Yap\n'))
    if secim == 1:
        kullanici_ekle(kullanicilar)
    elif secim == 2:
        kullanici_gor(kullanicilar)
    elif secim == 3:
        salla(kullanicilar)
    elif secim == 4:
        print('Kaç kişi olduğu hesaplanıyor...')
        time.sleep(2)
        sec(kullanicilar)
    elif secim == 5:
        print('Cikis Yapiliyor... Gorusmek Uzere :(')
        time.sleep(2)
        break
    else: 
        print('Hatali secim yaptiniz. Lutfen tekrar secim yapiniz...')
        

