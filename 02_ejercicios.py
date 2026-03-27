import json
import io
import csv

def main():

    data = [
        {"nombre": "Ana", "edad": 25},
        {"nombre": "Luis", "edad": 30}
    ]
    texto = '[{"nombre": "Ana", "edad": 25}]'

    ###########################################
    print("EJERCICIO 1 \n")
    ejercicio1 = Ejercicios()
    json_str=ejercicio1.dictToJson(data)
    print(json_str)
    print("")
    ###########################################
    print("EJERCICIO 2 \n")
    ejercicio2 = Ejercicios()
    output = ejercicio2.jsonToObject(json_str)
    print(output)       
    print(type(output)) 
    print(output[0].get("nombre")) 
    print("")

    ###########################################
    print("EJERCICIO 3 \n")
    ejercicio3 = Ejercicios()
    writed=ejercicio3.writeText(texto="Mi nombre es JORGE LUIS")
    print(f"memory: {writed}")
    print("\n")
    ###########################################
    print("EJERCICIO 4 \n")
    ejercicio4 = Ejercicios()
    print(ejercicio4.toCsv(data))
    print("\n")

    ###########################################
    print("EJERCICIO 5 \n")
    ejercicio5 = Ejercicios()
    lista = ejercicio5.csvToList("nombre,edad\nAna,25\nLuis,30")
    print(f"CSV -> list: {lista}") 
    print("\n")

    ###########################################
    print("EJERCICIO 6 \n")
    ejercicio6 = Ejercicios()
    json_texto = ejercicio6.csvToJson("nombre,edad\nAna,25\nLuis,30\nPepito,17")
    print(json_texto)
    print("\n")

    ###########################################
    print("EJERCICIO 7 \n")
    ejercicio7 = Ejercicios()
    csv_texto = ejercicio7.jsonToCsv(json_texto)
    print(csv_texto)
    print("\n")

    ###########################################
    print("EJERCICIO 8")
    ejercicio8 = Ejercicios()
    mayores_de_edad = ejercicio8.filtrar_mayor_y_exportar(json_texto)
    print(mayores_de_edad)
    print("\n")

    ############################################
    print("EJERCICO 9")
    ejercicio9 = Ejercicios()
    formato_json = ejercicio9.converir(data, "json")
    print(f"formato json: {formato_json}")
    print("\n")

    ##########################################
    print("EJERCICIO 10")
    ejercicio10 = Ejercicios()
    output_list = ejercicio10.simular_archivo(data)
    print(f"Ejercicio 10: {output}")
    print("\n")


class Ejercicios:

    # Convierte un dic en un str en formato JSON
    def dictToJson(self, data:list[dict])->str:
        return json.dumps(data, indent=4)        

    # Convierte un str JSON a objeto python
    def jsonToObject(self, jsonStr:str):
        return json.loads(jsonStr)

    # Escribir texto en memoria
    def writeText(self, texto:str)-> str:
        memory = io.StringIO()
        memory.write(texto)
        return memory.getvalue()

    # Crear un csv desde lista de diccionario
    def toCsv(self, data:list[dict])->str:
        output = io.StringIO()
        header = data[0].keys()

        write = csv.DictWriter(output, fieldnames=header)
        write.writeheader()
        write.writerows(data)

        return output.getvalue()

    # Leer un csv convertirlo en lista de diccionarios.
    def csvToList(self, data:str)->list[dict]:
        buffer = io.StringIO(data)
        reader = csv.DictReader(buffer)
        return list(reader)

    # convertir CSV -> JSON
    def csvToJson(self, data:str)->str:
        buffer = io.StringIO(data)
        reader = csv.DictReader(buffer)
        lista = list(reader)
        return json.dumps(lista, indent=4)

    # Convertir JSON -> CSV
    def jsonToCsv(self, texto_json:str)->str:
        data = json.loads(texto_json)

        if not data:
            return ""

        buffer = io.StringIO()
        fieldname = data[0].keys()

        write = csv.DictWriter(buffer, fieldnames=fieldname)
        write.writeheader()
        write.writerows(data)

        return buffer.getvalue()

    # Filtrar datos antes de exportar en formato CSV ejercicio 8
    def filtrar_mayor_y_exportar(self, texto_json:str):
        data = json.loads(texto_json)
        
        filtrados = [p for p in data if int(p.get("edad",0)) > 18]
        
        buffer = io.StringIO()
        if not filtrados:
            return ""
        
        fielname= filtrados[0].keys()
        write = csv.DictWriter(buffer, fieldnames=fielname)
        write.writeheader()
        write.writerows(filtrados)
        
        return buffer.getvalue()
    
    # Ejercicio9 - convertir list -> JSON | CSV
    def converir(self, data:list[dict[str,any]], formato:str)->str:
        formato = formato.lower()
        if formato == "json":
            return json.dumps(data, indent=4)
            
        elif formato == "csv":
            if not data:
                return ""
            
            buffer = io.StringIO()
            fieldname = data[0].keys()
            
            write = csv.DictWriter(buffer, fieldnames=fieldname)
            write.writeheader()
            write.writerows(data)
            
            return buffer.getvalue()
        else :
            raise ValueError("Formato no soportado")
        
        
    # 
    def simular_archivo(self, data:list[dict]):
        buffer = io.StringIO()
        fieldname = data[0].keys()
        writer = csv.DictWriter(buffer, fieldnames=fieldname)

        # Escribir
        writer.writeheader()
        writer.writerows(data)

        # Volver al inicio
        buffer.seek(0)

        # Leer
        reader = csv.DictReader(buffer)
        return list(reader)

if __name__ == "__main__":
    main()
