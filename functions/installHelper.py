from functions.helpers import botPrint
from functions.cli import showArt


def modelList():
  models = ['llama-7b', 'WizardCoder-Python-7B-V1.0']

  return models

def writeOnEnv(keyAndValue):
  with open(".env", "w") as f:
      f.write(keyAndValue)
      f.write(keyAndValue)

def availibleModels():
  i = 0
  for model in modelList():
    i += 1
    print (f"[{(i)}] {(model)}")


def modelSelect(modelName):
  while True:
    availibleModels()
    data = int(input(f"Model for {(modelName)}: "))
    if len(modelList()) < data: # Invalid option
        print(botPrint("\nInvalid model, try again\n", 'Red'))
        continue
    else:
        # Set env
        print("\n")
        break
