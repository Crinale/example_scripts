#Item Class gives discription of the items
class Item:
    def __init__(self, name, amount, url):
        self.name = name 
        self.amount = amount 
        self.url = url 

#Inventory Class Gives functions on what to do for the inventory
class Inventory:
	#initalize my dictionary
    def __init__(self):
        self.items = {}        
    #be able to add entries to dictionary and put key in a list    
    def add_item(self, name, amnt, url):
    #    self.items[item] = [item,amnt,url]
        self.items[name] = Item(name,amnt,url)

    def change_name(self, name, newname):
    	self.items[name].name = newname
    
    def change_amount(self, name, amnt):	
    	self.items[name].amount = amnt
    
    def change_url(self, name, url):
    	self.items[name].url = url
        #
    #print All items
    def print_items(self):
        print(" Name, Amt, Url ")
        for key, value in self.items.items():
        	print(value.name, value.amount, value.url)
        #print(self.items["j"])

#Implement Remove Item / Edit Item    
    def remove_item(self, name): 
   		self.items.pop(name)

def main():
	print("Pick a choice")
	print("1: Add an item")
	print("2: Edit Item")
	print("3: Print all items")
	print("4: Remove Item")
	print("5: Exit")
	x = input()		#Work on if user put in wrong input or wrong command

#	"case statement"	
	if x == 1:
		print("You picked 1")
		print("What is the Item")
		l = raw_input()
		print("How many is there")
		m = input()
		print("What is the URL (So we can order more)")
		n = raw_input()
		inventory.add_item(l,m,n)
		return main()

	elif x == 2:
		print("you picked 2")
		print("What is the name of the item?")
		name = raw_input()

		print("Do you want to change the name of the item?")
		a = raw_input("Yes/No: ")
		if a == "yes":
			print("What is the new name?")
			newname = raw_input()
			inventory.change_name(name,newname)

		print("Do you want to change the amount of the item?")
		b = raw_input("Yes/No: ")
		if b == "yes":
			print("How many are there now?")
			amount = input()
			inventory.change_amount(name,amount)

		print("Do you want to change the URL of the item?")
		c = raw_input("Yes/No: ")
		if c == "yes":
			print("What is the new URL now?")
			web = raw_input()
			inventory.change_url(name,web)
		return main()

	elif x == 3:
		print("you picked 3")
		inventory.print_items()
		return main()
	
	elif x == 4:
		print("you picked 4")
		print("What is the name of the item?")
		name = raw_input()
		inventory.remove_item(name)
		return main()
	elif x == 5:
		print("Exited")
		return

	else:
		print("Error")
		return main()

	

if __name__ == "__main__":
	keys = []
	inventory = Inventory()
	#test cases
	inventory.add_item("usb cable",22,"hello.com")
	inventory.add_item("hdmi adapter",5,"free.com")
	#
	main()


#Test cases to get inventory classes working

