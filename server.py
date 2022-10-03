from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', box=3)

@app.route('/play')
def play():
    return render_template('index.html', box=3)
@app.route('/play/<x>')
def playX(x):
    return render_template('index.html', box=int(x))
@app.route('/play/<x>/<y>')
def playY(x, y):
    return render_template('index.html', box=int(x), color=y)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  