from flask import Flask, jsonify, request 
app = Flask(__name__) 
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) 
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "mattu"
}

@auth.verify_password
def verify(username,password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
 
languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'C++'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'The RESTful_api is working properly!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}

	languages.append(language)
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True)