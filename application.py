from flask import Flask, request, render_template
from iris_classifier import predict_species

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)
        
        return render_template("index.html", prediction=prediction)
    
    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
