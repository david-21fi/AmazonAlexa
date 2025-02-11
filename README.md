# 📢 Predicción de Sentimientos en Reseñas de Amazon Alexa  

## 📌 Descripción del Proyecto  
Este proyecto tiene como objetivo desarrollar un **modelo de machine learning** para predecir la aprobación de los usuarios sobre el producto **Amazon Alexa** basado en comentarios y reseñas.  
Utilizando técnicas de **procesamiento de lenguaje natural (NLP)** y **modelos de clasificación**, analizamos la percepción del consumidor para obtener insights clave que ayuden en la toma de decisiones.  

---

## 🚀 Comprensión del Negocio  
En la era digital, la opinión de los clientes juega un papel fundamental en el éxito de los productos tecnológicos. **Amazon Alexa** es uno de los asistentes virtuales más populares, y su aceptación en el mercado depende en gran medida de la satisfacción del usuario.  
Este proyecto busca responder:  
- ¿Qué factores influyen en una **reseña positiva o negativa** de Amazon Alexa?  
- ¿Podemos construir un modelo que **prediga la aprobación del producto** con base en comentarios de usuarios?  
- ¿Cuáles son las **palabras clave y sentimientos** más asociados con opiniones favorables o desfavorables?  

---

## 📊 Descripción de los Datos  
Los datos utilizados en este análisis provienen de reseñas de **Amazon Alexa** y contienen las siguientes variables:  
- **`rating`**: Calificación otorgada por el usuario (escala de 1 a 5).  
- **`feedback`**: Clasificación binaria de satisfacción (1 = positivo, 0 = negativo).  
- **`verified_reviews`**: Texto de la reseña del usuario.  
- **`variation`**: Modelo o tipo de Amazon Alexa reseñado.  

💡 **Objetivo:** Utilizar las reseñas para construir un modelo de predicción de la variable `feedback`.  

---

## 📈 Análisis Exploratorio  
Antes de entrenar el modelo, realizamos un **análisis exploratorio de los datos (EDA)**, incluyendo:  
- **Distribución de las calificaciones** 📊  
- **Nube de palabras** para visualizar términos más frecuentes en reseñas positivas y negativas ☁️  
- **Análisis de correlación** entre la calificación y la polaridad de los comentarios 🔍  
- **Ejemplo de comentarios positivos y negativos** para identificar patrones clave  

✍️ _Puedes ver el análisis exploratorio completo en el siguiente Notebook:_  
👉 **[Análisis Exploratorio](./Notebooks/analisis_exploratorio.ipynb)**  

---

## 🤖 Modelos de Machine Learning  
Se probaron diferentes modelos para predecir la satisfacción del cliente:  
- **Naïve Bayes** (Multinomial y Gaussiano)  
- **Regresión Logística**  
- **Random Forest**  
- **XGBoost**  

### 🏆 **Modelo Final**  
El modelo que mejor rendimiento obtuvo fue `XGBoost`, con una capacidad de explicar el **57% de la variabilidad en las opiniones**.  
Este resultado permitirá a Amazon mejorar su producto al identificar **factores clave que influyen en la percepción del usuario**.  

📌 **Métricas utilizadas:**  
- **Accuracy**: 92 
- **Precision y Recall**  
- **F1_Score** para evaluar el balance de predicciones 
- **Matriz de confusión** para visualizar errores en clasificación  
- **F1_Score**

---

## 📂 Estructura del Proyecto  
