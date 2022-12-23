import data
import sys

def interactiveMode():
	while (True):
		command = input("Enter a command: ")
		interpretCommand(command)
		bank.exportData(data.dataPath)

def interpretCommand(command, input1=0, input2=0):
	if (command == "help"):
		print("Here's a list of the current implemented commands: ")
		print("\tview_log: Prints out the log")
		print("\timport_sheet: Imports an excel sheet given the file path and date")
		print("\tview_data: Prints out the current data")
		print("\tmerge_data: Merges 2 nodes together from a given list")
		print("\tadd_data: Adds a new node given a name, value, and date")
		print("\tremove_data: Removes a node from a given list")
		print("\texit: Exits the script safely")
	elif (command == "view_log"):
		data.printLog()
	elif (command == "import_sheet"):
		filePath = input("Enter path to sheet to input: ")
		fileMonth = input("Enter month: ")
		fileDay = input("Enter day: ")
		fileYear = input("Enter year: ")
		bank.importSheet(data.dateNode(fileMonth, fileDay, fileYear), filePath)
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