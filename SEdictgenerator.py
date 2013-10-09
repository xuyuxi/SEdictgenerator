# -*- coding: utf-8 -*-  
'''\
Social Engineering dict generator
Author:yufan
Blog:http://www.cnblogs.com/yufanpi/
Email:yufanpi@gmail.com
2013.10
'''
import sys
import re


gStr = [ 
       ]
gA = []
def OutPutDict(file , str,  remain):
    if len(str):
        #print (str)
        file.write(str  + '\n')
    if remain == 0:
        return
    for i in range(0,  len(gStr)):
        if gA[i]:
            gA[i] = 0
            for j in range(0,  len(gStr[i])):
                OutPutDict(file,  str + gStr[i][j],  remain - 1)
            gA[i] = 1





if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Social Engineering dict generator')
        print ('Usage:SEdictgenerator.py [input file] [output file]')
        print ('Example:')
        print ('\tin.txt:\n\tabc\n\t1 2 3')
        print ('\tcommond:SEdictgenerator.py in.txt out.txt')
        print ('\tout.txt:\n\tabc\n\tabc1\n\tabc2\n\tabc3\n\t1\n\t1abc\n\t2\n\t2abc\n\t3\n\t3abc')
        print ('Author:yufan')
        print ('Blog:http://www.cnblogs.com/yufanpi/')
        print ('Email:yufanpi@gmail.com')
        print ('Contact me if finding any bug, thanks.')
        exit(0)
        
    infilepath = sys.argv[1]
    outfilepath = sys.argv[2]
    
    #input
    infile = open(infilepath, 'r')
    pattern = re.compile(r'\S+')
    while True:    
        strLine = infile.readline()
        if len(strLine) == 0:
            break
        gStr.append(pattern.findall(strLine))
    gA = [1 for x in gStr]
    
    #output
    outfile = open(outfilepath, 'w')
    OutPutDict(outfile,  '',  len(gStr))
    outfile.close()

