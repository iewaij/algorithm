def check_sequence(sequence):
    i = 0
    j = 1
    while j < len(sequence) and i < j:
        if sequence[i] < sequence[j]:
            j = j+1
            i = i+1
        else:
            return(False)
    return(True)


sequence = [1, 2, 5, 8, 9, 13, 44, 24]
check_sequence(sequence)

def check(lista):
    i = 1
    while i < len(lista):
        if lista[i - 1] < lista[i]:
            i = i + 1
        else:
            print("It's not ascending")
            break
    if i == len(lista):
        print("It's ascending")


check([1, 2, 3, 4, 5]) 

def check(lista):
    i = 1
    while i < len(lista):
        if lista[i - 1] < lista[i]:
            i = i + 1
        else:
            return False
    if i == len(lista):
        print("It's ascending")

def check(i):
    return i
    return i + 1
