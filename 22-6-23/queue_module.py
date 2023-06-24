#stack implementation using inbuilt module
from queue import Queue
s=Queue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.empty())