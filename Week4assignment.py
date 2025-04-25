from os import path


def read_modify_write(filename_new, filename_orig):
    try:
        # Open the original file for reading
        with open(filename_orig, 'r') as file:
            lines = file.readlines()

        # Modify the content (prepend "Modified: " to each line)
        modified_lines = ['Modified: ' + line.strip() for line in lines]

        # Open the new file for writing
        with open(filename_new, 'w') as file:
            file.writelines(modified_lines)

        print(f"File {filename_new} created with modified content.")

    except IOError as e:
        print(f"Error: {e}. Ensure {filename_orig} exists and is readable.")

    except Exception as e:
        print(f"Unexpected error: {e}. Check the file path and permissions.")

def ask_for_file_and_handle_errors():
    while True:
        try:
            filename_orig = input("Please enter the filename to read (without path): ")
            filename_new = input("Please enter the filename to write (without path): ")


            filename_orig = f"{filename_orig}"
            filename_new = f"{filename_new}"

            # Check if the original file exists before attempting to read it
            if not path.exists(filename_orig):
                print(f"Error: File {filename_orig} does not exist.")
                continue

            read_modify_write(filename_new, filename_orig)
            break

        except FileNotFoundError:
            print(f"Error: File {filename_orig} does not exist. Please check the file name.")
            continue

        except PermissionError:
            print(f"Error: You do not have permission to read the file {filename_orig}.")
            continue

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue


ask_for_file_and_handle_errors()