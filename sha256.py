import random

def Bit_Cevirme(list):
    new_list = list[::-1]
    return new_list

def Kontrol(bit, sifrelenecek, bos):
    x = len(sifrelenecek)
    if x < bit:
        a = bit - x
        for i in range(a):
            bos.append(str(0))
        bos = "".join(bos)
        # print("\n0'ların bit sayısı: ", len(bos))
        sifrelenecek =  bos + sifrelenecek
        # print("Yeni bit: ", sifrelenecek)
        # print("\nToplam bit:", len(sifrelenecek))
        return sifrelenecek

def XORArray(A,B):
    XORED = []
    for i in range(len(rastgele_anahtar)):
        XORED.append(A[i]^B[i])
    return XORED


def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

sifrelenecek = []
rastgele_anahtar = ["11001011110011110010011000011110011110010011000011110011110010011000011110011110010011000011110011110010010101110101010101010101"]
rastgele_anahtar = "".join(rastgele_anahtar)
bos = []
mesaj = input("Mesaji Giriniz: ")

for i in mesaj:
    sifrelenecek.append(bin(ord(i))[2::])
sifrelenecek = "".join(sifrelenecek)
print("\nBit cevirmesiz:", sifrelenecek)
bit_cevirmesiz_boy=len(sifrelenecek)
# print("Bit cevirmesiz boy: ", bit_cevirmesiz_boy)

anahtar1 = [1, 2, 3, 4]
anahtar2 = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(anahtar1)
random.shuffle(anahtar2)
print("\nAnahtar1 : ---->", anahtar1)
print("\nAnahtar2 : ---->", anahtar2)

if bit_cevirmesiz_boy < 256:
    sifrelenecek2 = Kontrol(256,sifrelenecek, bos)
    # print(sifrelenecek2)
    sifrelenecek3 = Bit_Cevirme(sifrelenecek2)
    # print("\nBit cevrilmis: ", sifrelenecek3)
    # print("Mesaj ",len(sifrelenecek3), " bit\n")

asama1 = {}
asama2 = {}

asama1[anahtar1[0]] = sifrelenecek3[0:64]
asama1[anahtar1[1]] = sifrelenecek3[64:128]
asama1[anahtar1[2]] = sifrelenecek3[128:192]
asama1[anahtar1[3]] = sifrelenecek3[192:256]


# print(asama1)

son_liste = []
son_liste = asama1[1]+asama1[2]+asama1[3]+asama1[4]

# print("Elimizdeki son sayi: ", son_liste)

# print("Cevrilmemis Anahtar: ", rastgele_anahtar)

cevrilmis_anahtar = Bit_Cevirme(rastgele_anahtar)

# print("Cevrilmis Anahtar: ", cevrilmis_anahtar)

rastgele_anahtar = rastgele_anahtar + cevrilmis_anahtar
# print("Eklenmis rastgele anahtar: ", rastgele_anahtar)

rastgele_anahtar="".join(rastgele_anahtar)
sifrelenecek3="".join(sifrelenecek3)

results = [int(i) for i in rastgele_anahtar]
resultss = [int(i) for i in sifrelenecek3]

c = XORArray(results,resultss)
print("\nBit cevrilmis: ", sifrelenecek3)
print(c)

toplam = [str(i) for i in c]
toplam = "".join(toplam)
print("SON SIFRELI METIN: ",toplam)

asama2[anahtar2[0]] = toplam[0:32]
asama2[anahtar2[1]] = toplam[32:64]
asama2[anahtar2[2]] = toplam[64:96]
asama2[anahtar2[3]] = toplam[96:128]
asama2[anahtar2[4]] = toplam[128:160]
asama2[anahtar2[5]] = toplam[160:192]
asama2[anahtar2[6]] = toplam[192:224]
asama2[anahtar2[7]] = toplam[224:256]

son_liste2 = []
son_liste2 = asama2[1]+asama2[2]+asama2[3]+asama2[4]+asama2[5]+asama2[6]+asama2[7]+asama2[8]
# print(asama2)
print("Sifrelenmis anahtar: ", son_liste2)

son={}
for i in range(8):
    son[i+1]=asama2[anahtar2[i]]
print(son)
son_liste3=[]
son_liste3 = son[1]+son[2]+son[3]+son[4]+son[5]+son[6]+son[7]+son[8]
print(son_liste3)
a = [str(i) for i in son_liste3]
a="".join(a)
print("Geri donus 1: ",a)

results = [int(i) for i in rastgele_anahtar]
resultss = [int(i) for i in a]

c = XORArray(results,resultss)
# print(str(c))

c = [str(i) for i in c]
c = "".join(c)
print("Geri donus 2: ",c)


ppp = Bit_Cevirme(c)

ops = []
for i in ppp:
    ops.append(i)
print(ops)

del ops[0:len(bos)]

ops = "".join(ops)
print(ops)
str_data =' '
for i in range(0, len(ops), 7):
    temp_data = int(ops[i:i + 7])
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data)
print(str_data)

