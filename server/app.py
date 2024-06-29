#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>/')
def print_string(hello):
    print(f'{hello}')
    return f'{hello}'

@app.route('/count/<int:r>/')
def count(r):
    return '<br>'.join(str(i) for i in range(r))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == '+':
        result= num1+num2
    elif operation =='-':
        result=num1-num2
    elif operation=="*":
        result= num1*num2
    elif operation=='div':
        if num2==0:
            return 'Error:Division cannot be operrated on 0'
        result =num1/num2
    elif operation=='%':
        if num2==0:
            return 'Error Modulus cannit be operated on 0'
        result=num1%num2
    else:
        return 'Error: Unsupported operand'
    return f'The result of {num1} {operation} {num2} is result {result}'    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

