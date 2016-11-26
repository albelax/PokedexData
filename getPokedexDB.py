#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import urllib2

address = 'http://pokemondb.net/pokedex/all'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

num = 0;
names = []
finalDB = [] 
req = urllib2.Request(address,headers = hdr)
page = urllib2.urlopen(req)
p = 0

def cleanString(_string):
    ASCIIchar =''
    for i in range(len(_string)):
        if not str.isalnum(_string[i]):
            ASCIIchar = _string[i]
            break
    ret = str.split(_string, ASCIIchar)
    return ret


for i in page:
    #print '-----------------' + i
    lista = str.split(i, '>')
    #print '-----------------' + str(lista)
    for j in range(len(lista)):
        # take name from the string and starts a new pokemon
        if "ent-name" in lista[j]:
            if lista[j+1] not in names:
                cleanupList = cleanString(lista[j+1])
                #print '-----------' + str(cleanupList)
                names.append(lista[j+1])
                num += 1
                retList = []
                retList.append(num)
                retList.append(cleanupList[0])
                finalDB.append(retList)
                #print str(num) + '-----------' + lista[j+1]
        # adds the type of the pokemon
        if 'href="/type/' in lista[j]:
            cleanupList = cleanString(lista[j+1])
            #print cleanString(lista[j+1])
            #finalDB[num-1].append(retList)
            if num > 0:
                # adds only one type by making sure the list has less than 3 elements
                if cleanupList[0] not in finalDB[num-1] and len(finalDB[num-1]) < 3:
                    finalDB[num-1].append(cleanupList[0])
        # adds the stats of the pokemon
        if '<td class="num"' in lista[j] or 'class="num-total"' in lista[j]:
            if len(finalDB[num-1]) < 10:
                cleanupList = cleanString(lista[j+1])
                finalDB[num-1].append(cleanupList[0])
            #print str(num) + '----' + lista[j+1]



dst = open("pokemonDB.txt",'a')
for i in finalDB:
    #if i[0] == 150:
    #print i
    for j in range(len(i)):
        if (j == 0):
            if (int(i[j]) < 10):
                i[j] = '00'+str(i[j])
            elif (int(i[j]) < 100):
                i[j] = '0'+str(i[j])
        dst.write(str(i[j]))
        dst.write(";")
    dst.write('\n')
dst.close();


