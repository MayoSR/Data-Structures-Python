class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None


    def insertAtHead(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insertAtTail(self,data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node

    def insertAtN(self,pos,data):
        temp = self.head
        prev = None
        cnt = 1
        if(pos == 1):
            self.insertAtHead(data)
            return
        while(temp != None):
            cnt += 1
            prev = temp
            temp = temp.next
            if(cnt == pos):
                prev.next = Node(data)
                prev.next.next = temp

    def deleteAtHead(self):
        self.head = self.head.next
    
    def deleteAtTail(self):
        temp = self.head
        prev = None
        while(temp.next != None):
            prev = temp
            temp = temp.next

        prev.next = None

    def deleteAtN(self,pos):
        cnt = 1
        temp = self.head
        prev = None
        if(pos == 1):
            self.deleteAtHead()
            return
        while(temp != None):
            
            if(cnt == pos):
                break
            prev = temp
            temp = temp.next
            cnt += 1
        
        prev.next = temp.next

    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def printer(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.insertAtHead(30)
ll.insertAtHead(20)
ll.insertAtHead(10)
ll.insertAtTail(40)
ll.insertAtTail(60)
ll.insertAtN(5,50)
ll.deleteAtN(1)
ll.deleteAtHead()
ll.deleteAtTail()
ll.reverse()
ll.printer()