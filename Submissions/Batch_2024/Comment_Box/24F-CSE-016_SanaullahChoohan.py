comments = []

print("=== Welcome to the Comment Box ===")

while True:
    print("\nOptions:")
    print("1. Add a comment")
    print("2. View all comments")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        comment = input("Enter your comment: ")
        comments.append(comment)
        print("✅ Comment added successfully.")
    elif choice == "2":
        print("\n--- All Comments ---")
        if comments:
            for i, c in enumerate(comments, 1):
                print(f"{i}. {c}")
        else:
            print("No comments yet.")
    elif choice == "3":
        print("Exiting Comment Box. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
