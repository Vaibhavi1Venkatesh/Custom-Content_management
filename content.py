content = []

def add_content():
    title = input("Enter title: ")
    body = input("Enter content body: ")
    content.append({"title": title, "body": body})
    print("Content added successfully!")

def view_content():
    for i, item in enumerate(content, 1):
        print(f"{i}. {item['title']} - {item['body']}")

def edit_content():
    view_content()
    item_id = int(input("Enter content number to edit: "))
    if 1 <= item_id <= len(content):
        content[item_id - 1]["title"] = input("Enter new title: ")
        content[item_id - 1]["body"] = input("Enter new content body: ")
        print("Content updated!")
    else:
        print("Invalid content number.")

def delete_content():
    view_content()
    item_id = int(input("Enter content number to delete: "))
    if 1 <= item_id <= len(content):
        content.pop(item_id - 1)
        print("Content deleted!")
    else:
        print("Invalid content number.")

def main():
    while True:
        print("\n1. Add Content\n2. View Content\n3. Edit Content\n4. Delete Content\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_content()
        elif choice == '2':
            view_content()
        elif choice == '3':
            edit_content()
        elif choice == '4':
            delete_content()
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

main()