import pandas as pd

name = []
surname = []
number = []
note = []
harf_note = []
success = []
ders = input("Ders Girisi Yapiniz :")
ogrenci_sayi = int(input("Gireceğiniz öğrenci sayısı :"))
for i in range(ogrenci_sayi):
    name.append(input("İsminizi giriniz :"))
    surname.append(input("Soyisminizi giriniz :"))
    number.append(int(input("Numaranızı giriniz :")))
    nt = int(input("Notunuzu giriniz :"))
    note.append(nt)
    if nt >= 90 and nt <= 100:
        harf_note.append("AA")
    elif nt >= 85 and nt <= 89:
        harf_note.append("BA")
    elif nt >= 80 and nt <= 84:
        harf_note.append("BB")
    elif nt >= 75 and nt <= 79:
        harf_note.append("CB")
    elif nt >= 65 and nt <= 74:
        harf_note.append("CC")
    elif nt >= 60 and nt <= 64:
        harf_note.append("DC")
    elif nt >= 55 and nt <= 59:
        harf_note.append("DD")
    elif nt >= 50 and nt <= 54:
        harf_note.append("FD")
    else:
        harf_note.append("FF")
    if nt >= 60:
        success.append("GEÇTİ")
    else:
        success.append("KALDI")

def ogrenci_data(name, surname, number, note, harf_note, success):
    dataframe = list(zip(name, surname, number, note, harf_note, success))
    return pd.DataFrame(dataframe, columns=["İsim", "Soyisim", "Numara", "Not", "Harf Notu", "Basarı Durumu"])

data_1 = ogrenci_data(name,surname,number,note, harf_note, success)
data_1.to_excel(r'c:\Users\dtblackk\Desktop\excels\ders_notlari.xlsx', sheet_name=ders)