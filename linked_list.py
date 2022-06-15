from xml.dom.minidom import Element


class Node:
    
    def __init__(self,element,prev,next):
        self.element = element
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def insertNewElement(self,e,predesessor,successor):
        newest = self.Node(e,predesessor,successor)
        predesessor.next = newest
        successor.prev = newest
        size += 1
        return newest
        
        
     
        
        