import colors as c
from utils import ask

def yes():
    print('You are correct!!!')

def no():
    print('''I'm sorry, that is incorrect.''')

intro = c.cyan + "Welcome to the Eragon/Inheritance quiz."

def q1():
    a1 = ask("What is the word 'fire' in the ancient language?")
    if a1 == 'brisingr':
       yes()
       return True
    else:
        no()
        return False 

def q2():
    a2 = ask("What are the Razac's flying mounts called?")
    if a2 == 'letherblaka':
        yes()
        return True
    else:
        no()
        return False

def q3():
    a3 =  ask("What is the name of the group of magicians that work for the Varden?")
    if a3 == 'the wandering path':
        yes()
        return True
    else:
        no()
        return False

def q4():
    a4 = ask("What reward was offered for Eragon's capture?")
    if 'earldom' in a4:
        yes()
        return True
    else:
        no()
        return False

questions = [q1,q2,q3,q4]
