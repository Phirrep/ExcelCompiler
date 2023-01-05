This is just a program that reads excels sheets and compiles the data on them.

The program works by importing excel sheets via commands fed to the program, and records data from marked columns.
The program writes down names in the Name column and values in the Value column, which allows the program to make
data comparisons.

Here's a list of the current implemented commands:
- add_data: Adds a new node given a name, value, and date
- exit: Exits the script safely
- help: Displays the different commands that can be used
- import_sheet: Imports an excel sheet given the file path and date
- import_sheets: Imports multiple excel sheets, labels them based on the date they get assigned
- merge_data: Merges 2 nodes together from a given list
- remove_data: Removes a node from a given list
- view_data: Prints out the current data
- view_log: Prints out the log
