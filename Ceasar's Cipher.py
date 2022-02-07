n, s = int(input()), input()

for i in s:

	index = ord(i) - n

	if index < 97:
		index = (26 - n) + (ord(i) - 96) + 96

	if index >= 97:
		print(chr(index), end = '')
