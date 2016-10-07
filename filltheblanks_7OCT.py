# IPND Stage 2 Final Project

#these lists below are for the fill-in-the blank functions, questions, and pertinent answers. They are sequenced to one another
blanks = ["__1__","__2__","__3__","__4__"]
questions = ["__1__ prints the working directory.  __2__ lists the files in a directory.  __3__ returns back from a directory.  __4__ adds to a new directory.",
"__1__ makes a directory.  __2__ deletes a directory (directory must be empty).  __3__ removes a file (BEWARE THIS PERMANENTLY DELETES FILES) .  __4__ can create files",
"__1__ finds the occurence of a string starting in a unique position.  __2__ is used to replace a string within a string you can use this function.  __3__ is able to tell you where a string begins.  __4__ allows you to exit a loop."]
answers = [["pwd", "ls", "cd..", "cd /"],["mkdir","rmdir","rm -rf","touch"],[".find()",".replace()",".index()","break"]]

difficulty_selection = raw_input("Please enter the level of difficulty of play (easy, medium, hard):")
#this code evaluates the users performance during game_play and will congratulate them if they answered all questions with less than 3 tries
def game_results(n_tries):
	if n_tries!=3:
		print
		print("CONGRATS! You rocked it!")
	else:
		print
		print("Sorry. Please study and try again.")

#this code traverses the questions and gives a user three unsuccessful tries to answer the input_questions (list of questions provided to program)
#once the question is successfully answered, the blank is filled with the correct answer and the user moves to the next question
def game_play(input_questions):
	tries = 0
	maximum_tries = 3
	continue_play = True
	questions = input_questions
#this for loop is to iterate across the 4 questions
	for i in blanks:
#the while loop is used to provide the user with three attempts in the game
		while tries < maximum_tries and continue_play !=False:
			print(questions)
			user_answer = raw_input("What is the answer for blank # " + str(blanks.index(i)+1)+"?")
#if the user answers the present question correctly it will break from the while loop and continue traversing the questions
			if user_answer == answers[blanks.index(i)]:
				questions = questions.replace(blanks[blanks.index(i)],answers[blanks.index(i)])
				break
#if the user has tried 3 times incorrectly to answer the question then they will be kicked out of game_play and their results are evaluated in game_results to tell them they were unsuccessful
			elif tries == 3:
				continue_play = False
				return
#if they have unsuccesfully tried answering a question <3 times, they remain in the while loop until they hit the limit, as counted by the tries+=1 function
				else:
				tries +=1
				print("Sorry, wrong answer. You have " + str(maximum_tries-tries) + " guesses left")
	game_results(tries)




#this code prompts the user to choose the level of game_play.  Based on their answer, the user will be given a list of questions and answers that correspond
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