from kivy.app import *
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.boxlayout import *
from kivy.uix.screenmanager import *
from kivy.uix.scrollview import *

class ScrButton(Button):
   def __init__(self,screen,direction='right',goal='main',**kwargs):
      super().__init__(**kwargs)
      self.screen=screen
      self.direction=direction
      self.goal=goal
   def on_press(self):
      self.screen.manager.transition.direction = self.direction
      self.screen.manager.current = self.goal

class MainScr(Screen):
   def __init__(self,**kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation='vertical',padding=8,spacing=8)
      hl = BoxLayout()
      txt= Label(text='Choose your Screen')
      vl.add_widget(ScrButton(self,direction='down',goal='first',text='1'))
      vl.add_widget(ScrButton(self,direction='left',goal='second',text='2'))
      vl.add_widget(ScrButton(self,direction='up',goal='third',text='3'))
      vl.add_widget(ScrButton(self,direction='right',goal='fourth',text='4'))
      hl.add_widget(txt)
      hl.add_widget(vl)
      self.add_widget(hl)

class FirstScr(Screen):
   def __init__(self,**kwargs):
      super().__init__(**kwargs)
      vl= BoxLayout(orientation='vertical', size_hint = (.5, .5), pos_hint = {"center_x":0.5, "center_y":0.5})
      btn = Button(text="Choice: 1", size_hint = (.5, 1), pos_hint = {"left":0})
      btn_back=ScrButton(self,direction='up',goal='main',text='Back')
      vl.add_widget(btn_back)
      vl.add_widget(btn)
      self.add_widget(vl)


class SecondScr(Screen):
   def __init__(self,**kwargs):
      super().__init__(**kwargs)
      vl = BoxLayout(orientation = "vertical")
      self.txt =Label(text ="Choice:2")
      vl.add_widget(self.txt)

      hl_0 = BoxLayout(size_hint = (0.8, None), height = "30sp")
      lbl1 = Label(text = "Enter something:", halign = "right")
      self.input = TextInput(multiline = False)
      hl_0.add_widget(lbl1)
      hl_0.add_widget(self.input)
      vl.add_widget(hl_0)


      hl= BoxLayout(size_hint = (0.5, 0.2), pos_hint = {"center_x":0.5})
      btn_false = Button(text = "OK!")
      btn_back=ScrButton(self,direction='right',goal='main',text='Back')
      hl.add_widget(btn_back)
      hl.add_widget(btn_false)
      vl.add_widget(hl)
      self.add_widget(vl)
      btn_false.on_press = self.change_text

         
   def change_text(self):
      if self.input.text=='something':
         self.txt.text='Well done! I proud of you!'
      else:
         self.txt.text ="It didn't work ..."



class ThirdScr(Screen):
   def __init__(self,**kwargs):
      super().__init__(**kwargs)
      vl= BoxLayout(orientation='vertical')
      btn_back=ScrButton(self,direction='down',goal='main',text='Back')
      test_label = Label(text = "Your screen")
      vl.add_widget(btn_back)
      vl.add_widget(test_label)
      self.add_widget(vl)

class FourthScr(Screen):
   def __init__(self,**kwargs):
      super().__init__(**kwargs)
      
      text= "How to Make Pancakes\nYou'll find a detailed ingredient list and step-by-step instructions in the recipe below, but let's go over the basics:\nPancake Ingredients:\nYou likely already have everything you need to make this pancake recipe. If not, here's what to add to your grocery list:\n- Flour: This homemade pancake recipe starts with all-purpose flour.\n- Baking powder: Baking powder, a leavener, is the secret to fluffy pancakes.\n- Sugar: Just a tablespoon of white sugar is all you'll need for subtly sweet pancakes.\n- Salt: A pinch of salt will enhance the overall flavor without making your pancakes taste salty.\n- Milk and butter: Milk and butter add moisture and richness to the pancakes.\n- Egg: A whole egg lends even more moisture. Plus, it helps bind the pancake batter together.\nHow to Make Pancakes From Scratch\nIt's not hard to make homemade pancakes, you just need a good recipe. That's where we come in! You'll find the step-by-step recipe below, but here's a brief overview of what you can expect:\n1. Sift the dry ingredients together.\n2. Make a well, then add the wet ingredients. Stir to combine.\n3. Scoop the batter onto a hot griddle or pan.\n4. Cook for two to three minutes, then flip.\n5. Continue cooking until brown on both sides."
      label=Label(text='Additional task', size_hint=(1,1))

      
      self.label=Label(text=text, font_size='20sp',halign='left',valign='top')
      self.label.bind(size=self.change_size)
      self.scroll=ScrollView(size_hint=(1,1))
      self.scroll.add_widget(self.label)


      vl= BoxLayout(orientation='vertical', spacing=8)
      btn_back=ScrButton(self,direction='left',goal='main',text='Back',size_hint=(1,.2),pos_hint={'center-x':0.5})
      vl.add_widget(label)
      vl.add_widget(btn_back)
      vl.add_widget(self.scroll)
      self.add_widget(vl)
   def change_size(self,*args):
      self.label.text_size=(self.label.width,None)
      self.label.texture_update()
      self.label.height=self.label.texture_size[1]

class MyApp(App):
   def build(self):
      sm=ScreenManager()
      sm.add_widget(MainScr(name='main'))
      sm.add_widget(FirstScr(name='first'))
      sm.add_widget(SecondScr(name='second'))
      sm.add_widget(ThirdScr(name='third'))
      sm.add_widget(FourthScr(name='fourth'))
      return sm

app=MyApp()
app.run()