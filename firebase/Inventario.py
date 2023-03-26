import pyrebase
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen

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
class TuTienda(MDScreen):
    pass
class Inventarios(MDScreen):
    pass
class CrearProducto(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.select_item = None

    def on_enter(self, *args):
        self.set_menu_items()
        # PROBABILIDAD DE BORRAR EL MÉTODO, SE DEBE CORREGIR EL SELF.SCREEN
    def set_menu_items(self):
        datos = []
        # CREAR CONDICIONAL PARA SABER SI SE CREARÁ PRODUCTO O SERVICIO Y HACER LA OBTENCIÓN RESPECTIVA
        data = db1.child("categorias").child("producto").get()
        for dato in data.val():
            if dato != None:
                datos.append(str(dato))
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{dato}",
                "height": dp(40),
                "on_release": lambda x=f"{dato}": self.set_item(x),
            } for dato in datos
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            width_mult=2,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.menu.dismiss()
        self.select_item = text_item

        # GUARDAR DATOS

    def save_product(self, nombre_producto, cant_producto, precio_producto, description):
        if self.select_item is not None:
            categoria=self.select_item
            data = {
                "Id": '2',
                'Nombre_producto': nombre_producto,
                'cantidad': cant_producto,
                'precio': precio_producto,
                'categoria': categoria,
                'descripcion': description
            }
        # ESTE ESPACIO SERÍA PARA CREAR EL CONDICIONAL Y AUTENTICAR AL USUARIO
            db1.child("Productos").child().push(data)
class EditarProducto(MDScreen):
    pass
class Eventos(MDScreen):
    pass
class MainEventos(MDScreen):
    pass
class CrearPromocion(MDScreen):
    pass
class Oferta(MDScreen):
    pass
class CrearEvento(MDScreen):
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



if __name__== '__main__':
    InventarioApp().run()
