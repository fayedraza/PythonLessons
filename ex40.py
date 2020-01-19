class Snake:
    name = "Python"
   
    def change_name(self,new_name):
        self.name = new_name


def change2(s):
    print(s)

change2(90)    

dog = Snake("hi")
print(dog.name)
