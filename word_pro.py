from collections import Counter
import re
def word_count(file_name):
	with open(file_name,'r') as file:
		data = file.read()
		data = re.findall(r"[0-9a-zA-Z-']+",data)
		data = [x.lower() for x in data]
		print(data)
		counts = Counter()
		for word in data:
			counts[word] += 1
		print(counts)
		print("Most common 20 words:")
		for i in sorted(counts.keys(),reverse = True)[:20]:
			print(counts[i],"--->",i)
		return counts	
		
		
word_count("sample_two.txt")
