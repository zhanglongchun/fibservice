#!/usr/bin/python

from fib_service import fibonacci

def test_fib_5():
	fib_array = fibonacci(5)
	print fib_array
	assert fib_array[4] == 3
	
def test_fib_10():
	fib_array = fibonacci(10)
	print fib_array
	assert fib_array[9] == 34

def test_fib_50():
	fib_array = fibonacci(50)
	print fib_array
	assert fib_array[49] == 7778742049

def test_fib_100():
	fib_array = fibonacci(100)
	print fib_array
	assert fib_array[99] == 218922995834555169026L
