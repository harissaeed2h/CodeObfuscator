import os, ast, hashlib

chars = "abcdefghijklmnopqrstuvwxyz"
chars = "_1234567890"+chars+chars.upper()

filesInCodeDir = os.listdir("code")

def getNames(code):
	tree = ast.parse(code)
	functionNames = []
	variableNames = []
	for element in ast.walk(tree):
		if isinstance(element, ast.FunctionDef):
			functionNames.append(element.name)
		elif isinstance(element, ast.Assign):
			for target in element.targets:
				if isinstance(target, ast.Name):
					variableNames.append(target.id)
	return variableNames, functionNames

def generateCompressedNames(variableNames, functionNames):
	oldNames = variableNames+functionNames
	newNames = {}
	AllNames = []
	noOfVarNames = len(oldNames)
	for name in oldNames:
		newName = hashlib.sha256((name.encode())).hexdigest()
		newNames[name] = newName
	print(newNames)

for file in filesInCodeDir:
	with open("code/"+file) as f:
		fileCode = f.read()
		variableNames, functionNames = getNames(fileCode)
		generateCompressedNames(variableNames, functionNames)



#44e6647ae6923bdc6a27a5aaf48215a25c515525eff29ac86cf4bab35523e54