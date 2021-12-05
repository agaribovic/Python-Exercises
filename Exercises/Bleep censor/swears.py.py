# Replace with the actual swears and add as many as needed to the list.
swears = ["swear1", "swear2", "swear3", "swear4", "swear5"]

input = input("Enter something: ").split(' ')

output = ""

for word in input:
    if word in swears:
        for letter in word:
            word = len(word) * "*"
    output += word + " " 

print(output)

