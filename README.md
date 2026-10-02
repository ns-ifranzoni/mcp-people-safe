# mcp-people-safe

Servidor MCP sencillo para el sector farmacéutico con una herramienta de **resumen especializado en temas de gestion de personal** (ids, info, informes...). Hecho con [FastMCP](https://gofastmcp.com) y listo para desplegar en [Prefect Horizon](https://horizon.prefect.io).

## Herramienta

| Herramienta | Qué hace |
|---|---|
| `summary_for_people_topics(text)` | Crea un resumen pensado especialmente para temas de gestión de personal. Devuelve las pautas de resumen (datos, nombres, indicaciones, datos de empresa, advertencias...) junto con el texto, para que el modelo redacte el resumen. |

El título visible es "Summary for people topics"; el nombre técnico usa guiones bajos porque los clientes MCP no admiten espacios en los nombres de herramienta.

## Desplegar en Prefect Horizon

1. Entra en [horizon.prefect.io](https://horizon.prefect.io) e inicia sesión con GitHub.
2. *Servers → New server* y selecciona este repositorio (`ns-ifranzoni/pharma-safe-mcp`).
3. Configura:
   - **Entrypoint:** `server.py:mcp`
   - **Branch:** `main`
   - Las dependencias se leen de `requirements.txt`.
4. Despliega. Horizon te dará la URL del servidor MCP para conectarlo a Claude u otros clientes.

## Uso local

```bash
pip install -r requirements.txt pytest
fastmcp run server.py           # servidor MCP por stdio
fastmcp run server.py --transport http   # o por HTTP
pytest                          # tests
```
