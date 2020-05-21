def fin_po(li,num):
	index = list()
	for i in range(len(li)):
		if type(li[i]) == type(list()):
			index.append(fin_po(li[i],num))
		else:
			if li[i] == num:
				index.append(i)
	return index

x = [[1,2,3],[1,2,4],[2,2,3]]
print(fin_po(x,2))
				