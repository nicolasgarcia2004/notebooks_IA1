# Guía completa para los talleres 04 a 07 de Inteligencia Artificial I

Esta guía explica, con un lenguaje sencillo, todos los conceptos teóricos y prácticos que necesitas dominar para resolver los talleres 04 (estadística), 05 (clasificación), 06 (regresión) y 07 (deep learning). Cada sección retoma las ideas clave de los cuadernos de clase y detalla las funciones y librerías que utilizarás en los ejercicios.

---

## 1. Estadística aplicada (Taller 04)

### 1.1 Distribuciones normales
- **Distribución normal**: modelo de probabilidad en forma de campana definido por su media (μ) y desviación estándar (σ).
- **`scipy.stats.norm`**: permite crear distribuciones normales analíticas. Métodos importantes:
  - `.pdf(x)`: densidad de probabilidad en cada valor de `x`.
  - `.cdf(x)`: probabilidad acumulada hasta `x`.
  - `.ppf(q)`: percentil asociado a una probabilidad `q` (lo inverso de `cdf`).
- **Media y desviación muestral**: `np.mean(muestras)` y `np.std(muestras, ddof=1)` calculan el centro y la dispersión de tus datos.
- **Aproximación empírica**: cuando desconoces la distribución real, puedes aproximarla con `stats.norm(loc=media_muestral, scale=desviacion_muestral)`.

### 1.2 Combinación de gaussianas
- Puedes mezclar muestras generadas desde diferentes normales con `np.random.normal(media, desviacion, cantidad)`.
- Para mezclar porcentajes distintos (p. ej. 30% y 70%), genera cantidades proporcionales y usa `np.random.permutation` para barajar las muestras.

### 1.3 Distribución de Poisson
- Modela eventos raros con tasa media λ.
- **`np.random.poisson(lam, size)`**: genera muestras simuladas.
- **`scipy.stats.poisson(lam)`**: distribución analítica con métodos `.pmf(k)` (probabilidad exacta discreta) y `.cdf`.
- Para estimar probabilidades empíricas, cuenta cuántas muestras caen en un intervalo y divide entre el número total.

### 1.4 Teorema del Límite Central (CLT)
- Si tomas muchas muestras aleatorias del mismo tamaño `N` desde una población, la media de cada muestra se distribuye aproximadamente como una normal.
- Pasos prácticos:
  1. Toma la columna numérica del `DataFrame` y calcula su media y desviación poblacional.
  2. Repite 100 veces: extrae `N` elementos al azar sin reemplazo y calcula la media.
  3. Ajusta una normal empírica a las medias (`loc=np.mean(medias)`, `scale=np.std(medias, ddof=1)`).
  4. Para la versión analítica, usa la media poblacional y la desviación poblacional dividida por `sqrt(N)`.

---

## 2. Clasificación con scikit-learn (Taller 05)

### 2.1 Limpieza y preparación de datos
- **Eliminar valores nulos**: `df = df.dropna()`.
- **Eliminar columnas**: `df = df.drop(columns=[...])`.
- **Codificación categórica rápida**: `df[col], _ = pd.factorize(df[col])` asigna números consecutivos a cada categoría.
- **Separar características y etiqueta**:
  ```python
  y = df['columna_objetivo']
  X = df.drop(columns=['columna_objetivo'])
  ```

### 2.2 Dividir en entrenamiento y prueba
- Usa `train_test_split(X, y, test_size=0.2, random_state=21)` para obtener subconjuntos reproducibles.

### 2.3 Modelos de clasificación
- **`RandomForestClassifier`**: ensamble de árboles que promedia sus predicciones. Parámetros clave:
  - `n_estimators`: número de árboles.
  - `random_state`: fija la semilla.
- **`DecisionTreeClassifier`**: árbol único, útil para obtener importancias de características (`modelo.feature_importances_`).
- **`SVC` (Support Vector Classifier)**: clasificador basado en hiperplanos; define el `kernel`.

### 2.4 Métricas
- **`accuracy_score(y_true, y_pred)`**: proporción de predicciones correctas.
- **`cross_val_score`** con `KFold`: evalúa el modelo en particiones múltiples. Calcula media y desviación con `scores.mean()` y `scores.std()`.
- **`make_scorer(accuracy_score)`**: adapta la métrica para `cross_validate` si lo necesitas.

---

## 3. Regresión con scikit-learn (Taller 06)

### 3.1 Preprocesamiento
- Misma idea: elimina nulos y columnas, codifica categorías y separa `X` (características) y `y` (objetivo numérico).

### 3.2 Modelos de regresión
- **`LinearRegression`**: modelo lineal básico.
- **`PolynomialFeatures` + `LinearRegression`**: genera términos polinómicos para capturar curvaturas.
- **`Ridge` / `Lasso`**: regresiones lineales con regularización L2 o L1 respectivamente.
- **`RandomForestRegressor`**: ensamble de árboles para regresión.

### 3.3 Evaluación
- **`mean_squared_error` (MSE)**: promedio de errores al cuadrado.
- **`mean_absolute_error` (MAE)**: promedio de errores absolutos.
- **`r2_score`**: proporción de varianza explicada (1 es perfecto).
- Usa `train_test_split` para crear conjuntos de entrenamiento/prueba.

---

## 4. Redes neuronales con TensorFlow/Keras (Taller 07)

### 4.1 Preparación de datos
- Mantén los mismos pasos de limpieza y codificación que en scikit-learn.
- Convierte `DataFrame` a `numpy` (`X.to_numpy()`) y asegúrate de que las etiquetas sean numéricas.
- Divide con `train_test_split`.

### 4.2 Construcción de modelos
- **Modelos secuenciales (`keras.Sequential`)**: apila capas densas con `Dense(units, activation=...)`.
- **Inicialización reproducible**: fija semillas con `np.random.seed`, `tf.random.set_seed` y `tf.keras.utils.set_random_seed`.
- Capas finales:
  - Clasificación multiclase: `Dense(numero_clases, activation='softmax')`.
  - Clasificación binaria: `Dense(1, activation='sigmoid')`.
  - Regresión: `Dense(1, activation='linear')`.

### 4.3 Entrenamiento y evaluación
- **Compilar** con optimizador y métricas adecuadas:
  - Clasificación multiclase: `loss='sparse_categorical_crossentropy', metrics=['accuracy']`.
  - Regresión: `loss='mae', metrics=['mae', 'mse']`.
- **Entrenar** con `.fit(X_train, y_train, epochs=10, verbose=0)`.
- **Evaluar** con `.evaluate(X_test, y_test, verbose=0)` que retorna pérdidas y métricas.

### 4.4 Buenas prácticas
- Normaliza columnas numéricas si cambia mucho la escala (`(col - col.mean()) / col.std()`), especialmente para redes neuronales.
- Conserva los conjuntos de prueba separados para medir el desempeño real.

---

## 5. Librerías clave

| Librería | Uso principal |
|----------|----------------|
| `numpy` | Manejo de arreglos, generación de números aleatorios, estadísticas básicas. |
| `pandas` | Manipulación de datos tabulares, eliminación de nulos, codificación de categorías. |
| `scipy.stats` | Creación de distribuciones estadísticas (normal, Poisson), funciones `pdf`, `cdf`, `ppf`. |
| `matplotlib.pyplot` | Visualización de resultados (histogramas, curvas). |
| `scikit-learn` | Modelos de clasificación/regresión, división de datos, métricas y validación cruzada. |
| `tensorflow.keras` | Construcción y entrenamiento de redes neuronales densas. |

---

## 6. Flujo general para resolver los talleres

1. **Leer el enunciado** para identificar columnas objetivo, columnas a eliminar y transformaciones requeridas.
2. **Limpiar y preparar**: elimina nulos, factoriza categorías, separa `X` e `y` y divide en entrenamiento/prueba.
3. **Construir el modelo** indicado (distribución estadística, estimador de scikit-learn o red neuronal).
4. **Entrenar y evaluar** siguiendo los parámetros exactos pedidos (semillas, tamaños de muestra, épocas, etc.).
5. **Devolver los valores solicitados** en el mismo orden y formato que exige el ejercicio.
6. **Comentar el código** para recordar la lógica de cada paso cuando repases para el examen.

Con esta guía deberías contar con todas las herramientas conceptuales y prácticas necesarias para abordar los ejercicios de los talleres 04 a 07.
