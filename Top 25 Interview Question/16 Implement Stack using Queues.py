import queue
'''
it can be done using two queues, one operation either pop or push will be costly
'''


class Stack: # lets make pop costly
    def __init__(self):
        self.queuest1 = queue.Queue()
        self.queuest2 = queue.Queue()

    def push(self, n):
        self.queuest1.put(n)

    def pop(self):
        if self.empty():
            return None
        
        el = None
        while True:
            el = self.queuest1.get()
            if self.empty():
                break
            self.queuest2.put(el)

        self.queuest1, self.queuest2 = self.queuest2, self.queuest1

        return el
    
    def empty(self):
        return self.queuest1.empty()


st = Stack()

st.push(1)
st.push(2)
st.push(3)
st.push(4)

for i in range(2):
    print(st.pop(), end=" ")
# 4 3

st.push(5)
st.push(6)

print("\n", st.empty())

for i in range(5):
    print(st.pop(), end=" ")
# 6 5 2 1 -1

print("\n", st.empty())
