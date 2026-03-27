# 🟢 Nivel básico

## 1. JSON → string

Crea una lista de diccionarios y conviértela a JSON.

👉 Objetivo:

* Usar `json.dumps()`

```python
data = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]
```

✔️ Tarea: convertir `data` a string JSON e imprimirlo.

---

## 2. string → JSON

Convierte un string JSON a objeto Python.

👉 Objetivo:

* Usar `json.loads()`

```python
texto = '[{"nombre": "Ana", "edad": 25}]'
```

✔️ Tarea: convertirlo a lista y acceder al nombre.

---

## 3. Escribir texto en memoria

Simula un archivo en memoria.

👉 Objetivo:

* Usar `io.StringIO()`
* `.write()` y `.getvalue()`

✔️ Tarea: escribir "Hola\nMundo" y luego imprimir el contenido.

---

# 🟡 Nivel intermedio

## 4. Crear un CSV desde lista de diccionarios

👉 Objetivo:

* `csv.DictWriter`
* `.writeheader()`
* `.writerows()`

```python
data = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]
```

✔️ Tarea: generar un CSV en memoria usando `StringIO`.

---

## 5. Leer un CSV desde string

👉 Objetivo:

* `io.StringIO`
* `csv.DictReader`

```python
texto = "nombre,edad\nAna,25\nLuis,30"
```

✔️ Tarea: convertirlo en lista de diccionarios.

---

## 6. Convertir CSV → JSON

👉 Objetivo:

* `DictReader`
* `json.dumps()`

✔️ Tarea:

* Leer CSV
* Convertirlo a lista
* Transformarlo a JSON

---

# 🟠 Nivel avanzado

## 7. Convertir JSON → CSV

👉 Objetivo:

* Combinar `json.loads()` + `DictWriter`

✔️ Tarea:

* Recibir JSON
* Convertir a CSV en memoria

---

## 8. Filtrar datos antes de exportar

👉 Objetivo:

* Manipulación de listas
* Exportación

✔️ Tarea:

* Dado un JSON con personas
* Filtrar mayores de 18
* Exportar a CSV

---

## 9. Crear función reutilizable (estilo estrategia)

👉 Objetivo:

* Practicar funciones

✔️ Tarea:
Crear una función:

```python
def convertir(data, formato):
```

* Si `formato == "json"` → usar `json.dumps`
* Si `formato == "csv"` → usar `DictWriter`

---

## 10. Simular archivos reales (muy importante)

👉 Objetivo:

* Usar `.seek(0)`

✔️ Tarea:

* Escribir en `StringIO`
* Volver al inicio
* Leer con `DictReader`

---

