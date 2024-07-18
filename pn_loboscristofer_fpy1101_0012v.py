import random
import csv 

trabajadores = ['juan perez','maria garcia','carlos lopez', 'ana martines',
                'pedro rodrigez ', 'laura hernandez', 'miguel sanchez', 'isabel gomez', 'franciscodias',
                'elena fernandez'] 
sueldos = [0] * len(trabajadores)

def asignar_sueldos_aleatorio():
    for i in range(len(trabajadores)):
        sueldo  = random.randint(300000, 2500000)
        sueldos [i] = sueldo 
        
def mostrar_datos ():
    sueldo_maximo = max(sueldos)        
    sueldo_minimo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    
    print(f'Sueldo alto: {sueldo_maximo}')
    print(f'sueldo bajo {sueldo_minimo}')
    print(f'promedio de sueldo{promedio_sueldo} ')
    print(f"Promedio de sueldos: ${promedio_sueldo:.2f}")
    
def generar_reporte_detalle():
    descuento_salud = 0.07
    descuento_afp = 0.12

    print("\nReporte detallado de sueldos con descuentos:")
    print("Nombre empleado  Sueldo Base  Descuento Salud Descuento AFP  Sueldo Líquido")
    print("-" * 80)
    
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for i in range(len(trabajadores)):
            sueldo_base = sueldos[i]
            descuento_salud_calc = sueldo_base * descuento_salud
            descuento_afp_calc = sueldo_base * descuento_afp
            sueldo_liquido = sueldo_base - descuento_salud_calc - descuento_afp_calc

            nombre_empleado = trabajadores[i]
            print(f"{nombre_empleado} | ${sueldo_base} | ${descuento_salud_calc:.2f} | ${descuento_afp_calc:.2f} | ${sueldo_liquido:.2f}")

            writer.writerow([nombre_empleado, sueldo_base, descuento_salud_calc, descuento_afp_calc, sueldo_liquido])

def main():
    while True:
        print("\n MENU")
        print("1. Asignar sueldos aleatorios")
        print("2. Mostrar datos estadísticos de sueldos")
        print("3. Generar reporte detallado de sueldos")
        print("4. Salir del programa")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            asignar_sueldos_aleatorio( )
        elif opcion == "2":
            mostrar_datos()
        elif opcion == "3":
            generar_reporte_detalle()
        elif opcion == "4":
            print("Finalizando programa...")
            print("Desarrollado por cristofere lobos")
            print("RUT 19.343.166-6")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()