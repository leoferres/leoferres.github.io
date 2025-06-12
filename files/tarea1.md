---
title: Tarea 1
---

Leo Ferres <lferres@udd.cl>

Ya hemos decidido los grupos:

```
Group 1: Uruguay
Group 2: Ecuador
Group 3: Colombia
Group 4: Argentina
Group 5: Bolivia
Group 6: Brazil
Group 7: Venezuela
Group 8: Paraguay
Group 9: Peru
Group Leo: Chile
Out: Suriname and Guyana
```

## **Guía de Estudio: Instalación y Uso Básico de QGIS para la Creación del Proyecto "Geodengue"**

**Objetivo:**  
El objetivo de esta actividad es que los estudiantes instalen QGIS, aprendan a utilizarlo mediante un tutorial, descarguen los datos geoespaciales correspondientes a su país asignado y creen un proyecto con una estructura organizada. Al final de la tarea, deberán generar dos mallas regulares de 500m x 500m y 250m x 250m sobre su territorio.

Esta tarea es fundamental, ya que todos los análisis, modelados y estudios que se desarrollarán a lo largo del curso estarán basados en los datos obtenidos en esta primera actividad. Es crucial que los datos se descarguen correctamente y que la estructura del proyecto en QGIS esté bien organizada desde el inicio.

**Valor:** 3 puntos de homework.



### **Parte 1: Instalación de QGIS**

1. Descargue la última versión estable de QGIS desde el sitio oficial: [https://qgis.org](https://qgis.org/)
2. Instale el programa siguiendo las instrucciones para su sistema operativo (Windows, macOS o Linux).
3. Una vez instalado, abra QGIS para confirmar que funciona correctamente.



### **Parte 2: Introducción a QGIS**

1. Mire el siguiente tutorial introductorio a QGIS:
    - [Bajar](https://qgis.org/download/) e [instalar](https://mappinggis.com/2017/09/como-descargar-e-instalar-qgis-en-windows/) QGIS
    - [Buena intro](https://www.youtube.com/watch?v=sKfv6qAlrcw), y [otra](https://docs.qgis.org/3.40/es/docs/training_manual/index.html) muy completa (textual)
    - [Guía para principiantes de QGIS](https://www.qgistutorials.com/en/docs/3/getting_started.html) (muy completo)
	- [Este otro](https://www.youtube.com/watch?v=GVxo0j7FkjY) está bueno también, pero es más avanzado
2. Explore las herramientas básicas de QGIS, en particular:
    - Carga de capas vectoriales (shapefiles)
    - Simbología y estilos
    - Creación de nuevas capas y edición de geometrías



### **Parte 3: Descarga de Datos Geoespaciales**

1. Descargue los shapefiles de su país asignado. Busque fuentes oficiales como:
    
    - **GADM**: [https://gadm.org](https://gadm.org/) (para divisiones administrativas)
    - **OpenStreetMap (OSM)**: Puede usar la herramienta [https://download.geofabrik.de](https://download.geofabrik.de/) para descargar datos de su país.
    - **Portales gubernamentales** de datos geográficos.
2. Asegúrese de descargar al menos las siguientes capas:
    
    - Divisiones administrativas (país, provincias, municipios, parroquias, etc.).
    - Redes de carreteras principales.
    - (y otros archivos que encuentren y crean que puedan servirnos en el futuro)



### **Parte 4: Creación del Proyecto "Geodengue" en QGIS**

1. Abra QGIS y cree un nuevo proyecto.
2. Guarde el proyecto con el nombre **"Geodengue"** en una carpeta dedicada a esta actividad.
3. Cargue los shapefiles descargados en el proyecto.
4. Ajuste la simbología de las capas para que se visualicen claramente.
5. Configure el sistema de coordenadas adecuado para su país (WGS 84 o el CRS nacional recomendado).



### **Parte 5: Creación de una Grilla Regular**

1. Para generar una cuadrícula de referencia:
    - Vaya al menú **Vector > Herramientas de investigación > Crear rejilla**.
    - Configure el sistema de coordenadas adecuado.
    - Defina el tamaño de celda en 500m x 500m y genere la grilla.
    - Guarde la grilla en formato shapefile en su carpeta de trabajo.
2. Repita el proceso para generar una grilla de 250m x 250m.
3. Verifique que ambas grillas cubren adecuadamente el área de estudio y superpongan correctamente las capas cargadas.



### **Entrega**

Para completar la tarea, cree una carpeta en este [directorio de OneDrive]([iele754](https://uddcl-my.sharepoint.com/:f:/g/personal/lferres_udd_cl1/Eok4MgzdXtxOg3B_GNohRWUBVbBWannKxrguunK2fp-xfw?e=leJohI)) con el nombre de su país y, adentro de esa carpeta, suba los siguientes archivos:

1. El archivo del proyecto QGIS (**.qgz**) llamado "Geodengue".
2. Los shapefiles descargados.
3. Las dos grillas generadas.
4. Una captura de pantalla del proyecto en QGIS mostrando las capas correctamente cargadas.

En Canvas, entregue un archivo markdown con la lista de archivos entregados.



**Fecha de entrega:** Jueves 20, 2025

**Criterios de evaluación:** 

- Instalación y uso básico de QGIS (1 punto)
- Descarga y correcta carga de los shapefiles (1 punto)
- Generación y correcta visualización de las grillas de 500m y 250m (1 punto)



**Notas adicionales:**

- Si tiene problemas para descargar datos, consulte con el instructor.
- Se recomienda mantener una organización clara de archivos para facilitar el trabajo en futuras actividades.
