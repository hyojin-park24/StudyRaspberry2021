# Python파일 오픈 
f = open('./data/readme.txt', mode='r',encoding='utf-8') #text file open
line = f.readline()
while line:
    print(line)
    line = f.readline()

f.close()   # file close