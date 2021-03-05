#your code goes here
txt = input()

# Finding longest word
longest = max(txt.split(), key=len)

# Displaying longest word
print(longest)
