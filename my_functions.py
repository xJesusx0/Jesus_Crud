import csv

def registrar (user,passw):
  with open ("database.csv","a") as file:
   
   writer = csv.DictWriter(file, fieldnames=["username","password"])
   writer.writerow({"username":user,"password":passw})


def testuser(user):
 with open('database.csv',newline = '') as csvfile:
     reader = csv.DictReader(csvfile)
     
     for row in reader:
      
      if row['username'] == user:
        isre = True
        break
      
     else:
       isre = False
     return isre

def testpass(passw):
  with open('database.csv',newline = '') as file:
     reader = csv.DictReader(file)

     for row in reader:   
      if row['password'] == passw:
        isre = True
        break
      
     else:
       isre = False

     return isre

def delete_c():
    with open('database.csv', 'r') as file:

        lineas = file.readlines()
        print(lineas)
        new_file=[]

    for linea in lineas:
       if linea != "" and linea != "\n" and linea != ",":
          new_file.append(linea)

    print(new_file)
    with open('database.csv', 'w') as file:
        for line in new_file:
            file.write(line)

def get_id(user):
   with open('database.csv',newline = '') as csvfile:
     reader = csv.DictReader(csvfile)
     
     id=1
     for row in reader:
      id = id + 1
      if row['username'] == user:
        return id

def users_request():
    f_users = []

    with open('database.csv', 'r') as file:
        lines = file.readlines()
        c = 0
        for line in lines:
          if c != 0:
            f_users.append(line)
          c = c+ 1
    return f_users

def process_data():
  users = users_request()
  usernames = []
  passwords = []
  id = []
  id_counter = 1
  for user in users:
        username,password = user.split(",")
        usernames.append(username)
        passwords.append(password)
        id.append(id_counter)
        id_counter = id_counter + 1
  data = list(zip(id,usernames,passwords))
  return data

def new_delete(id):
  data = users_request()
  new_file = ["username,password\n"]
  counter = 1
  for i in data:
    if id != counter:
        new_file.append(i)
    counter = counter + 1

  with open('database.csv', 'w') as file:
        file.writelines(new_file)
  delete_c()

def edit(id,new_u,new_p):
  data = users_request()
  new_file = ["username,password\n"]
  editted = f"{new_u},{new_p}\n"
  counter = 1
  for i in data:
    if id != counter:
        new_file.append(i)
    else:
        new_file.append(editted)
    counter = counter + 1
  with open('database.csv', 'w') as file:
        file.writelines(new_file)

def check_Pass(password):
   if len(password) < 8:
      return False
   else:
      return True