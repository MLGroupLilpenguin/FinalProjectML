class Customer:
    def __init__(self,ID=None,CustomerID=None,Segment=None,Country = None,City = None,State = None,PostalCode=None,Region =None,Email=None,Password=None,IsDeleted=None):
        self.ID=ID
        self.CustomerID=CustomerID
        self.Segment=Segment
        self.Country = Country
        self.City = City
        self.State = State
        self.PostalCode = PostalCode
        self.Region = Region
        self.Email=Email
        self.Password=Password
        self.IsDeleted=IsDeleted
    def __str__(self):
        info="{}\t{}\t{}\t{}\t{}\t{}".format(self.ID,self.CustomerID,self.Segment,self.Country,self.City
                                             ,self.State,self.PostalCode,self.Region,self.Email,self.Password)
        return info
