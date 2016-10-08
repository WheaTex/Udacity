# IPND Stage 2 Final Project

#these lists below are for the fill-in-the blank functions, questions, and pertinent answers. They are sequenced to one another
blanks = ["__1__","__2__","__3__","__4__"]
questions = ["__1__ prints the working directory.  __2__ lists the files in a directory.  __3__ returns back from a directory.  __4__ adds to a new directory.",
"__1__ makes a directory.  __2__ deletes a directory (directory must be empty).  __3__ removes a file (BEWARE THIS PERMANENTLY DELETES FILES) .  __4__ can create files",
"__1__ finds the occurence of a string starting in a unique position.  __2__ is used to replace a string within a string you can use this function.  __3__ is able to tell you where a string begins.  __4__ allows you to exit a loop."]
answers = [["pwd", "ls", "cd..", "cd /"],["mkdir","rmdir","rm -rf","touch"],[".find()",".replace()",".index()","break"]]
maximum_tries=3
#this code evaluates the users performance during game_play and will congratulate them if they answered all questions with less than 3 tries
def game_results(n_tries):
	if n_tries!=maximum_tries:
		print
		print("CONGRATS! You rocked it!")
	else:
		print
		print("Sorry. Please study and try again.")

#this code prompts the user to choose the level of game_play.  Based on their answer, the user will be given a list of questions and answers that correspond
def level_of_play():
	global questions
	global answers
	difficulty_selection = raw_input("Please enter the level of difficulty of play (easy, medium, hard):")
	if difficulty_selection == "easy":
		answers = answers[0]
		questions = questions[0]
	elif difficulty_selection == "medium":
		answers = answers[1]
		questions = questions[1]
	elif difficulty_selection == "hard":
		answers = answers[2]
		questions = questions[2]
	else:
		print "Sorry, wrong selection. Please come again."

#this game_play function traverses the questions and gives a user three unsuccessful tries to answer the input_questions (list of questions provided to program)
#once the question is successfully answered, the blank is filled with the correct answer and the user moves to the next question		
def game_play(input_questions,input_answers):
	tries = 0
	continue_play = True
	questions = input_questions
	answers=input_answers
	for i in blanks:
		while tries < maximum_tries and continue_play !=False:
			print(questions)
			user_answer = raw_input("What is the answer for blank # " + str(blanks.index(i)+1)+"?")
			if user_answer == answers[blanks.index(i)]:
				questions = questions.replace(blanks[blanks.index(i)],answers[blanks.index(i)])
				break
			elif tries == maximum_tries:
				continue_play = False
				return
			else:
				tries +=1
				print("Sorry, wrong answer. You have " + str(maximum_tries-tries) + " guesses left")
	game_results(tries)
		
level_of_play()
game_play(questions,answers)