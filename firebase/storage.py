import Main
import pyrebase
import re
from firebase import firebase

from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivymd.app import MDApp
from  kivy.core.window import Window
storage1=Main.firebase

db=storage1.database()
nombre = Main.MainApp.data_cliente


print(nombre)
imagenes=storage1.storage()
class Cliente(Screen):
    pass
class StorageApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "white"
        smt = ScreenManager(transition=WipeTransition())

        smt.add_widget(Cliente(name="cliente"))
        return smt
    def subir_imagen(self, imagen,ruta):

        cloudfile = ruta
        filename=imagen
        imagenes.child("/gola/minombre/"+cloudfile).put(filename)

if __name__ == '__main__':
     StorageApp().run()