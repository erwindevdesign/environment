<a name="readme-top"></a>
<!-- 

Etiquetas Sugeridas:

python, virtualenv, venv, environment, dependencies, development, best practices, tutorial


 -->
<div align="center">
  <h1>ENVIROMENT</h1>
  <h2>Entornos Virtuales Python: </h2><h3>Una Guía Práctica para Desarrolladores</h3>
</div>
<br>

<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)<br> -->

<a title="python language icon" href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python"></a>   



El desarrollo de aplicaciones en lenguaje de programación Python, usualmente hace uso de diversas versiones de paquetes y módulos que requieren una especificidad de versión en su librería. Esto crea la necesidad de aislar estos requerimientos sin crear conflicto al trabajar en diferentes proyectos, esto haciendo uso de los entornos virtuales (venv).

Este repositorio es una referencia para desarrolladores que desean comprender y dominar la creación y gestión de entornos virtuales. A través de ejemplos prácticos y explicaciones detalladas, exploraremos los conceptos fundamentales de los entornos virtuales, su importancia en el desarrollo de proyectos Python y las mejores prácticas para su uso.


## Introducción

* **[¿Qué es un entorno virtual?](#what-is)**
* **[¿Por qué utilizar entornos virtuales?](#why-use)**


<details>
  <summary><b>📋 Contenido</b></summary>
    <ol>
      <li>
        <a href="#introduction" >Introducción</a>
          <ol>
            <li>
              <a href="#what-is" >
                ¿Qué es un entorno virtual y su importancia en el desarrollo?
              </a>
            </li>
            <li>
              <a href="#why-use" >
                ¿Por qué utilizar entornos virtuales?
              </a>
            </li>
          </ol>
      </li>
      <li>
        <a href="#create-virtual-environment">
          Creación de un Entorno Virtual: 
        </a>
          <ol>
            <li>
              <a href="#new-virtual-environment" >
                Crear un nuevo entorno con venv.
                </a>
            </li>
            <li>
              <a href="#activate-deactivate" >
                Activación y desactivación del entorno.
              </a>
            </li>
            <li>
              <a href="#install-packages" >
                Instalación de paquetes con pip.
              </a>
            </li>
            <li>
              <a href="#example-01" >
                Ejemplo completo.
              </a>
            </li>
          </ol>
      </li>
      <li>
        <a href="#package-management" >Gestión de Paquetes:</a>
          <ol>
            <li>Creación de un archivo requirements.txt.</li>
            <li>Instalación de paquetes desde requirements.txt.</li>
            <li>Actualización y eliminación de paquetes.</li>
          </ol>        
      </li>
      <li>
        <a href="#best-practices" >Mejores prácticas:</a>
          <ol>
            <li>Estructura de directorios recomendada.</li>
            <li>Uso de .gitignore para excluir archivos innecesarios.</li>
            <li>Automatización de la creación de entornos con scripts.</li>
          </ol>        
      </li>
      <li>
        <a href="#" >Ejemplos Prácticos:</a>
          <ol>
            <li>Creación de entornos para diferentes proyectos (Django, Flask, Machine Learning).</li>
            <li>Resolución de problemas comunes.</li>
          </ol>
      </li>
      <li>
        <a href="#" >Herramientas Adicionales:</a>
          <ol>
            <li>Integración con IDEs (Visual Studio Code, PyCharm).</li>
            <li>Uso de Docker para la contenerización de entornos.</li>
          </ol>
      </li>
    </ol>
</details>

<a name="introduction"></a>

#### Introducción

<a name="what-is"></a>

<div align="center">
  <p style="font-weight: bolder;">¿Qué es un entorno virtual y su importancia en el desarrollo?</p>
</div>
<br>

Un entorno virtual en Python es un directorio aislado que contiene una instalación de Python y todos los paquetes instalados dentro de él. Este aislamiento garantiza que las dependencias de un proyecto particular no interfieran con otros proyectos, evitando conflictos de versiones y asegurando un entorno de desarrollo consistente y reproducible.

<a name="why-use"></a>

<div align="center">
  <p style="font-weight: bolder;">¿Por qué utilizar entornos virtuales?</p>
</div>
<br>

 **Aislamiento de proyectos** 
    
- **Evita conflictos:** Cada proyecto puede tener sus propias versiones de paquetes, evitando colisiones entre diferentes versiones de una misma librería.
    
- **Gestión independiente:** Realiza actualizaciones de paquetes en un entorno sin afectar otros proyectos.

**Reproducibilidad** 

- **Entornos consistentes:** Garantiza que tu proyecto se ejecute de la misma manera en cualquier entorno donde se instale.

- **Facilita la colaboración:** Permite a otros desarrolladores configurar fácilmente el proyecto sin conflictos de versiones.

- **Simplifica la implementación:** Facilita la implementación en servidores de producción con las mismas dependencias.

**Colaboración** 

- **Proyectos aislados:** Cada desarrollador puede tener su propio entorno virtual, evitando interferencias entre diferentes estilos de trabajo.

- **Facilita la revisión de código:** Permite a los revisores recrear el entorno del proyecto para evaluar los cambios.

- **Mejora la gestión de equipos:** Facilita la gestión de múltiples proyectos y equipos.

**Otros beneficios**

- **Distribución:** Permite empaquetar aplicaciones con sus dependencias exactas, asegurando una instalación sin problemas en diferentes sistemas.

- **Limpieza:** Evita la contaminación del entorno de Python global, lo que facilita la gestión de múltiples proyectos.

- **Optimización de recursos:** Evita la instalación innecesaria de paquetes globales.

- **Mejora la seguridad:** Reduce el riesgo de instalar paquetes vulnerables.

- **Facilita la experimentación:** Permite probar nuevas versiones de paquetes sin afectar el proyecto principal.

- **Integración con herramientas de CI/CD:** Se integra fácilmente con herramientas de integración continua y entrega continua para automatizar procesos de construcción y despliegue.

En **resumen**, los entornos virtuales son una herramienta esencial para cualquier desarrollador Python que trabaje en múltiples proyectos o que necesite garantizar la reproducibilidad y consistencia de sus aplicaciones.

<a name="create-virtual-environment"></a>

#### Creación de Entorno Virtual

<a name="new-virtual-environment"></a>

##### ⅰ. Crea un nuevo entorno con venv.

1. Abre tu terminal o línea de comandos.

2. Navega al directorio donde deseas crear tu proyecto.

3. Ejecuta el siguiente comando para crear un nuevo entorno virtual:
    ~~~sh
    python -m venv mi_entorno_virtual
    ~~~
    *Reemplaza el nombre* `mi_entorno_virtual`*, con el nombre que desees para tu entorno.*

<a name="activate-deactivate"></a>

##### ⅱ. Activación y desactivación del entorno.

1. Activación

    - Windows:
    ~~~
    mi_entorno_virtual\Scripts\activate
    ~~~
    - Linux/macOS:
    ~~~
    source mi_entorno_virtual/bin/activate
    ~~~
    - *Una vez activado, verás el nombre del entorno, entre paréntesis, al principio de la línea de comandos.*

2. Desactivación
   
    ~~~
    deactivate
    ~~~
  
<a name="install-packages"></a>

#### ⅲ. Instalación de paquetes con pip.

Instala las dependencias requeridas para realizar tu proyecto.

~~~sh
pip install requests
~~~

<a name="example-01"></a>

##### ⅳ. Ejemplo Completo

~~~sh
# Posicionate en el directorio de tu proyecto
cd mi_proyecto

# Crea un entorno virtual llamado 'venv'
python -m venv venv

# Activa el entorno virtual
source venv/bin/activate

# Instala un paquete
pip install requests

# Desactiva el entorno virtual
deactivate
~~~

<a name="package-management"></a>

#### Gestión de Paquetes

Para la colaboración de código, es indispensable proporcionar a la comunidad la versión exacta de las dependencias que requiere nuestro software para su funcionamiento. Para ello, crearemos y respaldaremos dichas dependencias en un archivo **requirements.txt**.

##### ⅰ. Creación de un archivo requirements.txt.
~~~
touch requirements.txt
~~~
~~~
touch requirements.txt
~~~

##### ⅱ. Instalación de paquetes desde requirements.txt.

~~~sh
pip install -r requirements.txt
~~~


##### ⅲ. Actualización y eliminación de paquetes.

1. Actualización de Paquetes

    Instala la nueva versión del paquete:
    ~~~sh
    pip install <nombre_del_paquete>==<nueva_versión>
    ~~~

    Por ejemplo, para actualizar `requests` a la versión 2.28.1:

    ~~~sh
    pip install requests==2.28.1
    ~~~

2. Congela las dependencias.

    Para actualizar el archivo `requirements.txt` con las nuevas versiones instaladas:

    ~~~sh
    pip freeze > requirements.txt
    ~~~

3. Eliminando paquetes

    Desinstala el paquete.
    ~~~sh
    pip uninstall <nombre_del_paquete>
    ~~~

    Por ejemplo, para desinstalar `numpy`:
    ~~~sh
    pip uninstall numpy
    ~~~

<a name="best-practices"></a>

#### Mejores prácticas

##### i. Estructura de directorios recomendada.

Al crear un entorno virtual, se crea un directorio con la siguiente estructura (puede variar ligeramente según la versión de Python):

~~~mk
mi_entorno_virtual/
├── bin/
│   ├── activate
│   ├── python
│   └── ...
├── include/
├── lib/
└── pyvenv.cfg
~~~

##### ii. Uso de .gitignore para excluir archivos innecesarios.





Tecnologías y Herramientas:

  Python
  venv
  virtualenv
  pip
  Editores de código (Visual Studio Code, PyCharm, etc.)









---
---
---

~~~sh
sudo apt installl -y python3-venv
~~~

FIJAR nuestro entorno virtual en la carpeta del proyecto:

~~~sh*
python3 -m venv env
~~~

ACTIVAR entorno virtual

~~~sh
source env/bin/activate
~~~

DESACTIVAR entorno virtual:

~~~sh
deactivate
~~~

Revisar desde donde se ejecuta Python:

~~~sh
which python3
~~~

Revisar desde donde se ejecuta pip:

~~~sh
which pip3
~~~

INSTALAR dependencias con el entorno virtual activado:

~~~sh
pip3 install matplotlib
~~~

REVISAR dependencias instaladas:

~~~sh
pip3 freeze
~~~

INSTALAR dependencia espesifica por version:

~~~sh
python -m venv env
~~~

ARCHIVO requirements.txt para instalación de dependencias:

~~~sh

❯ pip3 freeze > requiremments.txt

❯ ls
charts.py  env  main.py  __pycache__  requiremments.txt

❯ cat requiremments.txt
contourpy==1.0.5
cycler==0.11.0
fonttools==4.38.0
kiwisolver==1.4.4
matplotlib==3.6.1
numpy==1.23.4
packaging==21.3
Pillow==9.2.0
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0

~~~

INSTALAR dependencias desde archivo requirements.txt

~~~sh
pip3 install -r requirements.txt
~~~




## Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

terminal:

~~~sh
cd game
python3 main.py
~~~

## App Project

~~~sh
> git clone

> cd app

>* python3 -m venv env

> source env/bin/activate

> pip3 install - requirements.txt

> python3 main.py
~~~


## FAKEAPI 
Recurso
~~~
https://api.escuelajs.co/api/v1/categories
~~~

## Status code

200 en https significa todo OK


CONECTAR con un server:


~~~sh

❯ mkdir web-server
❯ ls
charts  main.py  python  python2  README.md  web-server
❯ cd web-server
❯ ls
❯ ls
❯ python3 -m venv env
ls
❯ ls
env
❯ source env/bin/activate
❯ which python3
/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/bin/python3
❯ pip3 install requests
Collecting requests
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 KB 232.7 kB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.4-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.5/61.5 KB 180.4 kB/s eta 0:00:00
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.12-py2.py3-none-any.whl (140 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 140.4/140.4 KB 651.5 kB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2022.9.24-py3-none-any.whl (161 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 161.1/161.1 KB 646.0 kB/s eta 0:00:00
Collecting charset-normalizer<3,>=2
  Downloading charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2022.9.24 charset-normalizer-2.1.1 idna-3.4 requests-2.28.1 urllib3-1.26.12
❯ pip3 freeze
certifi==2022.9.24
charset-normalizer==2.1.1
idna==3.4
requests==2.28.1
urllib3==1.26.12
❯ pip freeze > requeriments.txt
❯ ls
env  requeriments.txt

❯ python3 main.py
200
[{"id":1,"name":"Clothes","image":"https://api.lorem.space/image/fashion?w=640&h=480&r=752"},{"id":2,"name":"Electronics","image":"https://api.lorem.space/image/watch?w=640&h=480&r=4869"},{"id":3,"name":"Furniture","image":"https://api.lorem.space/image/furniture?w=640&h=480&r=5876"},{"id":4,"name":"Shoes","image":"https://api.lorem.space/image/shoes?w=640&h=480&r=7342"},{"id":5,"name":"Others","image":"https://api.lorem.space/image?w=640&h=480&r=9995"}]
❯ python3 main.py
200
[{"id":1,"name":"Clothes","image":"https://api.lorem.space/image/fashion?w=640&h=480&r=752"},{"id":2,"name":"Electronics","image":"https://api.lorem.space/image/watch?w=640&h=480&r=4869"},{"id":3,"name":"Furniture","image":"https://api.lorem.space/image/furniture?w=640&h=480&r=5876"},{"id":4,"name":"Shoes","image":"https://api.lorem.space/image/shoes?w=640&h=480&r=7342"},{"id":5,"name":"Others","image":"https://api.lorem.space/image?w=640&h=480&r=9995"}]
<class 'str'>
❯ python3 main.py
200
[{"id":1,"name":"Clothes","image":"https://api.lorem.space/image/fashion?w=640&h=480&r=752"},{"id":2,"name":"Electronics","image":"https://api.lorem.space/image/watch?w=640&h=480&r=4869"},{"id":3,"name":"Furniture","image":"https://api.lorem.space/image/furniture?w=640&h=480&r=5876"},{"id":4,"name":"Shoes","image":"https://api.lorem.space/image/shoes?w=640&h=480&r=7342"},{"id":5,"name":"Others","image":"https://api.lorem.space/image?w=640&h=480&r=9995"}]
<class 'str'>
Clothes
Electronics
Furniture
Shoes
Others


~~~
IMPRIMIR HTML desde el servidor FastAPI


~~~sh

❯ pip3 freeze
certifi==2022.9.24
charset-normalizer==2.1.1
idna==3.4
requests==2.28.1
urllib3==1.26.12
❯ pip3 install fastapi
Collecting fastapi
  Downloading fastapi-0.86.0-py3-none-any.whl (55 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.5/55.5 KB 192.5 kB/s eta 0:00:00
Collecting pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2
  Downloading pydantic-1.10.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 6.7 MB/s eta 0:00:00
Collecting starlette==0.20.4
  Downloading starlette-0.20.4-py3-none-any.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.6/63.6 KB 1.0 MB/s eta 0:00:00
Collecting anyio<5,>=3.4.0
  Downloading anyio-3.6.2-py3-none-any.whl (80 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.6/80.6 KB 1.2 MB/s eta 0:00:00
Collecting typing-extensions>=4.1.0
  Downloading typing_extensions-4.4.0-py3-none-any.whl (26 kB)
Collecting sniffio>=1.1
  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)
Requirement already satisfied: idna>=2.8 in ./env/lib/python3.10/site-packages (from anyio<5,>=3.4.0->starlette==0.20.4->fastapi) (3.4)
Installing collected packages: typing-extensions, sniffio, pydantic, anyio, starlette, fastapi
Successfully installed anyio-3.6.2 fastapi-0.86.0 pydantic-1.10.2 sniffio-1.3.0 starlette-0.20.4 typing-extensions-4.4.0
❯ pip3 install "uvicorn[standard]"
Collecting uvicorn[standard]
  Downloading uvicorn-0.19.0-py3-none-any.whl (56 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.6/56.6 KB 222.8 kB/s eta 0:00:00
Collecting h11>=0.8
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 KB 855.4 kB/s eta 0:00:00
Collecting click>=7.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 KB 1.4 MB/s eta 0:00:00
Collecting websockets>=10.0
  Downloading websockets-10.4-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (106 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 106.8/106.8 KB 679.9 kB/s eta 0:00:00
Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0
  Downloading uvloop-0.17.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.1/4.1 MB 3.7 MB/s eta 0:00:00
Collecting watchfiles>=0.13
  Downloading watchfiles-0.18.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 3.4 MB/s eta 0:00:00
Collecting pyyaml>=5.1
  Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 682.2/682.2 KB 4.7 MB/s eta 0:00:00
Collecting httptools>=0.5.0
  Downloading httptools-0.5.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (414 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 414.1/414.1 KB 3.2 MB/s eta 0:00:00
Collecting python-dotenv>=0.13
  Downloading python_dotenv-0.21.0-py3-none-any.whl (18 kB)
Requirement already satisfied: anyio<4,>=3.0.0 in ./env/lib/python3.10/site-packages (from watchfiles>=0.13->uvicorn[standard]) (3.6.2)
Requirement already satisfied: idna>=2.8 in ./env/lib/python3.10/site-packages (from anyio<4,>=3.0.0->watchfiles>=0.13->uvicorn[standard]) (3.4)
Requirement already satisfied: sniffio>=1.1 in ./env/lib/python3.10/site-packages (from anyio<4,>=3.0.0->watchfiles>=0.13->uvicorn[standard]) (1.3.0)
Installing collected packages: websockets, uvloop, pyyaml, python-dotenv, httptools, h11, click, watchfiles, uvicorn
Successfully installed click-8.1.3 h11-0.14.0 httptools-0.5.0 python-dotenv-0.21.0 pyyaml-6.0 uvicorn-0.19.0 uvloop-0.17.0 watchfiles-0.18.0 websockets-10.4
❯ pip3 freeze
anyio==3.6.2
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
fastapi==0.86.0
h11==0.14.0
httptools==0.5.0
idna==3.4
pydantic==1.10.2
python-dotenv==0.21.0
PyYAML==6.0
requests==2.28.1
sniffio==1.3.0
starlette==0.20.4
typing_extensions==4.4.0
urllib3==1.26.12
uvicorn==0.19.0
uvloop==0.17.0
watchfiles==0.18.0
websockets==10.4
❯ pip3 freeze > requeriments.txt
❯ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20262] using WatchFiles
INFO:     Started server process [20267]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:44416 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:57560 - "GET /contact HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 419, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__
    return await self.app(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/fastapi/applications.py", line 270, in __call__
    await super().__call__(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/applications.py", line 124, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/middleware/errors.py", line 184, in __call__
    raise exc
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/middleware/errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/middleware/exceptions.py", line 75, in __call__
    raise exc
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/middleware/exceptions.py", line 64, in __call__
    await self.app(scope, receive, sender)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/routing.py", line 680, in __call__
    await route.handle(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/routing.py", line 275, in handle
    await self.app(scope, receive, send)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/routing.py", line 65, in app
    response = await func(request)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/fastapi/routing.py", line 235, in app
    raw_response = await run_endpoint_function(
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/fastapi/routing.py", line 163, in run_endpoint_function
    return await run_in_threadpool(dependant.call, **values)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/starlette/concurrency.py", line 41, in run_in_threadpool
    return await anyio.to_thread.run_sync(func, *args)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/anyio/to_thread.py", line 31, in run_sync
    return await get_asynclib().run_sync_in_worker_thread(
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 937, in run_sync_in_worker_thread
    return await future
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/env/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 867, in run
    result = context.run(func, *args)
  File "/home/erwin/Documentos/Desarrollo Web/python/PIP_and_Virtualenv/web-server/./main.py", line 12, in get_list
    return{name: 'Platzi'}
NameError: name 'name' is not defined
INFO:     127.0.0.1:57574 - "GET /favicon.ico HTTP/1.1" 404 Not Found
WARNING:  WatchFiles detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [20267]
INFO:     Started server process [20577]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:47552 - "GET /contact HTTP/1.1" 200 OK
WARNING:  WatchFiles detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [20577]
INFO:     Started server process [22236]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [22236]
INFO:     Started server process [22363]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
WARNING:  WatchFiles detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [22363]
INFO:     Started server process [22451]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:32930 - "GET /contact HTTP/1.1" 200 OK
Title desde main.py

I a text in p Title desde main.py

I a text in p ^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [22451]
INFO:     Stopping reloader process [20262]

~~~


<div align="center" max-width="70vw" >

<img src="https://drive.google.com/uc?export=view&id=1wBpfw_H6qm9VIMz1Uu50-LUbpypqTMO4">

</div>

<div align="center" max-width="70vw" >

[@erwindevdesign](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%40erwindevdesign)

</div>