import colors as c
from utils import ask

def yes():
    print('You are correct!!!')

def no():
    print('''I'm sorry, that is incorrect.''') 

intro = c.magenta + '''Welcome to the Pink Fluffy Unicorn quiz.
Let's test your knowledge to see what you've learned so far.
'''


def q1(): 
    a1 = ask('What color are the unicorns?')
    if 'pink' in a1:
        yes()
        return True
    no()
    return False

def q2():
    a2 = ask('Where are they dancing?')
    if 'rainbows' in a2:
        yes()
        return True
    no()
    return False

def q3():
    a3 = ask('Please use one word to describe the texture of their maaaaagical fur.')
    if a3 == 'smiles':
        yes()
        return True
    no()
    return False

questions = [q1,q2,q3]

