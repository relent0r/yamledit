
yamlex = "template.spec.brave"

class yamlinputcon:       
    def convertInput(self, yaml):
        yamlDataSet = yaml.split('.')
        return yamlDataSet

jim = yamlinputcon()
values = jim.convertInput(yamlex)
print(values)