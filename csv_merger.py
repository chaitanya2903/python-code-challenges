import csv

def merge_csv(file_list,output_file_name):
	dict_list = list()
	for file in file_list:
		with open(file,'r') as csv_file:
			dict = csv.DictReader(csv_file)
			dict_list.append(dict)
				
	with open(output_file_name,'w') as out_csv:
		writer = csv.DictWriter(output_csv)
		for dict in dict_list:		
			writer.writerow(dict)


			