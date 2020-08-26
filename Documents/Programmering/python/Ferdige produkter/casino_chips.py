def solve(arr):
    i = 0
    while True:
        number_of_substractions = 0
        arr.sort(reverse=True)
        for c,element in enumerate(arr):
            if element > 0:
                element -= 1
                arr[c] = element
                number_of_substractions += 1
                print(arr)
                if number_of_substractions == 2:
                    i += 1
                    break
        if number_of_substractions < 2:
            break
    return i
print(solve([5,4,3]))
        
            


