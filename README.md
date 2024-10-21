<a name="readme-top"></a>
<!-- 
Etiquetas Sugeridas:
python, virtualenv, venv, environment, dependencies, development, best practices, tutorial
-->
<br>
<div align="center">
  <h1>VIRTUAL ENVIROMENT</h1>
  <h3>Una guía práctica para desarrolladores.</h3>
</div>
<br>

<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)<br> -->

<a title="python language icon" href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="Made with Python"></a>   

<a name="introduction"></a>
<br>
<div align="center">
  <h3 style="font-weight: bolder;">Introducción</h3>
</div>
<br>

El desarrollo de aplicaciones en lenguaje de programación Python, usualmente hace uso de diversas versiones de paquetes y módulos que requieren una especificidad de versión en su librería. Esto crea la necesidad de aislar estos requerimientos sin crear conflicto al trabajar en diferentes proyectos haciendo uso de entornos virtuales (venv).

Este repositorio es una referencia para desarrolladores que desean comprender y dominar la creación y gestión de entornos virtuales. A través de ejemplos prácticos y explicaciones detalladas, exploraremos los conceptos fundamentales de los entornos virtuales, su importancia en el desarrollo de proyectos Python y las mejores prácticas para su uso.

<br>
<details>
  <summary><b>Contenido 📋</b></summary>
    <ul style="list-style: none;">
      <li style="list-style: none;">
        <a href="#introduction" >
          Introducción
        </a>
          <ul style=" list-style-type:none">
            <li>
              <a href="#what-is" >
                ~ ¿Qué es un entorno virtual y su importancia en el desarrullo?
              </a>
            </li>
            <li>
              <a href="#why-use" >
                ~ ¿Por qué utilizar entornos virtuales?
              </a>
            </li>
          </ul>
      </li>
      <li > 
        <a href="#create-virtual-environment">
          Creación de Entorno Virtual
        </a>
          <ul style=" list-style-type:none">
            <li>
              <a href="#new-virtual-environment" >
                ~ Crea un nuevo entorno con venv.
              </a>
            </li>
            <li>
              <a href="#activate-deactivate" >
                ~ Activación y desactivación del entorno.
              </a>
            </li>
            <li>
              <a href="#install-packages" >
                ~ Instalación de paquetes con pip.
              </a>
            </li>
          </ul>
      </li>
      <li>
        <a href="#package-management" >
          Gestión de Paquetes.
        </a>
          <ul style=" list-style-type:none">
            <li>
              <a href="#new-file" >
                ~ Creación de un archivo requirements.txt.
              </a>
            </li>
            <li>
              <a href="#packages-from-file" >
                ~ Instalación de paquetes desde requirements.txt.
              </a>
            </li>
            <li>
              <a href="#updating-removing">
                ~ Actualización de paquetes.
              </a>
            </li>  
            <li>
              <a href="#remove-dependencies">
                ~ Elimina paquetes.
              </a>
            </li>    
            <li>
              <a href="#freezes-dependencies">
                ~ Congela las versiones de paquetes.
              </a>
            </li>        
          </ul>        
      </li>
      <li>
        <a href="#best-practices">
          Mejores prácticas
        </a>
          <ul style=" list-style-type:none" >
            <li>
              <a href="#name-structure">
                ~ Nombre para tu entorno virtual.
              </a>
            </li> 
            <li>
              <a href="#recommended-structure">
                ~ Estructura de directorios recomendada.
              </a>
            </li> 
            <li>
              <a href="#gitignore-file">
                ~ Uso de .gitignore para excluir archivos innecesarios.
              </a>
            </li> 
            <li>
              <a href="#scripts">
                ~ Automatización de la creación de entornos con scripts.
              </a>
            </li> 
          </ul>        
      </li>
      <!-- <li>
        <a href="#" >
          Ⅴ. Ejemplos Prácticos
        </a>
          <ul style=" list-style-type:none">
            <li>Creación de entornos para diferentes proyectos (Django, Flask, Machine Learning).</li>
            <li>Resulución de problemas comunes.</li>
          </ul>
      </li>
      <li>
        <a href="#" >
          Ⅵ. Herramientas Adicionales
        </a>
          <ul style=" list-style-type:none">
            <li>Integración con IDEs (Visual Studio Code, PyCharm).</li>
            <li>Uso de Docker para la contenerización de entornos.</li>
          </ul>
      </li> -->
      <li>
        <a href="#license" >
          Licencia
        </a>
      </li>
      <li>
        <a href="#contributing" >
          Contribuyendo al proyecto
        </a>
      </li>
    </ul>
</details>
<br>

Contribuyendo al Proyecto

<a name="what-is"></a>
<br>
<div align="center">
  <b >
    ¿Qué es un entorno virtual y su importancia en el desarrollo?
  </b>
</div>
<br>

Un entorno virtual en Python es un directorio aislado que contiene una instalación de Python y todos los paquetes instalados dentro de él. Este aislamiento garantiza que las dependencias de un proyecto en particular no interfieran con otros proyectos, evitando conflictos de versiones y asegurando un entorno de desarrollo consistente y reproducible.

<a name="why-use"></a>
<br>
<div align="center">
  <b>
    ¿Por qué utilizar entornos virtuales?
  </b>
</div>
<br>

<details>
  <summary><b>Aislamiento de proyectos</b></summary>
    <ul style=" list-style-type:none">
      <li >
          <p>
            <b>Evita conflictos:</b> Cada proyecto puede tener sus propias versiones de paquetes, evitando colisiones entre diferentes versiones de una misma librería.
          </p>
      </li>
      <li >
          <p>
            <b>Gestión independiente:</b> Realiza actualizaciones de paquetes en un entorno sin afectar otros proyectos.
          </p>
      </li>
    </ul>
</details>

<details>
  <summary><b>Reproducibilidad</b></summary>
    <ul style=" list-style-type:none">
      <li >
          <p>
            <b>Entornos consistentes:</b> Garantiza que tu proyecto se ejecute de la misma manera en cualquier entorno donde se instale.
          </p>
      </li>
      <li >
          <p>
            <b>Facilita la colaboración:</b> Permite a otros desarrolladores configurar fácilmente el proyecto sin conflictos de versiones.
          </p>
      </li>
      <li >
          <p>
            <b>Simplifica la implementación:</b> Facilita la implementación en servidores de producción con las mismas dependencias.
          </p>
      </li>
    </ul>
</details>

<details>
  <summary><b>Colaboración</b></summary>
    <ul style=" list-style-type:none">
      <li >
          <p>
            <b>Proyectos aislados:</b> Cada desarrollador puede tener su propio entorno virtual, evitando interferencias entre diferentes estilos de trabajo.
          </p>
      </li>
      <li >
          <p>
            <b>Facilita la revisión de código:</b> Permite a los revisores recrear el entorno del proyecto para evaluar los cambios.
          </p>
      </li>
      <li >
          <p>
            <b>Mejora la gestión de equipos:</b> Facilita la gestión de múltiples proyectos y equipos.
          </p>
      </li>
    </ul>
</details>

<details>
  <summary><b>Otros beneficios</b></summary>
    <ul style=" list-style-type:none">
      <li >
          <p>
            <b>Distribución:</b> Permite empaquetar aplicaciones con sus dependencias exactas, asegurando una instalación sin problemas en diferentes sistemas.
          </p>
      </li>
      <li >
          <p>
            <b>Limpieza:</b> Evita la contaminación del entorno de Python global, lo que facilita la gestión de múltiples proyectos.
          </p>
      </li>
      <li >
          <p>
            <b>Optimización de recursos:</b> Evita la instalación innecesaria de paquetes globales.
          </p>
      </li>
      <li >
          <p>
            <b>Mejora la seguridad:</b> Reduce el riesgo de instalar paquetes vulnerables.
          </p>
      </li>
      <li >
          <p>
            <b>Facilita la experimentación:</b> Permite probar nuevas versiones de paquetes sin afectar el proyecto principal.
          </p>
      </li>
      <li >
          <p>
            <b>Integración con herramientas de CI/CD:</b> Se integra fácilmente con herramientas de integración continua y entrega continua para automatizar procesos de construcción y despliegue.
          </p>
      </li>
    </ul>
</details>



*En **resumen**, los entornos virtuales son una herramienta esencial para cualquier desarrollador* **`Python`** *que trabaje en múltiples proyectos o que necesite garantizar la reproducibilidad y consistencia de sus aplicaciones.*

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<a name="create-virtual-environment"></a>
<br>
<div align="center">
  <h3 style="font-weight: bolder;">Creación de Entorno Virtual</h3>
</div>
<br>

<a name="new-virtual-environment"></a>

**Crea un nuevo entorno con `venv`.**

Dentro del directorio del proyecto, ejecuta el siguiente comando para crear un nuevo entorno virtual: 
~~~sh
python -m venv mi_entorno_virtual
~~~
*Reemplaza el nombre* `mi_entorno_virtual`*, con el nombre que desees para tu entorno.*

<a name="activate-deactivate"></a>
<br>

**Activación**
~~~sh
source mi_entorno_virtual/bin/activate
~~~
*Una vez activado, verás el nombre del entorno, entre paréntesis, al principio de la línea de comandos.*

<br>

**Validación**

~~~sh
which python

# or

which pip
~~~
*Esto mostrará la ruta desde la cual se ejecuta* `Python` *y su gestor de paquetes por defecto* `pip`.

<br>

**Desactivación**

~~~sh
deactivate
~~~
*Una vez desactivado el entorno virtual, las dependencias instaladas posteriormente se alojaran de forma global en el equipo.*

<a name="install-packages"></a>
<br>

**Instalación de paquetes con pip.**

El gestor de paquetes de `Python` por defecto, `pip`. Nos permite buscar, instalar, actualizar y eliminar paquetes de forma sencilla desde el Python Package Index `(PyPI)`, el repositorio oficial de paquetes de Python.

Una vez activado el entorno virtual, instala las dependencias requeridas para el desarrollo de tu proyecto.

~~~sh
pip install <nombre_del_paquete>
~~~
Por ejemplo, para instalar `requests` 
~~~sh
pip install requests
~~~

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<a name="package-management"></a>
<br>
<div align="center">
  <h3 style="font-weight: bolder;">Gestión de Paquetes</h3>
</div>
<br>

<!-- 
Para la gestión de paquetes existen dos escenarios, el primero donde el desarrollo del proyecto es propio y requerimos respaldar las versiones exactas con las que funciona una aplicación, el segundo donde colaboramos en un proyecto ya existente del cual requerimos instalar las versiones exactas que refiere el creador para hacer uso de su codigo.
En la colaboración de código, es indispensable proporcionar la versión exacta de las dependencias que requiere nuestro software para su funcionamiento. Para ello, respaldaremos y/o instalaremos dichas dependencias en un archivo `requirements.txt`, el cual detallara las versiones adecuadas para el funsionamiento de la aplicación.
 -->

La gestión de paquetes en proyectos de desarrollo es crucial para garantizar la reproducibilidad y colaboración. 

Existen dos escenarios principales:

* Desarrollo propio: Al crear un proyecto, es fundamental registrar las versiones exactas de los paquetes utilizados para asegurar que la aplicación funcione correctamente en el futuro y en diferentes entornos.
* Colaboración en proyectos existentes: Cuando nos unimos a un proyecto ya en desarrollo, es imprescindible instalar las mismas versiones de los paquetes que el equipo original para evitar conflictos y asegurar la compatibilidad del código.

Para gestionar las dependencias de un proyecto, se recomienda utilizar un archivo `requirements.txt`. Este archivo contiene de forma precisa los paquetes y sus versiones requeridos para ejecutar la aplicación. Al compartir este archivo, facilitamos la instalación del entorno de desarrollo a otros colaboradores y garantizamos que todos trabajen con la misma configuración.

<a name="new-file"></a>
<br>

**Creación de un archivo `requirements.txt`.**
~~~
touch requirements.txt
~~~

<a name="packages-from-file"></a>
<br>

**Instalación de paquetes desde `requirements.txt`.**
~~~sh
pip install -r requirements.txt
~~~

<a name="updating-removing"></a>
<br>

**Actualización de paquetes.**

Instala la nueva versión del paquete:
~~~sh
pip install <nombre_del_paquete>==<nueva_versión>
~~~
Por ejemplo, para actualizar `requests` a la versión `2.28.1`:
~~~sh
pip install requests==2.28.1
~~~

<a name="remove-dependencies"></a>
<br>

**Eliminando paquetes.**

Desinstala el paquete.
~~~sh
pip uninstall <nombre_del_paquete>
~~~
Por ejemplo, para desinstalar `numpy`:
~~~sh
pip uninstall numpy
~~~

<a name="freezes-dependencies"></a>
<br>

**Congela las dependencias dentro del archivo** `requirements.txt`**.**

Para actualizar el archivo `requirements.txt` con las nuevas versiones instaladas.
~~~sh
pip freeze > requirements.txt
~~~

Para revisar el archivo `requirements.txt` con las nuevas versiones instaladas.

~~~sh
cat requirements.txt
~~~

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<a name="best-practices"></a>
<br>
<div align="center">
  <h3 style="font-weight: bolder;">Mejores prácticas</h3>
</div>
<br>

<a name="name-structure"></a>

**Nombre para tu entorno virtual.**

La elección del nombre para tu entorno virtual es en gran medida una cuestión de preferencia personal y convención de equipo. Sin embargo, te presento algunas recomendaciones para adoptar una mejor práctica:

- **Ser descriptivo:** El nombre del entorno debe reflejar el propósito del proyecto o la aplicación para la que se está creando. Por ejemplo, `my_web_app_env` o `data_analysis_env`.

- **Evitar nombres genéricos:** Evita nombres como `env` o `venv`, ya que pueden llevar a confusión si tienes múltiples entornos virtuales.

- **Utilizar guiones bajos:** Los guiones bajos `(_)` son una buena opción para separar palabras en los nombres de los entornos.

- **Ser consistente:** Adopta un esquema de nomenclatura consistente en todos tus proyectos para facilitar la organización y la gestión.

- **Convenciones de equipo:** Si trabajas en equipo, es importante establecer una convención de nomenclatura común para todos los miembros.

- **Longitud del nombre:** Los nombres demasiado largos pueden ser difíciles de manejar, así que trata de encontrar un equilibrio entre descriptividad y concisión.

- **Herramientas de gestión de entornos virtuales:** Algunas herramientas como `virtualenvwrapper` o `conda` ofrecen funcionalidades adicionales para la gestión de entornos virtuales y pueden tener sus propias convenciones de nomenclatura.

<a name="recommended-structure"></a>

<br>

**Estructura de directorios recomendada.**

Al crear un entorno virtual, se crea un directorio con la siguiente estructura:

~~~sh
env/
├── bin/
│   ├── activate.csh
│   ├── activate.fish
│   ├── Activate.ps1
│   ├── python
│   └── ...
├── include/
├── lib/
├── lib64/
├── share
└── pyvenv.cfg
~~~
*\* Puede variar ligeramente según la versión de* `Python`.

<a name="gitignore-file"></a>

<br>

**Uso de `.gitignore` para excluir archivos innecesarios.**

El archivo `.gitignore` es una herramienta esencial en `Git`, especifica qué archivos o directorios deben ser ignorados al realizar un commit. Esto es crucial para mantener un repositorio limpio y eficiente, evitando que se versionen archivos temporales, configuraciones locales o cualquier otro tipo de información que no sea relevante para el proyecto.

Crea un archivo `.gitignore` en la raíz de tu repositorio, para ignorar archivos específicos y evitar que sean rastreados:

~~~sh
touch .gitignore
~~~
<br>

\* Ejemplo del contenido de un archivo `.gitignore` básico para un proyecto en `Python`:

:eyes: revisa el archivo: <a href="https://github.com/erwindevdesign/pip/blob/develop/.gitignore" target="_blank" rel="noopener noreferrer">.gitignore</a>

<a name="scripts"></a>

<br>

**Automatización de la creación de entornos con scripts.**

Automatizar la creación de entornos virtuales con `venv` es una excelente práctica para agilizar tus flujos de trabajo en Python. 

:eyes: revisa el archivo: <a href="https://github.com/erwindevdesign/pip/blob/develop/scripts/enviroment_create.py" target="_blank" rel="noopener noreferrer">enviroment_create.py</a>

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<a name="license"></a>

### Licencia 

Distribuido bajo la licencia `MIT`

Consulte [`LICENSE`](LICENSE) para  más información.

<a name="contributing"></a>

### Contribuyendo al proyecto

¡Gracias por tu interés en contribuir a este proyecto! Tu ayuda es muy valorada.

* Cómo contribuir

  * **Forkea el repositorio:** Crea una copia de este repositorio en tu cuenta de GitHub.
  * **Crea una rama:** Basada en la rama `develop` (o la rama principal que estés utilizando), crea una nueva rama para tu contribución.
  * **Realiza tus cambios:** Edita los archivos y realiza los cambios necesarios.
  * **Commitea tus cambios:** Guarda tus cambios con mensajes claros y concisos.
  * **Envía un Pull Request:** Envía una solicitud de fusión a este repositorio, describiendo claramente los cambios que has realizado y por qué son necesarios.

<!-- * Guía de Estilo

  * **Sigue nuestro estilo de codificación:** [Enlace a la guía de estilo, si existe]
  * **Escribe código claro y conciso:** Utiliza nombres de variables y funciones descriptivos.
  * **Incluye pruebas:** Asegúrate de que tus cambios estén cubiertos por pruebas unitarias. -->

* Informando de errores

  Si encuentras algún error o tienes alguna sugerencia, por favor, abre un nuevo issue describiendo el problema de forma clara y concisa.

* Creando una nueva feature

  Si deseas agregar una nueva funcionalidad, por favor, abre un issue primero para discutir la propuesta con el equipo. 

<br>
<br>

<div align="center" max-width="70vw" >

  <img src="https://drive.google.com/uc?export=view&id=1wBpfw_H6qm9VIMz1Uu50-LUbpypqTMO4">

  [@erwindevdesign](https://linktr.ee/erwindevdesign)

</div>

<div align='center'>
  <a href="https://www.linkedin.com/in/erwindeveloper/" target="_blank" rel="noopener noreferrer"><img src="https://i.imgur.com/05pckYQ.png" title="LinkedIn" /></a>
  <a href="https://www.tiktok.com/@erwindevdesign" target="_blank" rel="noopener noreferrer"><img style="margin-inline:20px" src="https://i.imgur.com/ziLmhGy.png" title="TikTok" /></a>
  <a href="https://www.instagram.com/erwindevdesign/" target="_blank" rel="noopener noreferrer"><img src="https://i.imgur.com/riwyB8b.png" title="Instagram" /></a> 
</div>