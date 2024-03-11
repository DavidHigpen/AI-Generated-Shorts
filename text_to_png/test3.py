text = 'what in the world is going on in this car???'
spaceI = text.find(' ', 10)
prevI = text.rfind(' ', 0, spaceI)
print(text[spaceI + 1:])
print(text[prevI + 1:])