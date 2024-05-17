import os
import django

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria_dj.settings')
django.setup()

from proyecto_inmobiliaria.models import Inmueble, Comuna, Region # noqa: E402 (Para evitar advertencia, me molesta y es la unica solución que encontré.)

def consultar_inmuebles_por_comuna():
    comunas = Comuna.objects.all()
    resultados = []

    for comuna in comunas:
        inmuebles = Inmueble.objects.filter(comuna=comuna).values('nombre', 'descripcion')
        if inmuebles:
            resultados.append(f'Comuna: {comuna.nombre}\n')
            for inmueble in inmuebles:
                resultados.append(f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")
            resultados.append("\n")

    with open('inmuebles_por_comuna.txt', 'w') as file:
        file.writelines(resultados)

def consultar_inmuebles_por_region():
    regiones = Region.objects.all()
    resultados = []

    for region in regiones:
        inmuebles = Inmueble.objects.filter(comuna__region=region).values('nombre', 'descripcion')
        if inmuebles:
            resultados.append(f'Región: {region.nombre}\n')
            for inmueble in inmuebles:
                resultados.append(f" - Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")
            resultados.append("\n")

    with open('inmuebles_por_region.txt', 'w') as file:
        file.writelines(resultados)

if __name__ == "__main__":
    consultar_inmuebles_por_comuna()
    consultar_inmuebles_por_region()
