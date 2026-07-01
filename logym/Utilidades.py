#verificaciones,

import json
import os

archivo = "ejercicios_.txt"

def guardar_ejercicios(lista_nuevos):
  existentes = leer_ejercicios()
  print("pude leer los ejer")
  nombres_existentes = {
    e.get("nombre") for e in existentes
  }
  a_agregar = []

  for elemento in lista_nuevos:
      nombre = elemento.get("nombre")
      if nombre not in nombres_existentes:
          a_agregar.append(elemento)

  if a_agregar:
    existentes.extend(a_agregar)
    with open(archivo, "w", encoding="utf-8") as a:
      print("estoy por aca")
      json.dump(existentes, a, indent = 4)
  print("llegue al final de la funcion guardar_ejs")
  return a_agregar

def leer_ejercicios():
  print("holaaaaa")
  if not os.path.exists(archivo):
     return []

  with open(archivo, "r", encoding = "utf-8") as a:
    try:
      return json.load(a)
    except:
       print("no soy ninguno de los anteriroes")
       return []
