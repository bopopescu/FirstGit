import pygal

from .models import Fruit

class FruitPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'amount of fruits'

    def get_data(self):


    #    ''''query the database for chart data, pack them into  a dictionary and return it'''
        data = {}
        for fruit in Fruit.objets.all():
            data[fruit.name] = fruit.amt
        return data

    def generate(self):
        #get chart data
        chart_data = self.get_data()
        #add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        #return the rendered SVG

        return elf.chart.render(is_unicode= True)
        
