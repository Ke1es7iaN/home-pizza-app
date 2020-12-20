from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.graphics import (Color, Rectangle, Ellipse, RoundedRectangle)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'resizable','0')
Config.set('graphics', 'width','411')
Config.set('graphics', 'height','730')



class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    number = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.number.text != "" and \
            ((len(self.number.text) == 11 and self.number.text[0] == '8' and self.number.text.isdigit()) or\
            (len(self.number.text) == 12 and self.number.text[0:2] == "+7" and self.number.text[1:11].isdigit())):
            if self.password != "":
                db.add_user(self.number.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm(self)
        else:
            invalidForm(self)

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.number.text = ""
        self.password.text = ""
        self.namee.text = ""


    


class LoginWindow(Screen):
    number = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.number.text, self.password.text):
            MainWindow.current = self.number.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin(self)

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.number.text = ""
        self.password.text = ""




class MainWindow(Screen): 

    def infoOut(self):
        sm.current = "info"

    def basketOut(self):
        sm.current = "order"

    def pizzaOut(self):
        sm.current = "pizza"

    def rollsOut(self):
        sm.current = "rolls"

    def saladsOut(self):
        sm.current = "salads"

    def dessertOut(self):
        sm.current = "dessert"




class PizzaWindow(Screen):

    def MainPizzaOut(self):
        sm.current = "main"

    def infoOut(self):
        sm.current = "info"

    def basketOut(self):
        sm.current = "order"


class RollsWindow(Screen):

    def MainRollsOut(self):
        sm.current = "main"

    def infoOut(self):
        sm.current = "info"

    def basketOut(self):
        sm.current = "order"


class SaladsWindow(Screen):

    def MainSaladsOut(self):
        sm.current = "main"

    def infoOut(self):
        sm.current = "info"

    def basketOut(self):
        sm.current = "order"


class DessertWindow(Screen):

    def MainDessertOut(self):
        sm.current = "main"

    def infoOut(self):
        sm.current = "info"

    def basketOut(self):
        sm.current = "order"




class BasketWindow(Screen):

    def Out(self):
        sm.current = "main"


class  InfoWindow(Screen):

    def MenuOut(self):
        sm.current = "main"

    def logOut(self):
        sm.current = "login"

  










class WindowManager(ScreenManager):
    pass


def invalidLogin(self):
    pop = Popup(title='Неверный логин',
                  content=Label(text='Неправильное имя пользователя или пароль..'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()
    self.password.text = ""


def invalidForm(self):
    pop = Popup(title='Неверная форма',
                  content=Label(text='''
            Пожалуйста, заполните все поля 
            коректной информацией. 
            Примеры номеров телефонов: 
            +79120488575, 89120488575'''),
                  size_hint=(None, None), size=(400, 400))

    pop.open()
    self.password.text = ""


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), \
    BasketWindow(name="order"), InfoWindow(name="info"), PizzaWindow(name="pizza"), RollsWindow(name="rolls"), \
    SaladsWindow(name="salads"), DessertWindow(name="dessert")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):

        return sm


if __name__ == "__main__":
    MyMainApp().run()