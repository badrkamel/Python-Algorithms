# Python program for implementation of Selection Sort 

# time Complexity [worst = O(n^2), Θ(n^2), best = Ω(n^2)]
# Space Complexity [O(1)]

arr = [5,4,3,1,6,8,10,9] 
  
# Traverse through all array elements 
for i in range(len(arr)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(arr)): 
        if arr[min_idx] > arr[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    arr[i], arr[min_idx] = arr[min_idx], arr[i] 

print(arr)