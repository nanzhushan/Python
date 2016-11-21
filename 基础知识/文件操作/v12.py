#coding:utf8
poem='''\Programming is funWhen the work is doneif you wanna make your work also fun: use Python!'''
f=file('c:\\cc.txt','w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file
f=file('c:\\cc.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    else:
        print line


