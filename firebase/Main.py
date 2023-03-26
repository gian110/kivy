import subprocess
import Inventario
import UserCliente
import pyrebase
import re
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivymd.app import MDApp
from  kivy.core.window import Window
from collections import OrderedDict
from kivy.clock import Clock
Clock.max_iteration = 1000

firebaseConfig={'apiKey': "AIzaSyCw35eQBOfgBHQxC4P4WUmiXLwNWafOKZw",
     'authDomain': "proyecto-compy.firebaseapp.com",
     'databaseURL': "https://proyecto-compy-default-rtdb.firebaseio.com/",
     'projectId': "proyecto-compy",
     'storageBucket': "proyecto-compy.appspot.com",
     'messagingSenderId': "68945158948",
     'appId': "1:68945158948:web:2a584b3225293bc63209b1",
     'measurementId': "G-DXJ403HRZ9"}
firebase=pyrebase.initialize_app(firebaseConfig)
#firebasea = firebase.FirebaseApplication('https://proyecto-compy-default-rtdb.firebaseio.com/', None)
db=firebase.database()
auth=firebase.auth()

#storage=firebase.storage()
Window.size = (360, 640)
#Clases USUARIO CLIENTE
class Principal(UserCliente.Principal):
    pass
class Productos(UserCliente.Productos):
    pass

#Clases USUARIO NEGOCIO
class TuTienda(Inventario.TuTienda):
    pass
class Inventarios(Inventario.Inventarios):
    pass
class EditarProducto(Inventario.EditarProducto):
    pass
class CrearProducto(Inventario.CrearProducto):
    pass
class Eventos(Inventario.Eventos):
    pass
class MainEventos(Inventario.MainEventos):
    pass
class CrearPromocion(Inventario.CrearPromocion):
    pass
class Oferta(Inventario.Oferta):
    pass
class CrearEventos(Inventario.CrearEvento):
    pass


class Recuperar(Screen):
    pass
class Registro(Screen):
    pass
class Contrase(Screen):
    pass
class Negocio(Screen):
    pass
class Cliente(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "white"
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(Recuperar(name="recuperar"))
        sm.add_widget(Registro(name="registro"))
        sm.add_widget(Contrase(name="contrase"))
        sm.add_widget(Negocio(name="negocio"))
        sm.add_widget(Cliente(name="cliente"))
        sm.add_widget(TuTienda(name="tutienda"))
        sm.add_widget(Inventarios(name="inventarios"))
        sm.add_widget(CrearProducto(name="crearproducto"))
        sm.add_widget(EditarProducto(name="editarproducto"))
        sm.add_widget(Eventos(name="eventos"))
        sm.add_widget(MainEventos(name="maineventos"))
        sm.add_widget(CrearPromocion(name="crearpromocion"))
        sm.add_widget(Oferta(name="oferta"))
        sm.add_widget(CrearEventos(name="crearevento"))
        sm.add_widget(Principal(name="principal"))
        sm.add_widget(Productos(name="productos"))
        return sm

#print("loggeado")
    #REGISTRO USUARIOS

    def data_cliente(self,nombres_clientes, claves_clientes,email_clientes):
        try:
            auth.create_user_with_email_and_password(email_clientes,claves_clientes)
            if True:
                data = {
                    "Id": '1',
                    'Nombre': nombres_clientes,
                    'Claves': claves_clientes,
                    'Email': email_clientes
                }
                db.child("Clientes").child().push(data)
        except:
            print("Ya existe usuario")



    def data_negocio(self, nombres_negocios, claves_negocios, email_negocios):

        try:
            auth.create_user_with_email_and_password(email_negocios,claves_negocios)
            if True:
                data = {
                    "Id": '2',
                    'Nombre': nombres_negocios,
                    'Claves': claves_negocios,
                    'Email': email_negocios
                }
                db.child("Negocios").child().push(data)
        except:
            print("Ya existe Usuario")

    # LOGIN USUARIOS
    def get_data(self, correo,contraseña):

        comp = db.child('Negocios').order_by_child("Email").equal_to(correo).get()
        try:
            auth.sign_in_with_email_and_password(correo, contraseña)
            for i in comp.val():
                if correo == comp.val()[i]['Email'] and contraseña == comp.val()[i]['Claves'] and '2' == comp.val()[i]['Id']:

                    if True:
                        self.root.current = 'tutienda'
        except:
            print("Estan mal las credenciales1")
        comp1 = db.child('Clientes').order_by_child("Email").equal_to(correo).get()
        try:
            auth.sign_in_with_email_and_password(correo, contraseña)
            for j in comp1.val():
                if correo == comp1.val()[j]['Email'] and contraseña == comp1.val()[j]['Claves'] and '1' == comp1.val()[j]['Id']:
                    #auth.sign_in_with_email_and_password(correo, contraseña)
                    if True:

                        self.root.current = 'principal'
        except:
            print("Estan mal las credenciales2")






        #print(orden["Email"])


        '''
        try:
            auth.sign_in_with_email_and_password(correo, contraseña)
            print("Bienvenido")
        except:
            print("Credenciales incorrectas")

        '''

    def callback(self, screen):
        self.current = screen
        # root.manager.transition.direction = "left"
        # root.manager.current = "screen2"
        # link icon to screen2

if __name__ == '__main__':
     MainApp().run()