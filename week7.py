#Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.

file=input("Enter your file name:")
counter = 0
 
with open(file, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter=="e"):
                    counter=counter+1
print("Count of the letter 'e': ", counter)
