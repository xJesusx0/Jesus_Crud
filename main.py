import flask as flask
import my_functions as sw
app = flask.Flask(__name__)

@app.route("/")
def index():

    data = sw.process_data()
    return flask.render_template("index.html",data = data)

@app.route("/registrar", methods = ["GET","POST"])
def register():
    data = sw.process_data()
    if flask.request.method  == "POST":

        usuario = flask.request.form["username"]
        contraseña = flask.request.form["password"]

        user_request = sw.testuser(usuario)
    
        if user_request == True:
            error = "ese usuario ya esta ocupado"

            return flask.render_template("index3.html",error = error,data=data)

        elif user_request == False: 

            if usuario != "" and contraseña != "" :
                sw.registrar(usuario, contraseña)
            
    sw.delete_c()

    data = sw.process_data()
    return flask.render_template("index3.html",data = data)


@app.route("/tabla", methods = ["GET","POST"])
def tabla():
    data = sw.process_data()
    return flask.render_template("tabla.html",
                                 data = data)

@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    data = sw.process_data()
    
    if flask.request.method == "POST":
        try:
            id = flask.request.form["id"]
            converted_id = int(id)
            sw.new_delete(converted_id)
        except ValueError:
            return flask.render_template("delete.html",data=data)

    data = sw.process_data()
    return flask.render_template("delete.html",data=data)

app.run(debug = True,port=4000) 
