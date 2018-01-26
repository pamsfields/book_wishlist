class Book:

    ''' Represents one book in a user's list of books'''
    '''need to import datetime'''

    NO_ID = -1

    def __init__(self,title, author, read=False, read_date='',rating = '', id=NO_ID):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.read_date = read_date
        self.id = id
        self.rating = rating



    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            import datetime
            read_str = 'yes'
            today = datetime.datetime.now()
            read_date = str(today.month)+'/'+ str(today.day)+'/'+str(today.year)

        id_str = self.id
        if id == -1:
            id_str = '(no id)'


        template = 'id: {} Title: {} Author: {} Read: {} ReadDate: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, self.read_date,self.rating)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.read_date == other.read_date and self.rating == other.rating
