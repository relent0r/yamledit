from pathlib import Path
from ruamel.yaml import YAML

inputFile = "E:\\Python\\yamledit\\example.yaml"
inputImageName = '"MineCraftModified"'
inputMLAName = "mcmoded"

# Use pathlib to load the external yaml file. Easier than open method.
yamlFile = Path(inputFile)
yaml = YAML()
dataSet = yaml.load(yamlFile)

#set the yaml properties
dataSet['spec'] ['template'] ['spec'] ['containers'] [0]['name'] = inputImageName
dataSet['metadata'] ['labels'] ['app'] = inputMLAName

#log changes to stdout
print("\n","Image Name: ", inputImageName, "\n","Spec Metadata Label App: ", inputMLAName)

#write changes to file
yaml.dump(dataSet, yamlFile)
