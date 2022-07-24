import random      

print("\n\n\t\t\t\tWELCOME TO KBC GAME\n\n")

global ans, q, price, b, h, a, c, d, g   #global delaration

price, b, h, c, d, a, q, g = 0, 0, 0, 0, 0, 0, 1, 0

l2 = ['A', 'B', 'C', 'D']    #list of all possible answers.

player = list()

#A block for all the questions and answers.
def questions() :

	global ans
	print()

	if (q == 1):
		print("Q1. The country with the most pyramids in the world is ______\n")   #Question
		
		if (a == 0) :
			print("A. Egypt\nB. Libya\nC. Sudan\nD.Mexico")   #Normal Options
		else :
			print("A. Egypt\nB. \nC. Sudan\nD. ")    #If 50-50 choosen
		ans = 'C'    #Answer to the question

	if(q ==2) :
		print("Q2. Which is the largest coffee producing state of India?\n")
		if (a == 0) :
			print("A. Kerala\nB. Tamil Nadu\nC. Karnataka\nD. Arunachal Pradesh")
		else :
			print("A. \nB. Tamil Nadu\nC. Karnataka\nD. ")
		ans = 'C'

	if (q == 3):
		print("Q3. Which is the hottest planet in the solar system?\n")
		if (a == 0) :
			print("A. Earth\nB. Venus\nC. Mars\nD. Jupiter")
		else :
			print("A. \nB. Venus\nC. \nD. Jupiter")	
		ans = 'B'

	if (q ==4) :
		print("Q4. The most stolen book from public libraries in the US is ______\n")
		if (a == 0) :	
			print("A. Bible\nB. Guinness World Record\nC. Lord Of Rings\nD. Harry Potter")
		else :
			print("A. Bible\nB. Guinness World Record\nC. \nD.")
		ans = 'B'

	if (q ==5) :
		print("Q5. One People, One State, One leader” was/is the policy of which leader?\n")
		if (a == 0) :
			print("A. Stalin\nB. Hitler\nC. Sardar Vallabhbhai Patel\nD. Mussolin")
		else :
			print("A. \nB. Hitler\nC. Sardar Vallabhbhai Patel\nD. ")
		ans = 'B'

	if (q == 6) :
		print("Q6. What is the name of the river that flows from capital of India?\n")
		if (a == 0) :
			print("A. Ganges\nB. Indus\nC. Yamuna\nD. Narmada")
		else :
			print("A. Ganges\nB. \nC. Yamuna\nD. ")
		ans = 'C'

	if (q == 7) :
		print("Q7. Which is the largest fresh water lake in the world?\n")
		if (a == 0) :
			print("A. Great Bear Lake\nB. Great Slave Lake\nC. Lake Superior\nD. Erie Lake")
		else :
			print("A. Great Bear Lake\nB. Great Slave Lake\nC. Lake Superior\nD. ")
		ans = 'C'

	if (q == 8) :
		print("Q8. Who built the Jama Masjid?\n")
		if (a == 0) :
			print("A. Jahangir\nB. Akbar\nC. Imam Bukhari\nD. Shah Jahan")
		else :
			print("A. \nB. Akbar\nC. \nD. Shah Jahan")
		ans = 'D'

	if (q == 9) :
		print("Q9. Who was the first Indian in space?\n")
		if (a == 0) :	
			print("A. Rakesh Sharma\nB. Ravish Malhotra\nC. Kalpana Chawla\nD. Vikram Ambalal")
		else :
			print("A. Rakesh Sharma\nB. \nC. Kalpana Chawla\nD. ")
		ans = 'A'


def pricee() :
	global h, price

	if (h >= 2) :
		print("YOU WON")
		print("Final Won Price:-", (price - 200))
	else :
		print("YOU WON")
		print("Final Won Price:-", price)


for x in range(3) :   #Getting the names of all players.
	player.append(input("Enter Name Of Players:  "))


for x in range (3) :      #Range limit is showing the number of players.

	y = random.choice(player)     #Choosing any player randomly.
	print("\n" + y, "is the Player Now")

#Here the game begins...
	for x in range(8) :
		questions()    #One question at a time.
		
		if (h < 2) :    #Only print until two LifeLine used.
			print("\nWant to use LifeLine? (Y/N)")
		
		choice = input("\nEnter your Answer :  ")

		if (choice.upper() == ans) :     #Block for correct answer
			a = 0
			print("\nWoohoo!! Right Answer.")
			price = price + 200
			print("You won Rs.200")
			print("\n\n")
		
		elif (choice.upper() != ans and (choice.upper() in l2)) :   #Block for Wrong Answer
			a = 0
			print("Wrong Answer.\nYOU LOOSE\nGAME OVER!!")
			print("Total Won Price:-", price)
			g = 1
			break

		elif (choice.upper() == 'Y') :   #Block if wanna use LifeLine
			a = 0
			if (h < 2) :         #Checking whether two LineLine used or not
				
				print("\nLifeLine 1. 50-50")
				print("LifeLine 2. Change the Question")
				
				try :
					choice2 = int(input("\nEnter Your Choice:-"))
				except :
					print("\nOhoo!! Please try Again...")
					h = h - 1
					continue
				
				if (choice2 == 1) :    #Block for 50-50
					if (c == 0) :
						h = h + 1
						a = 1
						c = c + 1
						continue
					else :
						print("You can use this LifeLine only once during the game.")
						continue
				elif (choice2 == 2) :       #Block for Flip the question
					if (d == 0) :
						h = h + 1
						q = q + 1
						d = d + 1
						b = b + 1
						continue
					else :
						print("\nYou can use this LifeLine only once during the game.")
						continue

			else : #Block if user try to use LifeLine more than 2 times.
				print("\nOops!! You can only use 2 LifeLine in a game\n")
				continue
					
		else :   #Block if the user press any button in between by mistake
			a = 0
			print("\nOhoo!! Please Try Again...\n\n")
			b = b + 1
			continue
			
		q = q + 1     #Next question please


	for i in range(b) :         #Block same as above but for if user by mistake press any wrong key in between or flip the question
		questions()
		
		if (h < 2) :
			print("\nWant to use LifeLine? (Y/N)")
		
		choice = input("\nEnter your Answer :  ")

		if (choice.upper() == ans) :
			a = 0
			print("\nWoohoo!! Right Answer.")
			price = price + 200
			print("You won Rs.200")
			print("\n\n")
		
		elif (choice.upper() != ans and (choice.upper() in l2)) :
			a = 0
			print("Wrong Answer.\nYOU LOOSE\nGAME OVER!!") 
			print("Total Won Price:-", price)
			g = 1
			break

		elif (choice.upper() == 'Y') :
			a = 0
			if (h < 2) :
				
				print("\nLifeLine 1. 50-50")
				print("LifeLine 2. Change the Question")
				
				try :
					choice2 = int(input("\nEnter Your Choice:-"))
				except :
					print("\nOhoo!! Please try Again...")
					h = h - 1
					continue
				
				if (choice2 == 1) :
					if (c == 0) :
						h = h + 1
						a = 1
						c = c + 1
						continue
					else :
						print("\nYou can use this LifeLine only once during the game.")
						continue
				if (choice2 == 2) :
					if (d == 0) :
						h = h + 1
						q = q + 1
						d = d + 1
						b = b + 1
						continue
					else :
						print("You can use this LifeLine only once during the game.")
						continue
			
			else :
				print("\nOops!! You can only use 2 LifeLine in a game\n")
				continue
					
		else :
			a = 0
			print("\nOhoo!! Please Try Again...\n\n")
			b = b + 1
			continue
			
		q = q + 1
	if (g == 0) :
		pricee()

	player.remove(y)

	a, b, c, d, h, price, q, g = 0, 0, 0, 0, 0, 0, 1, 0
