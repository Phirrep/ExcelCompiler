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
		print("Here's a list of the current implemented commands: ")
		print("- add_data: Adds a new node given a name, value, and date")
		print("- auto_merge_data: Merges all the data that has the same name")
		print("- exit: Exits the script safely")
		print("- help: Displays the different commands that can be used")
		print("- import_sheet: Imports an excel sheet given the file path and date")
		print("- import_sheets: Imports multiple excel sheets, labels them based on the date they get assigned")
		print("- merge_data: Merges 2 nodes together from a given list")
		print("- remove_data: Removes a node from a given list")
		print("- squash0: Removes all nodes with a value of 0")
		print("- view_data: Prints out the current data")
		print("- view_log: Prints out the log")
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
	elif (command == "exit"):
		print("Exiting script...\n")
		sys.exit()
	else:
		print("Invalid command\n")

def showOptions():
	interpretCommand("view_data")
	print("%s. Exit" % (len(bank.people)+1))

#interpretFlag(a: str[], i: int): void
def interpretFlag(a, i):
	verifyArgs = True
	if (a[i] == "--view_log"):
		interpretCommand("view_log")

if __name__ == "__main__":
	bank = data.bank()
	bank.importData("logs/data.json")
	if (len(sys.argv) <= 1):
		interactiveMode()
	else:
		interpretFlag(sys.argv, 1)