# Guía de soluciones para los talleres 04 a 07

Esta guía repasa cada ejercicio resuelto en los talleres de estadística, clasificación, regresión y deep learning. En cada caso se resume el contexto teórico, la estrategia aplicada y se explican las porciones clave del código implementado en los cuadernos.

---

## Taller 04 · Estadística

### Ejercicio 1 · Ajuste de distribuciones normales
- **Marco teórico:** se compara una distribución normal analítica conocida con una aproximación empírica obtenida a partir de la media y desviación muestral.
- **Estrategia:** se usa `scipy.stats.norm` para construir ambas normales y `np.linspace` para generar el dominio de comparación.
- **Código clave:** cálculo de `sample_mean` y `sample_std` para parametrizar la distribución empírica y devolver ambos objetos junto con el rango de evaluación y el promedio de la muestra.

### Ejercicio 2 · Mezcla de gaussianas
- **Marco teórico:** combinación ponderada de dos distribuciones normales distintas.
- **Estrategia:** se generan muestras con `np.random.normal` respetando los porcentajes 30%/70% y luego se mezclan con `np.random.permutation`.
- **Código clave:** cálculo de los tamaños de muestra por distribución y concatenación de los arreglos antes de permutarlos.

### Ejercicio 3 · Distribución de Poisson
- **Marco teórico:** comparación entre una estimación Monte Carlo y la probabilidad exacta de una distribución de Poisson.
- **Estrategia:** se muestrean 10.000 valores con `np.random.poisson`, se calcula la probabilidad empírica por conteo, y se usa `scipy.stats.poisson` para la probabilidad analítica mediante la CDF.
- **Código clave:** uso de `np.mean((samples >= a) & (samples <= b))` para la estimación y `dist.cdf()` para la solución exacta.

### Ejercicio 4 · Probabilidad en un intervalo
- **Marco teórico:** integración de áreas bajo dos normales distintas utilizando la CDF.
- **Estrategia:** se modelan las dos distribuciones dadas y se suman las áreas izquierda y derecha respecto al punto de intersección.
- **Código clave:** invocaciones a `stats.norm(...).cdf()` con los límites `4`, `ins` y `8.5` para obtener la probabilidad total.

### Ejercicio 5 · CLT sobre GDP per cápita
- **Marco teórico:** aplicación del teorema del límite central sobre medias muestrales.
- **Estrategia:** se limpian los datos con `dropna`, se toman 100 muestras de tamaño 10 con `np.random.choice`, y se ajustan distribuciones normal empírica y analítica con `stats.norm`.
- **Código clave:** generación de `sample_means`, construcción de las distribuciones y cálculo de `ppf` al 1% y 99% para la versión analítica.

---

## Taller 05 · Clasificación

### Ejercicio 1 · Bosque aleatorio con perros de Zúrich
- **Marco teórico:** limpieza de datos categóricos y entrenamiento de un `RandomForestClassifier`.
- **Estrategia:** se eliminan columnas irrelevantes, se factoriza cada categoría y se mapea la variable objetivo `GESCHLECHT` a 0/1 antes de dividir el conjunto.
- **Código clave:** `pd.factorize` para columnas categóricas y `train_test_split(..., stratify=y)` para preservar el balance de clases.

### Ejercicio 2 · Comparación SVC vs Random Forest en cereales
- **Marco teórico:** evaluación de distintos clasificadores sobre datos categóricos convertidos a numéricos.
- **Estrategia:** se factoriza la columna `mfr`, se codifica la etiqueta `type` y se entrenan ambos modelos con la misma división 85/15.
- **Código clave:** entrenamiento consecutivo de `SVC` y `RandomForestClassifier`, devolviendo ambas exactitudes.

### Ejercicio 3 · Importancias en mordeduras de animales
- **Marco teórico:** uso de importancias de características para seleccionar las variables más relevantes.
- **Estrategia:** se eliminan columnas redundantes, se factoriza todo el bloque categórico, se entrena un árbol de decisión para obtener importancias y luego un bosque aleatorio solo con las dos variables principales.
- **Código clave:** `tree.feature_importances_` para identificar columnas críticas y un segundo `train_test_split` sobre el subconjunto reducido.

### Ejercicio 4 · Validación cruzada en ventas de supermercado
- **Marco teórico:** comparación de evaluación hold-out vs `KFold` usando un SVC polinómico.
- **Estrategia:** se factoriza cada columna categórica, se entrena el modelo con división 80/20 y se calcula `cross_val_score` con `KFold(2)`.
- **Código clave:** construcción manual del estimador para la validación cruzada y cálculo de media y desviación de la exactitud.

### Ejercicio 5 · Leave-one-out en pingüinos
- **Marco teórico:** validación cruzada extremo con `LeaveOneOut`.
- **Estrategia:** se eliminan nulos, se factorizan `species`, `island`, `sex` y se ejecuta `cross_val_score` con `LeaveOneOut` y métrica `accuracy_score`.
- **Código clave:** obtención del número de iteraciones con `loo.get_n_splits(X)` y cálculo de la media/desviación de la exactitud.

---

## Taller 06 · Regresión

### Ejercicio 1 · Bosque aleatorio para año de nacimiento de perros
- **Marco teórico:** regresión supervisada con variables categóricas codificadas.
- **Estrategia:** se limpian columnas, se factoriza cada categoría y se entrena un `RandomForestRegressor` con división 85/15.
- **Código clave:** cálculo de `mean_squared_error` y `mean_absolute_error` sobre el conjunto de prueba.

### Ejercicio 2 · Árbol de decisión para rating de cereales
- **Marco teórico:** regresión con un árbol profundo (`max_depth=100`).
- **Estrategia:** se eliminan nulos y la columna `name`, se factoriza `mfr` y `type`, y se calculan MAE/MSE del árbol sobre la división 90/10.
- **Código clave:** uso de `pd.factorize` para la codificación y el retorno ordenado `(mae, mse)` como pide el enunciado.

### Ejercicio 3 · Importancias y SVR lineal en ventas
- **Marco teórico:** selección de variables con importancias y entrenamiento posterior de un SVR.
- **Estrategia:** se factorizan columnas de supermercado, se ajusta un árbol para obtener importancias, se eligen las tres mejores características y se entrena un `SVR` lineal con ellas.
- **Código clave:** `np.argsort(importances)[-3:]` para seleccionar columnas y evaluación de ambos modelos con MAE.

### Ejercicio 4 · SVR polinómico con validación cruzada
- **Marco teórico:** evaluación combinada hold-out y `KFold` con error absoluto medio.
- **Estrategia:** se factorizan categorías, se entrena un `SVR` polinómico con `train_test_split(test_size=0.25)` y luego se calcula `cross_val_score` con `make_scorer(mean_absolute_error, greater_is_better=False)`.
- **Código clave:** inversión del signo de los puntajes (`mae_scores = -scores`) para reportar errores positivos.

### Ejercicio 5 · Leave-one-out para longitud de aletas
- **Marco teórico:** regresión evaluada con leave-one-out usando SVR.
- **Estrategia:** se limpian datos de pingüinos, se factorizan las categorías y se usa `cross_val_score` con `LeaveOneOut` para obtener la distribución de MAE.
- **Código clave:** conversión de los puntajes negativos a valores de error positivos antes de devolver media y desviación.

---

## Taller 07 · Deep Learning

### Ejercicio 1 · Clasificación de género en pingüinos
- **Marco teórico:** red densa para un problema multiclase con `sparse_categorical_crossentropy`.
- **Estrategia:** se factoriza cada categoría, se normalizan las columnas numéricas y se construye una red [256-128-64] más una capa de salida adaptada al número de clases.
- **Código clave:** determinación dinámica de `nc` y configuración de la última capa como `softmax` cuando hay más de dos clases.

### Ejercicio 2 · Clasificación del tipo de cereal
- **Marco teórico:** red densa de tres capas ocultas con activación `relu`.
- **Estrategia:** se eliminan nulos y la columna `name`, se factoriza `mfr` y `type`, se normalizan las variables y se entrena la red durante 10 épocas.
- **Código clave:** reutilización del patrón de capas con `keras.Sequential` y reporte de `(nc, loss, accuracy)` tras la evaluación.

### Ejercicio 3 · Clasificación de sucursal de supermercado
- **Marco teórico:** clasificación multiclase con tres capas densas de 256 neuronas.
- **Estrategia:** se factorizan todas las columnas categóricas, se normaliza el DataFrame y se entrena la red requerida con salida adaptada al número de clases.
- **Código clave:** normalización previa `(X - X.mean()) / X.std()` y el uso de `stratify=y` en la división para equilibrar clases.

### Ejercicio 4 · Regresión sobre precio unitario
- **Marco teórico:** red densa para regresión con pérdida MAE.
- **Estrategia:** se eliminan columnas y se factorizan categorías, se normalizan las variables y se configura la red [128, 256, 256, 1] entrenada durante 10 épocas.
- **Código clave:** capa final lineal (`Dense(1, activation='linear')`) y retorno de la pérdida (`loss`) obtenida con `model.evaluate`.

### Ejercicio 5 · Regresión sobre longitud de aletas
- **Marco teórico:** red densa profunda para regresión con MAE.
- **Estrategia:** se limpian valores nulos, se factorizan categorías, se normalizan las columnas y se entrena la arquitectura solicitada [128, 128, 256, 256, 1].
- **Código clave:** conversión de los datos a `np.float32` antes de ajustar el modelo y devolución de la pérdida de evaluación.

---

Con esta guía puedes repasar rápidamente la lógica aplicada en cada ejercicio y el razonamiento detrás de las implementaciones dentro de los notebooks de los talleres 04 a 07.
