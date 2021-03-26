import os
import json
import requests
os.chdir("C:\\Users\\User\\Desktop\\LipWeatherApi")#optional to be changed in real world
class LWA:
    def __init__(self,location):
        self.api_key=self.get_api_key()#insert api key here
        self.location=location
        self.city_last_infos=self.get_last_weather()
        self.city_5days_infos=self.get_weather_forecast()
    @staticmethod
    def get_api_key():
        with open("api_key_store.json") as f:
            mydict=json.load(f)
            api_key=mydict["api_key"]
        return api_key
    def get_last_weather(self):
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(self.location, self.api_key)
        r = requests.get(url)
        return r.json()
    def get_weather_forecast(self):
        url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format(self.location, self.api_key)
        r = requests.get(url)
        return r.json()
    def get_max_tempnhday(self):
        maxtp=-273.15#zero absolu
        znum=0
        for num,elm in enumerate(self.city_5days_infos["list"]):
            mytemp=elm["main"]["temp_max"]
            if mytemp>maxtp:
                maxtp=mytemp
                znum=num
        date=self.city_5days_infos["list"][znum]["dt_txt"]
        return {"Date":date,"max_temp":maxtp}

    def get_speed(self):
        speed=self.city_last_infos["wind"]["speed"]
        return speed
    def get_deg(self):
        deg=self.city_last_infos["wind"]["deg"]
        return deg
    def help_me_debug(self,open_show=True):
        file_store_temp="new_removable.json"
        with open(file_store_temp,"w") as fr:
            json.dump(self.city_5days_infos, fr,indent=3)
        if open_show:os.startfile(file_store_temp)
if __name__== "__main__":
    location="dublin"
    Z=LWA(location)
    print(Z.get_last_weather())