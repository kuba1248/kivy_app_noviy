import kivy
# from tkinter import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from kivy.lang import Builder

from kivy.lang import Builder
import random


Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition

<CustomScreen>:
    hue: random()
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size

    Label:
        font_size: 42
        text: root.name

    Button:
        text: 'Next screen'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_release: root.manager.current = root.manager.next()

    Button:
        text: 'Previous screen'
        size_hint: None, None
        size: 150, 50
        on_release: root.manager.current = root.manager.previous()

    BoxLayout:
        size_hint: .5, None
        height: 250
        pos_hint: {'center_x': .5}
        orientation: 'vertical'

        Button:
            text: 'Use SlideTransition with "up" direction'
            on_release: root.manager.transition = \
                        SlideTransition(direction="up")

        Button:
            text: 'Use SlideTransition with "down" direction'
            on_release: root.manager.transition = \
                        SlideTransition(direction="down")

        Button:
            text: 'Use SlideTransition with "left" direction'
            on_release: root.manager.transition = \
                        SlideTransition(direction="left")

        Button:
            text: 'Use SlideTransition with "right" direction'
            on_release: root.manager.transition = \
                        SlideTransition(direction="right")

        Button:
            text: 'Use SwapTransition'
            on_release: root.manager.transition = SwapTransition()

        Button:
            text: 'Use WipeTransition'
            on_release: root.manager.transition = WipeTransition()

        Button:
            text: 'Use FadeTransition'
            on_release: root.manager.transition = FadeTransition()

        Button:
            text: 'Use FallOutTransition'
            on_release: root.manager.transition = FallOutTransition()

        Button:
            text: 'Use RiseInTransition'
            on_release: root.manager.transition = RiseInTransition()
        Button:
            text: 'Use NoTransition'
            on_release: root.manager.transition = NoTransition(duration=0)
''')

class MyNote(TextInput):
    pass

class MyNote2(TextInput):
    pass

class MyNote3(TextInput):
    pass

class MyNote4(TextInput):
    pass

class MyNote5(TextInput):
    pass

class MyNote6(TextInput):
    pass

class MyNote7(TextInput):
    pass

class MyNote8(TextInput):
    pass

class MyNote9(TextInput):
    pass

class MyNote10(TextInput):
    pass

class MyNote11(TextInput):
    pass

class MyNote12(TextInput):
    pass

class MyNote13(TextInput):
    pass

class MyNote14(TextInput):
    pass

class MyNote15(TextInput):
    pass

class MyNote16(TextInput):
    pass

class MyNote17(TextInput):
    pass

class MyNote18(TextInput):
    pass

class MyNote(TextInput):
    pass

class MainNotesBoxLayout(BoxLayout):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainNotesBoxLayout, self).__init__(**kwargs)
        self.container.bind(minimum_height=self.container.setter('height'))
        self.add_text_inputs()

        
        # btn2 = Button(text="Обновить",
        #            font_size ="20sp",
        #            background_color =(1, 1, 1, 1),
        #            color =(1, 1, 1, 1),
        #            size_hint =(1, .1),
        #            pos =(1, 1))
        # self.add_widget(btn2)

        self.btn = Button(text="Обновить",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size_hint =(1, .1),
                   pos =(1, 1),
                   on_press = self.add_text_inputs2)
       
        self.add_widget(self.btn)


    def add_text_inputs2(self, *args):
        
        # my_note = MyNote4()
        # self.container.remove_widget(self.my_note)
        self.container.remove_widget(self.my_note1)
        self.container.remove_widget(self.my_note2)
        self.container.remove_widget(self.my_note3)
        self.container.remove_widget(self.my_note4)
        self.container.remove_widget(self.my_note5)
        self.container.remove_widget(self.my_note6)

        for x in range(7):
            if x == 0:
                   # self.container.remove_widget(self.my_note)
                    self.my_note4 = MyNote4()
                    self.container.add_widget(self.my_note4)
            
            elif x == 1:
                randnumb = random.randrange(0, 5) 
                if randnumb == 0:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note1 = MyNote9()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 1:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note1 = MyNote10()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 2:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note1 = MyNote11()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 3:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note1 = MyNote12()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 4:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note1 = MyNote13()
                    self.container.add_widget(self.my_note1)

            elif x == 2:    
               # self.container.remove_widget(self.my_note)
                self.my_note5 = MyNote5()
                self.container.add_widget(self.my_note5)
            
            elif x == 3:
                randnumb = random.randrange(5, 10) 
                if randnumb == 5:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note2 = MyNote14()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 6:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note2 = MyNote15()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 7:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note2 = MyNote16()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 8:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note2 = MyNote17()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 9:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note2 = MyNote18()
                    self.container.add_widget(self.my_note2)

            elif x == 4:
                #self.container.remove_widget(self.my_note)
                self.my_note6 = MyNote6()
                self.container.add_widget(self.my_note6)

            elif x == 5:
                randnumb = random.randrange(10, 15) 
                if randnumb == 10:
                #    self.container.remove_widget(self.my_note)
                    self.my_note3 = MyNote()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 11:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note3 = MyNote2()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 12:
                 #   self.container.remove_widget(self.my_note)
                    self.my_note3 = MyNote3()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 13:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note3 = MyNote7()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 14:
                  #  self.container.remove_widget(self.my_note)
                    self.my_note3 = MyNote8()
                    self.container.add_widget(self.my_note3)




    def add_text_inputs(self, *args):
        
        for x in range(7):
            if x == 0:
                self.my_note4 = MyNote4()
                self.container.add_widget(self.my_note4)
            
            elif x == 1:
                randnumb = random.randrange(0, 5) 
                if randnumb == 0:
                    self.my_note1 = MyNote9()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 1:
                    self.my_note1 = MyNote10()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 2:
                    self.my_note1 = MyNote11()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 3:
                    self.my_note1 = MyNote12()
                    self.container.add_widget(self.my_note1)
                elif randnumb == 4:
                    self.my_note1 = MyNote13()
                    self.container.add_widget(self.my_note1)

            elif x == 2:    
                self.my_note5 = MyNote5()
                self.container.add_widget(self.my_note5)
            
            elif x == 3:
                randnumb = random.randrange(5, 10) 
                if randnumb == 5:
                    self.my_note2 = MyNote14()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 6:
                    self.my_note2 = MyNote15()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 7:
                    self.my_note2 = MyNote16()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 8:
                    self.my_note2 = MyNote17()
                    self.container.add_widget(self.my_note2)
                elif randnumb == 9:
                    self.my_note2 = MyNote18()
                    self.container.add_widget(self.my_note2)

            elif x == 4:
                self.my_note6 = MyNote6()
                self.container.add_widget(self.my_note6)
 
            elif x == 5:
                randnumb = random.randrange(10, 15) 
                if randnumb == 10:
                    self.my_note3 = MyNote()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 11:
                    self.my_note3 = MyNote2()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 12:
                    self.my_note3 = MyNote3()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 13:
                    self.my_note3 = MyNote7()
                    self.container.add_widget(self.my_note3)
                elif randnumb == 14:
                    self.my_note3 = MyNote8()
                    self.container.add_widget(self.my_note3)

    # def update(self,*args):
    #     self.main_label.text = 'change to change'

    
class CitatyApp(App):
    def build(self):
        return MainNotesBoxLayout()


if __name__ == '__main__':
    CitatyApp().run()