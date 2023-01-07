from tkinter import filedialog
import lib.data as data
import sys

def interactiveMode():
	while (True):
		command = input("Enter a command: ")
		interpretCommand(command)
		bank.exportData(data.dataPath)

def interpretCommand(command, input1=0, input2=0):
	if (command == "help"):
		print("Here's a list of the current implemented commands and their respective flags: ")
		print("- add_data (--add_data): Adds a new node given a name, value, and date")
		print("- auto_merge_data (--auto_merge_data): Merges all the data that has the same name")
		print("- exit: Exits the script safely")
		print("- help (--help): Displays the different commands that can be used")
		print("- import_sheet (--import_sheet): Imports an excel sheet given the file path and date")
		print("- import_sheets (--import_sheets): Imports multiple excel sheets, labels them based on the date they get assigned")
		print("- merge_data (--merge_data): Merges 2 nodes together from a given list")
		print("- remove_data (--remove_data): Removes a node from a given list")
		print("- squash0 (--squash0): Removes all nodes with a value of 0")
		print("- view_data (--view_data): Prints out the current data")
		print("- view_log (--view_log): Prints out the log")
	elif (command == "view_log"):
		data.printLog()
	elif (command == "import_sheet"):
		filePath = filedialog.askopenfilenames()[0]
		fileMonth = input("Enter month: ")
		fileDay = input("Enter day: ")
		fileYear = input("Enter year: ")
		bank.importSheet(data.dateNode(fileMonth, fileDay, fileYear), filePath)
	elif (command == "import_sheets"):
		files = filedialog.askopenfilenames()
		fileMonth = input("Enter month: ")
		fileDay = input("Enter day: ")
		fileYear = input("Enter year: ")
		bank.importSheets(data.dateNode(fileMonth, fileDay, fileYear), files)
	elif (command == "view_data"):
		bank.printData()
	elif (command == "merge_data"):
		showOptions()
		index1 = int(input("Select first person to merge: "))
		if (index1 == len(bank.people) + 1):
			return
		index2 = int(input("Select second person to merge: "))
		if (index2 == len(bank.people) + 1):
			return
		bank.mergeData(index1-1, index2-1)
	elif (command == "auto_merge_data"):
		bank.autoMergeData()
	elif (command == "add_data"):
		name = input("Enter person's name: ")
		value = input("Enter person's value: ")
		month = input("Enter month: ")
		day = input("Enter day: ")
		year = input("Enter year: ")
		bank.addData(name, value, data.dateNode(month, day, year))
	elif (command == "remove_data"):
		showOptions()
		index = int(input("Select a person to remove: "))
		if (index == len(bank.people) + 1):
			return
		bank.removeData(index-1)
	elif (command == "squash0"):
		bank.squash0()
	elif (command == "sort_data"):
		print("How do you want to sort your data?")
		print("1. %s" % data.column1)
		print("2. %s" % data.column2)
		print("3. Date")
		selection1 = int(input("Enter an option: "))

		if (selection1 == 1 or selection1 == 2):
			print("Which order to you want to sort your data?")
			print("1. Ascending (low to high)")
			print("2. Descending (high to low)")
			selection2 = int(input("Enter an option: "))
			if (selection2 == 1):
				bank.sortData(selection1, selection2)
			elif (selection2 == 2):
				bank.sortData(selection1, selection2)
			else:
				print("Invalid option")
		elif (selection1 == 3):
			print("Most recent or least recent?")
			print("1. Most recent to least recent")
			print("2. Least recent to most recent")
			selection2 = int(input("Enter an option: "))
			if (selection2 == 1):
				bank.sortData(selection1, selection2)
			elif (selection2 == 2):
				bank.sortData(selection1, selection2)
			else:
				print("Invalid option")
		else:
			print("Invalid option")
	elif (command == "exit"):
		print("Exiting script...\n")
		sys.exit()
	else:
		print("Invalid command\n")

def showOptions():
	interpretCommand("view_data")
	print("%s. Exit" % (len(bank.people)+1))

def flagHelper(a, i, x, y):
	if (a[i] == x):
		interpretCommand(y)
		bank.exportData(data.dataPath)
		return True

#interpretFlag(a: str[], i: int): void
def interpretFlag(a, i):
	if (i > len(a) - 1):
		return
	verifyFlag = False
	verifyFlag = verifyFlag or flagHelper(a, i, "--view_data", "view_data")
	verifyFlag = verifyFlag or flagHelper(a, i, "--view_log", "view_log")
	verifyFlag = verifyFlag or flagHelper(a, i, "--import_sheet", "import_sheet")
	verifyFlag = verifyFlag or flagHelper(a, i, "--import_sheets", "import_sheets")
	verifyFlag = verifyFlag or flagHelper(a, i, "--add_data", "add_data")
	verifyFlag = verifyFlag or flagHelper(a, i, "--auto_merge_data", "auto_merge_data")
	verifyFlag = verifyFlag or flagHelper(a, i, "--squash0", "squash0")
	verifyFlag = verifyFlag or flagHelper(a, i, "--merge_data", "merge_data")
	verifyFlag = verifyFlag or flagHelper(a, i, "--help", "help")
	verifyFlag = verifyFlag or flagHelper(a, i, "--remove_data", "remove_data")
	if (not verifyFlag):
		print ("Invalid flag: %s" % a[i])
	interpretFlag(a, i+1)


if __name__ == "__main__":
	bank = data.bank()
	bank.importData(data.dataPath)

	if (len(sys.argv) <= 1):
		interactiveMode()
	else:
		interpretFlag(sys.argv, 1)