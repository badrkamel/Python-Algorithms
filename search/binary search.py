arr = [10, 20, 30, 40, 50, 60]

def binary_search(list, item):

	print("#Binary Search")
	first = 0
	last = len(list)-1

	while first <= last:
		med = (first+last)//2
		if list[med] == item:
			return f"`{item}` found at index [{med}]"
		else:
			if list[med] > item:
				last = med -1
			else:
				first = med +1
	return f"`{item}` not found!"


print(binary_search(arr, 50))
print(binary_search(arr, 70))