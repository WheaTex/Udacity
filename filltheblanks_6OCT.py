# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!
blanks = ["__1__","__2__","__3__","__4__"]
questions = ["__1__ prints the working directory.  __2__ lists the files in a directory.  __3__ returns back from a directory.  __4__ adds to a new directory.",
"__1__ makes a directory.  __2__ deletes a directory (directory must be empty).  __3__ removes a file (BEWARE THIS PERMANENTLY DELETES FILES) .  __4__ can create files",
"__1__ finds the occurence of a string starting in a unique position.  __2__ is used to replace a string within a string you can use this function.  __3__ is able to tell you where a string begins.  __4__ allows you to exit a loop."]
answers = [["pwd", "ls", "cd..", "cd /"],["mkdir","rmdir","rm -rf","touch"],[".find()",".replace()",".index()","break"]]

difficulty_selection = raw_input("Please enter the level of difficulty of play (easy, medium, hard):")

def game_play(input_questions):
	tries = 0
	maximum_tries = 3
	continue_play = True
	questions = input_questions
	for i in blanks:
		while tries < maximum_tries and continue_play !=False:
			print(questions)
			user_answer = raw_input("What is the answer for blank # " + str(blanks.index(i)+1)+"?")
			if user_answer == answers[blanks.index(i)]:
				questions = questions.replace(blanks[blanks.index(i)],answers[blanks.index(i)])
				break
			elif tries == 3:
				continue_play = False
				return
			else:
				tries +=1
				print("Sorry, wrong answer. You have " + str(maximum_tries-tries) + " guesses left")
	if tries!=3:
		print
		print("CONGRATS! You rocked it!")
	else:
		print
		print("Sorry. Please study and try again.")




if difficulty_selection == "easy":
	answers = answers[0]
	questions = questions[0]
	game_play(questions)
elif difficulty_selection == "medium":
	answers = answers[1]
	questions = questions[1]
	game_play(questions)
elif difficulty_selection == "hard":
	answers = answers[2]
	questions = questions[2]
	game_play(questions)
else:
	print "Sorry, wrong selection. Please come again."
	
def game_play(input_questions):
	tries = 0
	maximum_tries = 3
	continue_play = True
	questions = input_questions
	for i in blanks:
		print("in the for loop")
		while tries < maximum_tries and continue_play !=False:
			print(questions)
			user_answer = raw_input("What is the answer for blank # " + str(blanks.index(i)+1)+"?")
			print("in the while loop")
			if user_answer == answers[blanks.index(i)]:
				questions = questions.replace(blanks[blanks.index(i)],answers[blanks.index(i)])
				break
			elif tries == 3:
				continue_play = False
				return
			else:
				tries +=1
				print("Sorry, wrong answer. You have " + str(maximum_tries-tries) + " guesses left")
	if tries!=3:
		print
		print("CONGRATS! You rocked it!")
	else:
		print
		print("Sorry. Please study and try again.")