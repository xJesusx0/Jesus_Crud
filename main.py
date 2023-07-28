import flask as flask
import my_functions as sw
app = flask.Flask(__name__)


@app.route("/", methods = ["GET","POST"])
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
            pass_request = sw.check_Pass(contraseña)

            if pass_request == True:
                if usuario != "" and contraseña != "" :
                    sw.registrar(usuario, contraseña)
            else:
                error = "La contraseña debe tener 8 caracteres"
                return flask.render_template("index3.html",error = error,data=data)

    sw.delete_c()
    data = sw.process_data()
    return flask.render_template("index3.html",data = data)

@app.route("/tabla", methods = ["GET","POST"])
def tabla():
    data = sw.process_data()
    return flask.render_template("tabla.html",
                                 data = data)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    try:
        sw.new_delete(id)
    except ValueError:
        pass
    return flask.redirect("/")

@app.route("/editar/<int:id>/<username>/<password>",methods=["GET","POST"])
def editar(id,username,password):

    data = sw.process_data() 

    if flask.request.method  == "POST":
        new_u = flask.request.form["username"]
        new_p = flask.request.form["password"]
        
        user_request = sw.testuser(new_u)  
        if user_request == True:
            error = "ese usuario ya esta ocupado"
            return flask.render_template("edit.html",
                                 o_username = username,
                                 o_password=password,
                                 data=data,
                                 error=error)
        else:
            if sw.check_Pass(new_p) == True:
                sw.edit(id,new_u,new_p)
                return flask.redirect("/")
            else:
                error = "La contraseña debe tener 8 caracteres"
                return flask.render_template("edit.html",
                                 o_username = username,
                                 o_password=password,
                                 data=data,
                                 error=error)

    data = sw.process_data() 
    return flask.render_template("edit.html",
                                 o_username = username,
                                 o_password=password,
                                 data=data)
app.run(debug = True,port=4000) 
