import jsonDataAsPythonValue

def writeToJSONFile(path, filename, data):
    filePathNameWExt = " ./" + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

path = "./"
fileName = 'example.json'

data = {}
data['test'] = 'test'

writeToJSONFile(path, fileName, data)
