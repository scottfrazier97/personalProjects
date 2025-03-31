import os
import shutil
import re

root_folder = r'C:\Users\first.last\Desktop\OuterLayer'

def copy_files_based_on_date(root_folder):    
    # Regex pattern to extract year and month from the filename (handles additional text before the date)    
    date_pattern = re.compile(r"(\d{4})(\d{2})\d{2}")  # Matches YYYYMMDD        
    
    # Get the total number of files in the directory (for progress tracking)    
    total_files = 0    
    for subdir, dirs, files in os.walk(root_folder):        
        if subdir == root_folder:  # Skip the root folder itself            
            continue        
        total_files += len(files)        
        
    # Initialize a counter for processed files    
    processed_files = 0    
        
    # Walk through each folder in the "root_folder"    
    for subdir, dirs, files in os.walk(root_folder):        
        
        # Skip the root directory itself        
        if subdir == root_folder:            
            continue                
        
        # Iterate through each file in the current directory        
        for file_name in files:       

            # Skip directories (shouldn't happen, but just in case)            
            if os.path.isdir(os.path.join(subdir, file_name)):                
                continue            
            
            # Try to match the filename with the regex            
            match = date_pattern.search(file_name)            
            
            if match:                
                # Extract year and month from the matched groups                
                year = match.group(1)                
                month = match.group(2)                
                
                # Construct the target directory path for the year and month                
                year_folder = os.path.join(root_folder, year)                
                month_folder = os.path.join(year_folder, f"{month} {year}")                
                
                # Create the year folder if it doesn't exist                
                if not os.path.exists(year_folder):                    
                    os.makedirs(year_folder)                
                    
                # Create the month folder if it doesn't exist                
                if not os.path.exists(month_folder):                    
                    os.makedirs(month_folder)                
                    
                # Construct the source and destination paths                
                source_file = os.path.join(subdir, file_name)                
                destination_file = os.path.join(month_folder, file_name)                
                
                # Copy the file to the respective folder                
                shutil.copy(source_file, destination_file)                
                processed_files += 1                
                
                # Calculate and display the progress percentage                
                progress = (processed_files / total_files) * 100                
                print(f"Progress: {processed_files}/{total_files} ({progress:.2f}%)")            
            else:                
                print(f"File {file_name} doesn't match the expected format and was skipped.")
                
# Example usage: Specify the root folder containing "More Folders"
copy_files_based_on_date(root_folder)
