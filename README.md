This is just a program that reads excels sheets and compiles the data on them.

The program works by importing excel sheets via commands fed to the program, and records data from marked columns.
The program writes down names in the Name column and values in the Value column, which allows the program to make
data comparisons.

To run the program, type "python bank.py" in the command prompt

Requirements:
- Python
- openpyxl package

Here's a list of the current implemented commands and their respective flags:
- add_data (--add_data): Adds a new node given a name, value, and date
- auto_merge_data (--auto_merge_data): Merges all the data that has the same name
- exit: Exits the script safely
- help (--help): Displays the different commands that can be used
- import_sheet (--import_sheet): Imports an excel sheet given the file path and date
- import_sheets (--import_sheets): Imports multiple excel sheets, labels them based on the date they get assigned
- merge_data (--merge_data): Merges 2 nodes together from a given list
- sort_data (--sort_data): Sorts the data in ascending or descending order
- squash0 (--squash0): Removes all nodes with a value of 0
- remove_data (--remove_data): Removes a node from a given list
- view_data (--view_data): Prints out the current data
- view_log (--view_log): Prints out the log
