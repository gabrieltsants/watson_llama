from functions.helpers import botPrint
from functions.installHelper import *
from functions.cli import showArt

print('Under development!')
exit()

def main():

  showArt()
  print(botPrint("WatsonLlama installation wizard \n", 'Yellow'))

  modelSelect('questions')
  modelSelect('commands')
  modelSelect('interactive mode')


if __name__ == "__main__":
    main()
