# Creating a node.
class Node:
    #Constructor.
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A linked List class with a single head node.
class LinkedList:
    def __init__(self):
        self.head = None

    #Insertion Method.
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    #Print out the linked list
    def printLL(self):
        current = self.head
        print("The List items are: \n")
        while(current):
            print(current.data)
            current = current.next

#S LL with insertion and Print out.
LinkedL = LinkedList()
name1 = input("Enter the name to the list: \n")
LinkedL.insert(name1)
#LinkedL.insert(3)
#LinkedL.insert(4)
#LinkedL.insert(5)
#LinkedL.insert(6)
name2 = input("Enter the name to the list: \n")
LinkedL.insert(name2)
name3 = input("Enter the name to the list: \n")
LinkedL.insert(name3)
name4 = input("Enter the name to the list: \n")
LinkedL.insert(name4)
#Printing out the list.
LinkedL.printLL()


