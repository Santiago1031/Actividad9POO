from typing import Dict, Any

class AnalizadorLogs:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        total_solicitudes = 0
        solicitudes_por_metodo_HTTP = {}
        solicitudes_por_codigo = {}
        total_tamano_respuesta = 0
        tamano_promedio_respuesta = {}
        urls_solicitadas = {}

        with open(self.nombre_archivo, 'r', encoding= "utf-8") as f:

            for line in f:
                parts = line.split()
                if len(parts) == 7:
                    direccion_ip, fecha_hora, metodo, url, codigo_respuesta, tamano_respuesta = parts
                    total_solicitudes += 1
                    if metodo in solicitudes_por_metodo_HTTP:
                        solicitudes_por_metodo_HTTP[metodo] += 1
                    else:
                        solicitudes_por_metodo_HTTP[metodo] = 1

                    if codigo_respuesta in solicitudes_por_codigo:
                        solicitudes_por_codigo[codigo_respuesta] += 1
                    else:
                        solicitudes_por_codigo[codigo_respuesta] = 1
                    total_tamano_respuesta += int(tamano_respuesta)

                    if url in urls_solicitadas:
                        urls_solicitadas[url] += 1
                    else:
                        urls_solicitadas[url] = 1

        estadisticas = {
            "total_solicitudes": total_solicitudes,
            "solicitudes_por_metodo_HTTP": solicitudes_por_metodo_HTTP,
            "solicitudes_por_codigo": solicitudes_por_codigo,
            "total_tamano_respuesta": total_tamano_respuesta,
            "tamano_promedio_respuesta": tamano_promedio_respuesta,
            "urls_solicitadas": urls_solicitadas
        }

        return estadisticas


analizador = AnalizadorLogs(r"C:\Users\SANTIAGO\PycharmProjects\Actividad9POO\trafico_web.txt")
estadisticas = analizador.procesar_logs()
print(estadisticas)

