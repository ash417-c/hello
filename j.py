            
class Email:
    def __init__(self, prio, subject, date):
        '''
        a constructor containing class atributes 
        '''
        pass
        self.prio = prio
        self.subject = subject
        self.date = date

    def __lt__(self, other):
        '''
        overloads the less than operator so it works with the class, uses is_instance to check if other is of the Patient class
        '''
        pass
        prioToNum = {
            "Boss" : 5,
            "Subordinate" : 4,
            "Peer" : 3,
            "ImportantPerson" : 2,
            "OtherPerson" : 1
        }
        if isinstance(other, Email):
            return prioToNum[self.prio] < prioToNum[other.prio]

class Max_heap:
    def __init__(self):
        '''
        a constructor defining the internal list that makes the heap function
        '''
        pass
        self.internal = []
    
    def get_left(self, index):
        return (index*2) +1
    
    def get_right(self, index):
        return (index*2) +2
    
    def get_parent(self, index):
        return (index-1) //2
    
    def get_length(self):
        return len(self.internal)
    
    def get_top(self):
        return self.internal[0] if self.get_length() > 0 else 'No Value\n'
    
    def add(self, val):
        '''
        adds a value to the heap, then upheaps. Uses an internal recursive function
        '''
        pass
        self.internal.append(val)
        def _upheap(index):
            parent = self.get_parent(index)
            if self.internal[parent] < self.internal[index] and index != 0:
                self.internal[index], self.internal[parent] = self.internal[parent], self.internal[index]
                _upheap(parent)
        _upheap(len(self.internal)-1)

    def remove(self):#removes top
        '''
        removes the top value of the heap, then downheaps to correct the heap. Uses an internal recursive function
        '''
        pass
        if self.get_length() > 0:
            self.internal[0], self.internal[-1] = self.internal[-1], self.internal[0]
            self.internal.pop(-1)
            max_index = len(self.internal)-1
            def _downheap(index):
                left_index = self.get_left(index)
                right_index = self.get_right(index)
                if max_index >= left_index and self.internal[index] < self.internal[left_index]:
                    if max_index < right_index:
                        right_index = left_index
                    larger_index = left_index if self.internal[right_index] < self.internal[left_index] else right_index
                    self.internal[index], self.internal[larger_index] = self.internal[larger_index], self.internal[index]
                    _downheap(larger_index)
            _downheap(0)
    
    def print(self): #for testing purposes only
        print(self.internal)


def build_input(filename):
    '''
    builds input as a generator, for easy interation. The interator goes through each line as a list of its elements
    '''
    pass
    with open(filename, 'r') as file:
        file = file.read().splitlines()
        for line in file:
            line = line.split(",")
            if len(line) ==1:
                action = line[0]
            else:
                action = line[0].split()[0]
                line[0] = line[0].split()[1]
            yield action, line

def main():
    emails = Max_heap()
    for action,line in build_input("Assignment1_Test_File.txt"):
        match action:
            case "EMAIL":
                emails.add(Email(line[0],line[1],line[2]))
            case "COUNT":
                print(f"There are {emails.get_length()} emails to read.")
            case "NEXT":
                email = emails.get_top()
                if email != "No Value\n":
                    print(f"Next email:\n\tSender: {email.prio}\n\tSubject: {email.subject}\n\tDate: {email.date}\n")
            case "READ":
                emails.remove()
main()