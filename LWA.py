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
        zero_day=self.city_5days_infos["list"][0]["dt_txt"].split()[0]
        maxtp=-273.15#zero absolu
        wanted_date=""
        Lista=[]
        for num,elm in enumerate(self.city_5days_infos["list"]):
            date=elm["dt_txt"]
            actual_day=date.split()[0]
            if zero_day!=actual_day:
                Lista.append({"Date":wanted_date,"max_temp":maxtp})
                zero_day=actual_day
                maxtp=-273.15#zero absolu
            mytemp=elm["main"]["temp_max"]
            if mytemp>maxtp:
                maxtp=mytemp
                wanted_date=elm["dt_txt"]
        return Lista

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
# if __name__== "__main__":
#     location="paris"
#     Z=LWA(location)
#     print(Z.get_last_weather())
