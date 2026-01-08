def rot13(text):
	result = " "
	for char in text:
		if 'a' <= char <= '2':
			result +=chr((ord(char)-ord('a')+13)%26+ord('A'))

		elif'A'<=char='Z':
			result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))


		else:
			result+=char
		return result
