#!/usr/bin/env python3
#coding:utf-8

def factors(n):
	return ( i for i in range(1, int(n/2+1)) if n%i==0)

def perfacts(n):
	return ( i for i in range(1,n+1) if sum(factors(n))==i)

if __name__ == "__main__":
	print (perfacts(100))

