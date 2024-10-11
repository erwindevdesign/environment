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