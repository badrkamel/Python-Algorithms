# Python program for implementation of Bubble Sort 

# Time Complexity [worst = O(n^2), Θ(n^2), best = Ω(n)]
# Space Complexity [O(1)]

def bubble_sort(myList):

	print("#Bubble Sort Algorithm")
	moreSwaps = True

	while moreSwaps:
		moreSwaps = False
		for i in range(len(myList)-1):
			
			if myList[i] > myList[i+1]:
				moreSwaps = True
				temp = myList[i]
				myList[i] = myList[i+1]
				myList[i+1] = temp

	return myList

print(bubble_sort([11, 18, 5, 4, 6, 8]))