
Cantidad = int(input("Cantidad: "))
PrecioUnitario = 1200
TotalCompra = Cantidad * PrecioUnitario
PagoCliente = float(input("Pago: "))
if PagoCliente > TotalCompra:
    print("Compra aprobada")
else:
    print("Dinero insuficiente")
