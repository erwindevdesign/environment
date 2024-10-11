<a name="readme-top"></a>
<!-- 
Etiquetas Sugeridas:
python, virtualenv, venv, environment, dependencies, development, best practices, tutorial
-->

<div align="center">
  <h1>VIRTUAL ENVIROMENT</h1>
  <h3>Una guía práctica para desarrolladores.</h3>
</div>
<br>

<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)<br> -->

<a title="python language icon" href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python"></a>   

<a name="introduction"></a>

<div align="center">
  <h3 style="font-weight: bolder;">Ⅰ</h3>
  <h4 style="font-weight: bolder;">Introducción</h4>
</div>

El desarrollo de aplicaciones en lenguaje de programación Python, usualmente hace uso de diversas versiones de paquetes y módulos que requieren una especificidad de versión en su librería. Esto crea la necesidad de aislar estos requerimientos sin crear conflicto al trabajar en diferentes proyectos haciendo uso de entornos virtuales (venv).

Este repositorio es una referencia para desarrolladores que desean comprender y dominar la creación y gestión de entornos virtuales. A través de ejemplos prácticos y explicaciones detalladas, exploraremos los conceptos fundamentales de los entornos virtuales, su importancia en el desarrollo de proyectos Python y las mejores prácticas para su uso.

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
              <a href="#remove-dependencies">Elimina paquetes.
            </li>    
            <li>
              <a href="#freezes-dependencies">Congela las versiones de paquetes.
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
            <li>
              <a href="#scripts">Automatización de la creación de entornos con scripts.
            </li> 
          </ol>        
      </li>
      <!-- <li>
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
      </li> -->
    </ul>
</details>


<br>
<a name="what-is"></a>
<div align="center">
  <p style="font-weight: bolder;">
    ¿Qué es un entorno virtual y su importancia en el desarrollo?
  </p>
</div>

Un entorno virtual en Python es un directorio aislado que contiene una instalación de Python y todos los paquetes instalados dentro de él. Este aislamiento garantiza que las dependencias de un proyecto en particular no interfieran con otros proyectos, evitando conflictos de versiones y asegurando un entorno de desarrollo consistente y reproducible.

<br>
<a name="why-use"></a>
<div align="center">
  <p style="font-weight: bolder;">
    ¿Por qué utilizar entornos virtuales?
  </p>
</div>

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

*En **resumen**, los entornos virtuales son una herramienta esencial para cualquier desarrollador Python que trabaje en múltiples proyectos o que necesite garantizar la reproducibilidad y consistencia de sus aplicaciones.*

<a name="create-virtual-environment"></a>

<div align="center">
  <h3 style="font-weight: bolder;">Ⅱ</h3>
  <h4 style="font-weight: bolder;">Creación de Entorno Virtual</h4>
</div>

<a name="new-virtual-environment"></a>

#### ~ Crea un nuevo entorno con venv.

Dentro del directorio del proyecto, ejecuta el siguiente comando para crear un nuevo entorno virtual: 
~~~sh
python -m venv mi_entorno_virtual
~~~
*Reemplaza el nombre* `mi_entorno_virtual`*, con el nombre que desees para tu entorno.*

<a name="activate-deactivate"></a>

#### ~ Activación y desactivación del entorno.

Los paquetes y dependencias que se instalen al activar el entorno, se resguardaran en el directorio asignado a él, las dependencias y paquetes que se instalen cuando se encuentre desactivado se instalaran de forma global en el equipo. Una vez activado, verás el nombre del entorno, entre paréntesis, al principio de la línea de comandos*.
    
**Activación**

~~~
source mi_entorno_virtual/bin/activate
~~~

**Validación**

~~~
which python
~~~

**Desactivación**

~~~
deactivate
~~~

<a name="install-packages"></a>

#### ~ Instalación de paquetes con pip.

Cuando instalamos Python en nuestro sistema, obtenemos un conjunto básico de herramientas y librerías estándar que nos permiten comenzar a programar. Sin embargo, para desarrollar aplicaciones más complejas y específicas, es necesario instalar paquetes adicionales. Aquí es donde entra en juego pip.

pip es el gestor de paquetes de Python por defecto. Nos permite buscar, instalar, actualizar y eliminar paquetes de forma sencilla desde el Python Package Index (PyPI), el repositorio oficial de paquetes de Python.

Una vez activado el entorno virtual, instala las dependencias requeridas para el desarrollo de tu proyecto.

~~~sh
pip install <nombre_del_paquete>
~~~
Por ejemplo, para instalar `requests` 
~~~sh
pip install requests
~~~

<a name="example-01"></a>

#### ~ Ejemplo completo

~~~sh
# Posicionate en el directorio de tu proyecto
cd mi_proyecto

# Crea un entorno virtual llamado 'project_env'
python -m venv project_env

# Activa el entorno virtual
source venv/bin/activate

# Validación de ruta de acceso al entorno virtual.
which python
# or
which pip

# Instala un paquete
pip install requests

# Desactiva el entorno virtual
deactivate
~~~

La elección del nombre para tu entorno virtual es en gran medida una cuestión de preferencia personal y convención de equipo. Sin embargo, te presento algunas recomendaciones para adoptar una mejor práctica:

- **Ser descriptivo:** El nombre del entorno debe reflejar el propósito del proyecto o la aplicación para la que se está creando. Por ejemplo, `my_web_app_env` o `data_analysis_env`.

- **Evitar nombres genéricos:** Evita nombres como `env` o `venv`, ya que pueden llevar a confusión si tienes múltiples entornos virtuales.

- **Utilizar guiones bajos:** Los guiones bajos `(_)` son una buena opción para separar palabras en los nombres de los entornos.

- **Ser consistente:** Adopta un esquema de nomenclatura consistente en todos tus proyectos para facilitar la organización y la gestión.

- **Convenciones de equipo:** Si trabajas en equipo, es importante establecer una convención de nomenclatura común para todos los miembros.

- **Longitud del nombre:** Los nombres demasiado largos pueden ser difíciles de manejar, así que trata de encontrar un equilibrio entre descriptividad y concisión.

- **Herramientas de gestión de entornos virtuales:** Algunas herramientas como `virtualenvwrapper` o `conda` ofrecen funcionalidades adicionales para la gestión de entornos virtuales y pueden tener sus propias convenciones de nomenclatura.

<a name="package-management"></a>

<div align="center">
  <h3 style="font-weight: bolder;">Ⅲ</h3>
  <h4 style="font-weight: bolder;">Gestión de Paquetes</h4>
</div>
<!-- 
Para la gestión de paquetes existen dos escenarios, el primero donde el desarrollo del proyecto es propio y requerimos respaldar las versiones exactas con las que funciona una aplicación, el segundo donde colaboramos en un proyecto ya existente del cual requerimos instalar las versiones exactas que refiere el creador para hacer uso de su codigo.
En la colaboración de código, es indispensable proporcionar la versión exacta de las dependencias que requiere nuestro software para su funcionamiento. Para ello, respaldaremos y/o instalaremos dichas dependencias en un archivo `requirements.txt`, el cual detallara las versiones adecuadas para el funsionamiento de la aplicación.
 -->

La gestión de paquetes en proyectos de desarrollo es crucial para garantizar la reproducibilidad y colaboración. Existen dos escenarios principales:

* Desarrollo propio: Al crear un proyecto, es fundamental registrar las versiones exactas de los paquetes utilizados para asegurar que la aplicación funcione correctamente en el futuro y en diferentes entornos.
* Colaboración en proyectos existentes: Cuando nos unimos a un proyecto ya en desarrollo, es imprescindible instalar las mismas versiones de los paquetes que el equipo original para evitar conflictos y asegurar la compatibilidad del código.

Para gestionar las dependencias de un proyecto, se recomienda utilizar un archivo `requirements.txt`. Este archivo enumera de forma precisa los paquetes y sus versiones requeridos para ejecutar la aplicación. Al compartir este archivo, facilitamos la instalación del entorno de desarrollo a otros colaboradores y garantizamos que todos trabajen con la misma configuración.

<a name="new-file"></a>
**~ Creación de un archivo** `requirements.txt`**.**
~~~
touch requirements.txt
~~~

<a name="packages-from-file"></a>
**~  Instalación de paquetes desde** `requirements.txt`**.**
~~~sh
pip install -r requirements.txt
~~~

<a name="updating-removing"></a>
**~ Actualización de paquetes.**

Instala la nueva versión del paquete:
~~~sh
pip install <nombre_del_paquete>==<nueva_versión>
~~~
Por ejemplo, para actualizar `requests` a la versión `2.28.1`:
~~~sh
pip install requests==2.28.1
~~~

<a name="remove-dependencies"></a>
**~ Eliminando paquetes.**

Desinstala el paquete.
~~~sh
pip uninstall <nombre_del_paquete>
~~~
Por ejemplo, para desinstalar `numpy`:
~~~sh
pip uninstall numpy
~~~

<a name="freezes-dependencies"></a>
**~ Congela las dependencias dentro del archivo** `requirements.txt`**.**

Para actualizar el archivo `requirements.txt` con las nuevas versiones instaladas.
~~~sh
pip freeze > requirements.txt
~~~

Para revisar el archivo `requirements.txt` con las nuevas versiones instaladas.

~~~sh
cat requirements.txt
~~~

<a name="best-practices"></a>
<div align="center">
  <h3 style="font-weight: bolder;">Ⅳ</h3>
  <h4 style="font-weight: bolder;">Mejores prácticas</h4>
</div>

<a name="recommended-structure"></a>
**~ Estructura de directorios recomendada.**

Al crear un entorno virtual, se crea un directorio con la siguiente estructura:
~~~mk
env/
├── bin/
│   ├── activate.csh
|   ├── activate.fish
|   ├── Activate.ps1
│   ├── python
│   └── ...
├── include/
├── lib/
├── lib64/
└── pyvenv.cfg
~~~
*Puede variar ligeramente según la versión de `Python`.**

<a name="gitignore-file"></a>
**~ Uso de `.gitignore` para excluir archivos innecesarios.**

El archivo `.gitignore` es una herramienta esencial en `Git`, espesifica qué archivos o directorios deben ser ignorados al realizar un commit. Esto es crucial para mantener un repositorio limpio y eficiente, evitando que se versionen archivos temporales, configuraciones locales o cualquier otro tipo de información que no sea relevante para el proyecto.

Crea un archivo `.gitignore` en la raíz de tu repositorio, para ignorar archivos específicos y evitar que sean rastreados:

~~~sh
touch .gitignore
~~~

Ejemplo del contenido de un archivo `.gitignore` básico para un proyecto en `Python`:

revisa el archivo [.gitignore](https://github.com/erwindevdesign/pip/blob/develop/.gitignore).



<a name="scripts"></a>
**~ Automatización de la creación de entornos con scripts.**

Automatizar la creación de entornos virtuales con venv es una excelente práctica para agilizar tus flujos de trabajo en Python. 

~~~sh
import os
import subprocess

def crear_entorno_virtual(nombre_entorno):
    """
    Crea un entorno virtual con el nombre especificado.

    Args:
        nombre_entorno (str): Nombre del entorno virtual a crear.
    """

    # Comprobamos si el entorno ya existe
    if os.path.exists(nombre_entorno):
        print(f"El entorno virtual '{nombre_entorno}' ya existe.")
        return

    # Creamos el entorno virtual
    try:
        subprocess.run(["python", "-m", "venv", nombre_entorno], check=True)
        print(f"Entorno virtual '{nombre_entorno}' creado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al crear el entorno virtual: {e}")

# Ejemplo de uso
nombre_mi_entorno = "env"
crear_entorno_virtual(nombre_mi_entorno)
~~~






<div align="center" max-width="70vw" >

<img src="https://drive.google.com/uc?export=view&id=1wBpfw_H6qm9VIMz1Uu50-LUbpypqTMO4">

</div>

<div align="center" max-width="70vw" >

[@erwindevdesign](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=%40erwindevdesign)

</div>