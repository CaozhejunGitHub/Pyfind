# -*- coding:utf-8 -*-
import path
import sys
import os
import re


search_path = os.getcwd()
serach_pre = None
serach_suf = None
search_name = None
search_level = 0

params = []

def show_usage():
    print "print -h or help to show this mesage"
    print "[-p]    special path to search default pwd()"
    print "[-pre]  special prefix to file what you want to search"
    print "[-suf]  special suffix to file what you want to search"
    print "[-name] special file name what you want to search"
    print "[-l]    special level with directory where you want to search"
    print "tips: do not use -pre and -name or -suf and -name together"

if __name__ == '__main__':
    
    if (0 == len(sys.argv)):
        show_usage()
        pass
    
    for param in sys.argv:
        params.append(param)
        
    for index in range(0, len(params)):
        
        if (params[index] == "-h"):
            show_usage()
        elif(params[index] == "-p"):
            #print params[index+1]
            search_path = params[index+1]
        elif(params[index] == "-pre"):
            #print params[index+1]
            serach_pre = params[index+1]
        elif(params[index] == "-suf"):
            #print params[index+1]
            serach_suf = params[index+1]
        elif(params[index] == "-name"):
            #print params[index+1]
            search_name = params[index+1]
        elif(params[index] == "-l"):
            search_level = params[index+1]
    
    if (0 != path.param_check(serach_pre, serach_suf, search_name, search_path)):
        print "invalid param,please see the usage and check your param"
        
    path.do_search(search_path, search_level, serach_pre, serach_suf, search_name)
    #path.printPath(1, "d:/workspace")  
    #print '文件总数=', path.allFileNum 
    
    
