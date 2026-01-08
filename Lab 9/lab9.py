
import math
import random
import zlib

print('\n')
####  test with LATIN-1

def printEncoding(str):
    aList = []
    for c in str:
        aList.append(c)
    return aList

strLatin1 = bytearray('ÅÄÖ', 'LATIN-1')

#print(printEncoding(strLatin1)) #[197, 196, 214]

#### Test with UTF-8

strUTFTest = bytearray('ABC', 'UTF-8')   # [65, 66, 67]
strUTF = bytearray('ÅÄÖ', 'UTF-8') # [195, 133, 195, 132, 195, 150]

#print(printEncoding(strUTFTest))
#print(printEncoding(strUTF))

eg = 'ABC ÅÄÖ'
t = bytearray(eg, 'UTF-8')

#print('The length of {} is: '.format(eg), len(eg)) #7
#print('The length of {} is: '.format(t), len(t))  #10



###Compression


with open('exempeltext.txt') as f:
    fileEx = f.read()
    
fileBytes = bytearray(fileEx, 'utf-8')


def getFileLength(txt):
    #print('The file has {} number of symbols!'.format(len(txt)))    # 30491 number of symbols!
    #print('The file has {} number of bytes!'.format(len(fileBytes)))    # bytearray length = 30491 There is no difference.

    return len(txt)

charCount = getFileLength(fileBytes)

        
def checkFile(txt):
    i = 0
    for chars in f:
        #if chars == '\n': print(i, 'new line')
        #elif chars == '.': print(i, chars)
        i+=1
    
def fileToDict(text):
    symbolCount = {}
    for i in text:
        if i in symbolCount:
            symbolCount[i] += 1
        else:
            symbolCount[i] = 1
    #print(symbolCount)
    return symbolCount

fileDict = fileToDict(fileBytes)

def makeHisto(aDict):
    for key in aDict.keys():
        aDict[key] = (aDict[key]*256)/charCount
        #print(key, ' %: \t', '*'*int(int(aDict[key])/100))
        pass

makeHisto(fileDict)

def makeProb(histo):
    for key in sorted(histo.keys()):
        histo[key] = histo[key] / charCount
        #print(key, 'probability: \t ', '{:.5f}'.format(histo[key])) # 226 probablity 0.00003 -0.000
        
    return histo

probDict = makeProb(fileDict)


def entropy(prob):
    sum = 0
    for key in prob:
        if float(prob[key]) > 0:
            n = float(prob[key])*math.log2(1/float(prob[key]))
            sum += n
    #print('entropy is  ', sum) #entropy is   0.0964769851776259
    return sum

comp = entropy(probDict)

#print(fileEx)
fBytes = 30491
fBits = fBytes * 8
cBits = fBits / comp
#print('Compressed file has : ', cBits) #2528354.2966324952
#print('Comprssed file byte is : ', fBits) # 243928



theCopy = fileBytes.copy()
copyText = theCopy.decode('utf-8')
copyList = list(copyText)
random.shuffle(copyList) 
fileCopyShuffled = ''.join(copyList)
#print('Shufled symbol length is : ', len(fileCopyShuffled)) #  29091
#print('Shufled bytes length is : ', len(bytearray(fileCopyShuffled, 'utf-8'))) #30491



codeShuffled = zlib.compress(bytearray(fileCopyShuffled, 'utf-8'))

### How long is the zip-code measured in bytes?

zlibShuffledByteArray = len(codeShuffled)     

#print(zlibShuffledByteArray) # 19115

zlibShuffledBits = zlibShuffledByteArray * 8     

#print(zlibShuffledBits) #  153048

#print(len(fileCopyShuffled)) #29091

symbols = 29091

originalBytearry = 30491 * 8    
#print(originalBytearry)     # 243928 bites
zlibBytearry = 19100 * 8             
#print(zlibBytearry)  #  152800

#print(math.log2(152800/29091)) #2.392999748483363

compressed = 5.25
                     
codeCopy = zlib.compress(theCopy)

#print(len(codeCopy)) #12848

zlibByteArray = 12848
zlibBits = 102784
bitPerSymbol = 3.53      

#print(bitPerSymbol)

# 6.82 7.39 & 8.07

#5

t1 = """I hope this lab never ends because it is so incredibly thrilling!"""
t10 = 10*t1

#print(len(t1))      # 75
#print(len(t10))     # 750

first = bytearray(t1, 'utf-8')
second = bytearray(t10, 'utf-8')

firstCode = zlib.compress(first)     
secondCode = zlib.compress(second)           
#print(len(sorted(fileToDict(firstCode))))  # 57

print(len(firstCode)) #66
print(len(secondCode)) #76

#No the zip-code is not ten times longer but 10 more than
#Because the length of the t10 is shortened or compressed  example (AABCCDDDD-->A2B1C2D4)
print('\n')



