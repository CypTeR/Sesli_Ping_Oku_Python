import os
from gtts import gTTS #gtts kütüphanesi "pip install gtts"
from pythonping import ping #ping kütühanesi "pip install pythonping"

print("Host Giriniz: ")

try:
    host = input() #host girişi
    sonuc = ping(host)
    cevir = int(sonuc.rtt_avg_ms)
    strcvr = str(cevir)
    okut = host+" pinginiz ortalama "+strcvr+"ms" #birleştirme
    tts = gTTS(text=okut, lang='tr') #yazıyı sese çevir
    print(cevir)
    tts.save("merhaba.mp3") #sesi kaydet
    os.system("merhaba.mp3") #sesi oynat
    os.system("del merhaba.mp3") #sesi sil


except:
    print("Boş veya Geçersiz Host!")
