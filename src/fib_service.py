#!/root/emc_test/restapi_test/venv/bin/python
import string
from flask import Flask, jsonify, make_response
from flask.ext.httpauth import HTTPBasicAuth

######################################
# authentication
######################################
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'test':
		return 'test'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 401)

app = Flask(__name__)

######################################
# core function
######################################
def fibonacci(n):
	if n == 1:
		return [0]
	if n == 2:
		return [0, 1]
	
	fibs = [0, 1]
	for i in range(2, n):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs


######################################
# service interface
######################################
@app.route('/testservices/api/v1.0/fibonacci/<fib_n>', methods=['GET'])
@auth.login_required
def get_fibonacci(fib_n):
	try:
		fib_n_num = string.atoi(fib_n)
	except ValueError:
		return jsonify({'error': fib_n + ' is not a valid integer'})
	
	if fib_n_num > 10000:
		return jsonify({'error': fib_n + ' is larger than 10000'})
	if fib_n_num <= 0:
		return jsonify({'error': fib_n + ' is less than 1'})

	fib_array = fibonacci(fib_n_num)
	return jsonify({'fibonacci': fib_array})


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
