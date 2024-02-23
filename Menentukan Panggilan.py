umur = int (input("masukan umur anda  "))
if umur <= 2 :
    hasil = "bayi"
if umur >= 2 <= 5 :
    hasil = "balita"
if umur >= 5 <= 12 :
    hasil = "anak anak"
if umur >= 12 <= 17 :
    hasil = "remaja"
if umur >= 17 <= 30 :
    hasil = "Dewasa"
if umur >= 30 :
    hasil = "orang tua"

print (umur, "tahun adalah", hasil)