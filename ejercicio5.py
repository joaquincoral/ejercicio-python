IVA = 0.16
DESCUENTO = 0.10

print("==================================================")
print("     SISTEMA DE VENTA - REGISTRO DE COMPRA")
print("==================================================")

nombre_cliente = input("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")

precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad_comprada = int(input("Ingrese la cantidad de productos comprados: "))

subtotal = precio_unitario * cantidad_comprada
monto_descuento = subtotal * DESCUENTO
subtotal_con_descuento = subtotal - monto_descuento
monto_iva = subtotal_con_descuento * IVA
total_a_pagar = subtotal_con_descuento + monto_iva

tipo_cliente = type(nombre_cliente)
tipo_precio = type(precio_unitario)
tipo_cantidad = type(cantidad_comprada)


print("\n" + "="*50)
print("                  TICKET DE COMPRA")
print("="*50)

print(f" CLIENTE: {nombre_cliente}")
print("-"*50)

print(" DETALLE DEL PRODUCTO:")
print(f"  * Producto: {nombre_producto}")
print(f"  * Precio Unitario: ${precio_unitario:.2f}")
print(f"  * Cantidad: {cantidad_comprada}")
print("-"*50)

print(" TIPOS DE DATOS IDENTIFICADOS EN EL PROGRAMA:")
print(f"  * Variable 'nombre_cliente': {tipo_cliente}")
print(f"  * Variable 'precio_unitario': {tipo_precio}")
print(f"  * Variable 'cantidad_comprada': {tipo_cantidad}")
print("-"*50)

print(" RESUMEN DE LA COMPRA:")
print(f"  Subtotal bruto:           ${subtotal:.2f}")
print(f"  Descuento aplicado (10%): -${monto_descuento:.2f}")
print(f"  IVA (16%):                +${monto_iva:.2f}")
print("  " + "-"*40)
print(f"  TOTAL A PAGAR:            ${total_a_pagar:.2f}")
print("="*50)
print("          ¡Gracias por su preferencia!")
print("="*50)