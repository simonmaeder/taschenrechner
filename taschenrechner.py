#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function, division

#---------------------
def tokenize(program):
    return program.replace('(', ' ( ').replace(')', ' ) ').split()

#---------------------
def parse(tokens):
    return tokens  # FIXME

#---------------------
def parse_atom(token):
    return token  # FIXME

#---------------------
def add(a, b):
    return a+b

def sub(a, b):
    return a-b
    
def mult(a, b):
    return a*b

def div(a, b):
    return a/b

operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}

#---------------------
def evaluate(x):
    return x  # FIXME

#=====================
def repl():
    while True:
        try:
            prog = raw_input('> ').strip()
            if prog.lower() in ('q', 'quit', 'exit', 'x'):
                break
            print(evaluate(parse(tokenize(prog))))
        except Exception as e:
            print('Error')


if __name__ == '__main__':
    tests = [
        (tokenize, ('(+ 1 1)',), ['(', '+', '1', '1', ')']),
        (parse, (['(', '+', 1, 1, ')'],), ['+', 1, 1]),
        (parse_atom, ('1.1',), 1.1),
        (add, (1, 1), 2),
        (sub, (2, 1), 1),
        (mult, (2, 3), 6),
        (div, (7, 2), 3.5),
        (evaluate, (['*', ['+', 5, 9], ['-', 11, ['/', 128, 16]]],), 42)
    ]
    ok = True
    for func, args, expected_out in tests:
        try:
            actual_out = func(*args)
            if actual_out == expected_out:
                print(func.__name__, 'OK')
            else:
                ok = False
                print(func.__name__, 'not OK!', actual_out, '!=', expected_out)
        except Exception as e:
            ok = False
            print(func.__name__, 'not OK!, Failure:', e)

    if ok:
        print('Alles OK!')
        print()
        print("Drücke 'q' um zu beenden..")
        repl()
    else:
        print('Es scheint noch nicht alles ok zu sein. Korrigiere die oben angezeigten Fehler.')
