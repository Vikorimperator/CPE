CPE
==============================

Proyecto para normalizar y realizar sinteticos de los registros de pozos para el Campo Caparroso-Pijije-Escuintle

Organización del Proyecto
------------

    ├── LICENSE
    ├── README.md          <- El archivo README de nivel superior para desarrolladores que utilizan este proyecto.
    ├── data
    │   ├── interim        <- Datos intermedios que han sido transformados.
    │   ├── processed      <- Los conjuntos de datos finales, resultados.
    │   └── raw            <- El volcado de datos original e inmutable.
    │
    ├── docs               <- Un proyecto Sphinx predeterminado.
    │
    ├── models             <- Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos.
    │
    ├── notebooks          <- Cuadernos Jupyter. La convención de nomenclatura es un número (para ordenar),
    │                         las iniciales del creador y una breve descripción delimitada por `-`.
    │
    ├── references         <- Diccionarios de datos, manuales y todos los demás materiales explicativos.
    │
    ├── reports            <- Análisis generados como HTML, PDF, LaTeX, etc.
    │   └── figures        <- Gráficos y figuras generados que se utilizarán en los informes.
    │
    ├── requirements.txt   <- El archivo de requisitos para reproducir el entorno de análisis..
    │
    ├── setup.py           <- hace que el proyecto pip sea instalable para que se pueda importar src.
    ├── src                <- Código fuente para usar en este proyecto.
    │   ├── __init__.py    <- Hace que src sea un módulo de Python.
    │   │
    │   ├── data_transform <- Scripts para transformar o procesar datos.
    │   │   ├── __init__.py
    │   │   ├── load_csv.py
    │   │   ├── map_cimas_to_depth_multiple.py
    │   │   ├── normalize_well_log.py
    │   │   ├── normalize_well_logs_by_cima.py
    │   │   ├── print_unique_values.py
    │   │   └── save_data_csv.py    
    │   │
    │   ├── features       <- Scripts para convertir datos sin procesar en funciones para modelar
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para entrenar modelos y luego usar modelos entrenados para hacer predicciones.
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para crear visualizaciones exploratorias y orientadas a resultados.
    │       └── visualize.py
    │
    └── tox.ini            <- Archivo tox con configuraciones para ejecutar tox


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
