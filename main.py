from kivy.lang import Builder
Builder.load_file('main_menu/menu.kv')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty

# menu is now ScreenOne
import main_menu.menu

class ScreenTwo(Screen):
    pass
    
class ScreenThree(Screen):
    
    #def on_enter(self):
    #def on_leanve(self):
    pass

class Manager(ScreenManager):
    
    main_menu = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)


class ScreensApp(App):
    
    def build(self):
        m = Manager(transition=WipeTransition())
        return m
    
    
if __name__ == '__main__':
    ScreensApp().run()
