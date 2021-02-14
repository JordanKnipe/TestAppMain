

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import requests
import json



class WindowManager(ScreenManager):
    pass





class CreateLobbyWindow(Screen):
    yourName = ObjectProperty(None)
    mobileNumber = ObjectProperty(None)



    def SubmitLobby(self):
        print("Entering")
       # if self.lobbyName != "" and self.yourName != "" and self.password != "":

        sm.current = "lobby"


    def ReturnToMenu(self):
        sm.current = "main"

class MainWindow(Screen):
    print("mainWindow")
    def createBtn(self):
        #self.reset()
        sm.current = "create"





class LobbyWindow(Screen):
    longText = ObjectProperty(None)
    latText = ObjectProperty(None)
    print("in Lobby")
    def SendLocation(self):
        send_url = "http://api.ipstack.com/check?access_key=bc579ad140f186811b7bdc104b90e1d9"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        city = geo_json['city']
        print("Sending")
        self.latText.text = str(latitude)
        self.longText.text = str(longitude)
    current = ""

kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [CreateLobbyWindow(name="create"), MainWindow(name="main"), LobbyWindow(name="lobby")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()


