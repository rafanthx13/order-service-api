from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from json import dumps

# Ler modulo proprio
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/src')
import my_model_sklearn

# Lidar com Chamada Assincrona
app = Flask(__name__, static_url_path='')
CORS(app)

# API WEB REST

@app.route('/predict', methods = ['POST'])
@cross_origin()
def call_test():
	data = request.json['data'] # tem que por algo pra pegar
	print(data)
	# Check Data
	feat_continous = [
		'SR_month_1', 'SR_month_2', 'SR_month_3', 'avg_signal_up_week_4', 'avg_signal_up_week_3', 'avg_signal_up_week_2', 			'avg_signal_up_week_1', 'avg_signal_down_week_4', 'avg_signal_down_week_3', 'avg_signal_down_week_2', 'avg_signal_down_week_1', 		'avg_attenuation_up_week_4', 'avg_attenuation_up_week_3', 'avg_attenuation_up_week_2', 'avg_attenuation_up_week_1', 		'avg_attenuation_down_week_4', 'avg_attenuation_down_week_3', 'avg_attenuation_down_week_2', 'avg_attenuation_down_week_1', 		'std_attainable_rate_up_month_1', 'std_attainable_rate_up_month_2', 'std_attainable_rate_up_month_3', 			'std_attainable_rate_down_month_1', 'std_attainable_rate_down_month_2', 'std_attainable_rate_down_month_3', 		'std_current_rate_up_month_1', 'std_current_rate_up_month_2', 'std_current_rate_up_month_3', 'std_current_rate_down_month_1', 			'std_current_rate_down_month_2', 'std_current_rate_down_month_3'
	]
	valid_data = {}
	for feat in feat_continous:
		if(feat in data.keys()):
			if(data[feat] >= 0):
				valid_data[feat] = data[feat]
			else:
				return jsonify({"Error": "Feat " + feat +  " < 0, is invalid"})
		else:
				return jsonify({"Error": "Feat " + feat + " not found"})
			
	return jsonify(my_model_sklearn.classify_data(valid_data))

@app.route('/names', methods = ['GET'])
@cross_origin()
def get_names():
	return jsonify(my_model_sklearn.get_list_names())

@app.route('/person', methods = ['GET'])
@cross_origin()
def person():
	name = request.args.get('name')
    # print('name', name) # na URL substitui ' ' por %20 e volta para ' ' aki 
	return jsonify(my_model_sklearn.get_person(name))



if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
