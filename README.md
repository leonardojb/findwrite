# findwrite

Introduction
This script searches for all the text files in a specified folder and checks if a specific word is in the last 50 lines of each file. If the specific word is found, it extracts an ID from the file name and writes it to an output file.

Requirements
This script requires Python 3 to run. There are no additional dependencies.

Usage
Clone the repository to your local machine.
Open the script reading.py.
Modify the following variables to match your use case:
folder_path: The path to the folder where the script will search for text files.
output_file: The name and path of the file where the IDs will be written.
specific_word: The specific word to search for in the last 50 lines of each text file.
Run the script by executing python reading.py.
The script will run indefinitely, checking every 10 minutes for files with the specific word in the last 50 lines. When it finds such files, it writes their IDs to the output file.
