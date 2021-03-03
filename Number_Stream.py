def NumberStream(str):
	index = 0
	count = 1
	try:
		prev_number = str[index]
		next_number = str[index + 1]
	except Exception as e:
		return False
	target_count = int(prev_number)
	while True:
		if count == target_count:
			return True
		else:
			if prev_number == next_number:
				count += 1
				index += 1
			else:
				count = 1
				index += 1
			try:
				prev_number = str[index]
				try:
					next_number = str[index + 1]
				except IndexError  as e:
					next_number = prev_number
			except IndexError  as e:
				return False
			target_count = int(prev_number)
	else:
		return False

