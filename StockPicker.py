def StockPicker(arr):
	max_diff = 0
	n = len(arr)

	for i in range(0, n-1):
		for j in range(i+1, n):
			diff = arr[j]-arr[i]
			if diff > max_diff:
				max_diff = diff
	if max_diff == 0:
		return -1
	else:
		return max_diff


	# for i in range(0, n-1):
	# 	for j in range(0, n-i-1):
	# 		diff = j-i
	# 		if diff > max_diff:
	# 			max_diff = diff
	# if max_diff == 0:
	# 	return -1
	# else:
	# 	return max_diff



arr = [14,20,4,12,5,11]
print(StockPicker(arr))