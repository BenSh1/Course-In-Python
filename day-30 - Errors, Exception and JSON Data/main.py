
'''





#FileNotFound
try:
    file = open("a_file.txt")
    a_dicitionary = {"key":"value"}
    print(a_dicitionary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    #print("There was an error")
    file.write("Something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist.")

#if there were no exceptions that were thrown from the block of code try {}, 
# then it's going to jump to the else block
else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")

    raise TypeError("This is a error that I made up.")


'''


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3 :
    raise ValueError("Human height should not be over 3 meters.")


#bmi = weight / (height * height)
bmi = weight / height ** 2

print(bmi)


