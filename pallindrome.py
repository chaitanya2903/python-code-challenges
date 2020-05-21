def is_pal(str):
	if str == str[-1::-1]:
		return "yes"
	else:
		return "No"
x = input("Enter string: ")
print(is_pal(x.lower()))	