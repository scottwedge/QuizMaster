import csv
RoundOne = open('roundone.csv','rU')
R1reader = csv.reader(RoundOne)
titles = open('title.csv','rU')
TitleFile = csv.reader(titles)
RoundTwo = open('roundtwo.csv','rU')
R2reader = csv.reader(RoundTwo)
RoundThree = open('roundthree.csv','rU')
R3reader = csv.reader(RoundThree)
RoundFour = open('roundfour.csv','rU')
R4reader = csv.reader(RoundFour)
#for row in R4reader:
#	print row

score = 1000
name = ""

def title():
	for row in TitleFile:
		print(row[0])

def introduction():
	print 'Welcome to the QUIZ MASTER!  I am the GAME MASTER!  Unlike other games, the aim in this game is to get your score to zero!  Currently, your score is ' + str(score) + '!\n'
	name = raw_input("So player, what is your name?\n")
	print "Welcome " + name + "!  Let's get started!\n"
	print "You will have five rounds of games, and in each you will have opportunities to lower your points.  By the end of round four you will have had enough opportunity to lose a maximum of 1000 points, and if you have done so, you will move onto the final round!  Good luck!"
	newround(1, name)

def newround(x,name):
	print '*' * 71
	print '*' + (' ' * 69) + '*' 
	print '*' + (' ' * 31) + 'Round ' + str(x) + (' ' * 31) + '*'
	print '*' + (' ' * 69) + '*' 
	print '*' * 71
	if x == 1:
		roundone(name)
	elif x == 2:
		roundtwo(name)
	elif x == 3:
		roundthree(name)
	elif x == 4:
		roundfour(name)

def roundone(name):
	subtract = 0
	total = 0

	print 'Alright ' + name + '.  Time to get started.  This round is going to test your ability to estimate.  I am going to provide you with a number of descriptions.  Such as, the number of eggs you have if you buy a dozen.  Of course, this value is 12.  If you were to guess correctly, for instance, 12, I would take off proportionate number of points.  However, if you were to guess less than this number you would lose less points.  If you were to overestimate, however, you would end up losing no points.  You want to guess close, without going over.\n\n'
	print 'NOTE: Each question is scaled so that if you were to guess a number correctly, you would lose 20 points.  There will be 10 questions, and thus you are able to lose up to 200 points this round.  Good luck ' + name + '!\n\n'
	for row in R1reader:
		print row[2]
		guess = raw_input("So, what is your guess?  Remember, digits only!\n")
		x = 1
		try:
			x = int(guess)
			if int(guess) > int(row[0]):
				print "Woops!  You overestimated!  No losing points for you!  The answer was " + row[0] + "!"
			else:
				subtract = float(guess) * (20/(float(row[0])))
				print 'Congratulations.  The answer was ' + row[0] + ' and for your effort you get to lose ' + str(subtract) + ' points!'
				total = total + subtract
		except:
			print str(guess) + ' is not a number!  You lose 0 points!'
	print 'The round is over!  You managed to lose ' + str(total) + ' points!  Given that you could have lost up to 200 points, you have lost ' + str((total/200)*100) + '% of what you could have lost!'
	newround(2, name)

def roundtwo(name):
	correct = 0
	total = 0
	print 'Okay ' + name + ', in this round you have the opportunity to lose another 200 points!\n'
	print 'I am going to provide two options and you just have to select - THIS OR THAT\n'
	for row in R2reader:
		total += 1
		print 'Which of the following is ' + row[2] + '?\n  1. ' + row[0] + ' or 2. ' + row[1] + '?'
		guess = raw_input("So, what is your guess?  Put in the corresponding digit - 1 or 2, only.\n")
		try:
			int(guess) in [1,2]
			if guess == row[3]:
				print 'Correct!  Congratulations!'
				correct += 1
			else:
				print 'Sorry, that is incorrect.'
		except:
			print "That is not a valid option!  You are getting this one wrong as punishment!"
	num = ((float(correct))/float(total)) * 200
	print 'I asked you ' + str(total) + ' questions and you lose ' + str(correct) + ' of those correct!  Thus, this round you score ' + str(num) + ' points!  That is ' + str(num/2) + '% of what you could have lost!'
	newround(3,name)

def roundthree(name):
	guess = ''
	print 'Time to play Who Am I!\n'
	print 'I am going to choose somebody well-known.  All you have to do is guess who it is.  One-by-one I will give you clues about this persons identity, and the more clues it takes, the less points you lose.  Got it?  Also, you have to spell it correctly!\n\n'
	print 'Okay, let me think of somebody...\n\n\n GOT SOMEBODY!  \n\n\n'
	for row in R3reader:
		print("I am now thinking of somebody!  Let me think of the first clue...")
		print("Okay, my first clue is: " + row[1])
		guess = raw_input("Take your first guess!  Take care with spelling and capitalizations!\n")
		if guess == row[0]:
			print(row[6] + ' ' + name + '.' + '  That is correct!')
		else:
			print("Sorry, that was wrong!  \nOkay, my second clue is: " + row[2])
			guess = raw_input("Take your second guess!  Take care with spelling and capitalizations!\n")
			if guess == row[0]:
				print(row[6] + ' ' + name + '.' + '  That is correct!')
			else:
				print("Sorry, that was wrong!  \nOkay, my third clue is: " + row[3])
				guess = raw_input("Take your third guess!  Take care with spelling and capitalizations!\n")
				if guess == row[0]:
					print(row[6] + ' ' + name + '.' + '  That is correct!')
				else:
					print("Sorry, that was wrong!  \nOkay, my fourth clue is: " + row[4])
					guess = raw_input("Take your third guess!  Take care with spelling and capitalizations!\n")
					if guess == row[0]:
						print(row[6] + ' ' + name + '.' + '  That is correct!')
					else:
						print("Sorry, that was wrong!  \nOkay, my fifth and final clue is: " + row[5])
						guess = raw_input("Take your final guess!  Take care with spelling and capitalizations!\n")
						if guess == row[0]:
							print(row[6] + ' ' + name + '.' + '  That is correct!')
						else:
							print("Bad luck!  The answer was " + row[0] + '!')
	newround(4,name)

def roundfour(name):
	fiftyfifty = 1
	questionskip = 1
	percentage = 1
	print("You have reached the penultimate round " + name + "!  Are you read for some multiple choice questions!  I am feeling generous so I am going to give you three life-lines!  However, once you use them, they are gone.")
	for row in R4reader:
		print("Question: " + row[0])
		guess = raw_input("A. " + row[1] + "\nB. " + row[2] + "\nC. " + row[3] + "\nD. " + row[4] + "\nPlease type A, B, C, D, 50, %, or SKIP now.\n")
		if guess == row[5]:
			print "CORRECT!  Congratulations.  Time for the next question..."
		elif guess == "SKIP":
			if questionskip == 1:
				print("You have used your question skip.  Using this life-line again will automatically result in a question pass.  Time for the next question!")
				questionskip = 0
			else:
				print("You have used this life-line already!  You automatically forfeit this question.  Time for the next question...")
		elif guess == str(50):
			if fiftyfifty == 1:
				fiftyfifty = 0
				print("You have used your fifty-fifty.  If you use this again this result in an automatic forfeit of the question.")
				print("Question: " + row[0])
				if row[6] == row[1]:
					print ("A. " + row[6])
				if row[7] == row[2]:
					print ("B. " + row[7])
				if row[8] == row[3]:
					print ("C. " + row[8])
				if row[9] == row[4]:
					print ("D. " + row[9])
				guess = raw_input("Please type A, B, C, or D now.\n")
				if guess == row[5]:
					print "CORRECT!  Congratulations.  Time for the next question..."
				else:
					print "WRONG!  Time for your next question."
			else:
				print("You have used this life-line already!  You automatically forfeit this question.  Time for the next question...")
		elif guess == "%":
			if percentage == 1:
				percentage = 0
				print("A: " + row[10])
				print("B: " + row[11])
				print("C: " + row[12])
				print("D: " + row[13])
				print("Question: " + row[0])
				guess = raw_input("Please type A, B, C, or D now.\n")
				if guess == row[5]:
					print "CORRECT!  Congratulations.  Time for the next question..."
				else:
					print("WRONG!  Time for your next question...")
			else:
				print "You've already used this life-line.  What a waste!"
		else:
			print "WRONG!"




#roundfour("Samuel")
title()
introduction()
