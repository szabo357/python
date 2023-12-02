import colorama

"This is a basic example on how to use colorama"

print(colorama.Fore.BLUE, 
      colorama.Back.WHITE, 
      colorama.Style.BRIGHT, 
      'This is Awesome')
print('Blue and also White')
print('How is this going?')
print(colorama.Style.RESET_ALL)
print('back to normal now')
