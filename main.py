#Maru Puran
#October 23, 2023
#Analyze and investigate a program to get a better understanding of the syntax of if statements and how they're put to use in a program where the user guesses a number

# Example Code

number = 5 #set a created variable, number, equal to 5
print("I have thought of a number between 1 and 10") #print the following message, that the computer has a number between 1 and 10
guess = int(input("Can you guess what it is?")) #creates a variable guess in order to store an integer the user inputs, asks the user to guess the number between 1 and 10

if guess == number: #checks if the number guessed is equal to the number variable, 5
  print("Correct!") #if condition is true then print "correct" to let the user know
if guess < number: #checks if the number guessed by the user is less than the number variable, 5
  print("Too Low!") #if condition is true then let the user know they guessed too low
if guess > number: #checks if the number guessed by the usesr is more than the number variable, 5
  print("Too High!") #if condition is true then let the user know they guessed too high

# What happens if you input the guess '2'?
  # Answer: The message "too low" is printed if the user inputs the guess "2".

# What happens if you input the guess '6'?
  # Answer: The message "too high" is printed if the user inputs the guess "6".

# What happens if you input the guess '5'?
  # Answer: The message "correct" is printed if the user inputs the guess "5".

# What happens if you input the guess '-5'?
  # Answer: The message "too low" is printed if the user inputs the guess "-5".

# What happens if you input the guess '0'?
  # Answer:  The message "too low" is printed if the user inputs the guess "0".

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer: They mean less than and greater than, respectively. On line 9 it's used to tell if the guess is less than the number, on line 11 it's used to tell if the guess is greater than the number.

# What happens if you change line 5 to if guess = number: ?
  # Answer: There is a syntax error; to check if two things are equal you have to use "==" because the single "=" is used for assignment.

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer: They're indented beneath their respective if statements. If it's not indented then it will say there's an indentation error. 


