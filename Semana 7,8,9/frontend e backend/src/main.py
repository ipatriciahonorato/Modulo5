from flask import Flask, render_template, request, redirect
import sqlite3

# Initializing the Flask application 
app = Flask(__name__)

# Setting the name of the database 
DB_NAME = "robo.db"

# Function to create tables in the database 
def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS robo
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, x REAL, y REAL, z REAL)''')
    conn.commit()
    conn.close()

# Function to insert x, y and z values for the robot's position into the database
def insert_robo_position(x, y, z):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO robo (x, y, z) VALUES (?, ?, ?)", (x, y, z))
    conn.commit()
    conn.close()

# Function to get the latest position of the robot from the database
def get_robo_position():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT x, y, z FROM robo ORDER BY id DESC LIMIT 1")
    position = c.fetchone()
    conn.close()
    return position

# Handling the root endpoint by redirecting to '/robo'
@app.route("/")
def index():
    return redirect("/robo")

# Handling the '/robo' endpoint by rendering the template to display the robot's position
@app.route("/robo")
def ver_robo():
    position = get_robo_position()
    return render_template("robo.html", robo={"x": position[0], "y": position[1], "z": position[2]}) 

# Handling the '/mover' endpoint by handling the robot's movement using POST method
@app.route("/mover", methods=['POST'])
def mover_robo():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    insert_robo_position(x, y, z)
    return redirect("/robo")

# Handling the '/mover' endpoint by rendering the template to move the robot using GET method
@app.route("/mover", methods=['GET'])
def deslocamento_robo():
    return render_template("mover.html") 

# Handling the '/pos' endpoint by getting the robot's position using GET method and returning it as a JSON object
@app.route("/pos", methods=['GET'])
def pos():
    position = get_robo_position()
    return {"x": position[0], "y": position[1], "z": position[2]}

# Verify if the code is being run as the main program and running the app on port 3000.
if __name__ == '__main__':
    create_tables()
    app.run(host="0.0.0.0", port=3000) 