import math
import sys
import secrets

class RandyLineError(Exception):
    pass

def isprime(num: int) -> int:
    for x in range(math.floor(math.sqrt(num))):
        if num % x == 0:
            return 0
    return 1

def execute(program: str) -> str:
    lines = program.split('\n')
    state = {'lineno': 0, 'colno': 0, 'prognum': 0, 'quit': False, 'output': ''}
    exdict = {
        '+': lambda: state.update({'prognum': state['prognum'] + 1}),
        '-': lambda: state.update({'prognum': state['prognum'] - 1}),
        '*': lambda: state.update({'prognum': state['prognum'] * 2}),
        '/': lambda: state.update({'prognum': state['prognum'] / 2}),
        '^': lambda: state.update({'prognum': state['prognum'] ** 2}),
        'n': lambda: state.update({'lineno': state['lineno'] + 1, 'colno': -1}),
        'r': lambda: state.update({'lineno': secrets.choice(range(len(lines))) + 1, 'colno': -1}),
        'i': lambda: state.update({'lineno': state['lineno'] + state['prognum']}),
        'c': lambda: state.update({'colno': state['colno'] + state['prognum']}),
        '0': lambda: state.update({'prognum': 0}),
        'n': lambda: state.update({'prognum': int(input('Program is requesting input: '))}),
        'o': lambda: state.update({'output': state['output'] + chr(state['prognum'])}),
        'u': lambda: state.update({'output': state['output'] + str(state['prognum'])}),
        'p': lambda: state.update({'prognum': isprime(state['prognum'])}),
        'q': lambda: state.update({'quit': True}),
    }

    while True:
        if state['quit'] == True:
            break
        
        try:
            exdict[lines[state['lineno']][state['colno']]]()

            if state['quit'] == True:
                break

            state['colno'] = state['colno'] + 1
        except IndexError:
            break

        except Exception as e:
            raise RandyLineError(str(e))

    return state['output']

if __name__ == '__main__':
    print("Output:", execute(sys.stdin.read()))
    input("Press enter to quit")
