import csv, sys

'''
    Converts a CSV to JSON Array 
    Usage: python jsonify.py {filename} {json_key}[O]
'''

debugging = False

fileName = sys.argv[1]

if len(sys.argv) == 2:
    JSON_KEY = fileName.split(".")[0]
else:
    JSON_KEY = sys.argv[2]
    
if debugging:
    fileName = "Intent - Sheet1.csv"
    JSON_KEY = fileName.split(".")[0]
    
f = open(fileName , 'r')


# returns the first row of csv as a list
# the returned list is used as the keys of the json
def getKeys(fileName):
    with open(fileName , "r") as f:
        return [ i.strip() for i in f.readline().split(",")]



# generates a json array as string using the csv represented by fileName
def genJson(fileName):
    keys = getKeys(fileName)
    jsonStr = "["
    with open(fileName , "r") as f:
        c = csv.reader(f)
        valuesList = list(c)[1:]
        
        for i in range(len(valuesList)):
            j = "{"
            values = valuesList[i]
            for k in range(len(keys)):
                j += '"{0}" : "{1}" ,'.format(keys[k] , values[k])
            j = j[:-1] + "}"
            jsonStr += j + ","
        jsonStr = '"{0}" : {1}] '.format( JSON_KEY,  jsonStr[:-1])
        jsonStr = "{ " + jsonStr + "}"
        return jsonStr



print(genJson(fileName))





