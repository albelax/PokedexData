#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

def calculateMax(_list, _index):
    maxLen = 0
    for t_str in _list:
        tmp_list = str.split(t_str,';') 
        if len(tmp_list[_index]) > maxLen:
            maxLen = len(tmp_list[_index])
    return maxLen

def fileToList(_namefile):
    f = open(_namefile, "r");
    fileList = []
    for line in f:
        fileList.append(line)
    f.close()
    return fileList

def addPadding(_string, _targetLen):
    if len(_string) < _targetLen:
        _string += (_targetLen - len(_string)) * ' '
    return _string


def formatList(_list):
    ret = []
    for i in _list:
        tmp_list = str.split(i,';')
        tmp_list[1] = addPadding(tmp_list[1], calculateMax(_list,1))
        tmp_list[2] = addPadding(tmp_list[2], calculateMax(_list,2))
        ret.append(tmp_list)
    return ret
    
lista = fileToList("pokemonDB.txt")
#print calculateMax(fileToDoubleList("pokemonDB.txt"),1)
lista = formatList(lista)

def MaxLenLists(_list):
    maxLen = 0
    for t_list in lista:
        lenSum = 0
        for i in t_list:
            lenSum += len(i)
        if lenSum > maxLen:
            maxLen = lenSum
    return maxLen
        

def pareggiaListe(_list):
    maxLen = MaxLenLists(_list)
    #retList = []
    for t_list in lista:
        lenSum = 0
        for i in t_list:
            lenSum += len(i)
        if lenSum <= maxLen:
            t_list[-1] = (maxLen - lenSum)* ' ' + '|'
    return _list
        

lista =  pareggiaListe(lista)
#for i in lista:
#   print i

f = open("pokemonDB.txt", "w");
for t_list in lista:
    for i in range(len(t_list)):
        f.write(t_list[i])
        if (i < len(t_list)-1):
            f.write(';')
    f.write('\n')


f.close()

#print(MaxLenLists(lista))