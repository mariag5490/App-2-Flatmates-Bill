from fpdf import FPDF

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
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()

        #add title
        pdf.set_font(family='Times',style='B',size=24)
        pdf.cell(w=0,h=80,txt="Flatmates Bill",ln=1,border=0)

        #add period
        pdf.cell(w=100, h=20, txt='Period', border=1, align='L')
        pdf.cell(w=150, h=20, txt=bill.period, border=1, align='L',ln=1)

        #add flatemate1
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=1, align='L')
        pdf.cell(w=200, h=20, txt=str(flatmate1.pays(bill,mary)), border=1, align='L',ln=1)

        # add flatemate2
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=1, align='L')
        pdf.cell(w=200, h=20, txt=str(flatmate2.pays(bill, harry)), border=1, align='L',ln=1 )

        pdf.output(self.filename+'.pdf')



bill = Bill(amount=120, period="March_2021")
harry=Flatmate("Harry",20)
mary=Flatmate("Mary",25)

report=PdfReport(bill.period)
report.generate(harry,mary,bill)