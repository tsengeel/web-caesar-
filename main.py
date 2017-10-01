from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = 'post'>
            <div>
                <label for = "rot" > Rotate by :</label>
                <input name = "rot" value = "0" type= "text">
                <p class = "error"></p>
            </div>
            <textarea type ="text" name="text">{0}</textarea>
            <br>
            <input type="submit"> 
         
         
            
        

        </form>
      
      
    </body>
</html>
 """

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
   
    r = request.form['rot']
    t = request.form['text']
    text_rot = rotate_string(t , int(r))
   
    return '<h1>'+format(text_rot)+'</h1>'
   
    


    

app.run()