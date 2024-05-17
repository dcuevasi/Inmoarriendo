from .models import Usuario, Inmueble 

def crear_usuario(nombre, apellidos, rut, direccion, telefono, correo_electronico, tipo_usuario):
    usuario = Usuario(
        nombre=nombre,
        apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        telefono=telefono,
        correo_electronico=correo_electronico,
        tipo_usuario=tipo_usuario
    )
    usuario.save()
    return usuario

def listar_usuarios():
    return Usuario.objects.all()

def borrar_usuario(rut):
    try:
        usuario = Usuario.objects.get(rut=rut)
        usuario.delete()
        print(f"Usuario con RUT {rut} ha sido borrado exitosamente.")
    except Usuario.DoesNotExist:
        print(f"No se encontró un usuario con el RUT {rut}")

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones, baños, direccion, comuna, tipo_inmueble, precio_mensual, arrendador):
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_totales=m2_totales,
        estacionamientos=estacionamientos,
        habitaciones=habitaciones,
        baños=baños,
        direccion=direccion,
        comuna=comuna,
        tipo_inmueble=tipo_inmueble,
        precio_mensual=precio_mensual,
        arrendador=arrendador
    )
    inmueble.save()
    return inmueble

def listar_inmuebles():
    return Inmueble.objects.all()

def actualizar_inmueble(id, **datos):
    try:
        inmueble = Inmueble.objects.get(id=id)
        for key, value in datos.items():
            setattr(inmueble, key, value)
        inmueble.save()
        return inmueble
    except Inmueble.DoesNotExist:
        print(f"No se encontró un inmueble con el ID {id}")
        return None

def borrar_inmueble(id):
    try:
        inmueble = Inmueble.objects.get(id=id)
        inmueble.delete()
        print(f"Inmueble con ID {id} borrado exitosamente.")
    except Inmueble.DoesNotExist:
        print(f"No se encontró un inmueble con el ID {id}")