class CellPhone:
    def __init__(self, number):
        self.number = number
        self.contacts = {}

    def showContacts(self):
        print self.contacts

    def addContact(self, name, number):
        self.contacts[name] = number

    def dial(self, name):
        if name in self.contacts:
            print 'dialling %s' % self.contacts[name]
        else:
            print 'name not found in contacts'


a = CellPhone(12345)
a.showContacts() # prints {}

a.addContact('pce', 989512367)
a.dial('pce') #prints 'dialling 989512367'

a.dial('asok') #prints 'name not found in contacts'

    
