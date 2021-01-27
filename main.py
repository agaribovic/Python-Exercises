import os

filename = input("Please enter the file name: ")

def doesFileExists(filePathAndName):
   return os.path.exists(filePathAndName)

if doesFileExists(filename + '.txt'):
   print("Please choose one of the following options: ")
   print("A) Read the file")
   print("B) Delete the file and start over")
   print("C) Append the file")
   print("D) Replace a single line")
   chooseOption = input()
   if chooseOption.lower() == "a":
      f = open(filename + '.txt', "r")
      print("Text inside the file:", f.read())
   elif chooseOption.lower() == "b":
      os.remove(filename + '.txt')
      print("The file has been deleted. Please run the program again.")
   elif chooseOption.lower() == "c":
      f = open(filename + ".txt", "r")
      print("Text inside the file:", f.read())
      enterText = input("Please enter the text to append to the file: ")
      f = open(filename + ".txt", "a")
      f.write(enterText)
      f = open(filename + ".txt", "r")
      print("The file contains the following text now:", f.read())
      f.close()
   elif chooseOption.lower() == "d":
      f = open(filename + '.txt', "r")
      data = f.read()
      print("The file containts the following text:", data)
      word1 = input("Please enter the word to be replaced: ")
      if word1 not in data:
         print("The entered word does not exist in the file. Please run the program again.")
      else:
         word2 = input("Please enter the word to replace with: ")
         data = data.replace(word1, word2)
         f.close()
         f = open(filename + '.txt', "w")
         f.write(data)
         print("The file contains the following text now:", data)
         f.close()
else:
   enterText = input("The file does not exist. Please enter the text for the new file to be created: ")
   f = open(filename + ".txt", "a")
   f.write(enterText)
   f = open(filename + ".txt", "r")
   print("The new file has been created with the following content:", f.read())
   f.close()


