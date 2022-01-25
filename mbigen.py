from audioop import cross
from crypt import methods
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from random import randint, getrandbits, choice
import string

app = Flask(__name__)
CORS(app)

@app.route("/generate")
def generate():

    invalidLetters = ['S', 'L', 'O', 'I', 'B', 'Z']
    # Create a string of the valid characters by grabbing the alphabet and removing the invalid letters
    validLetters = "".join(i for i in string.ascii_uppercase if i not in invalidLetters)

    mbiList = []
    mbiList.append(randint(1, 9)) # The first character is 1-9, other numerics are 0-9
    mbiList.append(choice(validLetters))
    mbiList.append(randint(0, 9) if getrandbits(1) else choice(validLetters))
    mbiList.append(randint(0, 9))
    mbiList.append(choice(validLetters))
    mbiList.append(randint(0, 9) if getrandbits(1) else choice(validLetters))
    mbiList.append(randint(0, 9))
    mbiList.append(choice(validLetters))
    mbiList.append(choice(validLetters))
    mbiList.append(randint(0, 9))
    mbiList.append(randint(0, 9))

    mbi = ''.join(str(x) for x in mbiList)

    return jsonify(
        value=mbi
    )


@app.route("/verify", methods=['POST'])
def verify():
    if request.method == 'POST':
        invalidLetters = ['S', 'L', 'O', 'I', 'B', 'Z']

        mbi = request.form['mbi']

        # Make sure we received something
        if mbi is None: return json.dumps(False)

        # Remove the dashes (they're optional anyway)
        mbi = mbi.replace('-', '')
        mbi = mbi.upper()

        # Convert to a list of chars so it's easier to check each character
        mbiList = list(mbi)

        # If we fail at any point, return False
        if len(mbiList) != 11: return json.dumps(False)
        if not mbiList[0].isnumeric() or mbiList[0] is '0': return json.dumps(False)
        if not mbiList[1].isalpha() or mbiList[1] in invalidLetters: return json.dumps(False)
        if not mbiList[2].isnumeric() and (not mbiList[2].isalpha() or mbiList[2] in invalidLetters): return json.dumps(False)
        if not mbiList[3].isnumeric(): return json.dumps(False)
        if not mbiList[4].isalpha() or mbiList[4] in invalidLetters: return json.dumps(False)
        if not mbiList[5].isnumeric() and (not mbiList[5].isalpha() or mbiList[5] in invalidLetters): return json.dumps(False)
        if not mbiList[6].isnumeric(): return json.dumps(False)
        if not mbiList[7].isalpha() or mbiList[7] in invalidLetters: return json.dumps(False)
        if not mbiList[8].isalpha() or mbiList[8] in invalidLetters: return json.dumps(False)
        if not mbiList[9].isnumeric(): return json.dumps(False)
        if not mbiList[10].isnumeric(): return json.dumps(False)

        # We made it through the gauntlet
        return json.dumps(True)
    
    # Default return
    return json.dumps(False)

if __name__ == '__main__':
    # So the Procfile can start
    app.run()
