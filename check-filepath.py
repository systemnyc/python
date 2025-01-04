# This program looks files and counts them.
import os

isPath = False
# Check if a path exist
# Function does not return values
# Functions prints if the file path is valid
# Note check_path v2 will store file path in varible for use
def check_path(path):
	_path = path # assigned parameter path to local _path
	isPath = os.path.exists(path) # check if the path exist. This returns a boolean value
	if isPath == True:
		 print(f'The file path {_path} exists') 
	elif isPath == False:
		 print(f'The file path {_path} does not exist')

path_to_check = str(input('Enter path: ')) # Prompts for the pathname and stores it in the varible 'check_path'
check_path(path_to_check)


		

	
