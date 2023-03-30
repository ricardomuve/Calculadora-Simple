opcion = 0
while opcion != 5:
  print("""Bienvenidos a mi programa
  Menú:
  1. Suma
  2. Potencia
  3. División
  4. Resta
  5. Salir
  """)
  opcion = int(input("Ingresa tu opción: "))
  print('')
  if opcion == 1:
    val_uno = float(input("Ingresa tu 1er valor: "))
    val_dos = float(input("Ingresa tu 2o valor: "))
    print("La suma es ", val_uno + val_dos)
    input('')
  if opcion == 2:
    val_uno = float(input("Ingresa tu 1er valor: "))
    val_dos = float(input("Ingresa tu 2o valor:"))
    print("La potencia es ", val_uno ** val_dos)
    input('')
  if opcion == 3:
    val_uno = float(input("Ingresa tu 1er valor: "))
    val_dos = float(input("Ingresa tu 2o valor:"))
    print("La división es ", val_uno / val_dos)
    input('')
  if opcion == 4:
    val_uno = float(input("Ingresa tu 1er valor: "))
    val_dos = float(input("Ingresa tu 2o valor:"))
    print("La resta es ", val_uno - val_dos)
    input('')
