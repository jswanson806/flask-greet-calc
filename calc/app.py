# Put your app in here.
from flask import Flask, request
import operations
app = Flask(__name__)

@app.route('/add')
def add():
    """Add a and b"""
    return str(operations.add(int(request.args['a']), int(request.args['b'])))

@app.route('/sub')
def sub():
    """Subtract a and b"""
    return str(operations.sub(int(request.args['a']), int(request.args['b'])))

@app.route('/mult')
def mult():
    """Multiply a and b"""
    return str(operations.mult(int(request.args['a']), int(request.args['b'])))

@app.route('/div')
def div():
    """Divide a by b"""
    return str(operations.div(int(request.args['a']), int(request.args['b'])))