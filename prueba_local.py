#Esto es para poder probar el inicio de sesion y el menu de administrador y cliente sin tener que pasar por el menu principal.

# usuario: cliente contra: cliente123
# admin: admin contra: admin123

#Problemas encontrados:

# 1: - No se puede iniciar sesion sin antes salir del menu principal de MAIN, ya que el menu principal tiene un bucle infinito que no permite salir de el hasta que se cierre el programa. 
#  Esto hace que no se pueda probar el inicio de sesion y el menu de administrador y cliente sin tener que pasar por el menu principal.

# 2: En el menu principal de MAIN, al buscar una prenda debe coincidir el nombre exacto. Al buscar por una palabra parcial, por ejemplo "Jean" no figuran. 

# 3: Al ingresar el precio para modificarlo y no se ingresa ningun valor, el programa no lo toma como 0, sino que lo toma como un string vacio y da error.




import main as catalogo   
from autenticacion import iniciar_sesion
from historial import HistorialBusquedas
from menu_admin import menu_admin
from menu_cliente import menu_cliente


def mostrar_menu_inicio():
    print("\n========== TIENDA DE ROPA ==========")
    print("1. Iniciar sesión")
    print("0. Salir")
    print("====================================")


def main():
    historial = HistorialBusquedas()

    while True:
        mostrar_menu_inicio()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            usuario = iniciar_sesion()

            if usuario is None:
                print("Saliendo del sistema...")
                break

            if usuario.es_administrador():
                menu_admin(catalogo, catalogo.prendas, historial)
            else:
                menu_cliente(catalogo, catalogo.prendas, historial)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción incorrecta. Por favor, elegí una opción válida.")


if __name__ == "__main__":
    main()