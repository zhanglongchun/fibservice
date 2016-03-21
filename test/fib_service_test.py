#!/usr/bin/python

import sys, string, urllib2, json
import pytest
from urllib2 import HTTPError

from fib_client import fibonacci_service

def test_fib_svc_5():
	(flag, fib_array) = fibonacci_service(5)
	print fib_array
	assert flag == True
	assert fib_array[4] == 3
	
def test_fib_svc_10():
	(flag, fib_array) = fibonacci_service(10)
	print fib_array
	assert flag == True
	assert fib_array[9] == 34

def test_fib_svc_50():
	(flag, fib_array) = fibonacci_service(50)
	print fib_array
	assert flag == True
	assert fib_array[49] == 7778742049

def test_fib_svc_100():
	(flag, fib_array) = fibonacci_service(100)
	print fib_array
	assert flag == True
	assert fib_array[99] == 218922995834555169026L

# less than 1
def test_fib_svc_err_1():
	(flag, fib_array) = fibonacci_service(-1)
	print fib_array
	assert flag == False
	assert fib_array == "-1 is less than 1"

# larger then limitation
def test_fib_svc_err_2():
	(flag, fib_array) = fibonacci_service(1000000)
	print fib_array
	assert flag == False
	assert fib_array == "1000000 is larger than 10000"

# invalid number
def test_fib_svc_err_3():
	url = 'http://localhost:5000/testservices/api/v1.0/fibonacci/xxx'
	response = urllib2.urlopen(url)
	ret = response.read()
	decodejson = json.loads(ret)
	assert ('error' in decodejson)
	assert (decodejson['error'] == 'xxx is not a valid integer')

# wrong URL
def test_fib_svc_err_4():
	url = 'http://localhost:5000/testservices/api/v1.0/fibonaccixxx/5'
	with pytest.raises(HTTPError):
		response = urllib2.urlopen(url)
