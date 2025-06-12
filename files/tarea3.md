---
title: Tarea 3


**Profesor:** Leo Ferres
**Valor:** 4 puntos de homework
**Librerías clave:** `geopandas`, `pandas`, `matplotlib`, `rasterio`, `rasterstats`, `xarray`, `netCDF4`, `seaborn`, `scikit-learn`

## **Análisis Espacio-Temporal de Datos Climáticos**

## **Objetivo:**

En esta tarea, aprenderás a trabajar con datos ambientales y climáticos usando Python para visualizar y analizar patrones climáticos por regiones en un país, con énfasis en el análisis de series temporales. Crearás mapas temáticos de diferentes variables climáticas, identificarás zonas climáticas, y analizarás cómo estas variables cambian a lo largo del tiempo.



## **Parte 1: Búsqueda de Datos**

1. **País asignado:** Usa el mismo de las tareas anteriores.
2. **Datos requeridos (búscalos tú):**
	- **Divisiones administrativas** (nivel 1 o 2): usa el mismo shapefile limpio de la tarea anterior.
	- **Datos climáticos temporales:** busca datos mensuales o diarios para al menos 5 años en formato netCDF o series temporales para:
		- Temperatura media (WorldClim, ERA5, etc.)
		- Precipitación (WorldClim, CHIRPS, etc.)
		- Humedad relativa (ERA5, NCEP, etc.)
		- Velocidad del viento (ERA5, NCEP, etc.)
	- **Clasificación climática:** busca datos de clasificación climática de Köppen-Geiger (WorldClim, Beck et al. 2018, etc.)



## **Parte 2: Mapas de Variables Climáticas y Series Temporales**

1. Carga el shapefile de divisiones administrativas con `GeoPandas`.
2. Para cada variable climática (temperatura, precipitación, humedad, viento):
	- Carga los datos temporales usando `xarray` o `netCDF4`.
	- Calcula promedios mensuales y anuales por unidad administrativa.
	- Crea un mapa temático para el promedio anual. También pueden ver una animación [temporal usando qgis](https://www.qgistutorials.com/en/docs/3/animating_time_series.html).
	- Para dos regiones contrastantes (p. ej., la más húmeda y la más seca):
		- Grafica las series temporales mensuales de los últimos 5 años.
		- Identifica patrones estacionales.



## **Parte 3: Clasificación Climática**

1. Carga los datos de clasificación climática de Köppen-Geiger.
2. Crea un mapa mostrando las diferentes zonas climáticas en tu país.
3. Para cada zona climática, extrae y grafica las series temporales de temperatura y precipitación.
4. Compara los patrones estacionales entre diferentes zonas climáticas.



## **Parte 4: Análisis de Tendencias Temporales**

1. Para cada variable climática y por unidad administrativa:
	- Calcula promedios anuales para el período disponible.
	- Utiliza regresión lineal para identificar tendencias ( `sklearn.linear_model.LinearRegression`).
	- Crea un mapa temático mostrando donde las tendencias son más pronunciadas.
2. Identifica regiones con tendencias climáticas significativas:
	- Regiones que se están calentando más rápido.
	- Regiones con cambios significativos en patrones de lluvia.



## **Parte 5: Análisis de Eventos Extremos**

1. Para precipitación y temperatura:
	- Identifica valores extremos (percentiles 95 y 5) en las series temporales.
	- Crea mapas mostrando la frecuencia de eventos extremos por región.
	- Analiza si la frecuencia de eventos extremos ha cambiado con el tiempo.
2. Investiga un evento climático extremo específico (sequía, inundación, ola de calor) que haya afectado a tu país:
	- Visualiza cómo este evento se manifestó en tus datos.
	- Compara los valores con promedios históricos.



## **Parte 6: Correlaciones Espacio-Temporales**

1. Calcula correlaciones entre variables climáticas a lo largo del tiempo.
2. Investiga si estas correlaciones varían estacionalmente.
3. Crea un modelo predictivo simple que utilice datos de un mes para predecir valores del mes siguiente.
4. Evalúa la precisión de este modelo en diferentes regiones climáticas.



## **Entrega**

1. Un archivo `.ipynb` o `.py` con tu código bien comentado.
2. Un archivo Markdown (`README.md`) explicando:
	- Fuentes de datos utilizadas.
	- Metodología de procesamiento.
	- Resultados y conclusiones principales.
3. Incluye:
	- **Cuatro mapas temáticos** (uno por cada variable climática).
	- **Un mapa de clasificación climática**.
	- **Cuatro gráficos de series temporales** para diferentes regiones.
	- **Dos mapas de tendencias climáticas**.
	- **Un gráfico de eventos extremos**.



## **Estructura de Directorios**

Organiza tu proyecto con la siguiente estructura:

```
project/
|
+- data/
|  |
|  +- raw/                 # Datos originales sin procesar
|  +- processed/           # Datos procesados listos para análisis
|     |
|     +- climate/          # Variables climáticas procesadas
|     +- timeseries/       # Series temporales procesadas
|     +- geo/              # Datos geoespaciales procesados
|
+- notebooks/              # Jupyter notebooks
|
+- output/                 # Gráficos y mapas generados
|  |
|  +- maps/                # Mapas temáticos
|  +- timeseries/          # Gráficos de series temporales
|
+- README.md               # Documentación del proyecto
```



## **Fecha de entrega:** Viernes 11, 2025

## **Criterios de evaluación:**

| Criterio                                              | Puntos |
|-|--|
| Mapas de variables climáticas correctamente generados | 0.75   |
| Análisis de series temporales climáticas              | 1      |
| Clasificación climática implementada adecuadamente    | 0.5    |
| Análisis de tendencias y eventos extremos             | 1      |
| Implementación de correlaciones espacio-temporales    | 0.5    |
| Calidad de visualizaciones y análisis crítico         | 0.25   |



## **Recursos Recomendados:**

- Para datos climáticos temporales: [ERA5 Monthly](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land-monthly-means), [CHIRPS](https://www.chc.ucsb.edu/data/chirps), Tutorial on [downloading ERA5 data with Python](https://www.youtube.com/watch?v=jGWN53un6ZI&pp=ygULZXJhNSBweXRob24%3D), or maybe [Copernicus](https://www.youtube.com/watch?v=EIe7IBMqhsw&pp=ygUUZXJhNSBweXRob24gcGxvdHRpbmc%3D)
- Para trabajar con NetCDF ([tutorial](https://www.youtube.com/watch?v=ue55Mxe4yVQ))
- Para clasificación climática: [Beck et al. 2018](https://doi.org/10.1038/sdata.2018.214)
- Para aprender sobre series temporales climáticas: [Earth Data Science](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/)
- Tutorial para descomposición de series temporales: [Seasonal Decomposition with Python](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)
- Tutorial para análisis de eventos extremos: [Climate Extreme Indices with Python](https://climate-indices.readthedocs.io/en/latest/)
- Ejemplos de visualización de tendencias climáticas: [Climate Data Visualization](https://matplotlib.org/matplotblog/posts/warming-stripes/)
-
