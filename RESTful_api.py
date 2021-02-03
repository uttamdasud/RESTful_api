from flask import Flask, jsonify, request 
app = Flask(__name__) 
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__) 

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
@auth.login_required
def returnAll():
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
@auth.login_required
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
@auth.login_required
def addOne():
	language = {'name' : request.json['name']}

	languages.append(language)
	return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['PUT'])
@auth.login_required
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
@auth.login_required
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True)