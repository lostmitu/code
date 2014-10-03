#!/usr/bin/env python3
#coding:utf-8
#data:2014-10-3-23:21


def super_range(start, stop, step):
	r = start 
	while r < stop:
			yield r
			r += step



#import drange
#i0 = drange(0.0, 1.0, 0.1)
#["%g" % x for x in i0]
