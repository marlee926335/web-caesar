from flask import Flask

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
@app.route("/")
def index():
    return form

app.run()