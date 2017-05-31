import random
def random_number(first = 0, last = 10, count = 1) :
    if last > first and last - first > count :
        if count == 1 :
           return random.randrange(first, last)
        elif count > 1 :
            numbers = set()
            while len(numbers) < count:
                numbers.add(random.randrange(first, last))
            return sorted(numbers)
        else :
            print("Girdiğiniz Değerleri Kontrol Ediniz")

    else :
        print("Girdiğiniz Değerleri Kontrol Ediniz \nÖrnek Kullanım ==> 'random_number(2, 5, 2)'")
