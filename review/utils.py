"""This thing does stuff."""
import colors as c
def ask(question):
    print(question)
    answer = input(c.green + '> ' + c.red).lower
    print(c.reset)
    return answer

    
