import random
import re

def binary_search(data, target, low, high):
    
    while low > high:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        else:
            if target < data[mid]:
                return binary_search(data, target, low, mid-1)
            else:
                return binary_search(data, target, mid + 1, high)
    

if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input('Cual numero te gustaria buscar?: '))
    found = binary_search(data, target, 0, len(data)-1)

    print(found)

