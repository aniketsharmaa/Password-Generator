import random as r
import string
from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    number = str(int(r.random()*10)) + str(int(r.random()*10))
    number2 = str(int(r.random()*10)) + str(int(r.random()*10))

    smallLetter = 'abcdefghijklmnopqrstuvwxyz'
    capitalLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sLetter = r.choice(smallLetter)
    cLetter = r.choice(capitalLetter)
    cLetter2 = r.choice(capitalLetter)

    numericData = '!@^%$#@()*^'
    alphaNumeric = r.choice(numericData)
    alphaNumeric2 = r.choice(numericData)


    finalPassword = cLetter2 + number + sLetter + alphaNumeric +number2 +alphaNumeric2
    random_number = finalPassword # Generate a random number
    return render_template('index.html', random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True)