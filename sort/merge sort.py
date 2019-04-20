# Python program for implementation of Merge Sort 

# time Complexity [worst = O(n log(n)), Θ(n log(n)), best = Ω(n log(n))]
# Space Complexity [O(n)]

arr = [5, 8, 50, 4, 9, 2, 1]

def merge_sort(myList):
    if len(myList) > 1:
        med = len(myList)//2
        L = myList[:med]
        R = myList[med:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                myList[k] = L[i]
                i += 1
            else: 
                myList[k] = R[j] 
                j += 1
            k += 1

        # Checking if any element was left 
        while i < len(L): 
            myList[k] = L[i] 
            i += 1
            k += 1
          
        while j < len(R): 
            myList[k] = R[j] 
            j += 1
            k += 1

    return myList


print(merge_sort(arr))