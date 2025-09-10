print("Welcome to the Manga Recommender! ")
print("Answer a few questions to find your next read.")
genre = input("What genre do you like? (action, romance): ")
length = input("How long should the manga be? (short, medium, long): ")
decade = input("Which decade? (2010s, 2020s): ")

if genre == "action":
	if length == "short" and decade == "2010s":
	 print("Recommendation: Samurai Girls")
	elif length == "short" and decade == "2020s":
	 print("Recommendation: Tower of God")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation: Katanagatari")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation: Decadence")
	elif length == "long" and decade == "2010s":
	 print("Recommendation: Hakuoki")
	elif length == "long" and decade == "2020s":
	 print("Recommendation: Jujutsu Kaisen")
	else:
	 print("Sorry, no action manga matches your selection.")

elif genre == "romance":
	if length == "short" and decade == "2010s":
	 print("Recommendation: Kimi ni Todoke")
	elif length == "short" and decade == "2020s":
	 print("Recommendation: Kubo Won't Let Me Be Invisible")
	elif length == "medium" and decade == "2010s":
	 print("Recommendation: Maid Sama!")
	elif length == "medium" and decade == "2020s":
	 print("Recommendation: My Dress-Up Darling")
	elif length == "long" and decade == "2010s":
	 print("Recommendation: Angel Beats!")
	elif length == "long" and decade == "2020s":
	 print("Recommendation: The Quintessential Quintuplets")
	else:
	 print("Sorry, no romance manga matches your selection.")

else:
	print("Invalid genre. Please choose from 'action', or 'romance'.")





