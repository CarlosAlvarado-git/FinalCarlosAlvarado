import requests, validators
from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
respo = requests.get("http://demo7130536.mockable.io/final-contacts-100")
losjason = respo.json()
dict_file = dict()
dict_file = losjason
bandera = 1
while(bandera != 0):
    print("Bienvenido a ContactBook \n")
    print("Menu: \n")
    r = input("1. Agregar Contacto\n2. Buscar Contacto\n3. Listas y Ver Contacto\n4. Borrar Contacto\n5. Llamar contacto\n6. Enviar mensaje a contacto\n7. Enviar correo a contacto\n8. Exportat los Contactos\n9. Salir\n Ingrese su opción: ")
    correcto = r.isdigit()
    if correcto:
        if (r == "1"):
            nombre = input("Ingrese el nombre y apellido del contacto: ")
            nombre = nombre.strip()
            tele = input("Ingrese el número de telefono: ")
            tele = tele.strip()
            emails = input("Ingrese el correo: ")
            emails = emails.strip()
            compa = input("Ingrese la compañía: ")
            ex = input("Ingrese algún comentario exta o dato extra: ")
            coremail = validators.email(emails)
            cont = 0
            numeros = False
            for i in range(len(tele)):
                vali = tele[i].isdigit()
                if tele[i] == " ":
                    cont = cont + 1
                if (vali == True or tele[i] == "-" or tele[i] == "(" or tele[i] == ")" or tele[i] == "+") and cont <= 2:
                    numeros = True
                else:
                    numeros = False
            nombreyape = nombre.split(" ")
            nombreyape = len(nombreyape)
            letra = nombre[0:1].upper()
            if numeros == True and len(tele) >= 8 and len(tele) <= 19 and nombreyape == 2 and coremail == True:
                if letra in dict_file:
                    if nombre.title() in dict_file[letra]:
                        print("Este contacto ya existe")
                    else:
                        dict_file[letra].setdefault(nombre.title(), {"telefono": tele, "email": emails, "company": compa, "extra": ex})
                        print("Contacto guardado correctamente")
                else:
                    dict_file.setdefault(letra, {nombre.title() : {"telefono": tele, "email": emails, "company": compa, "extra": ex}})
                    print("Contacto guardado correctamente")
            else:
                print("Ha ingresado mal un dato, le daremos un ejemplo para que vea cómo debe ingresar los datso: \n")
                print("Nombre y Apellido: Carlos Alvardo Nombre y Apellido\nTeléfono: +502 (123) 123-5678 con sólo 7 números y un guión\nEmail: corre@domiono.com\n Los demás datos no requieren una sitaxis específica.\n")

        elif (r == "2"):
            busco = input("Buscar: ")
            if len(busco) >= 1:
                listakeys = list(dict_file.keys())
                Bandera = 1
                for i in listakeys:
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        if busco in x:
                            print(f"- {x}")
                            Bandera = 0
                if Bandera == 1:
                    print("No existe este contacto")
            pass
        elif (r == "3"):
            s = 1
            while(s != 0):
                listakeys = list(dict_file.keys())
                cont = 0
                for i in listakeys:
                    print(f"{i}:\n")
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        cont = cont + 1
                        print(f"  {cont}. {x}\n")
                contac = input("Ingrese el número del contacto que desee ver: ")
                vali = contac.isdigit()
                if vali == True:
                    if int(contac) >= 1 and int(contac) <= cont:
                        listakeys = list(dict_file.keys())
                        conts = 0
                        ban = 0
                        keyletra = ""
                        keynombre = ""
                        for i in listakeys:
                            nombreslist = list(dict_file[i].keys())
                            for x in nombreslist:
                                conts = conts + 1
                                if int(contac) == conts:
                                    ban = 1
                                    keynombre = x
                                    keyletra = i
                                    break
                            if ban == 1:
                                break
                        print(f"Nombre: {keynombre}:\n")
                        for i in dict_file[keyletra][keynombre]:
                            print(f"{i}: {dict_file[keyletra][keynombre][i]}\n")
                        
                        res = input("Deseea buscar otro contacto (s/n)")
                        if res == "s" or res == "si"or res == "S"or res == "Si"or res == "y"or res == "yes"or res == "Y"or res == "Yes":
                            s = 1
                        else:
                            s = 0
                    else:
                        print("Ingrese sólo los número presentes")
                else:
                    print("Ingrese sólo los número presentes")
        elif (r == "4"):
            s = 1
            while(s != 0):
                listakeys = list(dict_file.keys())
                cont = 0
                for i in listakeys:
                    print(f"{i}:\n")
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        cont = cont + 1
                        print(f"  {cont}. {x}\n")
                contac = input("Ingrese el número del contacto que desee borrar: ")
                vali = contac.isdigit()
                if vali == True:
                    if int(contac) >= 1 and int(contac) <= cont:
                        listakeys = list(dict_file.keys())
                        conts = 0
                        ban = 0
                        keyletra = ""
                        keynombre = ""
                        for i in listakeys:
                            nombreslist = list(dict_file[i].keys())
                            for x in nombreslist:
                                conts = conts + 1
                                if int(contac) == conts:
                                    ban = 1
                                    keynombre = x
                                    keyletra = i
                                    break
                            if ban == 1:
                                break
                        dict_file[keyletra].pop(keynombre, None)
                        toaster.show_toast("Contacto eliminado", f"{keynombre}", duration=3)
                        #print(f"Nombre: {keynombre}:\n")
                        res = input("Deseea borrar otro contacto (s/n)")
                        if res == "s" or res == "si"or res == "S"or res == "Si"or res == "y"or res == "yes"or res == "Y"or res == "Yes":
                            s = 1
                        else:
                            s = 0
                    else:
                        print("Ingrese sólo los número presentes")
                else:
                    print("Ingrese sólo los número presentes")
        elif (r == "5"):
            s = 1
            while(s != 0):
                listakeys = list(dict_file.keys())
                cont = 0
                for i in listakeys:
                    print(f"{i}:\n")
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        cont = cont + 1
                        print(f"  {cont}. {x}\n")
                contac = input("Ingrese el número del contacto que desee llamar: ")
                vali = contac.isdigit()
                if vali == True:
                    if int(contac) >= 1 and int(contac) <= cont:
                        listakeys = list(dict_file.keys())
                        conts = 0
                        ban = 0
                        keyletra = ""
                        keynombre = ""
                        for i in listakeys:
                            nombreslist = list(dict_file[i].keys())
                            for x in nombreslist:
                                conts = conts + 1
                                if int(contac) == conts:
                                    ban = 1
                                    keynombre = x
                                    keyletra = i
                                    break
                            if ban == 1:
                                break
                        telefono = dict_file[keyletra][keynombre]["telefono"]
                        toaster.show_toast(f"Llamando a {keynombre}:", f"{telefono}", duration=3)
                        #print(f"Nombre: {keynombre}:\n")
                        res = input("Deseea llamar a otro contacto (s/n)")
                        if res == "s" or res == "si"or res == "S"or res == "Si"or res == "y"or res == "yes"or res == "Y"or res == "Yes":
                            s = 1
                        else:
                            s = 0
                    else:
                        print("Ingrese sólo los número presentes")
                else:
                    print("Ingrese sólo los número presentes")
        elif (r == "6"):
            s = 1
            while(s != 0):
                listakeys = list(dict_file.keys())
                cont = 0
                for i in listakeys:
                    print(f"{i}:\n")
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        cont = cont + 1
                        print(f"  {cont}. {x}\n")
                contac = input("Ingrese el número del contacto que desee mandar un mensaje: ")
                vali = contac.isdigit()
                if vali == True:
                    if int(contac) >= 1 and int(contac) <= cont:
                        listakeys = list(dict_file.keys())
                        conts = 0
                        ban = 0
                        keyletra = ""
                        keynombre = ""
                        for i in listakeys:
                            nombreslist = list(dict_file[i].keys())
                            for x in nombreslist:
                                conts = conts + 1
                                if int(contac) == conts:
                                    ban = 1
                                    keynombre = x
                                    keyletra = i
                                    break
                            if ban == 1:
                                break
                        telefono = dict_file[keyletra][keynombre]["telefono"]
                        mensaje = input(f"Mensaje para {keynombre}: ")
                        toaster.show_toast(f"Mensaje enviado a {keynombre}: {telefono}", f"{mensaje}", duration=3)
                        #print(f"Nombre: {keynombre}:\n")
                        res = input("Deseea mandar mensaje a otro contacto (s/n)")
                        if res == "s" or res == "si"or res == "S"or res == "Si"or res == "y"or res == "yes"or res == "Y"or res == "Yes":
                            s = 1
                        else:
                            s = 0
                    else:
                        print("Ingrese sólo los número presentes")
                else:
                    print("Ingrese sólo los número presentes")
        elif (r == "7"):
            s = 1
            while(s != 0):
                listakeys = list(dict_file.keys())
                cont = 0
                for i in listakeys:
                    print(f"{i}:\n")
                    nombreslist = list(dict_file[i].keys())
                    for x in nombreslist:
                        cont = cont + 1
                        print(f"  {cont}. {x}\n")
                contac = input("Ingrese el número del contacto que desee mandar un correo: ")
                vali = contac.isdigit()
                if vali == True:
                    if int(contac) >= 1 and int(contac) <= cont:
                        listakeys = list(dict_file.keys())
                        conts = 0
                        ban = 0
                        keyletra = ""
                        keynombre = ""
                        for i in listakeys:
                            nombreslist = list(dict_file[i].keys())
                            for x in nombreslist:
                                conts = conts + 1
                                if int(contac) == conts:
                                    ban = 1
                                    keynombre = x
                                    keyletra = i
                                    break
                            if ban == 1:
                                break
                        emailcorre = dict_file[keyletra][keynombre]["email"]
                        print(f"Nombre: {keynombre}:\n")
                        subject = input("Ingrese el subject del correo: ")
                        mensajedecorre = input("Ingrese el mensaje de correo: ")
                        toaster.show_toast(f"Correo enviado a {keynombre}: {emailcorre}", f"Subject: {subject}\nMensaje: {mensajedecorre}", duration=3)
                        res = input("Deseea mandar correo a otro contacto (s/n)")
                        if res == "s" or res == "si"or res == "S"or res == "Si"or res == "y"or res == "yes"or res == "Y"or res == "Yes":
                            s = 1
                        else:
                            s = 0
                    else:
                        print("Ingrese sólo los número presentes")
                else:
                    print("Ingrese sólo los número presentes")
        elif (r == "8"):
            pass
        elif (r == "9"):
            bandera = 0
        else:
            print("Ingrese sólo los número que aparecen en el menú.\n")
    else:
        print("Ingrese sólo los número que aparecen en el menú.\n")