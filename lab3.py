def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        return number * factorial(number-1)


def linear_search(list, key):
    size = len(list) - 1
    returnValue = linear(list,key,size)
    return returnValue

def linear(array, key, size):
    if size < 0:
        return -1
    if array[size] == key:
        return size
    return linear(array, key, size-1)



def binary_search(list, key):
    high = len(list) - 1
    low = 0
    retVal = binary(list,key,high,low)
    return retVal

def binary(list,key,high,low):
    if high >= low:
        mid = (high + low) // 2
        
        if list[mid] == key:
            return mid        
        elif list[mid] > key:
            return binary(list,key,mid - 1,low)
        else:
           return binary(list,key,high,mid + 1) 
    else:
        return -1
