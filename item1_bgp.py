asn = int(input("Ingresa el número de AS: "))
if 64512 <= asn <= 65534:
    print("AS privado")
else:
    print("AS público")
