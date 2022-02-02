from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/hello/")
def hello_world():

    first_name = "Martin"
    last_name = "Luther king"

    kwargs = {
        "first_name" : first_name,
        "last_name" : last_name
    }

    return render_template('jinja_intro.html', **kwargs)

@app.route("/data-structures/")
def data_structures():
    movies = [
        "Titanic",
        "Independance Day",
        "My little pony adventures"

    ]

    car = {
        "brand" : 'BMW',
        "model" : 'Serie 1',
        "year" : '2010'
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies" : movies,
        "car" : car,
        "moons": moons
    }

    return render_template("data_structures.html", **kwargs)


@app.route("/conditionals-basics/")
def render_conditionnals():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)

@app.route('/for-loop/')
def render_loops_for():
    planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "jupyter",
    "Saturn",
    "Uranus",
    "Neptune"]
    return render_template("for_loop.html", planets=planets)
    
if __name__ == "__main__":
    app.run(port=5000)