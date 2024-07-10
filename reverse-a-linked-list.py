class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next  = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


llist = Linkedlist()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

print('Dada a lista vinculada')
llist.printlist()
llist.reverse()
print('\nLista vinculada reversa')
llist.printlist()