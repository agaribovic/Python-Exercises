def concatenate(*args):
	result = None
	for i in args:
		if result == None:
			result = i
		else:
			result += "-" + i
	return result

print(concatenate("I", "love", "Python", "!"))
