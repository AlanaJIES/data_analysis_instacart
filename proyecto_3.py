#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Al!
#
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
#
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
#
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
#
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Si todo está perfecto.
# </div>
#
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
#
# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
#
# Puedes responderme de esta forma:
#
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
#
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
#
# ¡Empecemos!

# # ¡Llena ese carrito!

# # Introducción
#
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
#
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
#

# ## Diccionario de datos
#
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
#
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# # Paso 1. Descripción de los datos
#
# Lee los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) con `pd.read_csv()` usando los parámetros adecuados para leer los datos correctamente. Verifica la información para cada DataFrame creado.
#

# ## Plan de solución
#
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.
#
# Primero es importar la librería correspondiente, en este caso "pandas as pd". Luego de esto se leen los archivos
# como valores separados por comas (los archivos son csv, de acuerdo a la terminación de los mismos).
# Se imprimen las 5 primeras filas usando el método "head()" para verificar cual es el delimitador de estos archivos.
# Luego, de ser necesario, se cambia el argumento del parámetro "sep=" por el delimitador correspondiente.
# Se lee la información general de los data frames usando el método "info()", observando la presencia de datos nulos y el tipo de datos que tenemos en los dataframes.

# In[1]:


# importar librerías
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


# leer conjuntos de datos en los DataFrames
insta_ord = pd.read_csv("/datasets/instacart_orders.csv", sep=';')

prod = pd.read_csv("/datasets/products.csv", sep=';')

aisles = pd.read_csv("/datasets/aisles.csv", sep=';')

deps = pd.read_csv("/datasets/departments.csv", sep=';')

order_prod = pd.read_csv("/datasets/order_products.csv", sep=';')


# In[3]:


# mostrar información del DataFrame
display(insta_ord)
insta_ord.info()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[4]:


# mostrar información del DataFrame
display(prod)
prod.info()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[5]:


# mostrar información del DataFrame
display(aisles)
aisles.info()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[6]:


# mostrar información del DataFrame
display(deps)
deps.info()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[7]:


# mostrar información del DataFrame
display(order_prod)
order_prod.info(show_counts=True)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# ## Conclusiones
#
# Escribe aquí tus conclusiones intermedias sobre el Paso 1. Descripción de los datos.
#
# Se importo la librería, se leyeron los data frames y se mostraron tomando en consideracion que el delimitador de todos los archivos es ";". Los titulos de las columnas concuerdan con el diccionario de datos, por lo que no se considero necesario cambiar los titulos por otros más concisos.
#
# Ahora con los archivos:
#
# En el archivo instacart_orders.csv encontramos que la columna "days_since_prior_order" posee datos nulos. Este último tiene datos tipo "float", lo cual podria estar relacionado con la presencia de los datos nulos.
#
# En el archivo products.csv encontramos que la columna "product_name" posee datos nulos. Este posee datos tipo "object", son los nombres de los productos.
#
# En el archivo order_products.csv, encontramos que la columna "add_to_cart_order" posee datos nulos. Este último tiene datos tipo "float", lo cual podria estar relacionado con la presencia de los datos nulos.
#
# Los datos de las demás columnas son enteros u objetos, dependiendo de la naturaleza de los mismos (si son numericos, como los ID, o nombres, de los departamentos y pasillos).

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy buenas conclusiones.
# </div>

# # Paso 2. Preprocesamiento de los datos
#
# Preprocesa los datos de la siguiente manera:
#
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
#
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# ## Plan de solución
#
# Escribe aquí tu plan para el Paso 2. Preprocesamiento de los datos.
#
# En el paso anterior, usando "info()", se observo el tipo de datos de los dataframes. Los datos tipo float podrían ser transformados en enteros, luego de identificar los valores ausentes y determinar la razón de los mismos. Esto podría hacerse con "astype()", siempre y cuando se haya verificado usando la función "array_equal()" de la librería numpy.
#
# La identificacion de los valores ausentes se hará principalmente usando "isna()", "dropna()" y/o "fillna()", dependiendo de las circunstancias.
#
# Los valores duplicados se eliminaran si son filas completas y se analizara con mayor detalle si son en determinadas columnas. Se usaran los métodos "duplicated().sum()", "value_counts()"
#

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien.
# </div>

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `orders` data frame

# In[8]:


# Revisa si hay pedidos duplicados

display(insta_ord.duplicated().sum())
display(insta_ord["order_id"].value_counts().head(16))
display(insta_ord.value_counts().head(16))
insta_ord[insta_ord["order_id"] == 2125197]
insta_ord[insta_ord["order_id"] == 1782114]
display(insta_ord[(insta_ord["order_hour_of_day"] == 2) & (
    insta_ord["order_dow"] == 3)].value_counts().head(16))


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta muy bien. Recorda no utilizar el print y llamar directamente al metodo.
#
# </div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?

# # Basándote en tus hallazgos,
#
# Si existen lineas duplicadas. Las 15 ocurrieron un miércoles a las 2:00 a.m.
#
# # Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.

# ¿Qué sugiere este resultado?
#
# Esto sugiere que debio ocurrir un error en la aplicación, generando estos duplicados por accidente.

# In[9]:


# Elimina los pedidos duplicados
insta_ord = insta_ord.drop_duplicates(subset="order_id").reset_index(drop=True)


# In[10]:


# Vuelve a verificar si hay filas duplicadas
insta_ord.duplicated().sum()


# In[11]:


# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
display(insta_ord["order_id"].value_counts().head(16))
display(insta_ord[(insta_ord["order_hour_of_day"] == 2) & (
    insta_ord["order_dow"] == 3)].value_counts().head(16))


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# Habia 15 filas duplicadas. Todas ocurrieron el miércoles a las 2 de la madrugada. Suponiendo un error de la aplicación que duplicó las ordenes, los duplicados fueron eliminados.

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# Para que quede mas claro podrias realizar expresiones anidadas dejando solo el dataframe donde este enmascarado los miercoles y a las dos de la mañana.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Excelente.</div>

# ### `products` data frame

# In[12]:


# Verifica si hay filas totalmente duplicadas
prod.duplicated().sum()


# In[13]:


# Verifica únicamente si hay IDs duplicadas de productos
prod["product_id"].duplicated().sum()


# In[14]:


# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
prod["product_name"] = prod["product_name"].str.upper()
prod["product_name"].duplicated().sum()


# In[15]:


# Revisa si hay nombres duplicados de productos no faltantes
duplicated_not_null = prod[prod["product_name"].duplicated(
    keep=False) & prod["product_name"].notnull()]
display(duplicated_not_null.duplicated().sum())

duplicated_and_not_null = prod[prod["product_name"].duplicated(
) & prod["product_name"].notnull()]
display(duplicated_and_not_null.duplicated().sum())


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# Se buscaron filas duplicadas en el dataframe de products (prod). No se encontraron filas duplicadas, ni ID's duplicados de productos.
# En los nombres de los productos, si hay duplicados y estan relacionados con los valores ausentes. Esto lo observamos al verificar dos dataframes donde los datos ausentes no se encuentran pero en una mantenemos los datos duplicados y en en el otro no. En ambos dataframes no se observaron los datos nomres duplicados de productos.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Si bien estan relacionados como muy bien observas, hace una mascara donde solo dejes un dataframe que muestre los que no son nulos con aquellos duplicados a ver si solo es esa la relacion y conclui al respecto.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# ### `departments` data frame

# In[16]:


# Revisa si hay filas totalmente duplicadas
print(deps.duplicated().sum())


# In[17]:


# Revisa únicamente si hay IDs duplicadas de productos
print(deps["department_id"].duplicated().sum())


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# No se observaron duplicados, ni de filas ni de ID's. No se modificó el dataframe.

# ### `aisles` data frame

# In[18]:


# Revisa si hay filas totalmente duplicadas
print(aisles.duplicated().sum())


# In[19]:


# Revisa únicamente si hay IDs duplicadas de productos
print(aisles["aisle_id"].duplicated().sum())


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# No se observaron duplicados, ni de filas ni de ID's. No se modificó el dataframe.

# ### `order_products` data frame

# In[20]:


# Revisa si hay filas totalmente duplicadas
print(order_prod.duplicated().sum())


# In[21]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
print(order_prod["order_id"].duplicated().sum())
print()
print(order_prod["order_id"].value_counts().head())
duplicated_tricky = order_prod[order_prod["product_id"].duplicated(keep=False)
                               & order_prod["add_to_cart_order"].notnull()]
print()
order_prod.info(show_counts=True)
print()
duplicated_tricky.info(show_counts=True)
print()
print(duplicated_tricky["order_id"].duplicated().sum())


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# No se observó duplicados de filas. Si se observó "duplicados" en los ID's de las órdenes, aunque esto se puede explicar con que cada fila es un artículo único de cada pedido, por lo que es normal que las personas pidan más cosas en un pedido o inclusive más de un mismo articulo en un pedido. No se modificó el dataframe. Los datos ausentes no parecen ser la principal causa de los datos duplicados, pero si hay una diferencia cuando retiramos los datos nulos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien.</div>

# ## Encuentra y elimina los valores ausentes
#
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
#
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[22]:


# Encuentra los valores ausentes en la columna 'product_name'
print(prod[prod["product_name"].isna()])


# Describe brevemente cuáles son tus hallazgos.
#
# Hay 1258 datos ausentes. Todos tienen en común el ID del pasillo 100 y el ID del departamento 21.

# In[23]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
print(prod[prod["product_name"].isna() & ~(prod["aisle_id"] == 100)])


# Describe brevemente cuáles son tus hallazgos.
#
# Cuando buscamos un dato ausente en otro id de pasillo que no sea 100, no encontramos un dato ausente.

# In[24]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
print(prod[prod["product_name"].isna() & ~(prod["department_id"] == 21)])


# Describe brevemente cuáles son tus hallazgos.
#
# Cuando buscamos un dato ausente en otro id del departamento que no sea 21, no encontramos un dato ausente.

# In[25]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.
print(aisles[aisles["aisle_id"] == 100])
print(deps[deps["department_id"] == 21])


# Describe brevemente cuáles son tus hallazgos.
#
# Cuando buscamos un cualquier dato que se encuentre en en el departamento 21 o en el pasillo 100 no podemos encontrar nada de información.

# In[26]:


# Completa los nombres de productos ausentes con 'Unknown'
prod["product_name"] = prod["product_name"].fillna("Unknown")
print(prod[prod["product_name"].isna()])
prod.info()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# LLenamos los datos ausentes con "Unknown" con todos aquellos productos relacionados con el pasillo 100 y departamento 21. Verificamos que ya no hay datos ausentes en el Dataframe.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien.</div>

# ### `orders` data frame

# In[27]:


# Encuentra los valores ausentes
# print(insta_ord[insta_ord["days_since_prior_order"].isna()])


# In[28]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
print(insta_ord[insta_ord["days_since_prior_order"].isna()
      & ~(insta_ord["order_number"] == 1)])

print()
insta_ord["days_since_prior_order"] = insta_ord["days_since_prior_order"].fillna(
    0)
print(insta_ord[insta_ord["days_since_prior_order"].isna()])
print()
insta_ord.info()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# No hay ningún valor ausente que no sea el primer pedido del cliente. Se llenó los datos ausentes con un "0" (cero), haciendo referencia a que no ha habido otro pedido anterior. No se osbervó un cambio en el el tipo de datos "float".

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta muy bien como lo pensaste.</div>

# ### `order_products` data frame

# In[29]:


# Encuentra los valores ausentes
order_prod.info(show_counts=True)
print()
print(order_prod[order_prod["add_to_cart_order"].isna()])


# In[30]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?
print(order_prod["add_to_cart_order"].min())
print()
print(order_prod["add_to_cart_order"].max())


# Describe brevemente cuáles son tus hallazgos.
#
# Los valores máximos y mínimos son 64.0 y 1.0, respectivamente en la columna "add_to_cart_order". Luego del 64 podría ser necesario hacer otra orden para agregar nuevos productos.

# In[31]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
order_ID_null = order_prod.loc[order_prod['add_to_cart_order'].isna(
), 'order_id']
order_ID_null.value_counts()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[32]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.
pedidos_con_valor_ausente = order_prod[order_prod['add_to_cart_order'].isna(
)].groupby('order_id')

print(pedidos_con_valor_ausente["product_id"].value_counts())
print()
print(pedidos_con_valor_ausente["product_id"].value_counts().min())


# Describe brevemente cuáles son tus hallazgos.
#
# No todos los pedidos con valores ausentes tienen más de 64 productos. El valor mínimo  es 1.

# In[33]:


# Remplaza los valores ausentes en la columna 'add_to_cart' con 999 y convierte la columna al tipo entero.
order_prod = order_prod.fillna(999)
order_prod.info(show_counts=True)


np.array_equal(order_prod['add_to_cart_order'],
               order_prod['add_to_cart_order'].astype('int'))
order_prod['add_to_cart_order'] = order_prod['add_to_cart_order'].astype('int')
order_prod.info()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
#
# Se llenaron los datos ausentes usando "999", y luego de verificar con np.array_equal(), los datos fueron transformados a enteros.

# ## Conclusiones
#
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos.
#
# Se procesaron los datos para tenerlos listos para los siguientes analisis. Se eliminaron las filas duplicadas, se aseguró el reemplazo o eliminación de los datos ausentes, de acuerdo a la naturaleza de los mismos.
#

# # Paso 3. Análisis de los datos
#
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
#
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[34]:


print(sorted(insta_ord["order_hour_of_day"].unique()))


# In[35]:


print(sorted(insta_ord["order_dow"].unique()))


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta muy bien. Podrias ordenerlo para que sea mas claro.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Excelente Al</div>

# Escribe aquí tus conclusiones.
#
# Los valores en las columnas 'order_hour_of_day' y 'order_dow' en la tabla insta_ord oscilan entre 0 y 23 y 0 y 6, respectivamente.

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[36]:


person_per_hour = insta_ord.groupby('order_hour_of_day')[
    'user_id'].count().sort_index()
person_per_hour.plot(figsize=[5, 5], kind='bar', title="Número de personas haciendo órdenes a cada hora del día",
                     xlabel="Hora del día", ylabel="Número de personas haciendo ordenes")
plt.show()


# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Para este tipo de visualizaciones lo mejor es utilizar un grafico de barras. Ya que la separacion hace que sea mucho mas visible las diferencias.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# Escribe aquí tus conclusiones
# En la madrugada es cuando vemos el menor número de pedidos, y conforme avanza la mañana aumenta hasta que encontramos el punto máximo a las 10:00 a.m. para mantenerse similar hasta las 4:00 p.m. donde hay un declive.

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[37]:


day_week = insta_ord.groupby('order_dow')[
    'user_id'].count().sort_index().reset_index()
day_week["order_dow"] = day_week["order_dow"].replace(
    {0: "Domingo", 1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado"})
day_week.plot(x="order_dow", y="user_id", kind='bar',  rot=45, legend=False, figsize=[
              5, 5], title="Número de personas haciendo órdenes cada día de la semana", xlabel="Día de la semana", ylabel="Número de personas haciendo ordenes")
plt.show()


# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Para este tipo de visualizaciones lo mejor es utilizar un grafico de barras. Ya que la separacion hace que sea mucho mas visible las diferencias.
#
# Me encanto la idea de los dias.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# Escribe aquí tus conclusiones
# Las personas compran los víveres usualmente los Domingos y Lunes, siendo el Jueves el día con menos compras.

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[38]:


waiting_time = insta_ord.groupby('days_since_prior_order')[
    'user_id'].count().sort_index().reset_index()
waiting_time.plot(x="days_since_prior_order", y="user_id", kind='bar',  rot=45, legend=False, figsize=[
                  10, 5], title="Tiempo de espera para hacer otro pedido", xlabel="Número de día", ylabel="Número de personas esperando para hacer otra orden")
plt.show()


# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Para este tipo de visualizaciones lo mejor es utilizar un grafico de barras. Ya que la separacion hace que sea mucho mas visible las diferencias.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Muy bien.</div>

# Escribe aquí tus conclusiones
#
# Hay tres picos inportantes que destacan: en el mínimo pareciera que una cantidad importante vuelve a pedir el mismo día, tal vez debido a que se les olvido un producto o si han llegado al máximo permitido por pedido. En el siguiente pico observamos lo que parecieran ser clientes recurrentes pidiendo una nueva orden luego de 7 días, para reabastecerse de los productos consumidos. Finalizando, el último punto nos indica que muchos clientes no vuelven a hacer un pedido o pueden tardar más de 30 días en usar la app. Una posible explicación es que estos clientes unicamente hicieron un pedido usando alguna clase de cupon o descuento (en su primer pedido, por ejemplo) y sin este apoyo, no consideran rentable hacer uso de la aplicación.

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
#
# ¿Porque crees la razon en que estan concentrados los mayores datos en que se piden cada 30 dias? ¿Y siete?. Responder este tipo de preguntas robustecen nuestro proyecto y le dan valor a nuestro rol de analista.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Muy bueno.</div>

# # [B] Intermedio (deben completarse todos para aprobar)
#
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[39]:


mi_sab_3 = insta_ord[(insta_ord["order_dow"] == 3)][[
    "order_hour_of_day"]].value_counts().sort_index()
mi_sab_6 = insta_ord[(insta_ord["order_dow"] == 6)][[
    "order_hour_of_day"]].value_counts().sort_index()


# In[40]:


mi_sab_concat = pd.concat([mi_sab_3, mi_sab_6], axis=1)
mi_sab_concat.columns = ['Miercoles', 'Sabado']
mi_sab_concat = mi_sab_concat.reset_index()
mi_sab_concat.head()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[41]:


mi_sab_concat.plot(x='order_hour_of_day',
                   kind='bar',
                   title='Diferencia entre miércoles y sábados',
                   xlabel='Hora',
                   ylabel='Número de órdenes')
plt.legend(['Miércoles', 'Sábado'])
plt.show()


# Escribe aquí tus conclusiones.
#
# Pareciera que hay diferencias significativas entre las 11:00 a.m. y 14:00 p.m. con una disminución de órdenes los miércoles a comparación de los sábados.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Excelente.</div>

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[57]:


num_per_user = insta_ord.groupby('user_id')['order_id'].count().sort_index()
display(num_per_user)


# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Cuidado, no estas calculando bien la frecuencia. Para esto debes agrupar el user id con el order id para contar cual es el total del pedido.
# </div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[43]:


num_per_user.plot(kind='hist', title="Distribución para el número de pedidos por cliente",
                  bins=30, figsize=[15, 6], ylabel="Cantidad de clientes")
plt.show()


# <div class="alert alert-block alert-danger">
#
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Para este tipo de visualizaciones lo mejor es utilizar un histograma. Ya que la distribucion es mucha y nos dara una mejor legibilidad.</div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# Escribe aquí tus conclusiones
#
# La gran mayoría de las personas no hacen más que unas pocos pedidos (Entre 1 y 5 pedidos). Pocos mantienen como hábito el seguir pidiendo. Este resultado parece estar relacionado con el de cuanto tiempo esperan los clientes en volver a pedir.

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[44]:


popular_product = order_prod[["product_id"]
                             ].value_counts().reset_index().iloc[0:20, :]
popular_product.columns = ['product_id', 'quantity']
display(popular_product.head(25))  # Se verifica el tamaño del dataframe


# In[45]:


produ_name = prod[["product_id", "product_name"]]


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[46]:


pop_prod_name = popular_product.merge(produ_name, on="product_id", how="left")
pop_prod_name.plot(x='product_name', y='quantity', kind='bar',
                   title="Los 20 productos más populares",
                   alpha=1, figsize=[15, 6], xlabel="Nombre del producto", ylabel="Cantidad del producto", rot=75)
plt.show()


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien. Recorda que en este caso le agregaria valor graficar ese top 20 con un grafico de barras. Tener a mano el grafico hara mas amena y legible la experiencia del cliente.</div>
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Excelente.</div>

# Escribe aquí tus conclusiones.
#
# En su mayoría los clientes piden productos orgánicos, sobretodo productos vegetales.

# # [C] Difícil (deben completarse todos para aprobar)
#
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[76]:


prod_per_order = order_prod.groupby("order_id")["product_id"].count()
prod_per_order_value_counts = prod_per_order.value_counts().sort_index().reset_index()
prod_per_order_value_counts.columns = ['num_objects_per_order', 'frequency']
prod_per_order_mean = prod_per_order_value_counts["num_objects_per_order"].mean(
)

display(prod_per_order)
display(prod_per_order_value_counts)
display(prod_per_order_mean)


# In[77]:


prod_per_order_value_counts.plot(kind='bar', x="num_objects_per_order", y="frequency",
                                 title="Distribución de productos por pedido", rot=45, legend=False,
                                 figsize=[21, 6], xlabel="Cantidad de productos", ylabel="Pedidos")
plt.show()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Cuando hablamos de cuantos articulos compran normalmente hacemos alusion a saber el promedio de articulos  que piden las personas. Para esto podemos agrupar  el id de la orden  (hacer un conteo) y el id del producto para luego si realizar el value counts() que realizas. Luego graficarlo en un barplot.</div>
#

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
#
# Hola Ezequiel, seguí tus comentarios. Hice modificaciones en el código aunque en particular en el inciso C1, no entendí tu explicación.
# Trate de seguirla aunque al tratar de graficar usando la grafica de barras se tardaba en mostrar el resultado, por lo que opte por un histograma.
#
# El razonamiento de mi anterior resultado era que de acuerdo al dataframe original, cada fila hace referencia a un articulo distinto, por lo que aunque agrupe usando tanto el ID de la orden como el ID del producto, obtendría el mismo resultado si solo me enfoco en cuantas veces se repite el ID de la orden en ese dataframe. Cada repetición sería un artículo distinto. En su momento obtuve que el promedio era: 10.098983215049127, como en este ultimo caso donde agrupe. Puse mi anterior código luego del "#".
#
# Entiendo que para que aquí se pueda formar una gráfica de barras, sería mejor usar una menor cantidad de datos. Por esto mismo entro en conflicto. ¿Me podrías explicar con otras palabras a qué te refieres con este inciso?
# </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Perdon si no fui claro Al, entiendo como lo planteaste y esta muy bueno.
#
# A lo que me refiero es que queremos saber la cantidad total de productos articulos por una persona, independientemente si son el mismo. (Por ejemplo : 2 arroz marca "p" son 2 articulos y no 1). Con el metodo unique estarias calculando uno solo. Para sanear eso podrias utilizar un count en la agrupacion del order id. Y para terminar contando todo podes ralizar un conteo de valores de toda la nueva agrupacion.
#
# A su vez estas usando un bins de 30 lo que no es la mejor opcion ya que te esta dividiendo el rango en algo muy amplio. Dejalo en predeterminado ya que en estos casos matplotlib entiende muy bien la escala o incluso podes ir probando. Ademas podrias graficarlo con un barplot, el histograma es otra opcion.
# </div>
#

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
#
# Hola Ezequiel, gracias por la explicacion, ahora me queda claro que era necesario un conteo y luego un conteo de valores para resumir la información deseada.
#
# </div>

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
#
# Corregido, te quedo muy bien.
#
# Te dejo dos consejos:
# 1- Cuando son tantos registros por ahi se pierde un poco los valores y la distribucion por lo que graficar el top 30 debajo de ese grafico puede ser una buena opcion.
#
# 2- Ordena los valores para que el analisis sea mucho mas rapido. Luego del 80 se te estan organizando por frecuencia y no por orden.
# </div>
#

# Escribe aquí tus conclusiones.
#
# El promedio de las órdenes tiene 47 productos. Sin embargo, este resultado está sesgado, debido a los valores atípicos, como el único pedido que tiene hasta 127 productos. En su mayoría, los clientes eligen entre 4-7 productos por pedido.

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[50]:


popular_product_freq = order_prod[(order_prod["reordered"] == 1)][[
    "product_id"]].value_counts().reset_index().iloc[0:20, :]
popular_product_freq.columns = ['product_id', 'quantity']

print(popular_product_freq.head(25))  # Se verifica el tamaño del dataframe


# In[51]:


produ_name = prod[["product_id", "product_name"]]


# In[52]:


pop_prod_freq_named = popular_product_freq.merge(
    produ_name, on="product_id", how="left")
pop_prod_freq_named.plot(x='product_name', y='quantity', kind='bar',
                         title="Los 20 productos más populares que se vuelven a pedir",
                         alpha=1, figsize=[15, 6], xlabel="Nombre del producto", ylabel="Cantidad del producto", rot=75)
plt.show()


# Escribe aquí tus conclusiones.
#
# En su mayoría los clientes piden de nuevo productos orgánicos. Los productos son similares a los 20 más populares aunque con ligeras diferencias en el ranking.

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien. Recorda que en este caso le agregaria valor graficar ese top 20 con un grafico de barras. Tener a mano el grafico hara mas amena y legible la experiencia del cliente.</div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Excelente.</div>

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[53]:


# Primero arreglamos los datos del dataframe donde tenemos el ID del producto y
# si se ha pedido de nuevo dicho producto o no, para contabilizar el total de pedidos de los productos
total_prod = order_prod[["product_id"]].value_counts().reset_index()
total_prod.columns = ['product_id', 'total_quantity']

# Segundo, arreglamos los datos del dataframe donde tenemos el ID del producto y lo filtramos con los productos
# que se han pedido anteriormente.
order_prod_again = order_prod[(order_prod["reordered"] == 1)][[
    "product_id"]].value_counts().reset_index()
order_prod_again.columns = ['product_id', 'quantity_reordered']


# In[54]:


# Tercero, unimos los datos de ambos dataframes usando el ID del producto como columna en común.
order_prod_proportion = total_prod.merge(
    order_prod_again, on="product_id", how="left")

# Cuarto, unimos los datos del anterior dataframe con los del dataframe que tiene el nombre de los productos
# de acuerdo a el ID de los mismos. Usaamos el ID del producto como columna en común.
# Todos los "NA" fueron reemplazados con cero.
produ_name = prod[["product_id", "product_name"]]
order_prod_proportion_names = order_prod_proportion.merge(
    produ_name, on="product_id", how="left").fillna(0)


# In[55]:


# Quinto, se  hizo una nueva columna para la tasa de repetición del pedido.
order_prod_proportion_names["proportion_of_reordered"] = order_prod_proportion_names["quantity_reordered"] / \
    order_prod_proportion_names["total_quantity"]
display(order_prod_proportion_names)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Cuidado. Tambien necesitamos sacar el nombre  del producto, de lo contrario seria muy poco practico tener que buscarlo por el id.
#
# Remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. Muy bien.</div>

# Escribe aquí tus conclusiones.
#
# Obtuvimos un dataframe con una columna que muestra la tasa del re-ordenado de cada producto. En el dataframe se muestran el id del producto, el nombre del producto y la tasa de repetición del pedido.

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[56]:


# Primero fusionaremos los dataframes de instacart_orders con el de order_products, usando order_id como columna en común.
user_order_prod_merger = order_prod.merge(insta_ord, on="order_id", how="left")
# Verificamos que la fusión sea correcta.
user_order_prod_merger.head()


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido.</div>

# In[57]:


# Luego, agrupamos los datos usando la columna user_id, usando el promedio de los valores de reordered.
groupby_data = user_order_prod_merger.groupby('user_id')['reordered'].mean()
# Observamos los resultados, obteniendo un objeto series con la tasa de repeticion de pedido para cada usuario,
# de acuerdo a su user_id.
groupby_data


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#
# Corregido. </div>

# Escribe aquí tus conclusiones
#
# Obtuvimos un objeto series que muestra muestra la tasa del re-ordenado los pedidos de los clientes.

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# In[58]:


# Primero fusionaremos los dataframes de order_products con el de produ_name (anteriormente creado), usando product_id como columna en común.
prod_merger = produ_name.merge(
    order_prod[order_prod["add_to_cart_order"] == 1], on="product_id", how="right")
print(prod_merger)
prod_merger.info()


# In[59]:


print(prod_merger["product_name"].value_counts().reset_index().head(20))


# Escribe aquí tus conclusiones
#
# El listado de los 20 principales artículos que la gente pone en su carrito es muy similar al de los productos populares. La mayoría son orgánicos. Podría ser que estos son los primeros productos que ven en la aplicación y por lo tanto, son los primeros que son guardados. O tambien podría ser que la aplicación es más popular en el estrato socioeconómico que puede adquirir y preocuparse de que sus alimentos son orgánicos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy bien. </div>

# ### Conclusion general del proyecto:

# La aplicación es usualmente usada durante el día y entre el domingo y el lunes.
# Las compras semanales se mantienen en una importante cantidad de clientes,
# aunque la gran mayoría de las personas no hacen más que unas pocos pedidos. Pocos mantienen como habito el seguir pidiendo.
# La gran mayoría de los pedidos tiene alrededor de 4-7 productos por pedido.
# La aplicación instacart tiene mayores ventas en los productos orgánicos. Los platanos resultaron el producto estrella lo cual tiene sentido, siendo la comida rápida biodegradable por excelencia.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Muy buena conclusion. </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario general #1</b> <a class="tocSkip"></a>
#
# Al, hiciste un muy buen trabajo. Este particularmente es bastante extenso y toca muchas aristas pero te has sabido manejar muy bien.
#
# Me gusto mucho tus analisis a traves del texto, en su mayoria muy acertados y bien redactados.
#
# Como te digo a nivel codigo estas muy bien, quizas en alguna parte te salteaste un paso pero en general muy bien. Los graficos estan bien planteados pero a veces hay unos que son mejor que otros, de igual manera muy bien.
#
#
# Te deje comentarios en cada seccion y si no fui claro podes dejarme cualquier duda que estoy a disposicion.
#
# Por ultimo muy buena conclusion, siempre es importante agregar valor. A veces se puede extender un poco mas que nunca es demasiado siempre que sea aclaratorio.
#
# Espero tu correccion, Saludos.</div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
#
# Hola Ezequiel, seguí tus comentarios. Hice modificaciones en el código aunque en particular en el inciso C1, no entendí tu explicación. En cuanto lo demás, muchísimas gracias por tus comentarios, estaré encantada de recibir tips y otros comentarios para mejorar.
#
# Espero tu respuesta, saludos.
# </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario general #2</b> <a class="tocSkip"></a>
#
# Al, tus correcciones fueron muy buenas. De hecho corregiste todo lo que te fui marcando y te quedo un proyecto completisimo.
#
# A su vez te deje en el c1 una explicacion mas robusta, espero que sea clara y de lo contrario estoy abierto a cualquier duda o aclaracion.
#
# Excelente correccion como te dije y con ese detalle el trabajo estara aprobado.
#
# Saludos.</div>

# Hola Ezequiel, seguí tus comentarios. Hice modificaciones en el código del inciso C1. De nuevo, muchísimas gracias por tus comentarios.
#
# Espero tu respuesta, saludos.

# <div class="alert alert-block alert-success">
# <b>Comentario general #3</b> <a class="tocSkip"></a>
#
# Al, corregiste muy bien lo que te marque por lo que el trabajo pasa a estar aprobado.
#
# Te deje dos consejos para ese tipo de graficos en el inciso c1.
#
# Exitos en lo que viene, saludos.</div>

# In[ ]:
