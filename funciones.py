import json
import numpy as np

mascotas = []

matriz_mascotas = np.empty((50, 7), dtype=object)
def cargar_datos(archivo):
    global mascotas
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            mascotas.extend(json.load(file))
        print("Datos cargados correctamente.")
    except IOError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print("El archivo está vacío o contiene datos inválidos.")

def ingreso_mascota():
    global mascotas
    nombre = input("Ingrese nombre mascota: ")
    codigo = input("Ingrese codigo de mascota: ")
    peso = input("Ingrese peso mascota: ")
    raza = input("Ingrese raza mascota: ")
    edad = input("Ingrese especie de mascota: ")
    diagnostico = input("Ingrese el diagnóstico: ")
    medicamentos = input("Ingrese los medicamentos recetados: ")

    mascota = {
        'nombre': nombre,
        'codigo': codigo,
        'peso': peso,
        'raza': raza,
        'edad': edad,
        'diagnostico': diagnostico,
        'medicamentos': medicamentos,
    }
    mascotas.append(mascota)
    print(f"Mascota {mascota['nombre']} {mascota['codigo']} agregado correctamente.")

def buscar_mascota_por_codigo(codigo):
    global mascotas
    for mascota in mascotas:
        if mascota["codigo"] == codigo:
            return mascota 
    return None 
def buscar_medicamentos_codigo(codigo):
    global mascotas
    codigo = input("Ingrese el codigo de la mascota: ")
    mascota = buscar_mascota_por_codigo(codigo)
    global mascotas
    for mascota in mascotas:
        if mascota["codigo"] == codigo:
            return mascota 
        return None 
    if mascota is not None:
        print(f"Medicamentos recetados: {mascota['medicamentos']}")
    else:
        print("Medicamentos no encontrados.")
def eliminar_mascota():
    global mascotas
    codigo = input("Ingrese el codigo de la mascota que desea eliminar: ")
    mascota = buscar_mascota_por_codigo(codigo)
    if mascota:
        mascotas.remove(mascota)
        print(f"Mascota {mascota['nombre']} {mascota['codigo']} eliminado correctamente.")
    else:
        print("No se encontró ficha de la mascota con ese codigo.")
def listado_mascota():
    global mascotas
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for mascota in mascotas:
        print(f"Nombre: {mascota['nombre']}, Codigo: {mascota['codigo']}, raza: {mascota['raza']}")
        print("------------------------")
def salirYguardar():
    global mascotas
    archivo = "datos_mascotas.json"
    try:
        with open(archivo, 'w') as file:
             json.dump(mascotas, file, indent=4, ensure_ascii=False)
        print(f"Datos guardados correctamente en {archivo}")
    except IOError as e:
        print(f"Error al guardar los datos ingresado: {e}")
        mostrar_menu()  

