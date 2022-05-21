class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive (self):
        print("this "+ self.model +" is driven")
    
    
    def sound(self):

       return "vruuuuuuuuuummmmmmmmmmm"   
    


class Corsa(Car):

    def __init__(self):
        super().__init__("chevrolet", "corsa", "2022", "grey")

    def sound(self):
       return super().sound() +"  nheeuuuuuum"    