from pyscript import display, document

class Classmate:
    def __init__(self, name, section, fav_sub):
        # attributes . . .
        self.name = name
        self.section = section
        self.fav_sub = fav_sub

    def introduce(self): # creating a method
        return f'Hi, I am {self.name} from {self.section}. My favorite subject is {self.fav_sub}'


# intantiating an object
classmate1 = Classmate('Ivy', 'Topaz', 'English')
classmate2 = Classmate('AJ', 'Topaz', 'Science')
classmate3 = Classmate('Harmony', 'Topaz', 'Social Studies')
classmate4 = Classmate('JR', 'Topaz', 'Math')
classmate5 = Classmate('Khloe', 'Topaz', 'Science')

Classmates = [classmate1, classmate2, classmate3, classmate4, classmate5]

def Listclassmates(e):
    document.getElementById('output1').innerHTML = ''
    document.getElementById('notification1').innerHTML = ''
    
    for i in Classmates:
        display(i.introduce(), target='output1')

def ClassmateInfo(e):
    document.getElementById('notification1').innerHTML = ''
    display(f'Your data has been added, please re-click the show list button.', target='notification1')
    
    document.getElementById('output1').innerHTML = ''
    username = document.getElementById('input1').value
    usersection = document.getElementById('input2').value
    userfavsub = document.getElementById('input3').value

    classmate6 = Classmate(username, usersection, userfavsub)

    Classmates.append(classmate6)