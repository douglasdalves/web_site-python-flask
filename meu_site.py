from flask import Flask,render_template

# requisito do flask
app = Flask(__name__,template_folder='templates')

# criar a pagina do site
# route -> siteteste.com/
# função -> o que vc quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

# nova pagina do site
@app.route("/contatos")
def contatos():
    return "Teste pagina de contatos"


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
