from Contact import Contact

class PhoneBook:

    def __init__(self):
        """
        The phonebook keeps track of all contacts. This class is an example of 
        interacting with other classes a coder will make. 

        Instance variables provided for this constructor.
        """
        self.contacts = []
    
    def addContact(self, c):
        """
        Given a contact, determine if you are given a dictionary or an instance of 
        a Contact class. Handle the adding to our phone book appropriately and update the counter.

        If you are given a dictionary, assume that a dictionary has the following keys 
        (and the values are in the correct format):
        - name
        - number
        - email
        - birthday

        NOTE: Why do we have to manually update the counter?
        """
        if isinstance(c, dict):
            self.contacts.append(Contact(c['name'], c['number'], c['email'], c['birthday']))
        elif isinstance(c, Contact):
            self.contacts.append(c)
        else:
            raise TypeError("You must pass a dictionary or a Contact object")

    def getContactCount(self):
        """
        Returns the number of contacts stored in the 
        """
        return len(self.contacts)
    
    def findContact(self, lName):
        """
        Given a last name, find the contact(s) and return the contact information. 

        Will be a list. 
        """
        namelist = []
        for contact in self.contacts:
            if contact.last == lName:
                namelist.append(contact)
        return namelist


    def groupChat(self, message):
        """
        Send a message to every contact in the phonebook
        """
        for contact in self.contacts:
            contact.sendText(message)

    def __str__(self):
        """
        Returns a string representation of the phonebook class. 

        The output will be
        > Phone Book: #

        Where # is the number of contacts in the phonebook. 
        """
        return "Phone Book: " + str(self.getContactCount())