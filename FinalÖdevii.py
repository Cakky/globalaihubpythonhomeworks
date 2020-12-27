#kütüphane yükleme
import sys

#giriş
print("Hoş geldiniz O* D*")
ad1="Oğuz"
soyad1="Dalaslan"

#declare
def getLogin():
    ad=input("Adınızı Giriniz:")
    soyad=input("Soyadınız hatalı:")

    return ad, soyad

#def check(ad, soyad):
#  if (ad1!= ad and soyad == soyad1):
#    print("Adınız Hatalı")
#    return False
#  elif (ad == ad1 and soyad != soyad1):
#      print("Soyadınız hatalı")
#      return False
#  elif (ad != ad1 and soyad!= soyad1):
#      print("Adınız ve soyadınız hatalıdır.")
#      return False
#  else:
#      return True

#------------------- üstteki fonksiyona alternatif öneri
def check(ad, soyad):
    if ad != ad1 or soyad != soyad1:
        print('Giriş bilgileriniz yanlış.')
        return False
    else:
        return True



def final(): # ders seçimi?
  dersler = []
  while True:
      ders_sayısı = int(input("Ders sayını giriniz lütfen: "))
      if ders_sayısı < 3:
          return 'You failed this class'
      elif ders_sayısı > 5:
          print('en fazla 5 ders seçebilirsin')
      else:
          break
  for i in range(ders_sayısı):
      dersler.append(input("{0}. dersin ismini giriniz lütfen: ".format(i)))

  return dersler

#main code
totalError = 0

ad, soyad = getLogin() # getLogin() unpack

while not check(ad, soyad):
  totalError += 1
  ad, soyad = getLogin()

  if totalError == 2:
    print("3 kere hatalı giriş!")
    sys.exit()

print(final())
print("Notlarınız")
print("Ara sinav: 38","Final: 66","Proje: 89")
arasinav=(38*0.3+66*0.5+89*0.2)
print(arasinav)
if arasinav < 30:
  print("FF")
elif 30 < arasinav < 50:
  print("DD")
elif 50 < arasinav < 70:
  print("CC")
elif 70 < arasinav < 90:
  print("BB")
else:
  print("AA")
