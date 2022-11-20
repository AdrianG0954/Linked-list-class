
class Node:
    #Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
    
    #this method returns the data stored at the node
    def __repr__(self):
        return f"Node({self.data})"
    

class LinkedList:

    #Constructor of a singly linked list
    def __init__(self):
        self.head = None
    
    #this method checks to see if the linked list is empty
    def empty_check(self) -> bool:
        return self.head == None
    
    #this method returns the size of the linked list
    def size(self) -> int:
        count = 0
        current_node = self.head  

        while current_node:
            count += 1
            current_node = current_node.next

        return count

    #this function adds a new node to the linked list
    def add(self,data) -> None:
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    #this method takes a value and returns the node in the linked list
    def search(self, value) -> Node:
        current = self.head
        while current:
            if current.data == value:
                return current.data
            else:
                current = current.next
        return None
    
    #this method inserts the value of the node at the given index
    def insert(self,value,index):
        if index == 0: 
            self.add(value)
            return

        if index > self.size():
            raise Exception("Index out of range")
        
        new = Node(value)
        current = self.head
        position = index

        while position > 1:
            current = current.next
            position -= 1
        
        new.next = current.next
        current.next = new

    #this method removes the node at the given value
    def remove(self,value) -> None:
        if self.head == None:
            return None
            
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return None
            else:
                prev = current
                current = current.next


    #this method clears the linked list        
    def clear(self):
        self.head = None
    
    #this works when you print the linked list and what it does is it represents the linked list as a string
    def __repr__(self):
        current = self.head
        nodes = []

        while current:
            nodes.append(f'{current.data}')
            current = current.next

        return " -> ".join(nodes)





#DO NOT CHANGE THESE FUNCTIONS
def size_test()-> int:
    print("\nSIZE TESTS\n")

    score = 0
    ll_sizeTest = LinkedList()

    for i in range(5):
        ll_sizeTest.add(i)

    if ll_sizeTest.size() == 5:
        print("Passed size test 1")
        score += 1
    else:
        print("Failed size test 1")

    print("\nACTUAL SIZE: 5")
    print(f"RESULT SIZE: {ll_sizeTest.size()}\n")
    

    ll_sizeTest2 = LinkedList()
    if ll_sizeTest2.size() == 0:
        print("Passed size test 2")
        score += 1
    else:
        print("Failed size test 2")

    print("\nACTUAL SIZE: 0")
    print(f"RESULT SIZE: {ll_sizeTest2.size()}\n")

    return score
    
def empty_check() -> int:
    print("\nEMPTY CHECK TESTS\n")

    score = 0
    ll_emptyTest = LinkedList()

    if ll_emptyTest.empty_check() == True:
        print("Passed empty check test 1")
        score += 1

    else:
        print("Failed empty check test 1")

    print("\nACTUAL: True")
    print(f"RESULT: {ll_emptyTest.empty_check()}\n")
    
    ll_emptyTest2 = LinkedList()
    ll_emptyTest2.add(1)
    if ll_emptyTest2.empty_check() == False:
        print("Passed empty check test 2")
        score += 1
    else:
        print("Failed empty check test 2")

    print("\nACTUAL: False")
    print(f"RESULT: {ll_emptyTest2.empty_check()}\n")

    return score

def add_test() -> int:
    print("\nADD TESTS\n")

    score = 0
    ll_addTest = LinkedList()
    ll_addTest.add(1)

    if ll_addTest.head.data == 1:
        print("Passed add test 1")
        score += 1
    else:
        print("Failed add test 1")
    
    print("\nACTUAL: 1")
    print(f"RESULT: {ll_addTest}\n")
    
    ll_addTest2 = LinkedList()
    ll_addTest2.add(1)
    ll_addTest2.add(2)
    if ll_addTest2.head.data == 2:
        print("Passed add test 2")
        score += 1
    else:
        print("Failed add test 2")

    ll_addTest3 = LinkedList()
    for i in range(10,-1,-1):
        ll_addTest3.add(i)
    
    print("\nANSWER: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")
    print(f"RESULT: {ll_addTest3}\n")
    return score

def clear_test() -> int:
    print("\nCLEAR TESTS\n")

    score = 0
    #creates linked list
    linked_list = LinkedList()
    for i in range(10,-1,-1):
        linked_list.add(i)


    #clear test 
    linked_list.clear()
    if linked_list.empty_check():
        print("Passed clear test")
        score += 1
    else:
        print("Failed clear test")

    print("\nBEFORE CLEAR: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")
    print(f"AFTER CLEAR: {linked_list}\n")

    return score

def search_test() -> int:
    #creates linked list
    score = 0
    linked_list = LinkedList()
    for i in range(10,-1,-1):
        linked_list.add(i)

    #search test 1
    if linked_list.search(5) == 5:
        print("Passed search test 1")
        score += 1
    else:
        print("Failed search test 1")

    print("\nNode to find: 5")
    print(f"list given to search {linked_list}:")
    print(f"Node found: {linked_list.search(5)}\n")

    #search test 2
    if linked_list.search(10) == 10:
        print("Passed search test 2")
        score += 1
    else:
        print("Failed search test 2")

    print("\nNode to find: 10")
    print(f"list given to search {linked_list}:")
    print(f"Node found: {linked_list.search(10)}\n")

    #search test 3
    if linked_list.search(11) == None:
        print("Passed search test 3")
        score += 1
    else:
        print("Failed search test 3")

    print("\nNode to find: 11")
    print(f"list given to search {linked_list}:")
    print(f"Node found: {linked_list.search(11)}\n")

    return score

def insert_test() -> int:
    print("\nINSERT TEST\n")

    score = 0
    #creates linked list
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add(i)

    #insert test
    linked_list.insert(100,0)

    if linked_list.search(100) == 100:
        print("Passed insert test 1")
        score += 1
    else:
        print("Failed insert test 1")

    print("ANSWER 1: 100 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0")
    print(f"RESULT 1: {linked_list}\n")

    linked_list.insert(200,5)

    if linked_list.search(200) == 200:
        print("Passed insert test 2")
        score += 1
    else:
        print("Failed insert test 2")

    print("ANSWER 2: 100 -> 9 -> 8 -> 7 -> 6 -> 200 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0")
    print(f"RESULT 2: {linked_list}\n")

    linked_list.insert(300,10)

    if linked_list.search(300) == 300:
        print("Passed insert test 3")
        score += 1
    else:
        print("Failed insert test 3")

    print("ANSWER 3: 100 -> 9 -> 8 -> 7 -> 6 -> 200 -> 5 -> 4 -> 3 -> 2 -> 300 -> 1 -> 0")
    print(f"RESULT 3: {linked_list}\n")

    return score

def remove_test() -> int:
    print("\nREMOVE TEST\n")

    score = 0
    #creates linked list
    linked_list = LinkedList()
    linked_list2 = LinkedList()
    for i in range(10,-1,-1):
        linked_list.add(i)
        linked_list2.add(i)


    #remove test
    linked_list.remove(0)
    if linked_list.search(0) == None:
        print("Passed remove test 1")
        score += 1
    else:
        print("Failed remove test 1")

    print("\nBEFORE REMOVE 1: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")
    print(f"AFTER REMOVE 1:  {linked_list}\n")

    linked_list2.remove(0)

    linked_list.remove(5)
    if linked_list.search(5) == None:
        print("Passed remove test 2")
        score += 1
    else:
        print("Failed remove test 2")

    print("\nBEFORE REMOVE 2: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")
    print(f"AFTER REMOVE 2:  {linked_list}\n")

    linked_list2.remove(9)

    linked_list.remove(9)
    if linked_list.search(9) == None:
        print("Passed remove test 3")
        score += 1
    else:
        print("Failed remove test 3")
    
    print("\nBEFORE REMOVE 3: 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10")
    print(f"AFTER REMOVE 3:  {linked_list}\n")

    return score


#this is the main function
#DO NOT MODIFY THIS 
if __name__ == "__main__":
    score = 0

    #Uncomment the tests as you complete them 
    #Order does not matter
    #some tests depend on others

    #clear test
    #score += clear_test()

    #tests empty check
    # score += empty_check()
    
    #tests size
    # score += size_test()
    
    #test add
    # score += add_test()

    #test search
    # score += search_test()

    #test insert
    # score += insert_test()

    #test remove
    # score += remove_test()


    
    print(f"{int(score * 6.25)} / 100")

    exit()

    


        

    

