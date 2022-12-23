import data
import sys

def interactiveMode():
	while (True):
		command = input("Enter a command: ")
		interpretCommand(command)
		bank.exportData(data.dataPath)

def interpretCommand(command, input1=0, input2=0):
	if (command == "help"):
		#TODO implement later
		print()
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
	elif (command == "add_data"):
		name = input("Enter person's name: ")
		value = input("Enter person's value: ")
		month = input("Enter month: ")
		day = input("Enter day: ")
		year = input("Enter year: ")
		bank.addData(name, value, data.dateNode(month, day, year))
	elif (command == "exit"):
		print("Exiting script...\n")
		sys.exit()
	else:
		print("Invalid command\n")

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