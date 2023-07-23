import sw_functions as sw


while True:

 menu=sw.get_num("que deseas hacer ahora? ",0,2)

 if menu == 0:
   break
 
 if menu == 1:
  usuario = input("ingresa el nombre ").lower()
  user_request = sw.testuser(usuario)

  if user_request == True:
   print("este usuario ya esta registrado")

  elif user_request == False: 
   contraseña = input("ingresa tu contraseña ")
   sw.registrar(usuario, contraseña)

  print("usuario registrado correctamente")

 if menu == 2:
    usuario = input("ingresa el nombre ").lower()
    user_request = sw.testuser(usuario)

    if user_request == True:
      contraseña = input("ingresa la contraseña ")
      pass_request = sw.testpass(contraseña)
      id = sw.get_id(usuario)

      if pass_request == True:
        print("sesion iniciada")
        opt = sw.login_menu()
        if opt == 1:
          sw.delete(id)
      
      else:
        print("contraseña incorrecta")
        
    elif user_request == False:
      print("no se encontró el usuario ")
 
 

 