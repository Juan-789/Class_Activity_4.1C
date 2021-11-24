"""
3. Write a program that takes from the user a word and prints it horizontally with two spaces between the letters.
"""
wordN = input("What word do you want me to print horizontally, with two spaces in between the letters ")
for i in wordN:
  print(i, end = "  ")
#Separates the letters of the word given by two spaces