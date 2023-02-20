import os
import time

folder_path = ""
output_file = ""
specific_word = ""

while True:
    # Find all txt files in the folder
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    # Loop over each txt file and check if the specific word is in the last 50 lines
    id_list = []
    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), 'r') as f:
            lines = f.readlines()[-50:]
            if specific_word in ''.join(lines):
                # Extract id from file name
                id = txt_file.split('_')[1]
                id_list.append(id)
                
    # Sort id_list in ascending order
    id_list = sorted(id_list)

    # Write id list to output file
    if id_list:
        with open(output_file, "w") as out:
            out.write("\n".join(id_list))

    # Print success message after first loop
    if not id_list:
        print("No files with specific word found in last 50 lines")
    else:
        print("Files with specific word found and written to output file")
    
    # Wait 10 minutes before checking again
    time.sleep(600)