class Animal:
    def __init__(self, name, species, age, color, hp = 100): 
        self.__name = name
        self.__species = species
        self.__age = age
        self.__color = color
        self.__hp = hp

    def printname(self):
        print("Hello, I am", self.__name)

    def talk(self):
        print("Hey there!")

    def species(self):
        print (f"I am a", {self.__species}, "type of animal!")
        
    def age(self):
        print (f'Today i turn, {self.__age} years old')
        
    def color(self):
        print (f'I can camoflauge in areas that are dark since my color is, {self.__color}')
    


    def battle(self):
        self.__hp -=1
        print ("ROAR")
        print (f'You have {self.__hp}, hp left in the tank (-1 hp)')

    def rest(self):
        print ("HUFF")
        print (f'You have {self.__hp}, hp left in the tank (+1 hp)')
    
    
    
        


    

