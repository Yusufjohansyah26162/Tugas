berat_mangga = int (input("masukan berat mangga yang dibeli "))
harga_mangga = [20000, 18000, 16000] # index 0 : <=2 Kg, index 1 : >= 2 && <= 5, index 3 : >= 5 
 
if berat_mangga <= 2 :
    hasil = berat_mangga * 20_000
if berat_mangga >= 2 <= 5 :
    hasil = berat_mangga * 18_000
if berat_mangga >= 5 :
    hasil = berat_mangga * 16_000

print ("harga yang harus dibayar adalah ", hasil, "Rupiah")

    