# Examen Transversal DRY7122 - Programación y Redes Virtualizadas

Repositorio oficial del examen transversal correspondiente a la asignatura **DRY7122**, semestre 2025.  
Contiene scripts y evidencias prácticas relacionadas a automatización de redes, APIs y tecnologías como Netconf y RESTCONF.

---

## 🧩 Ítem 1 – GitHub + Scripts básicos

**📍 Ubicación:**  
`item1_grupo.py`  
`item1_bgp.py`

**🔧 Descripción:**  
- `item1_grupo.py`: imprime los integrantes del grupo.  
- `item1_bgp.py`: identifica si un ASN ingresado es público o privado.

**📸 Evidencia recomendada:**  
- Screenshot del código ejecutado.  
- Commit visible en GitHub.

---

## 🧩 Ítem 2 – Geolocalización con API (GraphHopper)

**📍 Ubicación:**  
`item2_ruta.py`

**🔧 Descripción:**  
- Usa `requests` para obtener distancia entre dos ciudades ingresadas por el usuario.  
- Requiere una API Key de GraphHopper.

**📌 Consideraciones:**
- Se debe registrar y generar API key en https://graphhopper.com  
- Debes capturar la ejecución exitosa del script con el resultado de distancia.

**📸 Evidencia recomendada:**  
- Captura de pantalla con entrada y resultado correcto.  
- GitHub: archivo `item2_ruta.py` + commit.

---

## 🧩 Ítem 3 – Web App con Flask

**📍 Ubicación:**  
`item3_webapp.py`  
`usuarios.db`

**🔧 Descripción:**  
- Web app simple con Flask que almacena nombre y contraseña en SQLite.  
- Contraseña es encriptada con bcrypt.  
- La DB se visualiza con DB Browser for SQLite.

**📌 Consideraciones:**
- Instalar `flask`, `bcrypt` y `sqlite3`.  
- Ejecutar en entorno local `http://0.0.0.0:7500/`.

**📸 Evidencia recomendada:**  
- Screenshot de la terminal Flask corriendo.  
- Captura de DB con `nombre: Carlos` y hash en `usuarios.db`.

---

## 🧩 Ítem 4 – Script NETCONF con CSR1000v

**📍 Ubicación:**  
`item4_netconf.py`

**🔧 Descripción:**  
- Script que utiliza `ncclient` para conectarse al CSR1000v vía NETCONF.  
- Establece una sesión SSH con puerto 830.

**📌 Consideraciones:**
- Asegúrate que NETCONF esté habilitado en el CSR1000v:
```bash
conf t
netconf-yang
end
