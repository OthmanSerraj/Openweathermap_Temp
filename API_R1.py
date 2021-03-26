from LWA import LWA
from fastapi import FastAPI
R1_app = FastAPI()
@R1_app.get('/api/meteo/vent/{ville}')
async def index(ville):
    New_ville_infos=LWA(ville)
    New_ville_infos.get_speed()
    New_ville_infos.get_deg()
    return {"vitesse":New_ville_infos.get_speed(),
    "degre":New_ville_infos.get_deg()}
@R1_app.get('/api/meteo/tempmax/{nville}')
async def index(nville):
    ville_infos=LWA(nville)
    return ville_infos.get_max_tempnhday()
#Execute: uvicorn API_R1:R1_app --reload