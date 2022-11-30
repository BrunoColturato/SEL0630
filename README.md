# SEL0630
Prática 6 de SEL0630 - Aplicações de Microprocessadores II (2022).

Alunos:

* Alessandro de Freitas Guerreiro - NUSP 11233891
* Bruno Alvarenga Colturato - NUSP 11200251
# Bibliotecas

Neste projeto foi necessária a utilização das bibliotecas  Python: `picamera`, `time`, `requests`, `json` e `pprint`. Para a instalação, utilize, se necessário, os camandos:

```
    pip install picamera
    pip install time
    pip install requests
    pip install json
    pip install pprint
```

As bibliotecas foram importada como abaixo.

``` python
from picamera import PiCamera, Color
from time import sleep
from requests import get
import json
from pprint import pprint
```

# Código

## Acesso à API
Para obter dados de uma base climática, é necessário acessar a API por meio de uma `url`, como no código abaixo. O valor `966583` na `url` é referente ao ID da base climática instalada na UFSC. Por meio do comando `get(url)` é feita a requisição à API. O comando `get(url).json()['items']` transforma os dados obtidos da API e os organiza em uma arquivo `JSON`.

``` python
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'

weather = get(url).json()['items']
temperatura = weather[0]["ambient_temp"]
data = weather[0]["created_on"]
created = weather[0]["created_by"]
```

## Camera da Raspberry Pi

### Configurações
Para manipular a câmera da Raspberry Pi, é necessário instanciar um objeto `PiCamera()` e definir algumas configurações.

``` python
# Camera da Rasp
camera = PiCamera()

# Configuracoes da camera
camera.resolution = (1920, 1080)
camera.framerate = 15
```

É possível adicionar efeitos (`camera.image_effect`) e texto à imagem capturada, como exemplificado abaixo. Para anotações, é possível modificar a cor de fundo do texto (`camera.annotate_background`) e definir o texto (`camera.annotate_text`). No caso, o texto contém o nome dos integrantes do grupo e alguns dados obtidos da API de clima.

``` python
# Adicionando efeito
effect = 'cartoon'
camera.image_effect = effect

# Adicionando texto
camera.annotate_background = Color('black')
camera.annotate_text = f"Bruno 11200251 Alessandro 11233891\nTemperatura: {temperatura} \nData: {data} \nCriado por: {created}"
```

### Tirando foto
Foi utilizado o código abaixo para tirar uma foto com a rasp. É necessário iniciar um *preview* (`camera.start_preview`), dar um tempo de *delay* para posicionamento manual da câmera (`sleep`) e entao fazer a captura passando o caminho do diretório onde deve ser armazenada a imagem (`camera.capture`).

``` python
# Tirando foto com efeito e texto
camera.start_preview()
sleep(5)
camera.capture('/home/sel/workab/bruno_alessandrox.jpg')
camera.stop_preview()
```

### Gravando vídeo
Gravar um vídeo com a câmera da rasp é semelhante a tirar uma foto, como mostrado no código abaixo. Entretanto, é necessário iniciar a gravação (`camera.start_recording`) e finalizar (`camera.stop_recording`). Note que o tempo de gravação foi determinado por meio da função `sleep` entre o início e fim da gravação.

``` python
# Modificando a anotacao
camera.annotate_background = None
camera.annotate_text = "Bruno 11200251 Alessandro 11233891"

# Realizando gravacao
camera.start_preview()
camera.start_recording('/home/sel/workab/videox.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
```

# Resultados

A imagem e o vídeo obtidos com o código são apresentados abaixo.

![bruno_alessandro](https://github.com/BrunoColturato/SEL0630/blob/main/photos/bruno_alessandro.jpg)

[![Watch the video](https://github.com/BrunoColturato/SEL0630/blob/main/photos/bruno_alessandro.jpg)](https://github.com/BrunoColturato/SEL0630/blob/main/videos/video.mp4)



