from flask import Flask, render_template

# the special variable '__name__' will get the value of the python script
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")



# python automatically assigns the name "__main__" to the specail __name__ variable, therefore the app will run
if  __name__=="__main__":
    app.run(debug=True)
    # If the script was imported from another script, this would not be executed



