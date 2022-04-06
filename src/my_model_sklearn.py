from sklearn.ensemble import RandomForestClassifier
import numpy
import pandas as pd
import pickle

filepath = './src/df_base_join_renamed.csv'

def get_file():
	return pd.read_csv(filepath, encoding = 'utf-8', sep=';', header = 0, low_memory = False)

def classify_data(data_dict):
	return_data = {
		'porcentage_0': '',
		'porcentage_1': '',
		'prediction': '',
	}

	data = numpy.array(list(data_dict.values())).reshape(1, -1)
	
	filename_model = 'rfo.model'
	loaded_model = pickle.load(open(filename_model, 'rb'))
	
	proba_predict = loaded_model.predict_proba(data)
	p_0, p_1 = proba_predict[0][0], proba_predict[0][1]

	return_data['porcentage_0'], return_data['porcentage_1'], return_data['prediction'] = p_0, p_1, int(loaded_model.predict(data)[0])

	#print('return_data\n\n',return_data)
	return return_data

def get_list_names():
	df = get_file()
	return_data = { 'names': [] }
	return_data['names'] = df['Name'].tolist()[:200]
	return return_data

def get_person(name_person):
	df = get_file()
	df_person = df[ df['Name'] == name_person]

	if( len(df_person) == 0 ):
		person = {'Error': 'Name Not Found'}
	else:
		person = df_person.iloc[0].to_dict()
	return person

