def sort_words(ls):
	ls = ls.split(' ')
	words = [w.lower() + w for w in ls]
	words.sort()
	words = [w[len(w)//2:] for w in words]
	return ' '.join(words)
x = input("Enter string: ")
print(sort_words(x))
