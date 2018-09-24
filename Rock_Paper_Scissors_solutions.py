from random import choice

pool = ['rock', 'scissors', 'paper']

def rock_paper_scissors_comparator(your_choice):
	# get input from player
	your_choice = input("please show your choice! rock, paper, or scissors! Or enter 'quit' to end the games!\n")
	win = 0
	tie = 0
	lose = 0
	#another player is NPC
	flag = choice(pool)
	
	while True:
		# infinite loop, signal to quit
		if your_choice == "quit":
			print("You have win" + str(win) "games, " + "lost" + str(lose) " games", " and tie " + str(tie) "games")
			break
		else:
			# rock decision
			if your_choice == 'rock':
				if flag == 'paper':
					lose +=1
					print "Pity! Hope you do better next time!\n"
				elif flag == 'scissors':
					win += 1
					print "Wonderful! You win this round!\n"
				else:
					tie += 1
					print "Oops! You tied with me! Let's continue!\n"
			# scissors decision
			elif your_choice == 'scissors':
				if flag == 'paper':
					win +=1
					print "Wonderful! You win this round!\n"
				elif flag == 'scissors':
					tie += 1
					print "Oops! You tied with me! Let's continue!\n"
				else:
					lose += 1
					print "Pity! Hope you do better next time!\n"
			# paper decision
			elif your_choice == 'paper':
				if flag == 'scissors':
					lose +=1
					print "Pity! Hope you do better next time!\n"
				elif flag == 'rock':
					win += 1
					print "Wonderful! You win this round!\n"
				else:
					tie += 1
					print "Oops! You tied with me! Let's continue!\n"
			else:
				print "You have entered a wrong choice!\n"
		your_choice = input("please show your choice! rock, paper, or scissors! Or enter 'quit' to end the games!\n")
		flag = choice(pool)


