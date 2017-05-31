# !/usr/bin/python3

def fac(n):
    result = 1
    if n > 0 :
        while n > 0 :
            result = n * result
            n -= 1
        print(result)
    else:
        print("Lütfen 0 Dan Büyük Bir Değer Giriniz")
