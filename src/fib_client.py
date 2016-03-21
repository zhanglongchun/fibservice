#!/root/emc_test/restapi_test/venv/bin/python
# -*- coding:utf-8 -*-

import sys, string, urllib2, json

def fibonacci_service(fib_n):
	url = 'http://localhost:5000/testservices/api/v1.0/fibonacci/%d' % (fib_n)
	response = urllib2.urlopen(url)
	ret = response.read()
	decodejson = json.loads(ret)
	if 'error' in decodejson:
		return False, decodejson['error'];
	elif 'fibonacci' in decodejson:
		return True, decodejson['fibonacci']
	else:
		return False, ""

fib_n_num = 5
if (len(sys.argv) > 1):
	try:
		fib_n_num = string.atoi(sys.argv[1])
	except ValueError:
		print sys.argv[i], "is not a valid number"
		exit(1)

(flag, ret) = fibonacci_service(fib_n_num)

if flag == True:
	print ret
else:
	print "Err:", ret

