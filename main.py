from kivymd.app import MDApp
from kivy.lang import Builder

kv = """

Screen:
   AnchorLayout:
      
      MDRaisedButton:
         text:"hello"

"""

class App(MDApp):
   def build(self):
      return Builder.load_string(kv)
      
App().run()