import flask as flask
import sw_functions as sw
app = flask.Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def index3():
    data = sw.users_data()
    users = sw.users_request()
    if flask.request.method  == "POST":

        usuario = flask.request.form["username"]
        contraseña = flask.request.form["password"]

        user_request = sw.testuser(usuario)
    
        if user_request == True:
            error = "ese usuario ya esta ocupado"

            return flask.render_template("index3.html",users = users,error = error)

        elif user_request == False: 

            if usuario != "" and contraseña != "" :
                sw.registrar(usuario, contraseña)
            
    sw.delete_c()
    users = sw.users_request()
  
    data = sw.users_data()
    return flask.render_template("index3.html",users = users,data = data)

@app.route("/admin")
def admin():
    users = sw.users_request()
    usernames = []
    passwords = []
    for user in users:
        username,password = user.split(",")
        usernames.append(username)
        passwords.append(password)
    return flask.render_template("admin.html",
                                 users = users,
                                 usernames = usernames,
                                 passwords = passwords)

@app.route("/index", methods = ["GET","POST"])
def tabla():
    data = sw.users_data()
    return flask.render_template("tabla.html",
                                 data = data)

app.run(debug = True,port=4000) 