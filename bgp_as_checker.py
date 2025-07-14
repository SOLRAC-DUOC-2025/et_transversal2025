asn = int(input("Ingrese número de AS: "))
if 64512 <= asn <= 65534:
    print("AS Privado")
else:
    print("AS Público")
