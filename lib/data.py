from openpyxl import load_workbook
import os
import json
import datetime
import re

logPath = "logs/log.txt"
dataPath = "logs/data.json"

#Negative value = profit
#Positive value = buy in
def dateNode(month, day, year):
	date = {}
	date["month"] = int(month)
	date["day"] = int(day)
	date["year"] = int(year)
	return date
def getDate(date):
	return "%s/%s/%s" % (date["month"], date["day"], date["year"])

def personNode(name, value, date):
	person = {}
	person["name"] = name
	person["value"] = int(value)
	person["date"] = date
	return person


def getStr(person):
	personStr = "%s %s {} %s" % (person["name"], abs(person["value"]), getDate(person["date"]))
	return personStr.format("profit") if (person["value"] < 0) else personStr.format("buy in")

class bank:
	def __init__(self):
		self.people = []
	#pushNode(person: personNode): void
	def pushNode(self, person):
		writeLog("\tImporting %s...\n" % getStr(person))
		self.people.append(person)
	#squah(person: personNode): void
	def squash(self, person):
		try:
			writeLog("\tSquashing node: %s\n" % getStr(person))
			self.people.pop(self.search(person))
		except Exception as e:
			writeLog("\tError in squashing node: %s\n" % e)
	#merge(node1: personNode, node2: personNode): personNode
	#Returns new node with merged data
	def merge(self, node1, node2):
		try:
			name = node1["name"]
			if (node1["name"] != node2["name"]):
				print ("WARNING! Names do NOT match: %s and %s" % (node1["name"], node2["name"]))
				if (not getConfirmation()):
					return
				print("1. %s" % node1["name"])
				print("2. %s" % node2["name"])
				print("3. Exit")
				choice = input("Choose new name (default is %s): " % node1["name"])
				if (int(choice) == 3):
					return
				name = node2["name"] if int(choice) == 2 else node1["name"]
			writeLog("Merging node %s and %s...\n" % (getStr(node1), getStr(node2)))
			writeLog("\tCreating new node...\n")
			newNode = personNode(name, node1["value"]+node2["value"], getRecentDate(node1["date"], node2["date"]))
			writeLog("\tNew node created: %s\n" % getStr(newNode))
			self.squash(node1)
			self.squash(node2)
			self.pushNode(newNode)
		except Exception as e:
			writeLog("\tError in merging nodes: %s\n" % e)
	#search(node: personNode): int
	#Method searches peopleNode[] for the node and returns its index
	def search(self, node):
		match = lambda x: (x["name"] == node["name"]) and (x["date"] == node["date"]) and (x["value"] == node["value"])
		for i in range(len(self.people)):
			if (match(self.people[i])):
				return i
	#importSheet(date: date, filePath: str): void
	def importSheet(self, date, filePath):
		try:
			writeLog("Importing data from %s (%s)\n" % (getDate(date), filePath))
			wb = load_workbook(filename = filePath, data_only=True)
			sheet = wb["Sheet1"]
			valueColumn = 0
			for i in range(26):
				if (type(sheet["%s1" % chr(i+97)].value) != type("str")):
					continue
				elif (sheet["%s1" % chr(i+97)].value.lower() == "value"):
					valueColumn = chr(i+97)
					break
			if (valueColumn == 0):
				raise Exception("No Value column found\n")
			if (sheet["a1"].value.lower() != "name"):
				raise Exception("Name column isn't column A\n")
			i = 2
			currName = ""
			currValue = 0
			while (type(sheet["a%s" % i].value) == type("str")):
				currName = sheet["a%s" % i].value
				currValue = sheet["%s%s" % (valueColumn, i)].value
				person = personNode(currName, currValue, date)
				self.pushNode(person)
				i = i+1
			writeLog("\tImport sucessful! Exporting data to data.json\n")
		except Exception as e:
			writeLog("\tError loading in the workbook: %s\n" % e)
	def importSheets(self, date, files):
		for file in files:
			self.importSheet(date, file)

	#Imports data from json file into self.people
	def importData(self, filePath):
		with open(filePath, "r") as f:
			self.people = json.load(f)
	#Exports data from self.people to json file
	def exportData(self, filePath):
		with open(filePath, "w") as f:
			json.dump(self.people, f)
	#Adds data node given inputs
	def addData(self, name, value, date):
		person = personNode(name, value, date)
		writeLog("Adding new data...\n")
		self.pushNode(person)
	def removeData(self, number):
		try:
			person = self.people[int(number)]
			writeLog("Removing data %s...\n" % getStr(person))
			if (person["value"] != 0):
				print ("\tWARNING! Node is not 0")
				if (not getConfirmation()):
					return
			self.squash(person)
		except Exception as e:
			writeLog("\tError in removing data: %s\n" % e)
	def mergeData(self, n1, n2):
		self.merge(self.people[int(n1)], self.people[int(n2)])
	def printData(self):
		print("Current data:")
		print(self)
	def __str__(self):
		i = 1
		returnStr = ""
		for person in self.people:
			returnStr += ("%s. %s\n" % (i, getStr(person)))
			i = i+1
		return returnStr

#getRecentDate(date1: date, date2: date): date
def getRecentDate(date1, date2):
	if (date1["year"] != date2["year"]):
		return date1 if (date1["year"] > date2["year"]) else date2
	elif (date1["month"] != date2["month"]):
		return date1 if (date1["month"] > date2["month"]) else date2
	elif (date1["day"] != date2["day"]):
		return date1 if (date1["day"] > date2["day"]) else date2
	else:
		#Both dates are the exact same
		return date1

#logData(filePath: str, message: str): void
def writeLog(message):
	print(message.replace("\n", ""))
	with open(logPath, "a") as f:
		f.write("%s> %s" % (datetime.datetime.now(), message))

#viewLog(filePath: str): void
def printLog():
	with open(logPath, "r") as f:
		print(f.read())

def getConfirmation():
	answer = input("\tAre you sure? Y/N: ")
	if (answer.lower() == "y"):
		return True
	else:
		return False