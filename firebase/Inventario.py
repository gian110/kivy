
import pyrebase
from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window
from kivymd.uix.list import MDList
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

from kivymd.uix.menu import MDDropdownMenu

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
db1=firebase.database()
auth1=firebase.auth()


class ClienteEmpresa(ScreenManager):
    pass
class TuTienda(Screen):
    pass
class Inventarios(Screen):
    pass
class CrearProducto(Screen):
    pass
class EditarProducto(Screen):
    pass
class Eventos(Screen):
    pass
class MainEventos(Screen):
    pass
class CrearPromocion(Screen):
    pass
class Oferta(Screen):
    pass
class CrearEvento(Screen):
    pass
Window.size = (360, 640)



#obtengo= Main.MainApp()
#print(getattr(obtengo,'correo'))



class InventarioApp(MDApp):

    def build(self):
        CE= ScreenManager()

        CE.add_widget(TuTienda(name="tutienda"))
        CE.add_widget(Inventarios(name="inventarios"))
        CE.add_widget(CrearProducto(name="crearproducto"))
        CE.add_widget(EditarProducto(name="editarproducto"))
        CE.add_widget(Eventos(name="eventos"))
        CE.add_widget(MainEventos(name="maineventos"))
        CE.add_widget(CrearPromocion(name="crearpromocion"))
        CE.add_widget(Oferta(name="oferta"))
        CE.add_widget(CrearEvento(name="crearevento"))

        return CE

    # LOGIN USUARIOS
    def get_data(self, correo,contraseña):

        comp = db1.child('Negocios').order_by_child("Email").equal_to(correo).get()
        try:
            auth1.sign_in_with_email_and_password(correo, contraseña)
            for i in comp.val():
                if correo == comp.val()[i]['Email'] and contraseña == comp.val()[i]['Claves'] and '2' == comp.val()[i]['Id']:

                    if True:
                        print("si1")
        except:
            print("Estan mal las credenciales1")
        comp1 = db1.child('Clientes').order_by_child("Email").equal_to(correo).get()
        try:
            auth1.sign_in_with_email_and_password(correo, contraseña)
            for j in comp1.val():
                if correo == comp1.val()[j]['Email'] and contraseña == comp1.val()[j]['Claves'] and '1' == comp1.val()[j]['Id']:
                    #auth.sign_in_with_email_and_password(correo, contraseña)
                    print("si2")
        except:
            print("Estan mal las credenciales2")






if __name__== '__main__':
    InventarioApp().run()