from flask  import  Flask,  render_template
app =   Flask(__name__)
@app.route("/")
def home():
    return render_template(r"index.html")
@app.route("/dash1.html")
def dash1():
    return render_template(r"dash1.html")
@app.route("/dash2.html")
def dash2():
    return render_template(r"dash2.html")
@app.route("/story.html")
def story():
    return render_template(r"story.html")
@app.route("/team.html")
def team():
    return render_template(r"team.html")
@app.route("/contact.html")
def contact():
    return render_template(r"contact.html")
if __name__ == "__main__":
    app.run(debug=False,    port=8000)
    