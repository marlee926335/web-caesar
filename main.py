from flask import Flask, request
from caesar import rotate_string_13
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <form method="POST"> 
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" id="rot"><br>
        <textarea  name="text" id="text" rows="10" cols="60">
        </textarea>
        <br>
        <input type="submit" value="Submit Query">
        <style>
            form { 
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea { 
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
    </body>
</html>
"""

def index():
    return form

@app.route('/path', methods=['POST'])
def encrypt():
    rot = request.form['number to rotate']
    text = request.form['text']
    new_text = (rotate_string(text, rot))

    return '<h1>' + new_text + '</h1>'

app.run()