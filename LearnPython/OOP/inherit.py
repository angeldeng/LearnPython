class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initalized SchoolMember:{0})'.format(self.name))

    def tell(self):
        '''Tell my details'''
        print('Name:"{0}" Age:"{1}"'.format(self.name,self.age),end="")
        