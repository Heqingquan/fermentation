#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-07 10:39:09
# @Author  : Black_Horse (heqingquan_tim@163.com)
# @Link    : http://no.com
# @Version : $Id$
import json
import os,sys

reload(sys)
sys.setdefaultencoding("utf-8")

path = "ingredient.txt"

def load_data(filepath):
	fp = open(filepath,'r')
	if fp is None:
		print "没有找到配料文件"
		raise EOFError

	jlist = json.loads(fp.read().decode("GBK"))
	fp.close()
	return jlist

def load_config():
	fp = open('config.txt','r')
	if fp is None:
		print "没有找到配置文件"
		raise EOFError
	l_dic = {}
	for line in fp.readlines():
		word = line.decode("GBK").encode("utf-8").strip()
		if word.startswith('#') or word is "":
			continue
		l_word = word.strip().split("=")
		l_dic[unicode(l_word[0].strip())] = unicode(l_word[1].strip())
	fp.close()
	#print l_dic
	return l_dic

def compute_config(ingred,config):
	dic_in = {}
	#print config
	# print ingred
	for key,value in ingred.items():
		# print key
		size = float(config.get(key))
		#print size
		if size is None:
			print "设置中存在没有配置的元素"
			raise ValueError
		#print ingred
		for name,num in value.items():
			value[name] = round(float(num)*size,2)
	#print ingred
	return ingred

def computa_total(ingred):
	'''
	计算所有的元素
	'''
	total_integ= {}
	for val in ingred.values():
		for key,value in val.items():
			if total_integ.has_key(key):
				total_integ[key] += value
			else:
				total_integ[key] = value
	return total_integ


def print_config(ingredient,config):
	#print "book"
	#print "helloworld"
	output = []
	#添加标题文件
	output.append(config["name"]+"配料表")
	total_integ = computa_total(ingredient)
	output.append('*******************')
	output.append("#各类组份如下所示：")
	for key,value in config.items():
		if key == u"name":
			continue
		output.append("\t%s :%sL"%(key,value))
	#output.append('*******************')
	output.append("详细组份")
	for key,value in total_integ.items():
		if value <1000:
			output.append("\t%s :%.3fg"%(key,value))
		else:
			output.append("\t%s :%.3fkg"%(key,float(value)/1000))
	open('%s.txt'%config['name'],'w').write('\n'.join(output))


if __name__ == "__main__":
	ingred = load_data("ingredient.txt")
	# for key,value in ingred.items():
	# 	print key
	# 	for k2
	conf = load_config()
	ingred = compute_config(ingred,conf)
	#print ingred
	#computa_total(ingred)
	print_config(ingred,conf)

