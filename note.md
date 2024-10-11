Metodología de desarrollo de documentación de código en GitHub

[1]

1. planificar la estructura del indice previamente a iniciar la documentación, para tener una estructura base solida hacerca del contenido que permita una mayor eficiencia en la escritura.

2. se debe introducir un proceso previo, durante y posterior a la escritura de la documentación para la revisión de ortografia y gramatica.


Consideraciones adicionales para la documentación:

- Analogía: Puedes utilizar una analogía para explicar el concepto de forma más intuitiva. Por ejemplo, puedes comparar un entorno virtual con una caja de herramientas donde cada herramienta (paquete) tiene una versión específica.

- Visualización: Un diagrama simple que muestre la estructura de un entorno virtual puede ser útil para los lectores.

- Ejemplos: Incluye ejemplos de comandos para crear, activar y desactivar entornos virtuales.

- Comparación con otras herramientas: Puedes comparar los entornos virtuales con otras herramientas de gestión de paquetes como conda.

- Enfoque en la contenerización: Dado que mencionas la contenerización, puedes hacer una breve conexión entre entornos virtuales y contenedores, destacando cómo los entornos virtuales son un primer paso hacia la contenerización.1

Ejemplo de diagrama:

[Diagrama que muestra un directorio de proyecto con un entorno virtual y sus paquetes]

Ejemplo de código:
Bash

# Crear un nuevo entorno virtual
python -m venv my_env

# Activar el entorno virtual
source my_env/bin/activate

# Instalar un paquete
pip install numpy

# Crear un requirements.txt
pip freeze > requirements.txt

Usa el código con precaución.

Al incluir esta información detallada y bien estructurada, estarás proporcionando a tus lectores una base sólida para comprender y utilizar entornos virtuales en sus proyectos Python.

--- 

Seguimiento de refactorización de documentación.

Para hacer uso referencial de la construcción de un entrono virtual, se reestructurara la documentación previa en el repositorio `erwindevdesign/pip` para implementarla como referencial en diversos proyectos que requieran de esta herramienta para el desarrollo de proyectos elavorados, principalmente, en lenguaje de programación `Python`.

1. Se restructura de forma lógica la documentación.
    1. Se incluye un indice 
    2. se modifica el texto introductorio
    3. se reestructura la documentación basandoce en la estructura del indice previamente elaborado.
    4. 
2. Recursos adicionales
    1. iconos y animaciones 





---

Elegir entre venv, virtualenv y conda depende de sus necesidades específicas. Si estás trabajando en proyectos simples de Python y quieres seguir con las herramientas estándar de la biblioteca, venv es suficiente. Para una compatibilidad más amplia y funciones adicionales, virtualenv es su aliado. Mientras tanto, conda es ideal para proyectos complejos, especialmente en ciencia de datos, donde las dependencias se extienden más allá del ecosistema de Python.

Recomendaciones adicionales:

- Ejemplos concretos: Incluye ejemplos de cómo los entornos virtuales resuelven problemas comunes en el desarrollo de Python.

- Comparaciones: Compara el uso de entornos virtuales con otros métodos de gestión de paquetes (por ejemplo, instalación global).

- Casos de uso: Presenta casos de uso reales para ilustrar los beneficios de los entornos virtuales.



---


- solicitudes http
- solicitar respuesta al http
- tipos de solicitudes
- tipos de protocolos
- tipos de errores existe. que conlleva regresar un error 500 o  200
- framewors**

- seguridad**
- json web token
- pertenencia WHERE
- trabajar con DB
- ORM como funsiona
- validaciones
- ASINCRONIA

- programacion asincrona

-

-- Base de datos (Relacionales o no)
-- Tareas en segundo plano
-- REALTIME 
-- patrones de diseño (mediador, observable, factori, viewder, singelton**, estrategy, statte, ) decreacionales, estructurales, de comportamiento.
-- pruebas unitarias y covertura de código.
-- 




++ patron 









Exammen PIP - 1 



¿Qué es un entorno virtual?
La herramienta de Python para aislar o encapsular proyectos con sus propios paqutes y versiones sin afectar a otros proyectos y entornos virtuales.


2.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
¿Qué herramienta nos permite trabajar con entornos virtuales en Python 3?
pip

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
3.
¿Qué herramienta nos permite instalar paquetes de Python como dependencias en nuestros proyectos?
pip
4.
¿Con qué comando creamos entornos virtuales en Python 3?
python3 -m venv [ruta del entorno virtual]
5.
¿Con qué comando activamos entornos virtuales en Python 3?
source [ruta del entorno virtual]/bin/activate
6.   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
¿Qué herraminta nos permite aislar y encapsular nuestros proyectos y los paquetes de terceros que este utilice, aunque la versión de Python y el sistema operativo sigan siendo los mismos para todos los proyectos?
Docker

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
7.
Tienes un archivo de texto llamado requirements.txt con todos los paqutes que necesitas con cierta versión en particular. ¿Cómo los instalas todos leyendo el archivo de texto con un solo comando?

pip3 install -r requirements.txt
8.
¿Con qué comando guardamos el nombre y versión de todos los paquetes de terceros en nuestro proyecto dentro de un archivo de texto?
pip3 freeze > requirements.txt
9.
¿Con qué comando instalamos el paquete requests en su versión 2.27.1?
pip install requests==2.27.1
10.
¿Con qué comando instalamos el paquete FastAPI en su última versión estable (sin importar la fecha en que se ejecute ni las viejas o nuevas versiones que se desarrollen de FastAPI).
pip install fastapi
11.
Git y GitHub son herramientas indispensables para trabajar en equipo cuando usamos Python.
Verdadero
12.
Estás desarrollando un proyecto en Python que utiliza diferentes paquetes de terceros en versiones muy especificas. ¿Cuál es la mejor forma de trabajar con el resto de mi equipo para que siempre instalen esos paquetes en esas versiones cuando clonen el proyecto?
Creando un requirements.txt con todos los paquetes y sus versiones e indicando en el README que instalen las dependencias leyendo ese archivo con pip.




## Introducción

<a name="introduction"></a>

Este es el comienzo de nuestro documento.

## Sección 2

<a name="section2"></a>

Aquí hablaremos de otro tema.

### Subsección 2.1

<a name="subsection2.1"></a>

Esta es una subsección.

En la sección anterior, explicamos [lo básico](#introduction).









[Soy un enlace de estilo en linea](https://www.google.com)

[Soy en enlace de estilo con un enlace y un título](https://www.google.com "Google's Homepage")

[Soy en enlace de estilo con referencia][Texto de referencia insensible a mayúsculas / minúsculas]

[Soy una referencia relativa a un archivo del repositorio](../blob/master/LICENSE)

[Puedes usar números para definiciones de enlaces de estilo de referencia][1]

O dejarlo vacío y usa el [enlace de texto en sí].

Las URL y las URL en corchetes angulares se convertirán automáticamente en enlaces.
http://www.ejemplo.com o <http://www.ejemplo.com> y, a veces
ejemplo.com (pero no en Github, por ejemplo).

[Algún texto para mostrar en los enlaces de referencia pueden seguir más adelante.

[texto de referencia insensible a mayúsculas y minúsculas]: https://www.mozilla.org
[1]: http://slashdot.org
[enlace el texto en sí mismo]: http://www.reddit.com






<details>
  <summary><b>Contenido 📋</b></summary>
    <ul style=" list-style-type:none">
      <li >
        <a href="#introduction" >
        Ⅰ. Introducción
        </a>
          <ol style=" list-style-type:none">
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
      <li > 
        <a href="#create-virtual-environment">
          Ⅱ. Creación de Entorno Virtual
        </a>
          <ol style=" list-style-type:none">
            <li>
              <a href="#new-virtual-environment" >
                Crea un nuevo entorno con venv.
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
        <a href="#package-management" >
          Ⅲ. Gestión de Paquetes.
        </a>
          <ol style=" list-style-type:none">
            <li>
              <a href="#new-file" >
                Creación de un archivo requirements.txt.
              </a>
            </li>
            <li>
              <a href="#packages-from-file" >
                Instalación de paquetes desde requirements.txt.
              </a>
            </li>
            <li>
              <a href="#updating-removing">Actualización de paquetes.
            </li>
            <li>
              <a href="#freezes-dependencies">Congela las versiones de paquetes.
            </li>  
            <li>
              <a href="#remove-dependencies">Elimina paquetes.
            </li>            
          </ol>        
      </li>
      <li>
        <a href="#best-practices">
          Ⅳ. Mejores prácticas
        </a>
          <ol style=" list-style-type:none" >
            <li>
              <a href="#recommended-structure">Estructura de directorios recomendada.
            </li> 
            <li>
              <a href="#gitignore-file">Uso de .gitignore para excluir archivos innecesarios.
            </li> 
            <li>Automatización de la creación de entornos con scripts.</li>
          </ol>        
      </li>
      <li>
        <a href="#" >
          Ⅴ. Ejemplos Prácticos
        </a>
          <ol style=" list-style-type:none">
            <li>Creación de entornos para diferentes proyectos (Django, Flask, Machine Learning).</li>
            <li>Resolución de problemas comunes.</li>
          </ol>
      </li>
      <li>
        <a href="#" >
          Ⅵ. Herramientas Adicionales
        </a>
          <ol style=" list-style-type:none">
            <li>Integración con IDEs (Visual Studio Code, PyCharm).</li>
            <li>Uso de Docker para la contenerización de entornos.</li>
          </ol>
      </li>
    </ul>
</details>







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