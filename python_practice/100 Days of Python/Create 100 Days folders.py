import os 

base_name = "fake_file_path"

day_counter = 0

while day_counter < 100:

    day_counter += 1
    new_folder = f"{base_name}Day {day_counter}"

    try:
        os.mkdir(new_folder) # Creates a single directory
        print(f"Folder '{new_folder}' created successfully.")
    except FileExistsError:
        print(f"Folder '{new_folder}' already exists.")
    except OSError as e:
        print(f"Error creating folder: {e}")