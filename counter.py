
class Counter:
    pass

c = Counter()
c.show() # prints 0.
c.increment()
c.show() # prints 1
c.decrement() 
c.show() # prints 0
print c # prints 'Counter: 0' (implement the __str__ method)
c = Counter(10) # __init__ should accept an argument
c.show() # prints 10


