---
title: Tarea 2
---

**Profesor:** Leo Ferres
**Valor:** 4 puntos de homework
**Librerías clave:** `geopandas`, `pandas`, `matplotlib`, `rasterio`, `rasterstats`
## Limpieza

Ya posiblemente tenemos todas las capas de Sudamérica. Habíamos dicho en la clase del viernes que íbamos a limpirar un poco todos los archivos. Entonces, cada grupo tiene que hacer los siguiente:

1. Creen la estructura de directorios siguiente:
	1. ![[Pasted image 20250323181819.png]]

> [!info]
> No presten atención a `meta.ipynb`, ese es mi directorio y tiene cosas que todavia no les paso.)

2. En `raw` pongan todos los archivos de capas que tienen. En el `processed/raw` pongan la capa con el nivel administrativo más fino (sería comuna en Chile).

> [!warning]
>  Yo sé que habíamos hablado de poner todas las capas, pero quiero solo las capas más finas en `processed/geo`.

## **Mapas de Población, Aeropuertos y Luces Nocturnas**

## **Objetivo:**

En esta tarea, aprenderás a trabajar con datos geoespaciales usando Python para visualizar y analizar la población de un país por unidades administrativas. Harás un mapa temático (choropleth), buscarás y agregarás la ubicación de aeropuertos y correlacionarás datos de población oficial con datos satelitales de luces nocturnas (nightlights) usando estadísticas básicas.



## **Parte 1: Búsqueda de Datos**

1. **País asignado:** Usa el mismo de la tarea anterior.
2. **Datos requeridos (búscalos tú):**
	- **Divisiones administrativas** (nivel 1 o 2): usa fuentes como GADM, OSM, o datos oficiales del país.
	- **Población por unidad administrativa** (si no viene incluido, busca en censos o estimaciones oficiales).
	- **Aeropuertos:** puedes usar OSM o bases como OurAirports.
	- **Luces nocturnas:** descarga un raster reciente desde [VIIRS](https://eogdata.mines.edu/products/vnl/) o similar.



## **Parte 2: Mapa Coroplético**

1. Carga el shapefile de divisiones administrativas con `GeoPandas`. Ver un tutorial de `geopandas` [aqui](https://www.youtube.com/watch?v=HULN8-6t2pc)
2. Une los datos de población por unidad administrativa.
3. Usa `.plot(column="poblacion")` para crear un mapa donde el color represente la población. [Ver tutorial aqui](https://www.youtube.com/watch?v=Q0z1cPD_7yE)
4. Ajusta leyendas, títulos y estilos para mejorar la visualización.



## **Parte 3: Aeropuertos**

1. Busca y carga la base de datos de aeropuertos.
2. Usa `GeoPandas` para convertir las coordenadas en una capa geográfica.
3. Añade esta capa sobre el mapa anterior con puntos (usa `.plot(marker="o")`).



## **Parte 4: Análisis de Luces Nocturnas**

Esta parte está inspirada en el [trabajo de Andy Tatem en WorldPop](https://www.youtube.com/watch?v=nZAXpWwjOmQ). Pueden ver [este tutorial](https://www.youtube.com/watch?v=EbI8uUx4xPI) para saber como bajar raster de nightlights, no he podido encontrar uno mejor. Ustedes?

1. Carga el raster de luces nocturnas usando `rasterio`.
2. Usa `zonal_stats` de `rasterstats` para calcular el brillo total promedio en cada unidad administrativa.
3. Crea un `DataFrame` con dos columnas: población (oficial) y brillo (luces).
4. Calcula la correlación con `pandas.DataFrame.corr()`.



## **Parte 5: Análisis y Visualización**

1. Comenta si hay correlación alta o baja entre población y luces.
2. ¿Hay regiones con mucha luz pero poca población? ¿O al revés?
3. Incluye un gráfico de dispersión (`matplotlib.pyplot.scatter`) entre ambas variables.



## **Entrega**

1. Un archivo `.ipynb` o `.py` con tu código bien comentado.
2. Un archivo Markdown (`README.md`) explicando:
	- Fuentes de datos usadas.
	- Resultados y conclusiones.
3. Incluye al menos **dos mapas** (población y luces) y **un gráfico de correlación**.



## **Fecha de entrega:** Jueves 27, 2025

## **Criterios de evaluación:**

| Criterio                                             | Puntos |
| - |  |
| Mapa de población correctamente generado             | 1      |
| Aeropuertos localizados y visualizados correctamente | 0.5    |
| Análisis de raster y correlación completado          | 1.5    |
| Visualizaciones y análisis crítico                   | 1      |
