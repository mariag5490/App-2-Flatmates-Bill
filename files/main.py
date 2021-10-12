

class Bill:
    """
    Object Bill contains amount and period as attributes
    """
    def __init__(self,amount,period):
        self.amount=amount
        self.period=period

class Flatmate:
    """
    Person who lives in the flat
    """
    def __init__(self,name,days_in_house):
        self.name=name
        self.days_in_house=days_in_house

    def pays(self,bill,f2):
        weight= self.days_in_house/(self.days_in_house+f2.days_in_house)
        return weight*bill.amount


class PdfReport:
    """
    Creates pdf file with the name and share of the inmates in the flat
    """
    def __init__(self,filename):
        self.filename=filename

    def generate(self,flatmate1,flatmate2,bill):
        pass
bill = Bill(amount=120, period="March 2021")
harry=Flatmate("Harry",20)
mary=Flatmate("Mary",25)
print (harry.pays(bill,mary))
print(mary.pays(bill,harry))