from flask import Flask, request, render_template
from herpWizard.model import perform_inference

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        result = perform_inference(request.form.get("text_input"))
    return render_template("home.html", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)

