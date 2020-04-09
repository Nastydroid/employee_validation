#converting  to emojis
'''def emoji_converter(message):
    words = message.split()
    emojis = {
        ":)": "🙂",
        ":(": "😔"

    }
    output = ""

    for word in words:
        output += emojis.get(word, word) + " "
    return output



message = input('>')

print(emoji_converter(message))'''


#exception example


'''try:
    age =int(input("enter your age:" ))
    income= 20000
    risk= income / age
    print (age)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print('invalid data input')'''


#clases example

'''class point:
    def move(self):
        print("move")

    def draw(self):
        print('draw')


point1 =point()
point1.x=20
print(point1.x)
point2=point()
point2.x=50
print(point2.x)
point2.move()'''


#using constructor

class point:
    def __init__(self,x,y):    #this is constructor use to initialize or create an object
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')

#test

'''class person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'hi how are you doing?, I am {self.name}')
john = person("john smith")
bob =person("bob smith")
bob.talk()
john.talk()'''


#inhertance


'''class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("bark")'''


'''class cat(mammal):
    def be_annoying(self):
        print("annoying")

dog1 =dog()
dog1.walk()
cat1 =cat()
cat1.be_annoying()
dog1.bark()'''
#using a module
import convert

print(convert.lbs_to_kg(140))
