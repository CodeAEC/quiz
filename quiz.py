# "user_points" is the user guesses a question 10 points withh be added in this variable
# "correct_answers" this variable will be executes in the end to tell the user the Correct answers he/she gived
# "incorrect_answer" this variable will be executed at the end to tell the user the inccorect answers he/she gived  
user_points = 0
correct_answers = ""
incorrect_answers = ""

print(" /----------------------\ ")
print("| Created by: Error Code |")
print(" \----------------------/")

print("")
print("-------- History Quiz --------")
print("")


# first Question!
print("1. Who started World War 2? (10 points)")

print("")

print("a. Adolf Hitler")
print("b. Pablo Escobar")
print("c. Vladimir Putin")

print("")

# Taking User Input
user = input("Type your answer a, b or c: ")

# If user guess the correct answer, 10 points will be added in the "user_points" variable 
# and "question_answerd" variable is for telling the users the correct answers he gived
if user == "a" or user == "A":
	user_points += 10
	correct_answers += "1. Adolf hitler (Correct)"
elif user == "b" or user == "B":
	incorrect_answers += "1. Pablo Escobar (incorrect) "
elif user == "c" or user == "C":
	incorrect_answers += "1. Vladimir Putin (incorrect) "

print("")


print("==========================================")


# Second Question
print("2. Who invented Apple Iphone? (10 points)")

print("")

print("a. Elon Musk")
print("b. Steve Jobs")
print("c. Jeff Bezos")

print("")

# Taking users input
user = input("Type your answer a, b or c: ")

# If user guess the correct answer, 10 points will be added in the "user_points" variable 
# and "question_answerd" variable is for telling the users the correct answers he gived
if user == "b" or user == "B":
	user_points += 10
	correct_answers += ", 2. Steve Jobs (Correct)"
elif user == "a" or user == "A":
	incorrect_answers += "| 2. Elon Musk (incorrect)"
elif user == "c" or user == "C":
	incorrect_answers += "| 2. Jezz Bezos (incorrect)"

print("")

print("==========================================")

print("")

# Third Question
print("3. What was Pablos Escobar group called? (10 points)")

print("")

print("a. Cartel Medellin")
print("b. Los Pepes")
print("c. Nazi")

print("")

# taking users input
user = input("Type your answer a, b or c: ")

# If user guess the correct answer, 10 points will be added in the "user_points" variable 
# and "question_answerd" variable is for telling the users the correct answers he gived
if user == "a" or user == "A":
	user_points += 10
	correct_answers += ", 3. Medellin Cartel (Correct)"
elif user == "b" or user == "B":
	incorrect_answers += "| 3. Los Pepes (incorrect)"
elif user == "c" or user == "C":
    incorrect_answers += "| 3. Nazi (incorrect)"

print("")

print("-----------Final Resoult-----------")

# Telling the user his score
print(f'You got {user_points}  points! ')

# if user didn't get any questions right it will print "You didn't answer any questions correct!" 
# but if the user guesses some questions correct it will print them
if correct_answers == "":
	print("You didn't answer any questions correct!")
else:
	print(f'Correct answers: {correct_answers}')


# if user doesn't guess any question wrong it will print "You didn't answer any questions worng!"
# if user incorrents any question it will print the question he guessed wrong
if incorrect_answers == "":
	print("You didn't answer any questions worng!")
else:
	print(f'incorrect answers: {incorrect_answers}')


print("")

input("How was the experince? :")
