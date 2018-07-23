def space_to_20per(string):
	string_list = list(string)
	if " " not in string:
		return Error
	else:
		for char in range(len(string)):
			if string[char] == " ":
				string_list[char] ="%20"
	return string_list
space_to_20per(" ")
