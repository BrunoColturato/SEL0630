from picamera import PiCamera, Color
from time import sleep
from requests import get
import json
from pprint import pprint

# Obtendo dados do clima
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'

weather = get(url).json()['items']
temperatura = weather[0]["ambient_temp"]
data = weather[0]["created_on"]
created = weather[0]["created_by"]

# Camera da Rasp
camera = PiCamera()

# Configuracoes da camera
camera.resolution = (1920, 1080)
camera.framerate = 15

# Adicionando efeito
effect = 'cartoon'
camera.image_effect = effect

# Adicionando texto
camera.annotate_background = Color('black')
camera.annotate_text = f"Bruno 11200251 Alessandro 11233891 \nTemperatura: {temperatura} \nData: {data} \nCriado por: {created}"

# Tirando foto com efeito e texto
camera.start_preview()
sleep(5)
camera.capture('/home/sel/workab/bruno_alessandrox.jpg')
camera.stop_preview()

# Gravando video
# Modificando a anotacao
camera.annotate_background = None
camera.annotate_text = "Bruno 11200251 Alessandro 11233891"

# Realizando gravacao
camera.start_preview()
camera.start_recording('/home/sel/workab/videox.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
