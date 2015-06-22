"""thIS iS a veRy speCIAL modULE thAT cAN heLP yOU dO stuFF."""

import colors as c

def ask(question,color=c.yellow):
    print(color + question + c.reset)
    answer = input(c.green + "> " + c.red).lower().strip()
    print(c.reset)
    return answer


if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
    color = ask("What is your name in color?",c.random_color())
