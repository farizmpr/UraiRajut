#soal 3 mengurai dan merajut kata (40 poin)
#untuk yang urai polanya mirip setengah dari segitiga
def urai(string):
    length=len(string)#agar bisa diakses oleh for, diubah ke bentuk integer
    for row in range(0, length):#menentukan berapa panjang yang akan di print berapa baris kebawah
        for col in range(0, row+1):#mengeprint dari pertama kalias dari 0
            print(string[col], end='')#mengeprint string yang ada di sesuai colom berapa, jika kolom 0 maka C saja

urai("Code")

#soal 3 #not done yet
def rajut(string, delim):
    x = string.split(delim)
    processed = delim + x[-1]
    return processed

stringku = 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'
token = stringku[0]
new_text = rajut(stringku, token)
print(stringku)