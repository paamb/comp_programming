def solve(arr):
    arr.sort()
    if arr[0] + arr[1] < arr[2]:
        print(arr[0] + arr[1])
    else:
        sum_of_elements = sum(arr)
        print(sum_of_elements // 2)
solve([1,2,3])
     