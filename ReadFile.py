def read_and_modify_file():
    filename = input("Enter the name of the file you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Creating a new filename for the modified version
        new_filename = "modified_" + filename

        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")

# Run the function
read_and_modify_file()
