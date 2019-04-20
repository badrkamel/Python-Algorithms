arr = [10,5,20,18,15,8,6]

def linear_search(myList, item):

    print("#Linear Search")
    for i in range(len(myList)):
        if myList[i] == item:
            return  (f"`{item}` found at index [{i}]")

    return f"`{item}` not found!"

print(linear_search(arr, 15))
print(linear_search(arr, 30))