# -*- coding:utf-8 -*-


import os



def param_check(pre, suf, name, path):

    if(not os.path.isdir(path)):
        print path + "is not a valid path"
        return -1
    
    if ((name != None and pre != None) or (name != None and suf != None)):
        return -1
    return 0


def do_search(path, level, pre, suf, name):

    dir_list = []
    fileList = []
    
    files = os.listdir(path)
    
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            dir_list.append(path + '/' + f)
        elif (os.path.isfile(path + '/' + f)):
            fileList.append(path + '/' + f)
            
            if (name != None):
                # bi jiao wen jian ming
                if (len(name) > len(f)):
                    # wen jian min yu cha zhao bu pi pei
                    continue
                elif(f.find(name, 0, len(f)) != -1):
                    print "path + '/' + f"
    
            elif(pre != None and suf != None):
                print
            elif(pre != None and suf == None):
                if(len(pre) > len(f)):
                    continue
                else:
                    if (f.find(pre,0,len(f))!=-1):
                        print path + '/' + f
                    else:
                        continue
            elif(suf != None and pre == None):
                if(len(suf) > len(f)):
                    continue
                else:
                    if (f.endswith(suf,0,len(f))!=-1):
                        print path + '/' + f
                    else:
                        continue
                print

    for dl in dir_list:
        do_search(path, level, pre, suf, name)

    return

allFileNum = 0

def printPath(level, path):  
    global allFileNum  
  
    dirList = []  
    
    fileList = []  
   
    files = os.listdir(path)  
    
    dirList.append(str(level))  
    for f in files:  
        if(os.path.isdir(path + '/' + f)):  
            
            if(f[0] == '.'):  
                pass  
            else:  
                
                dirList.append(f)  
        if(os.path.isfile(path + '/' + f)):  
            
            fileList.append(f)  
    
    i_dl = 0  
    for dl in dirList:  
        if(i_dl == 0):  
            i_dl = i_dl + 1  
        else:  
            
            print '-' * (int(dirList[0])), dl  
            
            printPath((int(dirList[0]) + 1), path + '/' + dl)  
    for fl in fileList:  
        
        print '-' * (int(dirList[0])), fl  
        
        allFileNum = allFileNum + 1  
        
        
