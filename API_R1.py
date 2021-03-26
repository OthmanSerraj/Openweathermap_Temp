from LWA import LWA
from fastapi import FastAPI
R1_app = FastAPI()
@R1_app.get('/api/meteo/vent/')
async def get_speed_deg(ville:str):
    New_ville_infos=LWA(ville)
    return {"vitesse":New_ville_infos.get_speed(),
    "degre":New_ville_infos.get_deg()}
@R1_app.get('/api/meteo/tempmax/')
async def get_maxtemp_5day(ville:str):
    ville_infos=LWA(ville)
    return ville_infos.get_max_tempnhday()
#Execute: uvicorn API_R1:R1_app --reload, example: http://localhost:8000/api/meteo/vent/?ville=paris or http://localhost:8000/api/meteo/tempmax/?ville=dakar
