def sumArray(array = []):
    sumArray = 0
    for i in array:
        if type(i) == int :
            sumArray += int(i)
    print(sumArray)

if __name__ == '__main__':
    sumArray([1, 2, 3, 4, 'a'])