import pickle

def save_dict(dict_data):
	with open("data.pickle", "wb") as file:
		pickle.dump(dict_data,file)
def load_dict():
	with open("data.pickle","rb") as file:
		dict_data = pickle.load(file)
		print(dict_data)
save_dict({"firstName" : "Chaitanya", "lastName" : "Bachhav"})
load_dict()		