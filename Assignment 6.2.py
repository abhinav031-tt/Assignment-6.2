class Dog:
    def function(self,name,age):
        self.name = name    
        self.age  = age

    def get_info(self,coat_color):
        self.coat_color =coat_color        

class jackrusselterrior(Dog):
    def __init__(self,name,age,coat_color,gender,):
        #super()._init__(name,age,coat_color)
           self.gender = gender
        

class Bulldog(Dog):
    def __init__(self,name,age,coat_color,quality):
        #super()._init__(name,age,coat_color)
        
        self.quality = quality

    #def _str_(self):
            #return f"\nname :  {self.name}, \nage : {self.age}, \ncoat_color : {self.coat_color}, \ngender : {self.gender}"
            
dog_obj = Dog()
         
jackrusselterrior_obj = jackrusselterrior(input("Enter a jackrusselterrior_name :- "),int(input("Enter a age :- ")),input("Enter a coat_color :- "),input("Enter a gender :- "),)
Bulldog_obj = Bulldog(input("Enter a bulldog_name :- "),int(input("Enter a age :- ")),input("Enter a coat_color :-, "),input("Enter the Quality:-"))
print()
print()
print("Assignment done")
  