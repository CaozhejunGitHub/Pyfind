# -*- coding:utf-8 -*-
import path
import sys
import os
import re


search_path = os.getcwd()

params = []

if __name__ == '__main__':
    
    for param in sys.argv:
        params.append(param)
        
    for index in range(0, len(params)):
        
        if(re.match("-", params[index], 0)):
            print params[index]
            
           

                
               
            
        else:
            print params[index]
    
    #path.printPath(1, "d:/workspace")  
    #print '文件总数=', path.allFileNum 