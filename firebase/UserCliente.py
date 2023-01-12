
from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window
from kivymd.uix.list import MDList
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

from kivymd.uix.menu import MDDropdownMenu


class ClienteUsuario(ScreenManager):
    pass
class Principal(Screen):
    pass
class Productos(Screen):
    pass
Window.size = (360, 640)





class UserCliente(MDApp):

    def build(self):
        CE= ScreenManager()
        CE.add_widget(Principal(name="principal"))
        CE.add_widget(Productos(name="productos"))


        return CE

if __name__== '__main__':
    UserCliente().run()
