anime_list = []
while True:
	anime_title = input("Enter the title of an anime (or type 'exit' to finish): ")

	if anime_title.lower() == 'exit':
	 print("You have exited the anime entry program.")
	 break

	anime_list.append(anime_title)
	print(f"'{anime_title}' has been added to your anime list.")

	print("Your anime list:", anime_list)