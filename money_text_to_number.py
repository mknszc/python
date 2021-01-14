
def money_text_to_number(str):
    ones = {
        'bir'   : 1,
        'iki'   : 2,
        'üç'    : 3,
        'dört'  : 4,
        'beş'   : 5,
        'altı'  : 6,
        'yedi'  : 7,
        'sekiz' : 8,
        'dokuz' : 9
    }

    tens = {
        'on'    : 10,
        'yirmi' : 20,
        'otuz'  : 30,
        'kırk'  : 40,
        'elli'  : 50,
        'altmış': 60,
        'yetmiş': 70,
        'seksen': 80,
        'doksan': 90
    }

    hundred = {
        'yüz' : 100,
        'yuz' : 100
    }

    thousand = {
        'bin' : 1000,
        'bın' : 1000
    }

    million = {
        'milyon' : 1000000,
        'mılyon' : 1000000
    }

    arr = str.lower()
    arr = arr.split(' ')[::-1]
    arr = list(filter(None, arr))

    fac = 1
    total = 0

    while len(arr) > 0:
        if arr[0] in ones:
            total += ones[arr[0]] * fac

        elif arr[0] in tens:
            total += tens[arr[0]] * fac

        elif arr[0] in hundred:
            if len(arr) == 1 or arr[1] in thousand or arr[1] in million:
                total += fac * hundred[arr[0]]
            else:
                fac = fac * hundred[arr[0]]

        elif arr[0] in thousand:
            if len(arr) == 1 or arr[1] in million:
                total += thousand[arr[0]]
            else:
                fac = thousand[arr[0]]

        elif arr[0] in million:
            fac = million[arr[0]]

        else:
            return

        arr.remove(arr[0])

    return  total

if __name__ == '__main__':
    print(money_text_to_number('yüz beş milyon yüz beş bin yetmiş '))