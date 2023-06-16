ResAt={
    "resultados":{
        "Introducción":{
            "Tesis": "En el ámbito literario, la concepción sobre el plagio ha cambiado a lo largo de la historia. Desde la antigüedad grecolatina se aconsejaba una forma de creación literaria que duró hasta el siglo XVIII: la imitación de los mejores autores para tratar de igualarlos o superarlos.\n Quinto Horacio Flaco (Horacio) sugería a los escritores que eligieran temas conocidos reelaborándolos para darles una apariencia original. Y Marco Fabio Quintiliano (Quintiliano) aconsejaba imitar la forma y contenido de las mejores obras.\n En las escuelas se ensañaba a los niños a imitar a los modelos. No obstante, los adultos debían cultivar una forma de imitación elaborada de las obras de forma que los autores aportaran algo original. Se daba por supuesto que los autores imitaban obras y se creía innecesario indicar las fuentes.\n También se creía lícito tomar algunos versos o fragmentos cortos de otro autor. Pero no un poema entero o un fragmento largo, pues esto se consideraba un hurto o robo. \n Por lo tanto, hasta el siglo XVIII había tres prácticas básicas relacionadas con la imitación y el plagio:\n Imitación elaborada de temas y estilos ajenos\n Inclusión de versos o fragmentos cortos ajenos sin citar la procedencia\n Copia literal de composiciones extensas ajenas sin indicar la procedencia\n Solo las dos primeras se consideraban lícitas\n El constante desarrollo y crecimiento de las tecnologías de información y comunicación aunadas a los métodos de enseñanza antiguos en conjunto con la cultura del mínimo esfuerzo han mermado la creatividad a la hora de la creación de contenido original, ya sea de índole académica o informativa.\n El plagio es un delito al derecho de autor que causa grandes consecuencias a la persona que lo lleva a cabo, el castigo varía dependiendo el ámbito y la cantidad en la que se realice el mismo, sin duda representa un problema grave en la sociedad que puede llevar a problemas legales con el autor como lo son; la anulación del trabajo en el cual se lleva a cabo dicho acto, multas o penalizaciones que en conjunto pueden desacreditar no sólo al individuo, sino también a su institución.\n En México el plagio es considerado en el Artículo 427 en el Código Penal Federal (DOF 01-06-2021) como un delito que debe ser sancionado, lamentablemente el organismo que supervisa y da seguimiento a estas malas prácticas (Instituto Nacional del Derecho de Autor) se ve superado por la cantidad de peticiones que debe atender, haciendo que el plagio electrónico sea de los más afectados pues los contenidos de terceros pueden ser accedidos por cualquiera.",
            "Similitud": "",
            "Nivel":"Sin equivalencia"
        },
        "objetivos":{
            "Tesis": "Objetivo general.\n Diseñar y desarrollar un sistema web capaz de extraer tesis del repositorio digital del Instituto Politécnico Nacional en la sección de nivel superior mediante web scraping y redes neuronales potenciadas con técnicas de deep learning para el análisis profundo del lenguaje natural en formato de texto plano o texto procesado como imagen a fin de interpretar de manera adecuada las citas de la Asociación Americana de Psicología versión 7 e Instituto de Ingenieros Eléctricos y Electrónicos, en tesis a registrar en la Unidad Profesional Interdisciplinaria de Ingeniería y Tecnologías Avanzadas.\n Objetivos específicos.\n Diseñar una interfaz intuitiva para el usuario.\n Implementar un sistema web que permita la carga de archivos.\n Extraer tesis registradas en el Repositorio Digital del Instituto para comparar con el documento propio, con ayuda de web scraping.\n Realizar un análisis profundo del texto recabado en idioma español.\n Diseñar un modelo para la integración de redes neuronales que permitan el análisis de texto en español interpretado como imagen.\n Crear un  modelo de redes neuronales que interprete correctamente las normas de referencia estipuladas según la Asociación Americana de Psicología versión 7 y el  Instituto de Ingenieros Eléctricos y Electrónicos.\n Entrenar un modelo de redes neuronales óptimo.\n Enlistar los resultados del análisis de plagio en un pdf.",
            "Similitud": "El objetivo de este trabajo es:\\n Crear un sistema de realidad aumentada móvil que integre visualización de contenidos educativos, interacción con redes sociales y consumo de servicios Web, que apoye al proceso de aprendizaje bajo la metodología de flipped learning, utilizando la plataforma de Android.\\n Para lograr esta meta se tienen que alcanzar los siguientes objetivos específicos:\\n  Diseñar y desarrollar un Editor Móvil para la creación, publicación y distribución de contenidos de realidad aumentada para apoyar en la fase de autoria de flipped leaming.\\n  Diseñar y desarrollar la aplicación que sirva como cliente para interactuar con el editor móvil y la fase de consumo de flipped leaming.",
            "Nivel":"0.90459085"
        },
        "Analisis":{
            "Tesis": "Análisis\n Análisis de requerimientos del sistema\nPara el desarrollo del software se implementará un diseño evolutivo en espiral que permita construir módulos de acuerdo a la funcionalidad obtenida de los requerimientos y cada una de ellas sufrirá modificaciones en cada ciclo.\n Lo anterior con la finalidad de poder lograr los alcances planteados aplicando factores de calidad de software.\n Descripción General\n Perspectiva del proyecto:\n El sistema se desarrolla en un entorno web y se basa en el uso de microservicios y modelos de redes neuronales capaces de detectar si el texto o imágenes contenidas en documentos con estructura de tesis poseen algún tipo de plagio utilizando ''repositorios de confianza''.\n El punto de comparación serán las estructuras sintácticas y léxicas similares o iguales a las contenidas en documentos proporcionados por el usuario.\n El sistema web generará resultados por cada documento cargado, el cual será enviado al correo registrado por el usuario con toda la información obtenida en el análisis de plagio; el contenido del reporte dependerá del grado y cantidad de malas prácticas de redacción, así como en el uso incorrecto de los formatos de citación IEEE y APA7.\n Catálogo de requerimientos\n A continuación se describe un catálogo de todos los requerimientos funcionales y no funcionales asociados a la construcción del sistema web.\n Tablas de requerimientos.\n En la presente sección se expondrán a detalle los requerimientos del sistema y se les asignará un ID a cada uno de estos, así como la prioridad pertinente para ser desarrollados.Se agruparán los requerimientos (funcionales y no funcionales) en 3 grupos, los cuales son:\n Backend\n Frontend\n Microservicios (API's)\n DBA (Arquitectura de la Base de Datos)\n Tablas de requerimientos para Backend.\n Requerimientos funcionales.\n Tablas de requerimientos para Frontend.\n Requerimientos funcionales\n Requerimientos no funcionales\n Tablas de requerimientos para Bases de Datos.\n Requerimientos funcionales\n Requerimientos no funcionales\n Diagramas de casos de uso.\n Para un correcto entendimiento de como el usuario final interactúa con el sistema y sus componentes a profundidad, se hará uso de diagramas de casos de uso, los cuales hacen una notación gráfica para representar el comportamiento del sistema en las diferentes situaciones que podrían llegar a presentarse durante la interacción.\n Características de los actores:\n Usuario Final: Persona quien requiere los servicios ofertados por el sistema, sube los archivos a analizar a la aplicación web y espera un informe detallado acerca del documento, para verificar que no incurrió en algún tipo de plagio o citas mal redactadas, lo anterior condicionado a que la redacción sea en formato APA 7 ó IEEE.\n Respositorios: Fuente bibliográfica en línea procedente de las universidades elegidas para el proyecto.\n Base de datos:  Los datos recopilados para el funcionamiento se almacenanarán para su posterior uso.\n Casos de uso para el diagrama del prototipo general\n Modelos para Procesamiento de Lenguaje Natural\n Lingüística de corpus\n Se define como una rama de la lingüística que basa sus investigaciones en datos obtenidos a partir de corpus. Ciertamente, no hablamos de una disciplina lingüística en sentido estricto, sino de un enfoque metodológico que puede ser adoptado desde diversas disciplinas. De hecho, debido a su interdisciplinariedad, está adquiriendo una notable presencia en los estudios de lingüística actuales.\n La lingüística de corpus basa su aplicación en lo siguiente:\n La lengua en uso como insumo (corpus conformados por muestras reales de lengua oral o escrita).\n El análisis sistemático de la lengua (análisis que se ajusta a un conjunto de reglas estrictas de recolección, almacenamiento y anotación).\n La posibilidad de trabajar desde un enfoque cualitativo o cuantitativo en una investigación (por ejemplo, desde las observaciones e intuiciones de los investigadores y desde resultados cuantificables, como listas de palabras).\n Las características de un corpus son cualidades que interactúan entre sí de manera complementaria para la investigación lingüística\n Un corpus es una muestra de lengua. Los corpus son porciones de lenguas o de variedades lingüísticas capaces de representar sus tendencias o características.\n Las muestras de un corpus son reales. Lo que un corpus busca es ser una fuente confiable, con datos que permitan el estudio de la lengua natural. Por esto, los textos que componen un corpus, ya sean orales, escritos o visuales, se deben producir en situaciones comunicativas naturales y con un propósito comunicativo auténtico.\n Los corpus relacionan la teoría y los datos.\n Si bien los corpus son conjuntos de textos sin conceptos, explicaciones o definiciones, sí se construyen con criterios específicos y teniendo claro de dónde se toman los textos y por qué se ha elegido esta procedencia.\n Facilitan la extracción de datos homogéneos y cuantificables. Gran parte de la cualidad cuantitativa de los corpus está dada por el componente lógico-matemático utilizado en los procedimientos para el análisis de la información. Los corpus son una muestra de la lengua real, e incluso el número de apariciones de fenómenos lingüísticos se constituye en información relevante que se puede generalizar para la lengua o la variedad. Alguna información distribucional o estadística que se puede extraer con los procedimientos lógico-matemáticos son las frecuencias de ocurrencias, referidas a la frecuencia de aparición de morfemas, palabras, expresiones o patrones gramaticales, entre otros, y de concurrencias, referidas a la frecuencia de aparición de estos elementos dentro de un contexto específico.\n Tokens\n En el procesamiento del lenguaje natural el proceso de convertir secuencias de caracteres, palabras o párrafos en input's para la computadora se llama tokenización. Se puede pensar al token como la unidad para procesamiento semántico\n Dado que los tokens son los componentes básico del lenguaje natural, la forma más común de procesar texto sin formato ocurre a nivel de token, así la tokenización de palabras es el algoritmo más utilizado, divide un texto en palabras individuales según un delimitador determinado. Por lo tanto es el paso más importante al modelar datos de texto; se realiza en el corpus, las fichas obtenidas se utilizan para preparar un vocabulario. El vocabulario hace referencia al conjunto de tokens únicos en el corpus, el vocabulario se puede construir considerando cada token único en el corpus o considerando las k palabras más frecuentes\n Types\n Los types son tokens únicos presentes en un corpus. El conjunto de todos los tipos en un corpus es su vocabulario o léxico. Las palabras se pueden distinguir como palabras de contenido y palabras vacías. Palabras vacías como artículos y las preposiciones sirven principalmente para un propósito gramatical, como relleno que contiene las palabras de contenido\n La distinción entre un tipo y sus tokens es una distinción ontológica entre un tipo general de cosa y sus instancias concretas particulares (para decirlo de una manera intuitiva y preliminar). Entonces, por ejemplo, considere la cantidad de palabras en la línea de Gertrude Stein de su poema Sacred Emily en la página frente a los ojos del lector:\n Rose is a rose is a rose is a rose\n En un sentido de 'palabra' podemos contar tres palabras diferentes; en otro sentido podemos contar diez palabras diferentes.Las palabras en el primer sentido serán “types” y a las palabras en el segundo sentido “tokens”\n Modelos de redes neuronales para procesamiento de lenguaje natural\n El análisis de similitud de textos es fundamental para una amplia gama de tareas en el área de Procesamiento de Lenguaje Natural (PLN).Encontrar la similitud entre pares de textos se ha convertido en un gran reto de estudio del área, pudiéndose aplicar en diferentes tareas de PLN\n Para este enfoque la topología en redes neuronales a emplear van enfocadas a la clasificación y reconocimiento de patrones dentro del texto, por ende se requiere un procesamiento dinámico.\n En el amplio espectro disponible las redes neuronales recurrentes aportan una solución para el manejo de texto.\n Redes neuronales recurrentes\n En el ámbito de las redes neuronales recurrentes la característica más destacable es que las neuronas tienen la capacidad de realizar conexiones de retroalimentación, ya sea en entre neuronas de una misma capa o de diferentes capas. La retroalimentación permite que este tipo de redes posea memoria\n Esto es, para procesar datos en los cuales hay una dependencia de los datos procesados anteriormente\n Un modo más intuitivo de ver el funcionamiento de las neuronas en este tipo de redes, es desarrollarlas a lo largo del tiempo. Como se observa en la figura 16, en cada time step anterior. Este funcionamiento permite a la red recordar información de secuencias anteriores al momento de procesar datos del actual\n De igual forma se pueden construir capas de neuronas recurrentes, con la siguiente arquitectura:\n En el caso de una capa, cada neurona recibirá el vector de entrada y el vector de salida correspondiente al valor devuelto por todas las neuronas de la capa en el time step anterior.\n Topologías de redes neuronales recurrentes\n Red Hopfield\n La red Hopfield tiene una única capa de unidades procesadoras. Cada una de las unidades procesadoras tiene un valor o nivel de activación, también llamado estado, el cual es binario.\n Se considera que esta red tiene un estado en cada momento; este estado se define por el vector de unos y ceros construido por los estados de todas las unidades procesadoras. El estado de una red con n unidades, donde el elemento i tiene el estado se representa con la siguiente ecuación:\n En esta notación el signo + representa una unidad procesadora con el estado o valor 1 y el signo - representa una unidad procesadora con el estado o valor binario 0.\n Las unidades procesadoras de la red Hopfield están completamente interconectadas, cada unidad está conectada con todas las demás unidades. Esta topología convierte a la red Hopfield en una red recursiva ya que la salida de cada unidad está realimentada con las entradas de las demás unidades.\n Una característica de las redes Hopfield es la doble conexión por cada pareja de unidades procesadoras, como se aprecia en la figura anterior. Además los pesos asignados a ambas conexiones tienen el mismo valor\n Redes LSTM\n Las redes LSTM (Long Short-Term Memory) tienen un esquema similar a las redes recurrentes salvo que la capa oculta está formada por bloques de memoria que son la esencia de la precisión de este algoritmo\n Hay varias puertas en el proceso de LSTM. Cuando el estado celular lleva la información, estas puertas ayudan a que la nueva información fluya. Las puertas indicarán qué datos son útiles para guardar y qué datos no son útiles, lo que hace que esté bien para tirar. Así que sólo los datos relevantes pasan a través de la cadena de secuencia para una fácil predicción.\n Estas son las partes esenciales que componen a una red LSTM:\n Sigmoidea: Las puertas contienen varias activaciones llamadas sigmoides, que contienen algunos valores. Estos valores van de ceros a uno. Estos valores ayudan a olvidar y mantener la información. Si los datos se multiplican por uno, el valor de esos datos sigue siendo el mismo.\n Compuerta del olvido: La primera puerta que entenderemos es la puerta del olvido. La función de esta puerta es decidir mantener u olvidar la información. Sólo la información que proviene de capas previamente ocultas y la entrada actual se mantiene con la función sigmoide. Cualquier valor que esté más cerca de uno permanecerá, y cualquier valor más cercano a cero desaparecerá.\n  Compuerta de entrada: La puerta de entrada ayuda a actualizar el estado de las células. La información de la entrada actual y del estado previo pasa por la función sigmoide, que actualizará el valor multiplicándolo por cero y por uno. Del mismo modo, para regular la red, los datos también pasan por la función tanh. Ahora, la salida del sigmoide se multiplica por la salida de tanh. La salida del sigmoide identificará información valiosa para evitar la salida de tanh.\n Estado de la célula: Ahora, la información que posee nos ayudará a calcular el estado de las células. El valor del estado de la célula puede caer si el valor multiplicado está cerca de cero después de multiplicar el vector de olvido y el estado de la célula anterior. Ahora, podemos encontrar el nuevo estado de la célula sumando la salida de la puerta de entrada en sentido puntual.\n Compuerta de salida: El siguiente estado oculto se define en la puerta de salida. Para encontrar la información del estado oculto, necesitamos multiplicar la salida sigmoide por la salida tanh. Se puede predecir la siguiente información de un estado oculto. Ahora, el nuevo estado oculto y el nuevo estado celular viajarán al siguiente paso\n Redes GRU\n Propuesto en 2014, GRU (Unidades Recurrentes Cerradas) es una variante más eficiente de LSTM que comparte muchas propiedades similares. Con un rendimiento comparable al de LSTM en el modelado de secuencias, GRU tiene menos parámetros y es más fácil de entrenar. GRU puede extraer características y aprender representaciones sin un conocimiento experto o de dominio, pero puede que no sea robusto debido a la existencia de ruido en los datos sensoriales sin procesar\n En GRU, se introducen dos puertas que incluyen una puerta de reinicio que ajusta la incorporación de nueva entrada con la memoria anterior y una puerta de actualización que controla la preservación de la preciada memoria. La puerta de reinicio y la puerta de actualización controlan de forma adaptativa cuánto recuerda u olvida cada unidad oculta mientras lee/genera una secuencia\n Las GRU capturan dependencias en diferentes tiempos. Tienen puertas lógicas que manejan el flujo de información dentro de cada unidad. Se tiene que una activación htj en la GRU en el tiempo t es una interpolación linear entre la activación previa hr-1j y la posible activación htj\n Transformer Neural Network\n Transformer Neural Network es una arquitectura novedosa que tiene como objetivo resolver tareas de secuencia a secuencia mientras maneja dependencias de largo alcance con facilidad. Fue propuesto en el artículo “La atención es todo lo que necesitas” 2017.Es la técnica de vanguardia actual en el campo del procesamiento de lenguaje natural\n Transformer, es un modelo que tenía como principal innovación la sustitución de las capas recurrentes, como las LSTMs que se venían usando hasta ese momento en procesamiento de lenguaje natural, por las denominadas capas de atención.\n Estas capas de atención codifican cada palabra de una frase en función del resto de la secuencia, permitiendo así introducir el contexto en la representación matemática del texto, motivo por el cual a los modelos basados en Transformer se les denomina también Embeddings Contextuales\n El transformador sigue esta arquitectura general utilizando capas apiladas de auto atención y punto a punto, completamente conectadas tanto para el codificador como para el decodificador, que se muestran en las mitades izquierda y derecha de la figura 21 respectivamente\n La innovación de esta arquitectura se reduce a 3 conceptos esenciales:\n Codificaciones posicionales: La idea es tomar todas las palabras de la secuencia de entrada  y añadir a cada palabra un número en su orden. Así, usted alimenta a su red con una secuencia como: [(«Dale», 1), («dice», 2), («hola», 3), («mundo», 4)]. Conceptualmente, se puede pensar que esto es trasladar la carga de entender el orden de las palabras de la estructura de la red neuronal a los propios datos. Al principio, antes de que el Transformer haya sido entrenado con datos, no sabe cómo interpretar estas codificaciones posicionales. Pero a medida que el modelo ve más y más ejemplos de frases y sus codificaciones, aprende a utilizarlas con eficacia.\n Atención: Es una estructura de red neuronal que se introdujo en el contexto de la traducción y actúa como un mecanismo que permite a un modelo de texto «mirar» cada una de las palabras de la frase original al tomar una decisión sobre cómo traducir las palabras de la frase de salida.\n Autoatención:ayuda a las redes neuronales a desambiguar las palabras, hacer el etiquetado de partes del discurso, la resolución de entidades, aprender los roles semánticos. Un modelo entrenado con datos de texto puede aprender automáticamente las partes del discurso, las reglas gramaticales y si las palabras son sinónimas.Cuanto mejor sea la representación interna del lenguaje que aprende una red neuronal, mejor será en cualquier tarea lingüística. Y resulta que la atención puede ser una forma muy eficaz de hacer precisamente esto, si se dirige al propio texto de entrada\n Modelos de redes neuronales para procesamiento de imágenes\n Las técnicas para analizar una imagen digital se agrupan en un área llamada Procesamiento Digital de Imágenes. Estas herramientas se organizan según el nivel de procesamiento que se desea realizar para analizar la información contenida en una imagen digital. A continuación se describen brevemente:\n Pre-procesamiento: Operaciones para adaptar la información de una imagen y tener mejor análisis en pasos posteriores. Ejemplos de procesamiento son las operaciones de brillo y contraste\n Segmentación:  Operaciones para hacer una partición de la imagen en varias regiones que representen la información necesaria para el problema a resolver.\n Detección de objetos y clasificación: Determinación y clasificación de los objetos contenidos en la imagen.\n Análisis de la imagen: Obtener información de alto nivel acerca de lo que la imagen muestra\n Topologías de redes neuronales para imágenes\n Red neuronal pulso-acoplada\n Las Redes Neuronales Pulso-Acopladas son un sistema que emula efectivamente a las neuronas biológicas de la corteza visual de los mamíferos y han sido aplicadas en variedad de dominios, especialmente en el procesamiento de imágenes han sido útiles para remoción de ruido, reconocimiento de objetos, optimización, adelgazamiento, segmentación, fusión, identificación y remoción de sombras\n Los primeros experimentos demostraron que PCNN (Pulse-Coupled Neural Network ) podía procesar imágenes de modo que el resultado fuera invariante para las imágenes que se desplazaron, rotaron, escalaron y sesgaron. Una neurona PCNN contiene dos elementos principales: alimentación (Feeding) y enlace (Linking), cada uno de éstos se comunican con las neuronas vecinas a través de los pesos sinápticos M y W Estos dos comportamientos están determinados por las siguientes ecuaciones:\n donde Fij es el comportamiento de alimentación de la neurona en la posición (ij) incrustado en una matriz bidimensional de neuronas, y Lij es el comportamiento del enlace correspondiente. Los Ykl son las salidas de neuronas de una iteración previa [n-1]. Las constantes VF y VL son constantes de normalización.. M y W son matrices de pesos.\n Red neuronal probabilística\n Una red neuronal probabilista es la implementación de un algoritmo estadístico denominado análisis de discriminante en el cual las operaciones son organizadas en una red con cuatro capas las cuales son capaz de estimar límites o superficies de decisión no lineales mediante un enfoque óptimo Bayesiano. Cuando a la red se le presenta un vector y=yq ... yd a ser clasificado,la segunda capa se ocupa de calcular la distancias desde el vector  de entrada hasta cada uno de los vectores o patrones ejemplo a través de la función la cual funciona de acuerdo al kernel normal estándar utilizado como la función de densidad de probabilidad como se muestra en la siguiente ecuación:\n La capa de entrada contendrá los valores de los atributos que se presentan a la red en cada entrada, la capa de patrones calculará la distancia entre el vector de entrada y la salida esperada produciendo un vector cuyos elementos mostrarán la cercanía entre la entrada y la salida, la capa de sumatoria sumará las contribuciones para cada clase de entradas con el fin de producir un vector de salida que contendrá las probabilidades y finalmente la capa de salida contendrá una cantidad de neuronas igual a la cantidad de clases que se desea clasificar\n Red neuronal convolucional\n Las redes neuronales convolucionales es un algoritmo de Deep Learning que está diseñado para trabajar con imágenes, tomando estas como input, asignándole importancias (pesos) a ciertos elementos en la imagen para así poder diferenciar unos de otros. Este es uno de los principales algoritmos que ha contribuido en el desarrollo y perfeccionamiento del campo de Visión por computadora\n Las CNN (Convolutional Neural Network) combinan las características de bajo nivel dentro de caracteríısticas abstractas de alto nivel con transformaciones no lineales, lo que le permite tener la capacidad de aprender la representación semántica de las imágenes. Estas redes extraen características generalmente útiles de los datos con o sin etiquetas, detectan y eliminan redundancias de entrada y preservan solo aspectos esenciales de los datos en representaciones sólidas y discriminativas; pueden capturar las características mas obvias de los datos, por lo que podrían lograr mejores resultados\n Los tipos de capas que conforman una red neuronal convolucional son tres, capa convolucional, capa pooling y capa fully-connected.\n Capa convolucional: Esta capa aplica filtros convolucionales a la imagen con el objetivo de encontrar qué característica del modelo aplica con más fuerza. Las neuronas en la primera capa convolucional no están conectadas a cada pixel de la imagen de entrada, sino a cada pixel de su campo receptivo. A su vez, cada neurona de la segunda capa convolucional se encuentra conectada sólo con un rectángulo de la capa superior. Esto le permite a la red concentrarse en conceptos más pequeños para luego ensamblarlos en conceptos más grandes para la siguiente capa convolucional y así hasta la última. \n Capa pooling: Esta capa se encarga de reducir las dimensiones del resultado obtenido de la capa convolucional (downsampling) para reducir el tiempo de procesamiento, es decir, una compresión de los datos. Al igual que antes, las neuronas de esta capa se conectan con un número limitado de neuronas de la capa previa que a su vez tienen un campo receptivo reducido. El algoritmo más utilizado es max-pooling; Toma regiones de 2x2 pixeles y las reduce tomando el máximo valor de cada una.\n Capa fully-connected: Esta capa se denomina densa ya que todos los nodos están conectados entre sí y su objetivo es realizar la clasificación de la imagen en base a los resultados de las capas anteriores\n Interfaz de usuario.\n Según la Real Academia de la Lengua Española (RAE), la palabra interfaz proviene del ingles interface que significa ''superficie de contacto''; en campo informático hace referencia a la conexión física o lógica entre una computadora y el usuario\n La Interacción Humano-Computador (IHC) es una nueva disciplina que concierne con el componente interactivo entre las aplicaciones computacionales y los usuarios, así como las consideraciones del contexto de esta interacción. Es un área multidisciplinaria donde confluyen especialistas del dominio de la aplicación que se construye, especialistas en interfaces de usuario, psicólogos cognitivos, diseñadores gráficos, educadores y el usuario, entre otros.\n La IHC es un área en permanente evolución dados los cambios tecnológicos que se suceden continuamente. Las expectativas de desarrollo en los próximos años son tales que los grandes avances que se darán en la computación se centrarán en resolver los problemas de la interacción entre el humano y el computador.\n La interfaz de usuario es la parte accesible de un sistema computacional, tanto hardware como software, que permite al usuario interactuar con el sistema. El diseño de una buena interfaz se ha vuelto parte integral y relevante para las aplicaciones interactivas.\n Un sistema de software puede no tener aceptación si su interfaz es pobre (independientemente de que el software sea confiable y eficiente). El costo de desarrollo de una interfaz representa, en muchas aplicaciones, un porcentaje alto del costo de desarrollo de la aplicación\n UI y UX.\n Hoy en día cuando se desea realizar un sistema web es muy importante tomar en cuenta los aspectos de Interfaz de Usuario y Experiencia del Usuario, ya que juegan un factor determinante en la aceptación de la pagina por parte del usuario; a continuación se detallara más afondo en que consisten cada uno de estos factores.\n Interfaz de usuarios (UI).\n La idea del UI es guiar al usuario por la aplicación durante el tiempo que la usa; por lo cual un buen trabajo de diseño de UI te permitirá guiar a los usuarios por la navegación y los llevará a tomar dichas acciones de manera natural\n Experiencia del usuario (UX).\n La experiencia de usuario es aquel proceso que se desarrolla cuando el usuario navega en una interfaz digital; esto se logra mediante el diseño centrado en el humano, el cual se enfoca en conocer las necesidades de los usuarios y alinearlos a los objetivos del negocio tomando también en cuenta las limitaciones técnicas \n Las siguientes son tareas típicas de un UX diseñador:\n Conociendo a sus clientes:\n El diseño de UX tiene como objetivo comprender al público objetivo, sus deseos y necesidades, por lo que generalmente comienza con una investigación exhaustiva. La empatía es una habilidad importante que deben tener los diseñadores de UX. Ayuda a los diseñadores de UX a comprender y descubrir las necesidades y emociones ocultas de las personas que están diseñando.\n Proponer una estrategia de diseño:\n Comprender el propósito de un producto y trazar un recorrido lógico es parte de la estrategia de diseño.\n Examinando el diseño de interacción:\n Los diseñadores de UX estudian cómo las personas interactúan con los productos, incluidos sus hábitos de interacción, preferencias personales y atajos de interfaz de usuario. Toda la información se aprovecha para encontrar mejores soluciones de diseño.\n Creación de prototipos y wireframes:\n Para presentar sus ideas al equipo de diseño, los diseñadores de UX suelen utilizar software de UX para crear prototipos o wireframes. Los diseñadores de UX están involucrados en la ejecución de un producto en todo momento: se comunican con todos los miembros del equipo para asegurarse de que el diseño del producto va por buen camino\n Diferencias entre UI/UX\n El término interfaz de usuario, UI significa interfaz de usuario, se utiliza para referirse a los diseños de pantalla y el diseño visual de las aplicaciones de software utilizadas para proporcionar información o control de acceso. a los usuarios El término experiencia de usuario UX se utiliza para referirse a la experiencia general del usuario de un producto o servicio de software y la expectativa del usuario que debe cumplir el producto. Aquí hay algunos otros términos para recordar y entender:\n Interfaz: Una herramienta se llama interfaz cuando no realiza ningún trabajo por sí misma. Solo ayuda al usuario a realizar tareas. La interfaz puede ser una línea de comandos o una interfaz gráfica de usuario (GUI) Interfaz gráfica de usuario (GUI)\n Experiencia de usuario: Una interfaz gráfica de usuario (GUI) es una interfaz informática que permite al usuario controlar un programa informático mediante la manipulación de objetos gráficos en la pantalla de la computadora, como ventanas, iconos y menús desplegables.\n Diseño de la experiencia: \n En el contexto del diseño de la experiencia del usuario, la experiencia del usuario es una experiencia subjetiva que las personas tienen cuando usan tecnología e incluye todos los elementos de interacción, como información, dispositivo y contexto. El diseño de la experiencia del usuario se trata de diseñar tecnología que ayudará a las personas a crear una buena experiencia.\n Diseño de interfaz: En el contexto del diseño de interfaz de usuario, el diseño de interfaz de usuario es una forma de ayudar a las personas a usar un producto o aplicación de software. El diseño de la interfaz de usuario también incluye la forma en que un sistema informático responde a las entradas del usuario",
            "Similitud": "",
            "Nivel":"Sin equivalencia"
        },
        "diseño":{
            "Tesis": "Bosquejo de la BD\n Hasta este punto no se ha hablado acerca del diseño final que tendrá la base de datos dentro del sistema, puesto que no se ha determinado el tipo de tecnología que se empleará; pero es importante comenzar a identificar los campos de información a destacar dentro de cada entidad con la que interactúa el sistema, a continuación se presenta un primer diseño de la base de datos.\n Diagrama de secuencia del sistema\n Se usan principalmente para modelar principalmente las interacciones entre actores y objetos en un sistema. Ilustran la forma en que las diferentes partes de un  sistema interactúan entre sí para llevar a cabo una función y el orden en que se producen las interacciones cuando se ejecutan en cada caso.\n Diagrama de secuencia de las redes neuronales\n Diagrama de secuencia para la red de procesamiento del lenguaje natural\n Diagrama de secuencia para la red de procesamiento de imágenes\n Planeación del entrenamiento en redes neuronales\n Supervisados\n Se caracteriza porque el proceso de aprendizaje se realiza mediante un entrenamiento controlado por un agente externo (supervisor, maestro) que determina la respuesta que debería generar la red a partir de una entrada determinada\n Clasificación: La clasificación es una subcategoría del aprendizaje supervisado en la que el objetivo es predecir las etiquetas de clase categóricas (discreta, valores no ordenados, pertenencia a grupo) de las nuevas instancias, basándonos en observaciones pasadas. Hay dos tipos principales de clasificaciones:\n Clasificación binaria:  Es un tipo de clasificación en el que tan solo se pueden asignar dos clases diferentes (0 o 1). El ejemplo típico es la detección de email spam, en la que cada email es: spam → en cuyo caso será etiquetado con un 1 ; o no lo es → etiquetado con un 0.\n Clasificación multiclase: Se pueden asignar múltiples categorías a las observaciones. Como el reconocimiento de caracteres de escritura manual de números (en el que las clases van de 0 a 9)\n Regresión: El objetivo es establecer un método para la relación entre un cierto número de características y una variable objetivo continua.En este sentido, el ejemplo más común es la regresión lineal.Se trata de un algoritmo que establece una recta para proporcionar la tendencia de un conjunto de datos\n  Es una técnica paramétrica de machine learning. Con «paramétrica» se quiere dar a entender que incluso antes de mirar a los datos, ya se sabe cuántos parámetros (o coeficientes) se van necesitar. En el caso que se empleé usando una sola variable, x, en álgebra una línea necesita 2 parámetros. La fórmula para la regresión lineal con una sola variable x es: y=wx+b .El aprendizaje consiste en encontrar cuáles son los mejores parámetros (coeficientes) para los datos que se tienen. Los mejores coeficientes serán los que minimicen alguna medida de error.\n No supervisados\n En el ámbito de aprendizaje no supervisado, se suministra a la red los datos de entrada para que extraiga los rasgos característicos esenciales. En terminología estadística equivale a los modelos en los que solo hay vectores de variables independientes y buscan el agrupamiento de los patrones de entras: análisis de conglomerados o cluster, escalas multidimensionales, etc.  Estas redes deben encontrar las características, regularidades, correlaciones o categorías que se pueden establecer entre los datos de entrada. Puesto que no hay un supervisor que indique a la red la respuesta que debe generar una entrada concreta, cabría preguntarse precisamente porque la red genera en estos casos\n Clustering: Consiste en agrupar una serie de vectores seg´un un criterio en grupos o clusters. Generalmente el criterio suele ser la similitud por lo que diremos que agrupa los vectores similares en grupos Según la forma en que los clusters se relacionan entre sí y con los objetos del dataset, podemos establecer una primera división entre los diversos algoritmos existentes:\n Clustering Duro: donde cada objeto pertenece a un solo cluster (por lo que los clusters pasarían a ser algo así como una partición del dataset).\n Clustering Blando (o difuso): donde los objetos pertenecen a los clusters según un grado de confianza (o grado de pertenencia).\n Reducción de dimensiones: La reducción de dimensiones es un algoritmo usada como una etapa de pre proceso para condensar la información de un conjunto de variables y escoger un subconjunto de variables, de tal manera, que el espacio de características quede óptimamente reducido de acuerdo a un criterio de evaluación, cuyo fin es distinguir el subconjunto que representa mejor el espacio inicial de entrenamiento. Cada característica que se incluye en el análisis, puede llegar a incrementar el costo y el tiempo de proceso de los sistemas, por lo que hay una fuerte motivación para diseñar e implementar sistemas con pequeños conjuntos de características.\n Aprendizaje auto-supervisado\n Solo requiere datos sin etiquetar para formular las tareas pretexto. La idea principal es realizar una tarea pretexto como predecir la rotación de un conjunto de imágenes y gracias a esta tarea calcular el objetivo sin supervisión, aprenden de los conjuntos de datos.\n Rotación: La tarea funciona de tal forma que mediante el conjunto de datos se generan 4 copias con las imágenes giradas en {0, 90, 180, 270} grados. La red tiene que predecir la rotación de las imágenes aplicada donde un buen modelo debería aprender estas rotaciones en imágenes naturales\n Rompecabezas: Consiste en recuperar la posición espacial relativa de 9 parches de la imagen muestreados aleatoriamente después de una permutación al azar de estos parches. Los parches son enviados a través de la propia red neuronal, luego las representaciones se concatenan y pasan a través de un perceptrón multicapa que está totalmente conectado a las capas ocultas, donde predice la permutación utilizada. Posteriormente, se extraen las representaciones promediando las representaciones de 9 muestras normalizadas de los parches de la imagen\n Aprendizaje reforzado\n El aprendizaje por refuerzo (RL, reinforcement learning) proporciona un conjunto de técnicas para resolver problemas de decisión secuenciales. Durante el transcurso del tiempo el estado del sistema puede evolucionar, es decir, el valor de s puede sufrir cambios. Ahora supongamos que dichos cambios están influenciados en parte por acciones que se pueden realizar sobre el sistema y que el objetivo es alcanzar un determinado estado. Cuando se tiene que decidir qué acción aplicar en un único instante temporal, se dice que el problema de decisión es monoetapa, si se requiere una secuencia de decisiones entonces se trata de un problema de decisión multietapa o secuencial\n los diferentes componentes que participan en un sistema de aprendizaje por refuerzo:\n Agente: Es el modelo que se quiere entrenar. Aprende a tomar decisiones.\n Ambiente/Entorno: Entorno en donde interactúa el agente.\n Estado: Indicador o indicadores del estado de entorno.\n Recompensa:\n Positiva: Si la acción realizada tiene alguna bonificación \n Negativa: Si la acción realizada obtiene alguna penalización.\n Acción: Posibles acciones que puede realizar un agente\n El proceso de aprendizaje sigue una serie de pasos:\n El agente recibe un estado $s$, y una recompensa r\n El agente escoge una acción a del conjunto de acciones disponibles y la envía al entorno.\n El entorno ejecuta la acción $a$ y su estado pasa, entonces a s+1\n El interprete recibe, entonces una observación o+1, interpreta el nuevo estado $s+1$ y calcula la recompensa rt+1 correspondiente a la transición (s;a;s+1)\n Plan de entrenamiento para texto\n Para entrenar a esta red, se necesita un\n banco de datos o también conocido como dataset Para el caso de texto el tipo de entrenamiento consistirá en un entrenamiento híbrido (supervisado-no supervisado), esto dado a que los datos a procesar por la red neuronal es texto plano, por ende se debe poseer un contexto sobre lo que está escrito. En un primer plano se busca que la red entienda el texto escrito, para posteriormente hacer diferentes procesamientos, los cuales son:\n Identificar en que punto del texto plano se encuentra una cita.\n Tipo de cita localizada (APA 7 o IEEE)\n Identificar una redacción adecuada bajo las normas APA 7 e IEEE\n Extraer la idea general del texto.\n Hacer comparaciones en texto plano extraído de los repositorios de confianza para localizar parafraseo o plagio.\n En un inicio se alimentará a la red con un dataset de textos con formato tipo tesis para que comprenda la estructura de los trabajos escritos, este se definirá como en entrenamiento fase I, cuando la red sea capaz de identificar las estructuras la siguiente fase consistirá en el procesamiento por párrafos donde se busca que en cada párrafo se localice de normas de citación APA 7 e IEEE, aquí en entrenamiento tomará dos caminos, uno consistirá que las citas estén redactadas acorde a las normas previamente dichas, para esto se necesita un dataset donde se observen las normas propuestas y sus diferentes vertientes; el otro camino consiste en identificar las citas redactas de manera incorrecta, recibiendo este conjunto de dos caminos el nombre de fase II. La fase III consistirá en observar las ideas generales del trabajo, después las ideas generales por capítulo y sus subtemas para después obtener de manera granular el contexto de cada párrafo del trabajo a procesar, esto para identificar el plagio en los trabajos escritos.\n Plan de entrenamiento para imágenes\n El dataset de está red neuronal será llevada a cabo con un entrenamiento híbrido (supervisado-no supervisado). En un principio de un pequeño conjunto de imágenes extraídas del datset donde se encuentran los documentos con formato tipo tesis, se procesarán en la red, en una primera fase se plantea procesar pares de imágenes totalmente iguales para que se identifiqué una similitud del 100% después se buscará hacer pequeñas modificaciones en las imágenes y se empiece a detectar si existe similitudes, esta será la parte de entrenamiento supervisado.  Para un entrenamiento no supervisado solo se enviará una imagen y dentro de un documento con varias imágenes extraídas de un documento tipo tesis analizará si existe similitud en alguna de estas o no, de existir similitud pero ninguna cita reportada al pie de página se está incurriendo en plagio y se notificará en el reporte final, de tener cita, está se enviará al apartado de procesamiento de texto para reportar si está hecha correctamente o no.\n Branding\n Desde una perspectiva reduccionista, ha sido definido como la acción de colocarle un nombre al producto naming, diseñar un logosímbolo llamativo y exponer de manera permanente a consumidor a la marca a través de los medios de comunicación. También ha sido definido como la acción de crear y desarrollar una marca. Hoy en día, la definición de branding va más allá de marcar incesantemente al consumidor. De una manera más integral, se puede definir como el ejercicio orientado a capturar la esencia de una oferta (producto), trabajar a fondo una personalidad atractiva, diferente, llena de significados para el cliente potencial, y conectarla a un nivel emocional con la marca en cuestión, dotándola de cierta presencia en el mercado.\n Nombre comercial para el sistema\n La filosofía detrás del nombre para que los usuarios conozcan el sistema proviene de la mitología griega, tomando como inspiración el nombre de la diosa Palas Atenea, la razón fue la historia detrás de ella.\n Athena era la diosa de la sabiduría y la guerra, hija predilecta de Zeus. Era la más ingeniosa de los dioses del Olimpo, la más sabia y la más valiente\n Además de lo anteriormente mencionado, Athena era la diosa de las matemáticas, la fuerza, la estrategia, la habilidad artística, el coraje, la valentía, la inspiración, la ley y la justicia. Debido a la admiración que los griegos y los romanos tenían por esta diosa, con el paso de los siglos le fueron adicionando responsabilidades, por dicha razón esta diosa preside sobre tantas cosas\n Dado a que la mítica historia de este diosa coincide con los objetivos a la filosofía detrás del proyecto, a partir de este momento será conocido como Athena Sistema Antiplagio, siendo su nombre oficial para que sea conocido por la comunidad de la Unidad Profesional Interdisciplinaria en Ingeniería y Tecnologías Avanzadas, dicho nombre también será aplicado para el dominio de la página web donde se dará acceso a los servicios que se ofrecerán.\n Misión\n El equipo de desarrolladores de Athena Sistema Antiplagio forman parte de la Unidad Profesional Interdisciplinaria en Ingeniería y Tecnologías Interdisciplinaria en Ingeniería y Tecnologías Avanzadas, los cuales, comprometidos con la comunidad estudiantil ofrecen una herramienta para verificar la autenticidad de los trabajos desarrollados para obtener el grado de licenciatura, a través de la modalidad curricular para perseverar el ejercicio del método científico a través de la tecnología.\n Visón\n Ser un sistema que aporte a la comunidad de la Unidad Profesional facilidades para la revisión y verificación de la autoría en trabajos para obtener el grado de licenciatura, de tal manera que al pasar por dicha revisión se garantice que no existe un artículo similar en el repositorio digital del Instituto Politécnico Nacional.\n Logo comercial para el sistema\n De manera habitual se le llama logo al elemento gráfico que identifica a una empresa, un proyecto, una institución, un producto, habría que distinguir tres tipos diferentes de logos:\n Logotipo: la palabra de la marca funciona como imagen. Es bueno cuando la palabra es muy potente (ejemplo: coca cola).\n Isotipo: diseño donde la imagen funciona sin texto (ejemplo: la manzana de Apple).\n Isologo: interacción del logotipo y del isotipo (ejemplo: Nike). Este último es el más completo y el más funcional porque permite usos distintos en diferentes espacios, siempre que esté bien gestionado para permitir que tu target sea capaz de relacionar ambas cosas ( como cuando la marca Lacoste, usa solo el cocodrílo por ejemplo)\n El equipo de desarrolladores opto por un diseño tipo isologo para el logotipo del proyecto, dicho diseño fue el siguiente:\n Paleta de colores\n En diseño gráfico, una paleta de colores es el conjunto de tonalidades elegidas para ser usados en una ilustración, pieza gráfica  o página web.\n Una paleta de colores tiende a guardar un cierto grado de armonía y relación entre sí para generar una identidad propia de tu marca, perfil personal, etc\n Para el diseño web del sistema Athena Sistema Antiplagio se eligió la siguiente paleta de colores: \n Mockup's\n El diseño web del sistema Athena Sistema Antiplagio requiere de una noción para las vistas que se proporcionan  al usuario, en un primer acercamiento se presentan los bosquejos que tendrá en su diseño final.",
            "Similitud": "",
            "Nivel":"Sin equivalencia"
        },
        "marcoteorico":{
            "Tesis": "A continuación, se presenta una breve investigación y los términos de ingeniería que resultan importantes, ya que contienen detalles de las tecnologías a utilizar para el correcto desarrollo de los sub-módulos del sistema principal y por ende el proyecto en si.\n Lenguaje.\n Desde hace millones de años se han ido creando lenguajes y evolucionando a lo largo del tiempo como herramienta para transmitir conocimientos, deseos y necesidades\n Según La Real Academia española el lenguaje se define como la facultad del ser humano de expresarse y comunicarse con los demás y a su vez la comunicación es el uso del lenguaje  ya sean signos, gestos, sonidos o palabras consensuadas entre los entes que se están comunicando.Por tanto, ambos conceptos están unidos y son dependientes uno del otro\n Existen diferentes tipos de lenguajes los cuales se engloban en dos grandes grupos:\n Lenguaje natural\n Lenguaje artificial\n Lenguaje natural:\n Es el medio que utilizamos de manera cotidiana para establecer nuestra comunicación con las demás personas. Este tipo de lenguaje es el que nos permite designar las cosas actuales y razonar acerca de ellas, fue desarrollado y organizado a partir de la experiencia humana y puede ser utilizado para analizar situaciones altamente complejas y razonar muy sutilmente. La riqueza de sus componentes semánticos da a los lenguajes naturales su gran poder expresivo y su valor como una herramienta para razonamiento sutil\n Lenguaje artificial:\n Es un código creado arbitrariamente para establecer comunicación en una situación comunicativa especial que no permite o no aconseja emplear la lengua, así como: el código morse, el código de circulación, el lenguaje de las banderas, lenguajes lógicos y matemáticos, lenguajes de programación y de más son ejemplos de lenguajes artificiales. Todos ellos han sido creados ex profesor y, por tanto, no constituyen, en ningún caso un 'idioma'\n Procesamiento del lenguaje natural\n El procesamiento del lenguaje es de manera general, el conjunto de instrucciones que una computadora recibe en un lenguaje de programación dado (formal), que le permitirán comunicarse con un humano en su propio lenguaje, (inglés, francés, español, etc.).\n El procesamiento del lenguaje natural presenta múltiples aplicaciones:\n Corrección de textos\n Traducción automática\n Recuperación de la información\n Extracción de Información y Resúmenes\n Búsqueda de documentos\n Sistemas Inteligentes para la Educación y el Entrenamiento\n Clasificación de estructuras de textos científicos\n Un texto científico es una producción escrita que aborda teorías, conceptos o cualquier otro tema con base en el conocimiento científico a través de un lenguaje técnico especializado\n Los principios generales que cumple la redacción científica son:\n Precisión: Se refiere a la concisión y exactitud rigurosa en el lenguaje y estilo,  se logra cuando se utilizan palabras que comunican exactamente lo que se quiere decir, por tanto, se debe hacer una elección adecuada de las palabras y de los terminos que se van a emplear.\n Claridad: El texto se lee y se entiende rápidamente, se logra cuando el lenguaje es sencillo, las oraciones están bien construidas y cada párrafo desarrolla su tema siguiendo un orden lógico y coherente.\n Brevedad: Solo se incluye información pertinente al contenido del artículo y se comunica con el menor número de palabras. Su importancia radica en que el uso de ideas innecesarias desvía la atención del lector y por ende afecta la claridad del mensaje\n Existen diversos formatos para su publicación dependiendo el enfoque que se le quiera dar, los más comunes son:\n Revistas de divulgación científica\n Papers\n Tesis\n Cada uno de los textos de publicación y consulta científica cumplen un formato, el cual incluye las siguientes partes:\n Título: Es el apartado más leído y es de vital importancia para conseguir que un lector interesado acceda al contenido completo del trabajo. Es esencial para la búsqueda bibliográfica porque aparece en bases de datos, páginas de Internet referentes a revistas científicas y en la literatura citada de otros artículos.\n Autores: La forma en que se consignan los nombres de los autores es importante para la recuperación de sus respectivas biografías en el transcurso de sus carreras académicas. Es necesario firmar siempre igual y con un formato que sea interpretado correctamente en bases de datos internacionales.\n Afiliaciones: Se debe especificar el nombre de la institución en la cual los autores se encontraban trabajando cuando se llevó a cabo el estudio.\n Resumen: Más conocido como abstact en inglés, aparece inmediatamente después del título del artículo. Tiene como  objetivo permitir al lector identificar en forma rápida y precisa el contenido básico del artículo. Al elaborar resumen se debe tener una idea clara del lector al que va dirigido, utilizar un estilo y redacción sencillos, evitar excesivos tecnicismos, ser conciso y breve, no debe superar las 250 palabras.\n Palabras clave: Consta de una lista de términos específicos e importantes que aparecen en el texto, los cuales se escriben separados por comas y son utilizados por los servicios bibliográficos para catalogar un trabajo en un área específica.\n Introducción: Informa tres elementos muy importantes de la investigación, el propósito, la importancia y el conocimiento actual del tema. Requiere que el autor establezca el marco contextual en el que se inserta el problema que se va a resolver; esta sección es una forma de atraer al lector.\n Materiales y método: Tiene como meta describir minuciosamente la foma en que se realizó el estudio. Este acápite puede estructurarse en los siguientes epígrafes, diseño, población, entorno, intervenciones y análisis estadístico.\n Resultados: Es la parte más importante del texto y a menudo la más corta; el primer párrafo de este texto debe ser utilizado para resumir en una frase concisa, clara y directa el hallazgo del estudio, se presentan en orden lógico y sucesivo como fueron encontrados, de forma que sean comprensibles y coherentes por si mismos.  Se tiene que expresar de manera clara y sencilla porque representan los nuevos conocimientos que se están aportando. \n Lista de referencias: Constituye un grupo de datos precisos detallados para la identificación de una fuente documental impresa o no, de la cual se obtuvo información. En esta sección se detallarán los trabajos a los que se hizo referencia en el artículo y deben ser numerados consecutivamente en el orden en que se mencionan por primera vez en el texto.    mensaje\n El plagio\n Se trata de la apropiación indebida de la propiedad intelectual, el hurto de ideas, métodos y resultados de terceros, y acaso también de su expresión, al publicarlos bajo el nombre de uno mismo\n Se puede cometer plagio tanto de forma deliberada, intencionalmente, o de manera inconsciente, por desconocimiento apropiado del concepto o formas de prevenirlo\n Tipos de plagio\n De acuerdo con la Real Academia España (RAE) el plagio es la acción y el efecto de copiar obras ajenas sin embargo, la definición de plagio y derechos de autor se han ido ajustando según su entorno y desarrollo de la humanidad, actualmente se encuentran distintas formas de identificar el plagio como lo son:\n Plagio completo: se refiere a una copia textual de contenido de un artículo a otro sin hacer cambios o parafraseo del texto original y a su vez carece de una indicación de donde proviene.\n Plagio parcial: se refiere a copiar partes de textos de una o de varias obras y colocarlos en una obra (que se presenta como propia) sin citar o dar los créditos al autor original o la fuente de donde se obtuvo\n Auto plagio: consiste en reutilizar contenido de un trabajo para la creación de uno nuevo, pero ambos trabajos pertenecen al mismo autor.\n  Envío doble: contiene características similares al auto plagio, pero en este caso se habla de realizar exactamente la misma publicación de un artículo o texto en diferentes medios o tiempos, mientras que el auto plagio modifica la publicación anterior para la creación de una segunda.\n  Falsa Autoría: esta es la peor de todas ya que consiste en la introducción del nombre de una persona ajena al trabajo, es decir, dar crédito a una persona o personas que no realizaron ningún tipo de contribución. Esto aplica también en la introducción de nombres como coautores a las personas que financian el proyecto o investigación.\n Entre muchos otros que hacen referencia a cada uno de los medios de difusión que tenemos en la actualidad (ya sea, vídeo, audio o texto).\n Bases legales\n De acuerdo al TITULO VIGÉSIMO SEXTO De los Delitos en Materia de Derechos de Autor del Código Penal Federal en función a la hora de elaborar este documento (DOF 01-06-2021), Artículo 427 que dice “Se impondrá prisión de seis meses a seis años y de trescientos a tres mil días multa, a quien publique a sabiendas una obra sustituyendo el nombre del autor por otro nombre” y el Artículo 429 donde estipula “Los delitos previstos en este Título se perseguirán de oficio, excepto lo previsto en los artículos 424, fracción II,  424 Bis, fracción III y 427”\n Normas de citación\n La revisión de la literatura se asume como el punto de arranque del trabajo de investigación; de este se derivan los conceptos y las perspectivas teóricas de las investigaciones analizadas para el correcto encuadre del estudio. En la revisión de la literatura se puede encontrar la situación que guarda el objeto de estudio, como confirmar si:\n Existe una teoría completamente desarrollada que pueda aplicarse al problema de la investigación.\n  Hay teorías que se aplican al problema de investigación.\n No existe una teoría sino generalizaciones empíricas que se aplican al problema.\n Hay pocos o ningún estudio en el campo que se investiga\n Por ende las personas que escriben textos científicos o han publicado algún artículo se enfrentan a determinadas normas de citación, tales como: APA, Vancouver, Chicago, MLA, ISO, IRAM, IEEE; entre las más conocidas.  Lo que proponen estas normas, en síntesis, es un sistema codificado, con ligeras variantes, acerca de cómo se deben consignar las referencias de la bibliografía citada o en un sentido más amplio, de los documentos utilizados en un trabajo científico\n APA 7\n Las normas APA (American Psychological Association) son un conjunto de directrices diseñadas para facilitar la comunicación clara y precisa en las publicaciones académicas, especialmente en la citación y referenciación de las fuentes de información. Algunos tipos de citas son:\n Cita directa\n Pueden ser cortas (hasta 40 palabras) o en bloque (más de 40 palabras)\n Cita en indirecta\n El autor transmite en sus propias palabras una idea expresada en el trabajo referenciado. Al parafrasear, la persona investigadora debe asegurarse de conservar el sentido de la idea citada.\n Las normas APA utilizan el método fecha-autor. Esto significa que a cada cita, deberás informar el apellido del autor y el año de publicación de la fuente. Existen dos formatos básicos para representar las citas en el texto y son:\n Cita narrativa (basadas en el autor): Al comienzo de la cita se agrega el nombre del autor. Ejemplo\n “La aceleración de las partículas y su posterior calma es la prueba cabal de la existencia divina y de la presencia de un ser más poderoso entre nosotros” (Berrío, 2019, p. 87).\n Citando corporaciones, instituciones o fundaciones como autores: Se abrevia el nombre completo de la institución a un acrónimo apropiado cuando la abreviatura sea bien conocida (una universidad famosa o una institución como la ONU, solo por mencionar algunos ejemplos). En caso que la institución no sea muy conocida se escribe el nombre completo en la primera cita y posteriormente la abreviatura para utilizarla en citas posteriores. Ejemplo: (Asociación Americana para el Avance de la Ciencia [AAAC], 2014, p. 18)\n Lista de referencias\n La lista de referencias debe iniciar en una nueva página separada del texto. Cada entrada en una lista de referencias debe incluir los cuatro elementos básicos de una referencia: el autor, fecha de publicación título del trabajo y fuente para recuperación.\n Esta lista debe ser ordenada alfabéticamente por el primer apellido del autor seguido de las iniciales del autor; en la versión 7 de las normas APA se aceptan hasta 20 coautores por cada referencia \n IEEE\n El estilo de citación IEEE es utilizado principalmente en el área de las ingenierías tales como: electrónica, telecomunicaciones, ciencias de la computación y recursos naturales. Las tres partes principales de una referencia bajo este sistema son:\n Nombre del autor.\n Título del artículo, patente, ponencia de congreso, entre otros, entre comillas.\n Título de la revista o libro en letra itálica.\n Elementos que cumplen las citas dentro del texto\n Las referencias deben estar numeradas en el orden en que aparecen en el manuscrito.\n Una vez asignado un número a una referencia dada, el mismo número debe emplearse en todas las ocasiones en que ese documento sea citado en el manuscrito.\n Cada número de referencia debe estar entre corchetes [ ].\n No es necesario incluir la palabra 'referencia'.\n Para citar, dos o más fuentes consecutivas se pueden tener corchetes separados\n Ejemplo de una cita en formato IEEE\n [1] R. Yousefian y S. Kamalasadan, “A Lyapunov function based optimal hybrid power system controller for improved transient stability”\n Electr. Power Syst.} Res., vol. 137, pp. 6-15, 2016.\n Lista de referencias\n Para terminar de citar las fuentes, se debe proporcionar una lista numerada de referencias al final del artículo. La lista se compone de citas secuenciales enumeradas, con detalles,comenzando con [1], y no debe estar en orden alfabético; sí no por orden de aparición\n Lenguaje de programación\n Un lenguaje de programación es una herramienta que permite desarrollar software o programas para computadoras permitiendo definir y administrar el comportamiento de los dispositivos físicos y lógicos del ordenador. Así mismo un lenguaje de programación se conforma de una serie de símbolos y reglas de sintaxis y semántica las cuales definen la estructura principal del lenguaje y le dan un significado a sus elementos y expresiones \n Aplicaciones web.\n Una aplicación web es un tipo de software que se codifica en un lenguaje que pueda ser soportado y ejecutado por los navegadores de Internet o por una intranet o red local\n Usando la página web ''Ranking IEEE Spectrum'' se muestran a continuación los 10 lenguajes de programación más usados durante el año 2021 en cuestión de web:\n Arquitectura para diseño web\n La arquitectura para un sitio web es la planificación y el diseño de los componentes técnicos, funcionales y visuales de un sitio web antes de que sea diseñado, desarrollado e implementado.\n Una buena arquitectura web es muy importante por que afecta:\n Al posicionamiento\n A la facilidad de indexación del sitio por los motores de búsqueda\n Al comportamiento del propio sitio\n Al comportamiento de las personas que interactúan con el sitio\n A la hora de implementar una buena arquitectura web se debe tomar en cuenta los siguiente:\n Planeación y previsión\n Sencillez\n URLs\n Lenguajes de programación para Backend\n El Backend es la capa de acceso a datos de un software o cualquier dispositivo, que no es directamente accesible por los usuarios.Contiene la lógica de la aplicación que maneja dichos datos\n A la hora de hacer BackEnd se pueden usar varias opciones como son:\n Python\n JS\n PHP\n Java\n Ruby\n GoLang\n Lenguaje de programación para Frontend\n El Frontend es la parte de un programa o dispositivo que interactúa con los usuarios (el usuario puede acceder directamente). Son todas las tecnologías de diseño y desarrollo web que corren en el navegador y que se encargan de la interactividad con los usuarios, por eso se dice que esta del lado del cliente\n A la hora de hacer FrontEnd es importante usar:\n HTML\n CSS\n JS\n Pero dentro de estas existen diferentes herramientas como son:\n CSS\n Bootstrap\n Less\n Sass\n JS\n Angular\n React\n npm\n Vue.js\n Node.js\n jQuery\n Web Scraping.\n El web scraping (''raspado web'' o ''scrapear'') es un proceso dentro del data science's qué se utiliza para la extracción de datos de sitios web, normalmente en el lenguaje de programación Python y mediante machine learning, simulando cómo navegaría un ser humano en determinadas páginas web. El objetivo puede ser transformar contenidos, almacenar datos de la web, reconocer estructuras de código HTML único, recopilar información, hacer minería y análisis de datos, automatizar la creación de enlaces\n Tipos de Web scraping\n Manual\n Expresiones regulares\n Protocolo HTTP \n Algoritmos de minería\n Pasers de HTML\n Reconocimiento de red semántica\n Aplicaciones para web scraping\n Ecosistemas de desarrollo para web scraping\n Scrapy\n Selenium\n Import.io\n Scrapers\n Dexi.io\n Screaming Frog\n Sistema informático\n Un sistema informático esta compuesto por hardware y software; la función principal de un sistema informático es el procesamiento de datos almacenados\n Sistema distribuido.\n Un sistema distribuido es aquel en el que los componentes localizados en computadores, conectados en red, comunican y coordinan sus acciones únicamente mediante el paso de mensajes.\n Esta definición lleva a las siguientes características de los sistemas distribuidos: concurrencia de los componentes, carencia de reloj global y fallos independientes de los componentes\n Diagramas para documentación\n Para el desarrollo de la ingeniería de software los desarrolladores se apoyan de diagramas para describir el comportamiento de los sistemas informáticos.\n  Estos se dividen en dos grandes grupos:\n Diagrama de estructura: muestran la organización de un sistema, en términos de los componentes que constituyen dicho sistema y sus relaciones. Los modelos estructurales son modelos estáticos, que muestran la estructura del diseño del sistema, o modelos dinámicos, que revelan la organización del sistema cuando se ejecuta. No son lo mismo: la organización dinámica de un sistema como un conjunto de hilos en interacción tiende a ser muy diferente de un modelo estático de componentes del sistema.\n Diagrama de comportamiento: Los modelos de comportamiento son modelos dinámicos del sistema conforme se ejecutan. En ellos se muestra lo que sucede o lo que se supone que pasa cuando un sistema responde ante un estímulo de su entorno. Tales estímulos son de dos tipos:\n Datos Algunos datos que llegan se procesan por el sistema.\n Eventos Algunos eventos activan el procesamiento del sistema. Los eventos pueden tener datos asociados, pero esto no es siempre el caso\n Los anteriores grupos tienen diferentes métodos, y de estos se puede elegir cual sea más conveniente para el sistema que se desee maquetar.\n Diagramas de estructura:\n Diagrama de clase\n Diagrama de despliegue\n Diagrama de objetos\n Diagrama de componentes\n Diagrama de estructura\n Diagrama de paquetes\n Diagramas de Comportamiento:\n Diagrama de actividad\n Diagrama de máquina de estados\n Diagrama de Casos de uso\n Diagrama de interacción\n Diagrama de tiempos\n Diagrama de secuencia\n Diagrama de comunicación\n Diagrama global de interacciones\n Bases de datos\n Una base de datos es un sistema que convierte un conjunto de datos de gran tamaño en una herramienta abstracta, permitiendo al usuario buscar y extraer elementos pertinentes de información, de una forma cómoda para él\n Tipos de bases de datos\n Bases de datos relacionales\n En estas bases de datos los datos son representados como si estuvieran almacenados en tablas rectangulares, denominadas relaciones, que son similares al formato en el que se visualiza la información en los programas de hoja de cálculo\n Bases de datos orientadas a objetos\n En estas bases de datos la información es representada en forma de objetos, como en la programación orientada a objetos.\n Almacenes de datos\n Repositorio central de datos, un data warehouse es un tipo de base de datos diseñado específicamente para consultas y análisis rápidos.\n Bases de datos NoSQL\n Una base de datos NoSQL o no relacional, permite almacenar y manipular datos no estructurados y semiestructurados (a diferencia de una base de datos relacional, que define cómo se deben componer todos los datos insertados en la base de datos).\n Bases de datos orientadas a grafos\n  Una base de datos orientada a grafos almacena datos relacionados con entidades y las relaciones entre entidades.\n Bases de datos OLTP\n Es una base de datos rápida y analítica diseñada para que muchos ususarios realicen un gran número de transacciones\n Base de datos distribuida (BDD)\n Una base de datos distribuida o BDD consiste en varias bases de datos situadas en diferentes espacios físicos o lógicos, conectados entre sí por un sistema principal de comunicaciones que coordine y gestione sus procesos\n Entornos de desarrollo para Bases de Datos\n Un entorno de desarrollo integrado (IDE) es un sistema de software para el diseño de aplicaciones que combina herramientas comunes para desarrolladores en una sola interfaz de usuario gráfica (GUI)\n Algunos entornos para el desarrollo de Bases de Datos (BD) son:\n MongoDB\n Azure SQL Server\n PostgreSQL\n Oracle\n FireBase\n Amazon Simple DB\n MySQL Gestión Base de Datos\n SQL Server Data\n SAP HANA\n Oracle CDM in the Cloud\n Maria DB\n Cassandra\n Redis\n Nota al lector: para mayor referencia consulte el anexo A\n Servidores\n Los servidores son parte importante de la culminación de todo proyecto que comprenda el desarrollo de software, a continuación hablaremos un poco más de estos y su importancia dentro de nuestro contexto.\n Definición\n En primer instancia puede definirse como un conjunto de computadores informáticos que son capaces de atender las peticiones de un cliente a través de la web con ayuda de los protocolos HTTPS y devolverle una respuesta en concordancia, sin embargo una definición más más formal enuncia lo siguiente.\n Un servidor es un sistema que proporciona recursos, datos, servicios o programas a otros ordenadores, conocidos como clientes, a través de una red. En teoría, se consideran servidores aquellos ordenadores que comparten recursos con máquinas cliente. Existen muchos tipos de servidores, como los servidores web, los servidores de correo y los servidores virtuales\n Tipos de servidores\n Como ya se menciono un servidor es aquel que proporciona recursos, datos o servicios a otros ordenadores, ya sean:\n Recursos audiovisuales\n Bases de datos\n Textos\n Por ende es común pensar que existen múltiples compañías que proporcionan sus servicios en base a los recursos e información que requiera el mercado, pudiendo clasificar los servidores en:\n Servidor email\n Uno de los más antiguos que encontraremos en esta lista. Funciona como una especie de oficina de correo para almacenar, recibir, enviar y permitir múltiples operaciones que tienen que ver con el correo personal de los clientes.Los servidores de email son de los más comunes en el mercado, gracias a la popularidad que tiene el correo electrónico en nuestra vida, debido a su eficacia en términos informativos y de gestión.Son programados para responder efectivamente ante requisitos de los clientes en cuanto al tipo de correo que reciben o envían. Asimismo, estos tienen subtipos:\n POP3  Retienen los email's recibidos hasta que el usuario los abre, momento en que son enviados al dispositivo (computadora, teléfono, tablet).\n IMAP  Permite interactuar con la información recibida como un mensaje de email, pero sin descargarla en el equipo. Gracias a ellos, es posible las vistas previas para poder organizarlos, descargarlos o eliminarlos.\n SMTP Administran todos los email's salientes. Funcionan con una combinación entre POP3 y IMAP.\n Servidor Web Tras casi 28 años de Internet, según El Tiempo, existen más de 1.7 mil millones de páginas web, y cada una de ellas debe estar almacenada dentro de un servidor. Un servidor web se ocupa de guardar la información en formato HTML de los sitios, donde se incluye texto, imágenes, vídeos y todo tipo de datos. Mediante un explorador web, los usuarios puedan visualizar todo esto en sus pantallas.Todos se comunican entre sí con otros servidores mediante el protocolo HTTP, para brindar estabilidad y rapidez en la transmisión de datos y están clasificados por:\n Apache El más común de todos, es un sistema multiplataforma que brinda estabilidad y seguridad.\n Microsoft IIS  Solo funciona para sistemas Windows y permite convertir una computadora en un servidor web a menor escala.\n Sun Java System Web Server\n Servidor de código abierto, para tecnologías como PHP, JSP, entre otras.\n Lighttpd\n Muy ligero y rápido, está diseñado para entornos donde se necesita la velocidad.\n Servidores virtuales\n Te brindan la posibilidad de optimizar costos en hardware, puesto que otorgan flexibilidad para accionar varios sistemas operativos y programas a la vez.\n Servidor de base de datos\n Son dispositivos diseñados para almacenar grandes cúmulos de información y poder gestionar los datos uno por uno.También son capaces de analizar, manipular y alojar los datos de acuerdo a los requerimientos del usuario.\n Servidores Cloud\n  Estos sirven para compañías que se dedican a rentar un espacio en sus servidores para que otras personas o empresas guarden la información de manera remota. Sirven para almacenar grandes cantidades de datos y así proteger la información de las organizaciones o personas naturales. Generalmente es utilizada como una “caja fuerte” de información, ya que los proveedores garantizan, además del acceso inmediato, el resguardo de los datos ante pérdidas o fugas.\n Servidores DNS\n Están encargados de gestionar los nombres de los dominios de las páginas web. Es decir, su trabajo es crear un vínculo entre el dominio del sitio con su IP (un conjunto de números que identifica jerárquica y lógicamente una interfaz en red a un dispositivo).De esta manera, cuando se escribe un dominio en un explorador, el servidor lee este requerimiento y regresa la información de la interfaz de la página.\n Servidores Telnet\n Utilizado principalmente en las telecomunicaciones, es un protocolo de red que le permite a los usuarios gestionar, enviar y recibir datos para solucionar problemas con las redes relacionadas con la telefonía.Así mismo, almacena los datos de los mensajes de voz, contestadoras, encima las llamadas y controla la red del Internet móvil.\n  Servidor SIP\n Es conocido como Proxy SIP y su trabajo es establecer la conexión para llamadas telefónicas por Internet. El mismo no transmite audio ni video; únicamente almacenan la dirección IP para generar la comunicación con otro usuario.\n Servidor FTP\n Es un servidor que está conectado a Internet que permite la posibilidad de transferir archivos y datos entre otros ordenadores y servidores.\n Servidor de acceso remoto (RAS)\n Vigila las líneas de módem de los ordenadores u otros medios de comunicación de Internet, de manera tal que los requerimientos conecten con la red en forma remota, contesta llamadas e interviene la petición de la red.\n Servidor compartido\n Otorgan espacio para guardar información y al mismo tiempo comparte recursos con la memoria RAM, el CPU, el sistema operativo, la conectividad a Internet y la dirección IP.Este servidor se usa para recibir requerimientos de muchos clientes. La única desventaja es que los usuarios del servidor compartido no pueden realizar muchas peticiones al mismo tiempo, ya que no es suficientemente rápido.Como puedes ver, los distintos tipos de servidores se extienden, básicamente, a casi todas las tareas de almacenamiento, transmisión y alojamiento de datos que se ejecutan en la red\n Machine Learning.\n El machine learning es una disciplina del campo de la inteligencia artificial que, a través de algoritmos, dota a los ordenadores de la capacidad de identificar patrones en datos masivos y elaborar predicciones (análisis predictivo). Este aprendizaje permite a los computadores realizar tareas específicas de forma autónoma, es decir, sin necesidad de ser programados\n Redes neuronales.\n Las redes neuronales son modelos simples del funcionamiento del sistema nervioso. Las unidades básicas son las neuronas, que generalmente se organizan en capas.\n Una red neuronal es un modelo simplificado que emula el modo en que el cerebro humano procesa la información: Funciona simultaneando un número elevado de unidades de procesamiento interconectadas que parecen versiones abstractas de neuronas. Las unidades de procesamiento se organizan en capas. Hay tres partes normalmente en una red neuronal:\n Una capa de entrada: La capa de entrada con unidades representan los campos de entrada\n Una o varias capas ocultas: Que se encargan del procesamiento de la información\n Una capa de salida: Donde se especifican las unidades para dar salida al sistema\n Las unidades se conectan con fuerzas de conexión variables (o ponderaciones). Los datos de entrada se presentan en la primera capa, y los valores se propagan desde cada neurona hasta cada neurona de la siguiente capa; al final, se envía un resultado desde la capa de salida.\n La red aprende examinando los registros individuales, generando una predicción para cada registro y realizando ajustes a las ponderaciones cuando realiza una predicción incorrecta. Este proceso se repite muchas veces y la red sigue mejorando sus predicciones hasta haber alcanzado uno o varios criterios de parada.\n Clasificación de las redes neuronales\n Red neuronal de avance (RNN)\n La información fluye en una sola dirección (hacia adelante). Es decir los flujos de información comienzan en la capa de entrada  van a las capas “ocultas” y terminan en la salida. La red no tiene bucle. La información se detiene en las capas de salida.\n Red neuronal recurrente (CNN)\n Red neuronal de varias capas que puede almacenar información en nodos de contexto, lo que permite aprender secuencia de datos y generar un número u otra secuencia (o sea, las conexiones entre neuronas incluyen bucles); estas redes neuronales son muy adecuadas para procesamiento de un insumo\n Modelos de redes neuronales\n Perceptrón simple\n Este modelo neuronal fue introducido por Rosenblatt a finales de los años cincuenta. La estructura del perceptrón se inspira en las primeras etapas de procesamiento de los sistemas sensoriales de los animales (por ejemplo, el de visión), en los cuales la información va atravesando sucesivas capas de neuronas, que realizan un procesamiento progresivamente de más alto nivel.\n El perceptrón simple es un modelo neuronal unidireccional, compuesto por dos capas de neuronas, una de entrada y otra de salida\n Red Hopfield\n Este modelo consiste en una red monocapa con N neuronas cuyos valores de salida son binarios : 0/1 ó -1/+1. Las funciones de activación eran del tipo escalón. Se trata, por tanto, de una red discreta con entradas y salidas binarias; posteriormente Hopfield desarrolló una versión continúa con entradas y salidas analógicas utilizando neuronas con funciones de activación de tipo sigmoidal.\n Existen conexiones laterales (cada neurona se encuentra conectada a todas las demás) pero no autor recurrentes (no consigo misma). Los pesos asociados a las conexiones entre pares de neuronas son simétricos wi=wij\n Perceptrón multicapa\n El procedimiento Perceptrón multicapa (MLP) genera un modelo predictivo para una o más variables dependientes (de destino) basada en los valores de las variables productoras\n Las Redes neuronales de tipo Perceptrón Multicapa (PM) se encuentran entre las arquitecturas de red más poderosas y populares. Están formadas por una capa de entrada, un número arbitrario de capas ocultas, y una capa de salida. Cada una de las neuronas ocultas o de salida recibe una entrada de las neuronas de la capa previa (conexiones hacia atrás), pero no existen conexiones laterales entre las neuronas dentro de cada capa\n Red neuronal competitiva simple\n Las neuronas de una red competitiva reciben idéntica información de la entrada, pero compiten por ser la única que se activa. Cada neurona se especializa en un área diferente del espacio de entradas, y sus salidas se pueden utilizar para representar de alguna manera la estructura del espacio de entradas. Vamos a introducir topologías y reglas de aprendizaje específicas que están dirigidas a la competición. La competición se muestra como un método rápido de organización automática de los recursos de la red y se ha mostrado muy efectiva en la práctica\n Redes neuronales Online ART1\n Las redes basadas en la teoría de resonancia adaptativa sirven para clasificar patrones de manera no supervisada, esto es, la red forma grupos y crea el número de categorías que crea conveniente en función de la configuración que le demos y las cualidades de los patrones.\n ART hace uso de dos términos usados en el estudio del comportamiento del celebro: Estabilidad y Plasticidad para llevar a cabo esta clasificación. Estabilidad refleja la capacidad del sistema para recordar patrones previamente aprendidos. Plasticidad es la capacidad de aprender nuevos patrones.\n El equilibrio entre Estabilidad y Plasticidad es resuelto en las redes ART usando un parámetro llamado, granulidad , según algunos autores , otros lo llaman parámetro de vigilancia , yo he usado el anterior nombre por que expresa mejor la idea de una red con muchas categorías formando muchos y pequeños gránulos de patrones o formando pocos y grandes gránulos. Este parámetro nos cuantifica cuanto debe diferenciarse un patrón al clasificar, del almacenado (estabilidad) en una categoría para que sea considerado una nueva categoría (plasticidad)\n Redes neuronales competitivas ATR2\n La red ART2 es una ampliación de la red ART1 que admite valores reales, como la anterior red, sirve para clasificar patrones de manera no supervisada\n La arquitectura de la red ART2 es la misma que la de la ATR1. Consta de dos capas: la capa de entrada de sensores y la capa de salida, que en un principio no tiene ninguna neurona, pero que según vamos entrenando la red, esta va formando grupos de patrones que clasifica en una categoría cuyo patrón representativo son los pesos de entrada de la neurona de la capa de salida\n Mapas de kohonen\n Los  mapas  de  Kohonen  son  también    denominados  mapas   auto-organizativos.   Desarrollados   por   Teuvo   Kohonen  a  partir  de  1989,  se  basan  en  las  redes  neuronales  para  realizar  un  análisis  y  categorización  automática  del  contenido  semántico  de  documentos  textuales.  El  resultado  gráfico  de  este  análisis  es  un  mapa  2D  de  categorías  en  las  que  cada  categoría  ocupa un espacio proporcional a las frecuencias de sus componentes. Los patrones más frecuentes ocupan un espacio mayor a expensas de los menos habituales. Kohonen  estaba  motivado  por  la  idea  de  que  “la  representación  del  conocimiento  en  una  particular  categoría  de  cosas  en  general  debiera  asumir  la  forma  de  una  mapa  de  características  organizado  geométricamente  sobre  la  parte  correspondiente  del  cerebro”. El algoritmo toma un conjunto N dimensional de  objetos  como  entrada  y  entrena  una  red  neuronal  que  converge  finalmente  a  la  forma  de  un  mapa  2D.  Parece ser, además, que los SOM se cuentan entre los modelos más realistas del funcionamiento cerebral\n Ecosistemas para desarrollo de redes neuronales\n Los lenguajes para programas redes neuronales son las siguientes:\n Python (Pytorch) \n Lenguaje R\n JavaScript \n Keras\n TensorFlow",
            "Similitud": "En este capítulo se aborda el concepto de la creatividad a la luz de la teoría existente. Se presentan definiciones enunciadas por diversos autores a lo largo de la historia, se expone la relación que tiene con el aprendizaje, se analizan varias teorías del proceso creativo en los individuos, se exponen algunos estudios relacionados, así como propuestas y herramientas que pueden afectar positivamente en dicho desarrollo.\\n Definiciones de creatividad\\n Los antiguos creían que la genialidad y la creatividad era simplemente un don o un chispazo de iluminación pero hoy en día después de muchas investigaciones, estudios y observaciones se ha podido constatar que la creatividad es producto de un proceso mental y no producto de la casualidad o gracia como muchos creían.\\n Según Runco (2007) los personajes que han hecho inventos, descubrimientos e innovaciones, tuvieron que pagar un precio, no fue casualidad, sino que estos fueron perseverantes, constantes, toleraron la frustración y estaban abiertos a diferentes puntos de vista. Inclusive soportaron críticas de colegas los cuales no confiaban en sus propuestas, pero después de todo lograron concretar el producto o bien alcanzar el éxito con sus nuevas ideas.\\n Algunos de estos personajes fueron entre muchos otros, Los Beatles en los cuales  las disqueras no creían y se rehusaban a grabarlos, argumentando que no les gustaba su música y que no gustarían en el mercado. Un editor de un periódico en San Francisco rechazó a Rudyard Kipling pues según él, este escritor no sabía utilizar el lenguaje. Mientras que Picasso pintaba su famoso cuadro Las Doncellas de Avignon en 1906 un grupo de famosos artistas lo visitaron y expresaron su disgusto por la obra (Runco, 2007).\\n Hoy en día el término de 'creatividad', es del dominio público. Este término se escucha prácticamente en todos los ámbitos, desde el artístico, hasta el empresarial y por supuesto en el científico y en el educativo al igual que en muchos otros, la creatividad es un concepto multidisciplinario. Con el fin de que se tenga claro el concepto de creatividad a continuación se ofrecen algunas definiciones.\\n En el siglo XIX algunos autores como Galton, Lambroso, Kretschmer entre otros, defendían la postura de que la creatividad no era un don divino o bien un momento de iluminación, sino que tenía un fundamento fisiológico y por lo tanto una carga genética y hereditaria. A principios del siglo XX , Terman y Segond también apoyaron la tesis de que la genialidad se heredaba, inclusive Segond sostenía que desde el vientre materno el individuo ya contaba con los rasgos innatos de la genialidad (Velasco, 2007).\\n Actualmente, gracias a las investigaciones se sabe que la capacidad de crear es una combinación de varios elementos. Monreal (citado en Velasco, 2007) dice que tanto en la conducta humana y por ende en la creatividad lo genético y la influencia del medio ambiente interactúan entre sí.\\n A través del tiempo muchos son los autores que han dado su propia definición de lo que cada uno supone que creatividad es. Uno de tantos es Mayer, que define creatividad como una 'actividad cognitiva que tiene como resultado soluciones nuevas a un problema' (Mayer, 1983, p. 376).\\n Según Sternberg y Lumbart (citados en Ward, 2007), la creatividad es producto de la interacción entre el conocimiento, el entorno, las habilidades intelectuales, el estilo de aprendizaje, la motivación y la personalidad del individuo. Por su lado Stenberg (2000, 2003), sostiene que la creatividad es una decisión personal, que lleva al individuo a salir de la corriente del modo de pensar tradicional.\\n Otra definición de creatividad es, 'proceso de descubrimiento o producción de algo nuevo que cumple determinadas exigencias sociales y en el cual se da el vínculo de los aspectos cognitivos y afectivos de la personalidad' (González y Mintjáns, citados en Mendoza, 2001, p. 271). Dicha perspectiva está fundamentada en tres aspectos. El primero, la creatividad es la expresión de la conjunción de dos elementos el cognitivo y el afectivo a través de la motivación, el elemento afectivo es definitivo para la regulación conductual. El segundo, no hay creatividad sin motivación. El tercero, en el proceso creativo son expresados los elementos de la personalidad, tanto los de contenido como los funcionales (Mendoza, 2001).\\n Después de haber realizado algunas investigaciones sobre creatividad en Cuba, Mitjáns (2000, 2004) la definió como una difícil evolución personal del ser humano, pero a su vez en las peculiaridades individuales y sociales, la cual es reflejada en la elaboración de un producto novedoso, el cual puede emplearse en beneficio de la humanidad.\\n Por otro lado, Mendoza (2001) explica que la creatividad es aquella capacidad que tiene el individuo para innovar y modificar tanto ideas, como acciones por medio de su propia intervención afectiva y cognitiva, en la que los contextos con los que se interactúa influyen, esta capacidad se va desarrollando desde la temprana edad.\\n Para Betancourt (2000) la creatividad es la capacidad de innovar productos, dentro de un contexto creativo, los cuales son de gran valor social y en ocasiones trascienden el contexto histórico. En dicha capacidad intervienen elementos cognitivos, afectivos, intelectuales y volitivos.\\n Ciskszentmihalyi difiere en cuanto a la concepción del individuo creativo, además considera que una persona es creativa siempre y cuando la innovación que propone tenga un impacto sociocultural. Por lo tanto la creatividad no es meramente un producto de capacidad personal o individual sino que depende de la interacción que tenga con el ámbito, el cual ha de determinar si ese producto es creativo o no. A partir de esta conclusión, Ciskszentmihalyi propone su teoría de sistemas, la cual ilustra como un triángulo en cual intervienen tres factores definitivos para el proceso creativo. Estos tres elementos son, el campo, el ámbito y el individuo, de tal forma que la creatividad ocurre cuando el sujeto utiliza los símbolos del campo para innovar o inventar, más tarde el ámbito evalúa dicha producción y decide si la acepta o no como producto creativo, ya que esto dependerá en gran manera del contexto (Velasco, 2007).\\n El concepto de la creatividad ha sido visualizado bajo diferentes conceptos, según  Torre (2008) a principios del siglo XX , algunos autores la concebían como capacidad imaginativa, Th. Ribot fue uno de los primeros en describir dicho proceso imaginativo, en los años cincuenta, esta concepción da un giro pues es concebida como una capacidad mental y es Guilford quién le da el nombre de creatividad, identificando los elementos de fluidez, originalidad, elaboración, inventiva y redefinición.\\n Varios fueron los autores que se sumaron a esta perspectiva donde la creatividad es un proceso mental superior. Más tarde el concepto de la creatividad adquiriría una nueva connotación, habilidad de resolución de problemas y toma de decisiones, esta técnica se desarrolló en las empresas primeramente pero también ha alcanzado el ámbito escolar con muy buenos resultados, algunos de los autores que comulgan con esta perspectiva son: Torrance, Osborn y Shallcross entre otros (Torre, 2008).\\n Por su lado Maslow conjuntamente con otros autores humanistas, concebían a la creatividad como autorrealización, dando más importancia a lo actitudinal y a la capacidad del individuo de enfrentar la vida y autorrealizarse que a lo cognitivo. Sternberg consideraba la creatividad como inversión, para él la creatividad es una decisión personal en la cual el individuo es audaz, no tiene miedo al cambio pero requiere conjugar la habilidad sintética, analítica y práctica. El individuo invierte poco y gana mucho al transformar, reorganizar o bien producir ideas, conceptos o productos nuevos (Torre, 2008).\\n En la actualidad el concepto de creatividad ha pasado a un contexto más amplio, ha dejado de considerarse meramente procesos cognitivos superiores en los cuales el individuo tiene capacidad de resolución y decisión. Varios autores de la talla de Goleman, Amabile, Cskiszentmihalyi, entre muchos otros, consideran que la creatividad es un potencial futuro, el cual es factor de cambio en la sociedad. Consideran que la creatividad no es propiedad individual, sino que en ella interactúan tres factores, lo individual, lo cultural y lo social (Torre, 2008).\\n Existe otro tipo de creatividad, la cual es denominada paradójica o adversidad creadora. Torre (2003) dice que ésta se produce en tiempos de crisis y el individuo la aplica para la supervivencia. Sin duda alguna los mexicanos son maestros en este tipo de creatividad, donde los prejuicios quedan relegados y el individuo tiene una actitud de superación ante la adversidad.\\n A decir de todas estas propuestas, tienen fundamentos teóricos, indicadores y elementos que intervienen en dicho proceso y que por años han sido estudiadas, aceptadas, desarrolladas y evaluadas. Sin embargo, según Torre (2008), de unos años para acá ha surgido una nueva visión de la creatividad, bajo el concepto de creatividad cuántica, la cual va más allá de creer que la creatividad es exclusiva del ser humano o las organizaciones, sino que voltea su mirada a la naturaleza, la energía, la materia, a lo espiritual y a cualquier sistema complejo capaz de organizarse por sí mismo y transformarse para convertirse en uno nuevo o superior. Entre los autores que han avalado esta perspectiva están, Monraes, Bohm, Chopra, Roze y el mismo Torre, por mencionar algunos.\\n En el paradigma ecosistémico 'La creatividad es concebida como un campo  vibracional de energía transformadora, es la manifestación de flujos de energía subyacente entre los sistemas vivos' (Torre, 2008, p. 9).\\n El concepto de creatividad que se tomará para fines de este trajo es el propuesto por Mendoza (2001) el cual dice que la creatividad es una capacidad individual de innovación y modificación de ideas y acciones donde los aspectos cognitivos y afectivos intervienen en dicho proceso, también sostiene que ésta se desarrolla desde temprana edad y que los contextos con los que el individuo interactúa influyen.\\n La educación y la creatividad\\n El campo de la educación puede ser terreno fértil para la promoción de la creatividad en los individuos, siempre y cuando todos los involucrados en la comunidad educativa persigan este objetivo.\\n Según Bernstein y Bernstein (2002) la creatividad, es la combinación de varios elementos: el deseo que tiene el individuo por comprender, la capacidad intelectual, las emociones y la percepción sensorial, estos tres elementos interactúan entre sí, están íntimamente ligados unos con otros de tal forma que lo intelectual y lo mental no pueden separase de lo corporal y lo emocional, ya que en el pensamiento creativo estás son indispensables.\\n Getzels y Jackson, Anastasi, y Chaefer (citados en Freiría, 2004), realizaron investigaciones acerca de la relación que tiene el coeficiente intelectual con la creatividad, llegaron a la conclusión, de que lo uno no depende de lo otro ya que la correspondencia entré éstas es tan baja que carece de importancia. Lo que sí pudieron demostrar Getzels y Jackson, es que las personas que tienen un pensamiento creativo también tienen un buen rendimiento académico.\\n Desafortunadamente como bien mencionan Getzels y Jackson, la educación escolar hoy en día, fomenta el pensamiento convergente, en lugar de tomar las medidas necesarias para desarrollar en los alumnos el pensamiento divergente y estos se transformen en creadores. 'Enseñar creatividad implica enseñar a las personas cómo generar ideas nuevas para una situación dada' (Mayer, 1983, p. 376).\\n En los años cincuenta, dos profesores de la Universidad de Chicago, Bloom y Broder, fueron los primeros en enfocarse al estudio de la capacidad de solución de problemas. Estos al realizar sus investigaciones pudieron notar que un grupo de estudiantes aunque aplicados, dedicados, responsables y con la suficiente capacidad, además de tener el conocimiento y la motivación, a diferencia de otro grupo, no lograban buenos resultados en los exámenes de comprensión. Esto condujo a los investigadores a cuestionarse por qué esa diferencia de resultados entre estos dos grupos de estudiantes, lo cual los llevó a estudiar el proceso utilizado en la solución de problemas por los integrantes de ambos grupos (Mayer, 1983).\\n Con este estudio pudieron darse cuenta que aun cuando los estudiantes llegaban a la  respuesta del problema, el proceso de solución a este era diferente ya que en el grupo de los exitosos era congruente y completo, y en el otro presentaba varias fallas. También registraron las siguientes diferencias: 'la comprensión de la naturaleza del problema, la comprensión de las ideas incluidas en el problema, qué planteamiento se realizaba para su solución, y qué actitud se tenía en cuanto a la solución de problemas' (Zimmerman y Schunk, 2003, p. 373).\\n Por tal motivo se dieron a la tarea de diseñar una estrategia para la enseñanza efectiva de resolución de problemas, esto ayudó a desarrollar dicha habilidad en los estudiantes, pero dejando en claro que para que la resolución de problemas el conocimiento del tema, es un factor definitivo.\\n En la década de los sesenta, varios fueron los proyectos que se diseñaron con el fin de promover el pensamiento creativo. A continuación se mencionan dos de ellos. 'Pensar creativamente' de Davis y Houtman (1968). El cual fue diseñando como un comic donde los personajes se veían involucrados en controversias. Y el 'Programa de creatividad Purdue' de (Feldhusen, Trenffinger y Bahlke, 1970), con el cual se pretendía promover el pensamiento divergente en los niños de primaria (Mayer, 1983).\\n Durante la conferencia mundial sobre la educación en 1998, la Organización para la Educación, la Ciencia y la Cultura de las Naciones Unidas (UNESCO), en el artículo noveno, hizo una declaración de reforma educativa, la cual dio una nueva dirección a la educación, se les pide a las instituciones que desarrollen métodos innovadores.\\n En dicha declaración la UNESCO, urge a los países a realizar los cambios pertinentes en los procesos de enseñanza aprendizaje, los cuales deberán estar enfocados en el alumno, pretende se modifique la impartición de la educación, que se planteen métodos de transmisión de conocimientos eficaces y que se revisen los contenidos de los programas.\\n Así mismo solicita a las instituciones de enseñanza superior, que implementen los programas, contenidos y dinámicas necesarios para que su alumnado desarrolle un perfil con el cual sean mejores ciudadanos. Que estén bien informados, sean buenos comunicadores, que desarrollen un pensamiento crítico reflexivo, analicen y resuelvan problemas, tengan motivación intrínseca, propongan soluciones para los problemas sociales y sean responsables.\\n La UNESCO menciona que dicho cambio se logrará a través del cambio de  programas de gran carga de contenido cognitivo, por programas que se enfoquen en el desarrollo de competencias para la vida, donde los alumnos pongan en práctica sus conocimientos y los puedan transferir a su vida cotidiana. Promoviendo en los pupilos la comunicación, el análisis y solución de problemas, la convivencia y el trabajo colaborativo en diferentes contextos, así como la reflexión y el sentido crítico. Para tener éxito en esta empresa no se debe de perder de vista los aspectos culturales, sociales, económicos, históricos, entre otros.\\n La nueva práctica docente empleará recursos para fomentar la creatividad en el alumno, promoviendo conocimientos, habilidades, actitudes y destrezas. Para que por sí mismo construya un aprendizaje significativo y perdurable. Dejando atrás los métodos sistemáticos y mecánicos, basados en la memorización los cuales no rendían muchos frutos en su educación para la vida (UNESCO, 1998).\\n Rodríguez y Ketchum (1995), preocupados por que en México se establezca la creatividad como una forma de pensamiento, dan algunas recomendaciones tanto a  maestros como a padres de familia, para educar a los niños en la creatividad.\\n Darles oportunidad de que experimenten y exploren. \\n No tener actitud de instructor todo el tiempo, aprender de ellos y disfrutarlo.\\n No sentirse mal cuando el niño no tome la opción que usted está proponiendo.\\n  Resuelva problemas junto con los niños, tome en cuenta sus propuestas.\\n Acondicione el espacio para propiciar la creatividad, que sea confortable para el niño, donde pueda crear con libertad y tranquilidad.\\n Lipman (1998), presenta una hipótesis de la existencia de dos paradigmas totalmente divergentes entre sí. El paradigma de práctica educativa estándar y el paradigma reflexivo de la práctica crítica.\\n Comenzando con el paradigma estándar, Lipman (1988) sostiene que este es mera  transmisión de conocimientos, los conocimientos son sobre el mundo y no tienen margen de error ni son novedosos, el conocimiento se secciona en las diferentes disciplinas. En este paradigma el profesor actúa autoritariamente y controla el proceso de aprendizaje limitándolo bajo sus propios conocimientos, los estudiantes son receptores del conocimiento el cual almacenan en sus memorias.\\n En cambio en el paradigma reflexivo de la práctica crítica, se supone que la educación es una práctica comunitaria de indagación, donde el profesor es un guía para que los alumnos consigan la comprensión y apropiación de los conocimientos. Se estimula a los estudiantes a pensar sobre el mundo en que viven, en lo conocido, lo desconocido, inclusive pensar en lo misterios, sin temor a ser juzgados por su ignorancia, con lo que sin duda alguna obtendrá nuevos conocimientos. En el proceso de indagación se da la interacción multidisciplinaria con lo que se favorecen diferentes dimensiones en diversos contextos fortaleciendo así la adquisición del conocimiento. El profesor es parte de la dinámica, su propuesta no es la única, es cuestionable y comprobable, en una palabra no existe el profesor perfecto sabelotodo en este paradigma. El objetivo de este paradigma es que los alumnos desarrollen sus capacidades reflexivas, que sean capaces de razonar por sí mismos  para que ejerzan un pensamiento crítico reflexivo con juicio propio. En este paradigma lo más importante no es la transmisión de información, si no los procesos que se dan durante la indagación.\\n Cuando la educación tiene como objetivo educar para la creatividad, habrá que poner atención en conjugar armoniosamente los aspectos teóricos con los estéticos, ya que lo estético tiene gran relevancia en el desarrollo del talento creativo de los estudiantes. Para educar en la creatividad es necesario que el individuo tenga experiencias que le permitan percibir el significado, haga uso de analogías, metáforas, practique el juego imaginativo y actividades sensoriales. Según algunos estudios, la intuición puede fomentarse, adquirirse e incrementarse a través de la práctica de la transferencia mirando y solucionando el problema desde varios puntos de vista y ambientes (Carabús, 2004).\\n Elementos que influyen en las personas creativas \\n Según Guilford (citado en Mayer, 1983), la creatividad en los individuos está  relacionada con tres elementos: la fluencia, la flexibilidad y la originalidad. La fluencia consiste en la capacidad del individuo de responder con variedad de opciones ante una situación o circunstancia. La flexibilidad se refiere a la capacidad de abordar el problema desde diferentes puntos de vista y utilizar diferentes estrategias para darle solución. La originalidad tiene que ver con la capacidad de innovar, salirse de los estándares proponiendo nuevas soluciones.\\n A mediados de los años setenta, a través de diversas investigaciones se pudo evidenciar que la creatividad está estrechamente ligada a varios aspectos, como son la motivación, la competencia y el medio que rodea al individuo (Hennessey, 2003).\\n Según Csickszentmihalyi (2000), hay algunos factores que ayudan al desarrollo de la creatividad en el individuo, pero el principal factor es la atención voluntaria y consciente que cada individuo realiza para innovar. Uno de los factores es conservar el interés y curiosidad, poniendo atención en los pequeños detalles sin perder la capacidad de asombro. Hacer crecer el fluir en el diario vivir, marcándose objetivos diarios a alcanzar, provocando así en el individuo satisfacción y confianza, para luego elevar el nivel del reto.\\n La consistencia, es un factor importante para alcanzar el éxito, la constancia y la administración efectiva del tiempo, sin duda alguna permitirán alcanzar los objetivos trazados. También es importante crear un ambiente propicio, relajado, donde el individuo se sienta feliz y cómodo. Un factor más es el carácter y la personalidad por tal motivo la introspección debe practicarse con frecuencia, analizando y reconociendo sus debilidades tomando las medidas necesarias para convertirlas en fortalezas (Csickszentmihalyi, 2000).\\n Para aplicar la capacidad creativa práctica y con eficacia, un factor definitivo es la productividad sin la cual de nada serviría ser creativo. Otro factor que influye en las personas creativas es la inconformidad, éstas pueden ver el problema desde diferentes puntos de vista, están abiertas a nuevas opciones, son flexibles y audaces para tomar nuevos caminos para solucionar un problema. La utilización continua del pensamiento divergente es otro factor indispensable en la producción de la creatividad. Las personas con una actitud creativa son un factor de cambio en su entorno, debido a que constantemente están innovando, esto beneficia su mundo inmediato (Csickszentmihalyi, 2000).\\n Según Sternberg y Lubart (citado en Bernabeu y Goldstein, 2009), sostienen que existen tres aspectos relevantes para descifrar o entender la creatividad, éstos son la capacidad de síntesis, análisis y la pragmática. En cuanto a la capacidad de síntesis se refiere, es la habilidad de producir ideas originales y efectivas. \\n Los elementos que influyen en las personas creativas son varios, según Runco (1998), la herencia genética, el potencial creativo, la madurez, la motivación, el nivel de talento creativo, la educación, el entorno y el estado de ánimo.\\n Por otro lado Gardner (2005) menciona el tipo de inteligencia que tenga el individuo influirá en su creatividad, ya que este será más creativo en la inteligencia que mejor fluya, aunque también podrá serlo en algunas otras. El mismo autor sostiene que según sea las inteligencias en las que mejor se desenvuelva el sujeto, este podrá desarrollar mejor algunos trabajos, oficios o profesiones. Por ejemplo si predomina la inteligencia lingüística, éste podrá desarrollarse como abogado, poeta, escritor o bien orador. Si es kinestésico será un buen bailarín o deportista. Si tiene inteligencia lógico matemática, puede desempeñarse como científico, contador, matemático o ingeniero y así en cada una de las inteligencias (Gardner, 2001).\\n Desde tiempo atrás se ha hablado de la dominancia cerebral. Estudiosos como Broca, Hughlins y Sperry, han aportado sus teorías, observaciones y estudios que han realizado sobre este tema. Estos autores sostienen que uno de los hemisferios cerebrales es más dominante que otro, pero son igualmente importantes y tienen características con las cuales se complementan uno al otro. Mientras que el hemisferio izquierdo es lineal, racional, secuencial y analítico. El hemisferio derecho es intuitivo, imaginativo, flexible y tiene la capacidad de percibir las cosas holísticamente, por tal motivo se le ha relacionado fuertemente con la capacidad creativa del individuo, siendo así que los que tienen una dominancia hemisférica derecha pueden fluir en la creatividad. La explicación fisiológica es debido a que este hemisferio tiene más materia blanca y logra hacer mejores conexiones neuronales (Cruz, 2005).\\n El pensamiento creativo\\n El pensamiento creativo es la adquisición de un conocimiento específico, con connotaciones cognitivas, éste cuenta con los elementos de la originalidad, los cuales son flexibilidad, plasticidad y fluidez. Este conocimiento es utilizado por el individuo como estrategia o mecanismo cognitivo en la resolución de problemas, provocando así la construcción del propio aprendizaje. Este tipo de pensamiento es innovador. Según Parnés el pensamiento creativo es una habilidad enseñable (Freiría, 2004).\\n Guilford identificó dos clases de pensamiento, el convergente, el cual es lineal, éste no ofrece opciones si no que se centra en una única respuesta y el divergente, el cual es flexible y original, ya que puede reconocer varias soluciones y estrategias para resolver el mismo problema o situación. Por lo tanto la creatividad está muy ligada con el pensamiento divergente (Mayer, 1983).\\n Por otro lado Sternberg (2003) opina que para tener un pensamiento creativo, basta con tomar la decisión de querer tenerlo, pensar lo 'impensable', en lo que otros no habían  considerado, estar dispuesto a aprender no importando cuanta experiencia se tenga, ser tolerante, aceptar la innovación, tener autoconfianza, ser abierto a la diversidad de opiniones aún cuando no se esté de acuerdo y tener la capacidad de aceptar que siempre hay alguien que puede tener mejores ideas. En fin, la persona que tiene un pensamiento creativo tiene que ser valiente y tener convicciones ya que mucha gente se opone a las nuevas propuestas. \\n El pensamiento de orden superior, según Lipman (1998), está formado por dos ejes principales, uno está constituido por los criterios, y el otro eje por los valores inmersos en el contexto en el cual se genera el pensamiento. El pensamiento de orden superior es la percepción y la interacción de dos diferentes maneras de conducta mental, una tiene connotación racional o crítica y la otra creativa. En resumen está compuesto por el pensamiento crítico, el cual abarca la razón y el juicio. El otro componente es el pensamiento creativo en el cual se albergan el arte, las destrezas y el juicio creativo.\\n Según Bernstein y Bernstein (2002) el pensamiento creativo comienza en el ámbito sensorial, pero además existen varios mecanismos cognitivos que forman parte de la producción creativa. Estos son: la observación, atender conscientemente lo que percibimos sensorialmente. La imaginación consiste en revivir y representar dichas sensaciones. La abstracción se refiere a construcciones mentales por medio de las cuales el individuo rescata lo esencial conscientemente y lo simple lo asume inconscientemente.\\n La formación de pautas, es el resultado de combinar dos o más componentes estructurales lo cual deriva en la formación de una nueva pauta. La analogía es la capacidad de establecer semejanzas entre dos estructuras diferentes, por lo que varios autores la consideran un componente indispensable del pensamiento creativo. El reconocimiento de pautas, es el momento en que se generan nuevas expectativas a partir de principios generales de percepción para después transferirlas a nuevas experiencias. 'El pensamiento corporal depende de la sensación del movimiento corporal, de la postura, del equilibrio y del tacto, en suma de la propiocepción', estableciendo así una relación entre la imaginación corporal y el pensamiento creativo (Bernstein y Bernstein, 2002, p. 198).\\n Producir buenas ideas y soluciones creativas a los problemas puede convertirse en  un hábito, para ello deben observarse algunos principios, según menciona Cerda (2006):\\n uicio diferido: no emitir juicio alguno en cuanto a las ideas generadas, dejando que la imaginación sea liberada.\\n Registro de ideas: dar la importancia debida a todas las propuestas y hacer un registro de ellas.\\n Información: consultar y allegarse de información útil y de vanguardia. \\n Combinación: mezclar propuestas e ideas con el fin de encontrar la mejor, más eficaz y novedosa.\\n Analogías: establecer semejanzas y similitudes entre diferentes situaciones y relacionarlas entre sí, sin duda ayudará a solucionar problemas similares.\\n De Bono es otro importante estudioso del pensamiento creador, él menciona dos tipos de pensamiento, el vertical y el lateral. El primero es un pensamiento lógico, lineal, secuencial, predecible, selectivo, específico y analítico donde no hay cabida al error y el resultado es de suma importancia. Otra característica que tiene este tipo de pensamiento es que la categorización es inflexible y permanente. En cambio el pensamiento lateral es creador, provocativo, la secuencia no tiene relevancia, permite el margen de error, contempla variedad de procesos para llegar a un fin o resultado, acepta la relación de diversos temas, la categorización es contextual y por lo tanto flexible. El pensamiento lateral es arriesgado, innovador y puede llegar a varias soluciones por lo que el resultado no es específico. El fin del pensamiento lateral es provocar una reordenación en los modelos conceptuales (De Bono, 1970).\\n Este autor, hace referencia a dos formas de pensamiento dentro del pensamiento lateral, el retrospectivo y el progresivo. El retrospectivo tiene que ver con el proceso y el progresivo con la innovación, pero ambos juegan un importante papel en la modificación y refinamiento de los conceptos existentes.\\n En el proceso creativo, intervienen diversos factores, y según Wallas el pensamiento creativo consta de cuatro fases. El proceso creativo no es producto de la casualidad sino que es un proceso cognitivo, tal como se explica en la figura 1.\\n Oech (citado en Cerda, 2006), sostuvo la esencia del proceso creativo de Wallas 1946, pero éste reconoció las siguientes siete etapas: motivación, etapa de interés y aspiración. Búsqueda, etapa exploratoria y visionaria. Manipulación, etapa donde se moldea y emplea la información sin prejuicios. Incubación, etapa en la que inconscientemente se va formando o encontrando una solución al problema. Iluminación, en esta etapa es donde las ideas se aclaran y se da el chispazo de creatividad. Estas primeras cinco etapas forman parte de lo que Oech llama fase germinal o sea donde germinan y crecen las ideas. Las etapas restantes son: evaluación, etapa donde se evalúan y valoran la viabilidad de las ideas y por último la acción, etapa en la cual el proceso creativo es concretado y arroja un resultado. Estas dos forman la fase práctica, en la cual las ideas generadas en la fase anterior son valoradas, probadas y puestas en práctica. \\n Aunque no todos los investigadores están de acuerdo con la organización del proceso creativo propuesto por Wallas como por Oech, aceptan que por medio de éste se pueden conocer algunas características y peculiaridades de la identidad creadora. Pero  argumentan que el proceso creativo es individual y específico por lo que no se puede generalizar (Cerda, 2006).\\n Aprendizaje y creatividad\\n Como ya se ha mencionado anteriormente el aprendizaje que por años se promovió en las instituciones educativas en México, ha sido meramente convergente, carente de reflexión, dejando por un lado el pensamiento crítico reflexivo. En la actualidad se está pugnando que la educación sea través del desarrollo de competencias, donde los individuos además de adquirir conocimientos, desarrollen habilidades y actitudes para la resolución de problemas, la cual sea una educación para la vida, al menos es lo que pretende la Reforma integral para la educación básica (RIEB).\\n El aprendizaje creativo o también llamado aprendizaje por descubrimiento o constructivo, se refiere a la adquisición de aprendizajes significativos. La creatividad es posible debido a la libertad de transformación entre los esquemas cognitivos. Hoy en día el proceso de aprendizaje está dirigido a enseñar al individuo a 'aprender a aprender', donde el estudiante tiene una motivación intrínseca, por lo que el aprendizaje adquirido es permanente y trascendente (Claxton, citado en Freiría, 2004).\\n El proceso creativo sin duda alguna es un proceso cognitivo donde intervienen el conocimiento y la acción, donde la prueba y el error, son elementos importantes debido a la información que se puede obtener de ellos. Así que estos deben de ser estudiados y considerados ya que pueden ser valiosas aportaciones para dicho proceso (Cerda, 2006).\\n Autores como Guilford, Torrance, Marín, Gardner y Maslow entre otros, para  determinar si un producto o un comportamiento tienen carácter creativo deben ser utilizados varios indicadores de la creatividad. Entre estos indicadores están originalidad, invención o innovación, fluidez, flexibilidad, comunicación, solución de problemas, apreciación de lo nuevo, curiosidad y motivación, productividad y emergencia, imaginación y fantasía, el estudiar estos indicadores facilitará el asimilar el proceso creativo (Cerda, 2006).\\n La originalidad consiste en la exclusividad del producto y que la idea o proceso sea inédito. No hay que perder de vista que la originalidad depende de algunos factores tales como, el contexto sociocultural, la edad y el momento histórico entre otros. Otro indicador es la invención e innovación. Invención es la capacidad que tiene el ser humano de producir o crear cosas que no existían. Innovar en cambio, es utilizar lo ya existente para algo nuevo y diferente o bien en un contexto diferente al tradicionalmente utilizado. Los inventos pueden ser científicos, culturales, sociales o artísticos. Dentro del campo de la educación la innovación se refiere a solucionar problemas antiguos con soluciones actuales, utilizando nuevas estrategias (Cerda, 2006).\\n La fluidez es la capacidad de producir sin mucho esfuerzo, con naturalidad y elocuencia. Otro indicador es la flexibilidad, esto es la habilidad de adaptación y transformación que se tiene para hacer modificaciones y así mudarse a lo nuevo. Uno más es la comunicación, consiste en la forma que el individuo publicará sus creaciones tanto en la comunidad científica y al resto de la sociedad. La capacidad de solucionar eficazmente problemas específicos. La elaboración es el transformar uno o varios materiales a través de un procedimiento preconcebido en un producto final (Cerda, 2006).\\n En cuanto a la apreciación de lo nuevo, este indicador tiene que ver con el contexto cultural y entorno, ya que lo 'nuevo' algo diferente que sale de lo conocido, depende si en ese ámbito o contexto lo es. Por lo general la curiosidad es el preámbulo al invento, es un motivador que lleva al individuo a explorar, indagar, observar, hacer hipótesis y experimentar. Sin duda alguna la curiosidad y la motivación son indispensables para el proceso de aprendizaje. La productividad es el resultado que arroja el proceso creador, se podría decir que es la concreción de las ideas o acciones. La imaginación es la capacidad que tiene el individuo de imaginar, crear, representar ideas, objetos o imágenes totalmente inexistentes para él (Cerda, 2006).\\n Koestler dio a conocer su teoría tripartita acerca de la creatividad en 1964. En la que supone que los campos creativos establecen correspondencia enlazando lo científico con lo creativo y la innovación cómica. Sostiene que la creatividad es un proceso mental, al cual nombró bisociación, dicho proceso tiene dos fases, la primera disociar o sea pensar cosas fuera de lo cotidiano o inusual. La segunda asociar es establecer relaciones entre objetos, hechos y contextos que aparentemente no tienen mucho que ver o poco tienen en común (Bernabeu y Goldstein, 2009).\\n La creatividad debe considerarse como uno de los elementos primordiales en la educación hoy en día, el acto de crear además de divertido es sumamente benéfico, por lo tanto es necesario encauzar a los alumnos para que tengan una actitud creativa. Para lograrlo es importante provocar en los alumnos el deseo de aprender constante y permanentemente. Fortalecer la creatividad a través del trabajo colaborativo, lo cual les servirá en lo futuro en el aspecto laboral. Utilizar la creatividad para que el alumno pueda construir un pensamiento divergente, crítico reflexivo. Tener una actitud creativa para diseñar actividades atractivas a través de las cuales se alcancen los objetivos de manera amena (Scaglia, 2004).\\n Los estudiantes prefieren aprender a través de actividades novedosas, que les  represente un reto, en las cuales estén expectantes de lo que va a pasar o de lo que van a aprender.\\n  El profesor creativo\\n El profesor ha existido desde tiempos ancestrales y según el diccionario de la Real Academia Española (2001), un profesor es 'persona que ejerce o enseñan una ciencia o arte'. Sin duda alguna esta definición se queda corta, ya que un profesor no sólo enseña una ciencia o un arte, además facilita la adquisición y construcción del conocimiento. Es una persona que comparte su vida y conocimientos con otros, que transmite su actitud y emociones a sus pupilos, que en muchas ocasiones actúa como un'padre' o una 'madre'. Hay infinidad de testimonios de personas que declaran que sus vidas fueron cambiadas o transformadas gracias a sus maestros.\\n Según Mendoza (2001), la creatividad es un elemento de la personalidad, por lo anterior el profesor creativo debe tener varios aspectos característicos para definirlo como tal. Primeramente el docente debe de estar motivado intrínsecamente para realizar su labor, de tal modo que la motivación se combine con lo afectivo y realice efectivamente su intervención educativa. El profesor creativo debe ser flexible y activo, no conformarse con la práctica tradicional, sino que siempre este reflexionando en busca de la transformación, de la solución práctica de los problemas, debe ocuparse de diseñar estrategias que les permitan tanto a él como a sus alumnos considerar diferentes posibilidades de resolución o acción para determinada situación. El profesor creativo, está abierto a aprender nuevas formas y aún si se requiere a cambiar su punto de vista.\\n Una característica indispensable en el profesor creativo mencionada por Mendoza (2001), es la autoconfianza, debe ser una persona con la capacidad de autoevaluarse continuamente, reconociendo sus fortalezas y ventanas de oportunidad. Haciendo esta reflexión, el docente podrá reconocer las áreas y aspectos donde necesita mejorar y podrá determinar cuáles son las medidas que debe tomar para construirse así mismo. Debe de ser una persona tan segura de sí mismo, que no se sienta amenazada por las circunstancias, los retos o por sus compañeros. No debe temerle a los cambios, y siendo consciente de sus debilidades sea capaz de allegarse las herramientas, los elementos, las habilidades y capacidades para transformase en un profesor más creativo que constantemente esté innovando y provocando este mismo sentir en sus alumnos.\\n Otra característica no menos importante en el profesor creativo es que debe tener sentido del humor. Por otro lado la persona creativa tiene aptitudes distintivas tales como, la elocuencia, la capacidad de toma de decisiones, puede mirarse así misma objetivamente, está abierta a nuevas propuestas, y concibe alegorías con facilidad (Bernabeu y Goldstein, 2009).\\n Según Betancourt (2007), el profesor creativo debe ser un facilitador del aprendizaje más que un protagonista de este y deberá cumplir con varias funciones para propiciar un aprendizaje para la creatividad.\\n  Dar la importancia debida a cada una de las aportaciones de sus alumnos.\\n Propiciar una comunidad dialéctica de intercambio.\\n Establecer una ambiente de intercambio.\\n Respetar a cada individuo sin prejuicios. \\n Motivar a los alumnos a la reflexión de sus actos.\\n Promover la participación de los estudiantes.\\n Diseñar actividades con carácter abierto.\\n Guiar a los alumnos a que lleven a cabo el método científico en las diferentes actividades realizadas.\\n Sus estrategias de intervención deberán cubrir las necesidades de todos y cada uno de sus alumnos.\\n Inculcar valores universales en los alumnos. Después de conocer diferentes programas para la promoción de la creatividad en los estudiantes, Torrance sostuvo que estos nunca serán efectivos, si el docente no está comprometido con el desarrollo de dicha habilidad en sus alumnos. Por lo tanto es imprescindible que el profesor tenga conocimiento de la naturaleza de la creatividad y pueda desarrollar un pensamiento creativo primeramente en su persona para después modelarlo a sus pupilos (Mayers, 1983).\\n Por lo tanto es importante que el profesor este enterado de cuáles son los factores que le coartan la creatividad y así pueda quitar del camino los aspectos o circunstancias que frenan el desarrollo de habilidades creativas en sus alumnos. Entre más comprensión tenga el profesor del concepto de la creatividad y cómo se puede promover en los individuos, mejores resultados tendrá en que sus alumnos adquieran esta habilidad (Ward 2007).\\n Así que es indispensable que los profesores del siglo XXI, estén seriamente comprometidos con educar a los estudiantes de una nueva manera, preparados para cualquier reto que puedan enfrentar, que además de ser personas con altos valores, también sean individuos capaces de tener una mente abierta, que sean flexibles, dispuestos a cambiar de punto de vista, mirar las situaciones desde diferentes perspectivas y puedan salir victoriosos de los retos enfrentados, no rindiéndose ante las circunstancias adversas.\\n Factor cultural en el desarrollo de la innovación y creatividad\\n Según Rodríguez (citado por Cerda, 2006), existen diferencias entre la creatividad del pueblo anglosajón y el pueblo latino. El autor considera que el origen de estas diferencias radica en la concreción del producto, ya que a pesar de que el pueblo latino tiene una gran capacidad creativa, no tiene la capacidad de trabajar, transformar y comunicar las ideas. La mayoría de las veces esa gran capacidad se queda sólo en el proceso, sin llegar a una producción eficaz.\\n En cambio aunque el pueblo anglosajón carece de la frescura y espontaneidad del latino, es eficaz en concretar el producto, ya que es disciplinado, perseverante, objetivo, esforzado y metódico, entre otras características. Rodríguez basó su observación en la estadística de los premios Nobel y sugiere que las diferencias en la capacidad creativa entre los pueblos, no sólo es genética o racial, sino que también el factor ambiental y cultural son definitivos en la capacidad creativa de cada pueblo (Cerda 2006). \\n Sin lugar a dudas el factor cultural es un aspecto de gran relevancia en el desarrollo de la motivación y la creatividad. Son tres los entornos principales donde esta puede ser detonada o promovida por su gran carga cognoscitiva, el familiar, escolar y social (Mendoza, 2001).\\n Entorno Familiar\\n El entorno familiar juega un papel definitivo ya que las habilidades creadoras en el individuo pueden comenzar a promoverse desde la temprana edad, o en su defecto dejar de hacerlo y privar al infante de un cúmulo de oportunidades para que se convierta en un ser creativo\\n Además, las habilidades creativas están íntimamente ligadas con lo afectivo, y en la gran mayoría de los casos el hogar es en donde primeramente se desarrolla la afectividad del individuo.\\n Según Rodríguez y Ketchum (1995), en distintas investigaciones realizadas con niños, se ha podido observar que los individuos creativos gozan de un ambiente confortable en casa, donde los progenitores son desenvueltos, alegres, actúan de manera natural y estos dan al pequeño la misma libertad de acción. También se ha podido observar que los niños creativos, generalmente tienen padres creativos y esto no en referencia a lo artístico, sino al diario vivir. Los padres pueden promover la creatividad en sus hijos a través de permitirles solucionar problemas cotidianos, o través de juegos, entre otras muchas acciones.\\n Una particularidad que se notó en los padres de niños con mayor grado de creatividad, es que estos son sumamente originales, no les gusta ser como todos los demás, luchan por su identidad, por ser únicos y especiales, de tal modo que este sentir es inculcado en el niño, que a su vez comparte con sus padres el orgullo de ser distinto, único y especial (Rodríguez y Ketchum 1995).\\n Tomando en cuenta lo anterior, es el hogar donde el niño aprenderá a apreciar su habilidad creativa como un rasgo individual, que lo anime a desarrollarla y diversificarla o en su defecto a inhibirla por falta de aceptación o en el peor de los casos la desechará por temor al juicio, a la crítica y nunca más se ocupe de desarrollarla. Perdiendo con esto muchas oportunidades de realización tanto personal como profesionalmente.\\n Entorno escolar\\n Es muy triste pensar que actualmente en México, en ocasiones la educación formal inhibe la creatividad, debido a que generalmente las escuelas no cuentan con el currículo adecuado para la promoción de esta. En su lugar los objetivos que se persiguen en los programas curriculares son meramente conceptuales, basado en la evaluación cuantitativa y no en el desarrollo de competencias que promuevan el pensamiento divergente.\\n Desafortunadamente no sólo en México fue así, en muchos otros países por años como bien menciona Lipman (1998) las universidades o escuelas normalistas formadoras de futuros profesores, que se ocupaban mayormente de transmitir la mayor cantidad de conocimientos posibles a sus aspirantes. Equivocadamente se creía que entre más conocimiento tuvieran, mejores resultados obtendrían en su intervención docente, reproduciendo en sus alumnos este mismo perfil llenándolos de conocimientos, esto se traducía como buena educación.\\n Hoy en día las instituciones educativas formadoras de docentes han tomado conciencia de la importancia del cambio en el perfil docente, y han modificado sus currículos con el fin de que éste sea un profesionista mejor preparado y con una nueva concepción de la educación. La que va más allá del conocimiento, donde las actitudes y valores tienen la misma importancia que lo cognitivo.\\n La escuela es un campo fértil para la promoción de procesos cognitivos, es el templo del conocimiento, donde los alumnos son expuestos a información de todo tipo con la cual deberán construir su propio aprendizaje. Pero también es un espacio que les ofrece un cúmulo de experiencias, los pupilos pueden desarrollar habilidades y adquirir destrezas. Donde los valores y sentimientos son importantes y forman parte del proceso de aprendizaje. Un espacio donde pueden convivir con tranquilidad, al igual que disfrutar, reír, divertirse o bien compartir sus historias de vida con sus compañeros y maestros, y a través de esta interacción nutrirse los unos a los otros.\\n Algunos de los factores que pueden favorecer el desarrollo de la creatividad en el entorno escolar según Betancourt (2007) son, tomar en cuenta la correspondencia que tiene el aprendiz con su entorno, ya que esto es de suma importancia. La relación entre lo cognitivo y lo afectivo debe ser equilibrada, de modo que pueda desarrollarse en la misma medida el pensar como el crear. No debe dársele más valor a los resultados, ya que el proceso es tan valioso como estos. El darle una connotación positiva al error, quitándole la etiqueta de fracaso y poniéndole la de oportunidad de aprendizaje.\\n Este autor también menciona la importancia de promover o inculcar valores universales ya que están íntimamente ligados a la creatividad, algunos valores son determinantes en el proceso creativo, tales como tolerancia, perseverancia, respeto, entre otros. Otro factor que favorece ampliamente la creatividad son las actividades lúdicas, en el juego intervienen elementos afectivos y cognitivos además de habilidades sociales y en ocasiones la imaginación. Durante los momentos lúdicos los estudiantes están sumamente motivados y se sienten felices, además de que están aprendiendo y desarrollando habilidades, por lo tanto es un medio propicio para la promoción de la creatividad.\\n El docente es un factor determinante en el entorno escolar, ya que de este depende que el aula sea un ambiente favorable para la promoción de la creatividad en los alumnos. También de ser él mismo un modelo de esta para sus pupilos. Por lo tanto deberá tener una actitud creadora, propiciar un ambiente de confianza donde los alumnos tengan la libertad para expresarse sin temor a ser juzgados o burlados (Betancourt, 2007).\\n Para crear un ambiente conveniente para desarrollar la creatividad en los niños, aún los pequeños detalles son importantes, los olores, sonidos, iluminación, la temperatura, que el lugar este limpio y que sea agradable aún para la vista. Para estar motivado el alumno debe sentirse cómodo.\\n  Entorno social \\n En ocasiones los factores culturales pueden ser el freno al desarrollo de la creatividad, más en las sociedades tradicionalistas donde no hay voluntad de cambio o temor a lo desconocido, esta se va inhibiendo.\\n Culturalmente el error se ha manejado como un fracaso, o algo vergonzoso, socialmente se pueden leer algunos lemas, 'el que se equivoca pierde', 'prohibido equivocarse', 'si te equivocas eres un perdedor', etc. Como sociedad se ha caminado con ese estigma durante muchas generaciones y tal vez lleve otras tantas para modificarlo, quitando la pesada carga que la misma sociedad se ha puesto. El temor a cometer errores es en gran parte uno de los obstáculos para desarrollar la creatividad pues como se dice en la cultura mexicana, 'más vale malo conocido, que bueno por conocer'. Sin duda a la sociedad mexicana no pocos paradigmas son la que la tienen atada y le impiden potenciar y concretizar ese ingenio que la caracteriza.\\n A lo anterior se puede agregar lo que Gardner (2005) comentaba de los grandes inventores, que algunos de ellos en su momento tuvieron que enfrentar rechazo de la sociedad, familia y círculos más cercanos, debido a sus ideas, las cuales diferían de lo tradicional, conocido o aceptado hasta ese momento.\\n Rodríguez y Ketchum (1995), sostienen que la capacidad creativa de un pueblo está íntimamente ligada con el nivel de creatividad que tienen los juegos infantiles. Si se cultiva la creatividad en los niños, se tendrá una sociedad creativa, la cual será capaz de respetar la espontaneidad y sinceridad.\\n Tomando en cuenta las observaciones hechas tanto por Gardner (2005), como por Rodríguez y Ketchum (1995), es inminente que la sociedad tendrá que cambiar drásticamente su perspectiva en cuanto a la creatividad y la importancia que esto tiene a nivel social. Por lo que deberá ser más abierta, recibir las nuevas propuestas y en su defecto adoptarlas si estas representan mejoras y beneficios sociales. Dejando atrás los sentimientos tradicionalistas. Todo esto si quiere transformarse en una sociedad más productiva y que esté a la vanguardia a nivel internacional.\\n Socioculturalmente la creatividad se desarrollará en contextos donde sea tolerada, aceptada, valorada, reconocida y por qué no hasta premiada (Runco, 1998). Esta proliferará en sociedades maduras, las cuales estén abiertas al cambio, a la diversidad, dispuestas a romper con paradigmas y a evolucionar.\\n Herramientas y métodos que fomentan la creatividad\\n Sin duda alguna la mejor etapa para fomentar y desarrollar la capacidad creativa es durante la infancia, momento en que los niños son curiosos y exploradores por naturaleza, la imaginación es parte de su vida cotidiana, no diciendo con esto que los adultos no puedan desarrollarla, solo que en los niños en esta etapa la creatividad es inherente.\\n Según Gardner (2005), una forma de fomentar la creatividad en los niños es a través de las actividades artísticas, donde los niños pueden utilizar su imaginación, innovando y utilizando diferentes formas de expresión artística. Aprovechando la etapa infantil donde el niño es acrítico y no tiene miedo al juicio.\\n Desde los años treinta, Crawford fue quien inició con la enseñanza de creatividad a nivel empresarial, su método 'Listado de atributos', consiste en hacer un listado de las cualidades del producto, para después mejorarlas haciendo innovaciones y transferir dichas cualidades a otros productos (Mayer, 1983).\\n Otro método es el de 'sugerencias de buenas ideas' o mejor conocido como brainstorming de Osborn, el cual es utilizado a partir de los años cuarenta. Este método consiste en solucionar los problemas en grupo. Para tal objetivo Osborn estableció algunas reglas, a) no se vale criticar las ideas aportadas, b) entre mayor sea la cantidad de ideas mejor, c) aportar ideas originales no importando cuan descabelladas sean, d) combinar las ideas y utilizarlas para el mejoramiento y solución de problema. Gordon, propuso el método de la 'sinética' que consiste en juntar componentes para solucionar problemas, los cuales supuestamente no tienen relación alguna entre sí, ya que el propósito es que las personas sean capaces de resolver problemas utilizando analogías (Mayer, 1983).\\n El programa de pensamiento productivo propuesto por Convington y otros autores (citados en Tapia, 1986), pretendía incrementar las habilidades de los estudiantes en la resolución de problemas, esto a través de la utilización de historietas. El método consistía en efectuar varios pasos: generación de ideas, innovación de ideas, variedad de soluciones, enfrentamiento del problema de modo sistemático, persistir hasta proponer o encontrar la solución, utilizar gráficos en caso de requerirlos, ir de lo general a lo específico, reunir evidencias, visualizar claramente el problema y utilizar la imaginación.\\n Otro programa para la resolución de problemas científicos 'Entrenamiento para la investigación', fue diseñado por Suchman. Este consistía en sesiones de una hora en la cual había tres fases. En la primera se presentaba el problema a través de un corto mudo. En la segunda fase los alumnos podían hacer todas las preguntas con respeto al filme, pero el maestro sólo contestaba afirmativa o negativamente. En la tercera etapa el profesor evaluaba las técnicas y las preguntas hechas por los alumnos, en ocasiones grababa las sesiones con el fin de guiar a los alumnos a mejor su estrategia de indagación (Sharma, 2005).\\n Otra técnica para propiciar la creatividad en los alumnos es la 'Enseñanza basada en habilidades de investigación', propuesta por dos famosos autores, Torrance y Mayers. Esta técnica está orientada a que los estudiantes aprendan practicando el método científico, por medio del cual formulen y comprueben sus hipótesis (Sharma, 2005).\\n La lectura creativa es otro método utilizado para el desarrollo de la creatividad, este fue presentado por Torrance y Harmon, los cuales argumentaban que los alumnos podían aprender a resolver problemas a través de esta metodología. La cual consistía en dividir el grupo por mitad, a una parte de la clase se le pedía que leyera la selección críticamente, estos señalarían los errores y cosas negativas, y simplemente estudiarían lo propuesto por el autor. A la otra mitad se le indicaba que leyera la selección de manera creativa, pesando como podía mejorar lo propuesto por el autor, aportar nuevas soluciones, aportar nuevas conclusiones, etc., (Sharma, 2005).\\n Michalko (1991), expone un sin número de actividades lúdicas y detonadoras del pensamiento creativo, tales como el registro de buenas ideas, método utilizado por la CIA, 'Máscaras', donde se lleva a cabo la inversión de ideas. 'La división de la cereza', fraccionando el problema a soluciones diferentes las cuales después pueden ser una manera novedosa de solucionar dicho problema.\\n Rodríguez (2005) habla de dos tipos de inteligencia, la receptiva y la productiva. La inteligencia receptiva es aquella que solo se limita a aprender y a memorizar, no es trascendente y permanece en el pasado, en cambio la productiva, inventa, visualiza, va más allá del objetivo, no es temporal y va estableciendo cimientos sólidos. Utilizar la inteligencia productiva, conlleva a la promoción de la creatividad. \\n Rodríguez y Ketchum (1995) sugieren que una herramienta que fomenta la capacidad creativa de los individuos son los juegos. Estos autores sostienen que la creatividad está más relacionada con el juego que con el trabajo, ya que ésta del mismo modo que el juego, es una conducta exploratoria. En el juego hay espacio para 'ser' y al igual que la creatividad nace de adentro del individuo y luego se proyecta al exterior. En el juego 'todo es posible', 'todo se vale', por lo que en este sentido comulga con la creatividad. Rodríguez y Ketchum realizaron una tabla comparativa entre los elementos del juego y de la creatividad (ver tabla 1).\\n Torre (2008), desde la perspectiva cuántica sugiere que para promover la creatividad, habría que desarrollar más la conciencia y la relación cuerpo mente. Ponderar las intenciones, los deseos, los pensamientos y expresiones constructivas, aplicar la programación neurolingüística y fomentar una buena autoimagen. Echar mano de las creencias que son factores de creatividad transformadora. Enseñar a los alumnos a relajarse, concentrarse en la tarea y a meditar para que sean más creativos.\\n Torrance a través de sus investigaciones ha constatado que Japón es el país más creativo, ya que es el que cuenta con mayores patentes registradas, novelas escritas, además de contar con músicos y deportistas talentosos. Este autor se dio a la tarea de investigar cuáles eran los métodos que empleaba este país para lograr que su sociedad tuviera un perfil creativo. Entre las cosas que descubrió fue que 1979 el primer ministro Ohira lazó una convocatoria a toda la sociedad, desde los hogares hasta las industrias retándolos a fomentar la creatividad individual, a lo que se le llamó 'The long look' o 'mirada a largo plazo' en español, esto con el fin de que la sociedad Japonesa estuviera a la altura de los retos que exigía la nueva etapa mundial, no solo pensando en el presente si no también en el porvenir (Torrance, 2008).\\n Este autor, también pudo observar que en los preescolares japoneses son altamente promovidas las habilidades musicales, artísticas, la dramatización así como las habilidades sociales, sin menospreciar la creatividad expresiva y la solución de problemas. Otro factor interesante que observó, es que en Japón la creatividad es reconocida y galardonada, con lo cual los individuos se sienten altamente motivados.\\n Además de la importancia que este pueblo le da al pensamiento intuitivo, pudo constatar que los japoneses son sumamente persistentes y disciplinados. Practican el aprendizaje auto-dirigido, pero también trabajan colaborativamente en grupos de estudio, y resolución de problemas, donde comparten sus conocimientos, enriqueciéndose los unos a los otros. Son solidarios y aunque es un país con muchas tradiciones son libres pensadores, lo cual les permite innovar, inventar o bien modificar estructuras. Con todo esto Japón ha logrado establecer culturalmente un ambiente creativo donde todos los sectores están involucrados (Torrance 2008).\\n Según Penagos y Aluni (2000) existen varias condiciones las cuales pueden favorecer y potenciar las técnicas para el desarrollo de la creatividad. La primera es el individuo, debe poseer la habilidad y capacidad de identificar o plantear problemas novedosos, los cuales sean resueltos eficaz y prácticamente, muchas técnicas para el desarrollo de la creatividad están basadas en esta dinámica.\\n Otra condición importante es la motivación intrínseca que mueve al individuo a ser tenaz y persistente, a seguir adelante a pesar de los 'fracasos', lo cual implica en ocasiones un largo proceso hasta lograr el producto. La tercera condición para el desarrollo de la creatividad está basada en el postulado de Gardner (1988), el cual dice que cada individuo es creativo en diferentes áreas o bien en aspectos específicos. Entonces esta condición está enfocada a las habilidades, intereses y necesidades específicas de cada individuo, donde este ha de desarrollar su creatividad.\\n La cuarta condición relacionada con el aprendizaje y aproximaciones sucesivas, a través del reconocimiento y reforzamiento sistemático de una conducta o acción hasta lograr el comportamiento deseado. La quinta condición es el nivel o estado de conciencia del individuo frente a los cambios conceptuales y la percepción, ya que esto influye directa y favorablemente en la creatividad (Penagos y Aluni, 2000).\\n Un método eficaz para desarrollar o incrementar la creatividad en los adolescentes y adultos es la utilización de tácticas, las cuales están íntimamente ligadas con conocimientos procedimentales ya que las tácticas son acciones deliberadas. Pero también los conocimientos actitudinales juegan un papel importantísimo ya que el simple hecho de querer lograr una mejora depende de una actitud, según Runco (1999), algunas de las tácticas propuestas por Parnés son, 'deja que suceda', esta se trata de no estresarse por no obtener el resultado o la solución, si no dar su tiempo a la etapa de incubación y que a su tiempo aflore la nueva idea, parte de esta táctica es estar abierto al cambio y a descubrir cosas repentinamente, además implica confiar en la propia intuición. Otra se llama 'haz que suceda', esta táctica es más estructurada que la anterior e implica el seguimiento de algunos pasos, por ejemplo 'ir contra la corriente, pensar en lo que nadie más pensaría', en resumen actuar intencionalmente para obtener resultados diferentes.\\n Para obtener mejores resultados en el diseño de currículos y planes de estudio Bernabeu y Goldestein (2009), hacen una propuesta para fomentar la creatividad en los alumnos. En esta propuesta los autores identifican algunas acciones que deben llevarse a cabo para obtener mejores resultados en dicha tarea. Primeramente proponen que los maestros eviten ofrecer a sus alumnos actividades rutinarias y aburridas, en su lugar estas sean variadas, representen un reto para los estudiantes y sean dinámicas. Que se promuevan valores dentro del aula, para que la convivencia sea con respeto y equidad. Plantear problemas donde los estudiantes puedan poner en práctica su pensamiento crítico reflexivo, entablen discusiones, establezcan acuerdos y tomen sus propias decisiones.\\n Otras actividades que fomentan la creatividad dentro del aula propuestas por Bernabeu y Goldstein (2009), son propiciar actividades a través de las cuales los alumnos, pongan a trabajar su imaginación y la fantasía, desarrollen la intuición, el lenguaje creativo utilizando metáforas e inventando chistes, cuentos, canciones, etc. Por último sugieren la importancia de fomentar en ellos una actitud lúdica, donde los alumnos disfruten el aprendizaje a través de todos sus sentidos libremente. El ambiente deberá permitir la expresión de emociones y sentimientos, a lo cual el profesor deberá estar atento.\\n Michalko (1998) propone un estrategia la cual era utilizada por el famoso Da Vinci, esta estrategia consiste en 'saber ver', en otras palabras ver lo que no toda la gente ve, para lo cual hay que mirar un problema, objeto o situación de maneras distintas.\\n La técnica del desafío sin duda alguna fomenta la creatividad, en esta técnica se  formulan varias preguntas a las cuales habrá que darles respuestas. Quién, qué, donde, cuando, por qué y cómo. El contestar estas preguntas marcará la dirección que debe seguir para salir con éxito de este desafío (Michalko, 1998).\\n Después de que el error tenía una connotación negativa y que estaba prohibido, actualmente se ha reconocido que este puede servir como una gran herramienta para la creatividad si se aborda desde el punto de vista de oportunidad de aprendizaje y al no tenerle miedo posibilita que el individuo experimente sin ningún temor.\\n Michalko (1998) presenta una estrategia más para desarrollar la creatividad 'forma de encontrar lo que no se está buscando', está basada en los 'accidentes' creativos. Cuando se está tratando de inventar x cosa el producto resultante es y, por lo que sugiere que el creador deje por un lado su proyecto inicial y adopte el producido por accidente, en lugar de desecharlo o menospreciarlo.\\n Este mismo autor, sostiene que una herramienta efectiva en el fomento de la creatividad es el trabajo colaborativo, ya que a través de esta dinámica los participantes pueden combinar sus ideas y formar una nueva, o bien aportar sus conocimientos y habilidades. Tal como lo propone en su estrategia 'Como despertar el espíritu de colaboración', la cual está basada en los supuestos de Bohm. A través de esta los participantes construyen una comunidad de conocimiento, actitudes y habilidades. Apoyándose unos a otros trabajan por un mismo objetivo, ampliando sus propias perspectivas y de este modo, ser más efectivos en concretar el producto (Michalko, 1998).\\n Como se ha mencionado en los párrafos anteriores existen varias herramientas y estrategias para promover y desarrollar la creatividad, de modo que hay que implementarlas para alcanzar el objetivo eficazmente. 'El fomentar la creatividad es apostar por un futuro de progreso, de justicia, de tolerancia y de convivencia. Creatividad es sentipensar y hacer algo que repercuta en beneficio de los demás' (Torre, 2008, p. 14).\\n Factores que inhiben la creatividad\\n Así como hay métodos y herramientas que fomentan la creatividad, también existen factores que la inhiben, debilitan o en su defecto la aniquilan. Respaldadas por los muchos años de investigación Amabile y Hennessey (Hennessey 2003), llegaron a la conclusión que existen cinco factores aniquiladores de la creatividad: que el individuo este condicionado a un premio o recompensa, el temor a la evaluación, estar bajo monitoreo constante, los límites de tiempo y los concursos o entrar en competencia con otros.\\n Otro factor que no favorece el desarrollo de la creatividad, son los padres  autoritarios ya que no dan libertad de acción ni de decisión a los infantes (Rodríguez y Ketchum, 1995).\\n Por todo lo anteriormente mencionado, valdría la pena que tanto en el ámbito escolar, como en el familiar se realizara una evaluación, para conocer si las dinámicas que se están llevando a cabo en cada uno de estos contextos, fomentan o inhiben el desarrollo de la creatividad en los individuos",
            "Nivel":"0.9273244"
        },
        "justificacion":{
            "Tesis": "En el ámbito científico el manejo de la información en cuanto a referencias consultadas es amplio, por lo tanto el hecho de escribir una tesis para aprobar un grado requiere de sumo cuidado al momento de la redacción.\n La revisión y comparación del documento propio con los ya existentes dentro del Instituto Politécnico Nacional resulta una tarea monótona, debido a la inversión de tiempo, esfuerzo y recursos para tener la certeza de un trabajo pulcro y libre de algún tipo de plagio que lleve al autor a problemas jurídicos.\n Dada esta situación se tiene contemplado agilizar este proceso mediante la implementación de un software que sea capaz de identificar las citas, normas y formatos redactados en un documento para evaluar el contenido con el fin de servir como apoyo tanto para estudiantes como personal docente en las unidades académicas del instituto, sin la necesidad de pagar licencias para su uso.\n Haciendo que la elaboración del escrito para la tesis sea óptima y tenga una reducción significativa en la cantidad de plagio, lo que conlleva a la elevación de calidad de éste.",
            "Similitud": "Hoy en día, el ser humano se está enfrentado a una feroz competencia con la tecnología. En la cuestión laboral, cada vez más se requiere de personal mejor capacitado, que innove, que no tenga miedo al cambio y que proponga ideas frescas.\\n La Secretaría de Educación Pública (SEP) está preocupada por crear un nuevo perfil de egreso del estudiante al término de la educación básica, por lo que ha renovado su currículo y está implementando el programa por competencias Programa de Educación Preescolar 2004, el programa 2006 para secundaria y la nueva RIEB 2009, en toda la República Mexicana, las escuelas oficiales y particulares deben seguir los planes de estudio según la Ley General de Educación.\\n Este programa SEP (2009) se enfoca en promover cinco tipos de competencias las cuales son: competencias para el aprendizaje permanente, las cuales se refieren a la habilidad de autoconstruir el aprendizaje, el manejo del lenguaje escrito, a la transferencia de conocimientos culturales, sociales, lingüísticos, tecnológicos y científicos, para de esta forma interpretar la realidad. Las competencias para el manejo de la información, las cuales están vinculadas con el buscar, analizar, evaluar, seleccionar y estructurar información.\\n Estas competencias también están relacionadas con el pensamiento, la reflexión, la argumentación, la expresión critica, el análisis, la síntesis y la capacidad de compartir información.\\n Las competencias para la convivencia según SEP (2009) se refieren a la habilidad del individuo para relacionarse equilibradamente, tanto con la sociedad como con la naturaleza y comunicarse eficazmente, ser empático, solidario, respetuoso, que pueda tener buenas relaciones interpersonales, que desarrolle una buena autoimagen, que sea capaz de trabajar en equipo y colaborar para mejorar su comunidad y sociedad. Por otro lado las competencias para el manejo de soluciones implican, además de la capacidad de solucionar problemas, tomar decisiones asumiendo las consecuencias de estas, el manejo de la tolerancia a la frustración, tener iniciativa, administrar eficazmente el tiempo y llevar a cabo los proyectos emprendidos.\\n En cuanto a las competencias para la vida en sociedad, están vinculadas con el derecho a tener convicciones individuales, al libre albedrío, a los valores, pero respetando la diversidad ideológica, los derechos humanos, las normas socioculturales y la democracia.\\n Todo lo mencionado en los párrafos anteriores con el objetivo que los estudiantes desarrollen competencias para lo largo de la vida y al término de la educación básica, estos sean capaces de: utilizar correctamente el lenguaje oral y escrito, así mismo manejen a nivel básico una lengua además de la materna. Que identifique problemas, proponga soluciones, tome decisiones y los resuelva. Maneje la información de manera responsable. Que identifique y explique procesos en diferentes contextos y trabaje por el bien común. Que sea un individuo responsable, con valores y respetuoso de la ley y sus semejantes. Que identifique y valore su identidad personal y social, que sea promotor de la salud y del cuidado ambiental. Que pueda apreciar las bellas artes así como expresarse a través de ellas (SEP, 2009).\\n Por tal motivo es necesario que el docente esté capacitado y comprometido para guiar al estudiante a que desarrolle un pensamiento creativo, brindándole las herramientas necesarias para la resolución de problemas y fomentar en él una mente abierta a un sin fin de posibilidades, en otras palabras, que desarrolle un pensamiento divergente según Guilford (citado en Mayer, 1983).\\n Es importante aprovechar la etapa temprana en que los niños son creativos por naturaleza, no restándoles importancia por su corta edad, si no detectar las características de éstos para que la promoción de la creatividad sea más efectiva utilizando diseños instruccionales adecuados y novedosos.\\n La necesidad de mejorar la calidad educativa en el país es inminente, en este cambio los actores principales son los maestros, los cuales si modifican su perfil y práctica docente podrían marcar un parte aguas en la educación. Para esto será necesario que conozcan cuáles son las características de un profesor creativo, las aprendan y las desarrollen en su. persona para luego ponerlas en práctica en sus aulas.\\n Por lo antes mencionado, se considera que esta investigación es importante ya que puede a aportar valiosa información a la comunidad educativa para ofrecer una enseñanza creativa poniendo al descubierto los factores que favorecen el pensamiento divergente en los estudiantes. De esta forma los docentes puedan promoverlo eficazmente en cada uno de sus alumnos. Así como el crear conciencia de la importancia de promover y desarrollar un nuevo perfil docente.",
            "Nivel":"0.90398115"
        },
        "antecedentes":{
            "Tesis": "Estado del arte.\n El avance de la tecnología en estos años, junto al fácil y rápido acceso a Internet hace que ideas, opiniones, teorías, gráficos, dibujos, citas, documentos en formato digital, entre otros. Se encuentren disponibles para su uso en cualquier momento.La gran disponibilidad de documentos, ideas, imágenes, programas y todo tipo de material de Internet hace que el público en general esté más alerta y preocupado por la evaluación de documentos con derechos de autor\n Una rama para abordar la problemática es el uso de la minería de texto.\n La minería de texto se define como un proceso mediante el cual se busca patrones destacados y nuevos conocimientos en un conjunto de textos, es decir, es el proceso encargado de descubrir conocimientos que no existen en ningún texto del conjunto seleccionado.\n Un problema que aborda la minería de texto es el de procesamiento de lenguaje natural, por sus siglas en inglés (NLP)\n Las aportaciones que se han hecho desde el procesamiento de lenguaje natural han mejorado, permitiendo el procesamiento de ingentes cantidades de información en un formato aceptable\n Junto al avance del proceso de minería de texto es natural pensar en métodos novedosos apoyados de disciplinas que a la par han ido avanzado con el procesamiento de lenguaje natural,  por ejemplo el machine learning.\n Los inicios del machine learning los encontramos en los años 50s, cuando Arthur Samuel, pionero en el campo de los juegos informáticos e inteligencia artificial, escribió el primer programa de aprendizaje informático\n Tradicionalmente si alguien quería resolver un problema con la ayuda de un ordenador, tenía que diseñar  e implementar un algoritmo que especificara, hasta el más mínimo detalle, qué es lo que el ordenador tenía que hacer. Para algunos problemas, con multitud de casos particulares imposibles de prever, esta estrategia, simple y llanamente no funciona\n Las aplicaciones del procesamiento del lenguaje natural que abordaremos en esta investigación se enfocan en la búsqueda avanzada de información, que consiste en la detección y recuperación de la misma en coalición con  la detección de topics, similitudes o anomalías en los textos, gracias al análisis lingüístico podemos realizar más fácilmente una detección del plagio\n Comparación entre herramientas.\n Actualmente existen una gran variedad de herramientas enfocadas en la detección del plagio en los textos, todas estas con diferentes enfoques pero con la misma meta, aplicaciones como:\n Turnitin\n El software trabaja de manera simultánea en línea y almacena información de textos que fueron agregados con anterioridad. Básicamente es un archivo gigante donde todas las instituciones cuelgan los trabajos académicos, también se alimenta de información colgada en Internet\n Ninguna empresa cuenta con el 100% de acceso a la producción científica y académica. Además, no todos los contenidos están totalmente digitalizados o con sus textos en formato comparable. Desde PlagScan creen que se detecta el plagio en un 70% de las veces.El 30% restante se escapa\n Plagiarism checker de Prepostseo\n  El software analiza textos de 300 caracteres y puede constatar la originalidad; en caso de que alguien genere un contenido igual al subido nos notificará mediante una alarma\n Plagiarism checker de Dupli Checker\n Duplicheker es una herramienta de verificación de plagio que puede encontrar instancias de contenido duplicado.\n Busca en Internet las mismas oraciones, frases o párrafos que tiene en su sitio web y lo dirige a URL externas que tienen el mismo contenido.\n Tiene una capacidad de 1000 palabras por búsqueda; tiene problemas a la hora de copiar y pegar texto, ya que añade espacios vacíos generando errores\n Viper\n Se trata de un software que coteja más de 14 billones de páginas web, artículos, libros de texto, periódicos o revistas para detectar un plagio. Con simplemente escanear el documento, la aplicación muestra si se ha copiado o no, destacando incluso las partes del contenido que han sido reproducidas tal cual\n Plagiarisma.Net\n Este sitio limita la búsqueda a 2,000 palabras, eso sí, no puedes revisar más de tres textos al día. El funcionamiento es muy sencillo, aunque la interfaz sea algo obsoleta o incluso pueda resultar incómoda, pero cumple su objetivo sin necesidad de instalar un software extra\n PlagTracker\n  Este sitio cuenta con una versión gratuita que nos permite comparar el documento con una base de datos de más de 14000 páginas web; esta web te dira en que parte del texto debería aparecer como una cita y la página de internet donde está expuesta\n Plag.es\n Este software usa tecnología de navegación SSL lo que le permite verificar documentos de hasta 1000 páginas; nos permite detectar y corregir los plagios detectados y descargar la versión corregida, Plag. es funciona con 128 idiomas\n Wcopyfind\n No compara el documento con otros disponibles online, solo compara con documentos que el usuario añada de forma manual\n Copyleaks\n  La versión gratuita solo te permite analizar las 10 primeras páginas de tu documento\n Paper rate\n Solo analiza textos en inglés aunado a que su versión gratuita solo te permite análisis de 5 páginas y un uso de 10 veces por mes\n Quetext plagiarism checker\n La versión gratuita solo analiza 500 palabras; realiza su análisis de plagio consultando el las páginas de : Google, Yahoo, Babylon, Google Scholar y Google Books\n Edubirdie\n Soporta varios formatos como los son: .doc, .docx, txt, rtf y odt; esta herramienta puede analizar ensayos, curriculums y el contenido de páginas web; no cuenta con informes tan detallados ni un motor de búsqueda tan potente como otras plataformas\n Plagiarism detector\n Solo analiza textos superficiales,es decir, no hace búsquedas profundas, su versión gratuita analiza textos de 1,000 palabras\n Plagius\n Aplicación de escritorio que busca coincidencias tanto en internet como en los archivos locales\n Docode\n Aplicación de paga que analiza el documento contra tres fuentes: Web, Repositorio y entre Documentos, indica el porcentaje global del texto y citas encontradas\n Compilatio\n No es gratuito, cuenta con versiones tanto para el estudiante como para el docente\n Este tipo de tecnologías detecta el plagio gracias a sus algoritmos, incluso variaciones en la manera de redactar de las personas que entregan sus documentos pudiendo incurrir en comportamientos anómalos, es decir, si un estudiante entrega ocho documentos y el noveno distorsiona mucho su forma gramatical habitual de expresarse, los sistema activarán algoritmos adicionales para analizar la posibilidad de indagar en los documentos con mayor detalle.\n Su uso se dirige especialmente a las universidades dada la calidad, robustez y potencia de análisis de los sistemas que permiten descargar trabajos a un colectivo del ámbito científico que suele estar desbordado y que en muchos casos entiende que el trabajo es original del autor pero no sabe cómo demostrarlo.\n Estas herramientas son fantásticas para eso y para promover conceptos de integridad académica y científica al intentar minimizar el plagio mediante el fomento de la originalidad de los trabajos",
            "Similitud": "",
            "Nivel":"Sin equivalencia"
        },
        "bibliografia":[ 
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE",
        "CITA IEEE"
    ]
    },
    "imagenes":{
        "introduccion": [
            {
              "similitud": False,
              "porcentaje": 0.4468179511105692,
              "imagenes a comparar": [
                "./images/1.PNG",
                "./images/1_1IPN4.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.49609394804706414,
              "imagenes a comparar": [
                "./images/1.PNG",
                "./images/1_IPN4.PNG"
              ]
            },
            {
              "similitud": True,
              "porcentaje": 0.5151764135216256,
              "imagenes a comparar": [
                "./images/1.PNG",
                "./images/1_TEC4.PNG"
              ]
            }
          ],
        "analisis":[
            {
              "similitud": False,
              "porcentaje": 0.4803056540233935,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/ateneaTEC5.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.46986453357025154,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.49851031543417673,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_1.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.48567753725200663,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_2.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.48089140818308324,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_3.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.49269767815735116,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_4.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.48307902284886906,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_5.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4887318791989032,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_6.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4968097786131187,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_7.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4576541366718199,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_8.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.467640883355344,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_9.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4868661587352064,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_10.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.49795115778317217,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_11.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.47564452758461817,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_12.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.48348121587640386,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_13.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4842978454218134,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_14.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.47145974005814084,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_15.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4754828705527958,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_16.PNG"
              ]
            },
            {
              "similitud": True,
              "porcentaje": 0.5091054669801516,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_17.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4803779013974443,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_18.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4717204606600773,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_19.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.49933436619820526,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_20.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.4725541951285337,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_21.PNG"
              ]
            },
            {
              "similitud": False,
              "porcentaje": 0.47463708812438926,
              "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5024270264783527,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.499491082741244,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47191935502170285,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.510141394173038,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42937271743834643,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5587241111140949,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5503182418719438,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5709281351816764,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5540242276037272,
                "imagenes a comparar": [
                "./images/athenea1.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5431985064786039,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5039331306014294,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5056589125377993,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5448803924789046,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5095788712051587,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5035264710037674,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5329854555211999,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.498302205378316,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5088693074268499,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5096559983478998,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5182770949717673,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.527984187349955,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5339828609451859,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5373924168192711,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5181423315950315,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5314419734506374,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5442457280189026,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5276169973523362,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49657494636352045,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5396766813716742,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5001892406497861,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5374886749888134,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5246713173112336,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5190421346701161,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5290496759000592,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5496128961484148,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4331090597956222,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5440305207317536,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5169248851999866,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5496444534615983,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5344854323114823,
                "imagenes a comparar": [
                "./images/athenea2.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5210611269419386,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5051242434259887,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.540320824204302,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5052268448130522,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48376442909341016,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4984106500352765,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4679591617877376,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.511241557286699,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4846373004226751,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5308349527425986,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5116706450102565,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5378934282707005,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47859423373577004,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5110204377474511,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5312709750136664,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5256481403426916,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5000605108338516,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5117042125297908,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4960268627703995,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5020510313573382,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49189837896391303,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5040433599211882,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5003366577344989,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49705719624657974,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.516251139098336,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41604145744502435,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.500647454762855,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4938163390427202,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49626116004378945,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4992741131648398,
                "imagenes a comparar": [
                "./images/athenea3.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4062041690474845,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.405356699495848,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4018279676827192,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3867151179866826,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38657050956862243,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3790495704637163,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3752507676970948,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39258659371835253,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37050596289074883,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40759814697611185,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3881662640072691,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.406597257591608,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38433123350258674,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3966194244852789,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4037670886549026,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4082958805569237,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3660765456462178,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3818531114663875,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3932694661345635,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3930087484048758,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39801627561497144,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3972048076000454,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40204581595716776,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3945161014724603,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4192887724631724,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45910189289633063,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4635414964376392,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5434605606780232,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5276523752338902,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5288066294938488,
                "imagenes a comparar": [
                "./images/athenea4.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46176047646233886,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4534114699238038,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46594975854160753,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4394977081146248,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4441775446195269,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4398810774555553,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4345118952893305,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4407275885259853,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42883552292412325,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46871213042340454,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4567887189095255,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46448277050123954,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43344291571618987,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45414324827754177,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46540240944849437,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4695950913262387,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42688402702928924,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44159006006281426,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4583508203670905,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43767570106721393,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45295978554985267,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44346640965714784,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45260108167854823,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43285142583879127,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48026489789642984,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4944421890989263,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5224700940039041,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5599745478299107,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5553455603161831,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5536251823545936,
                "imagenes a comparar": [
                "./images/athenea5.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47323991763077705,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4711514484121757,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4642534234718199,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4499269040687152,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46060456365961294,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4396006852849099,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45573898781850225,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4579387827768702,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45072484759950443,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4826247735230506,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4541533515527223,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4736212064834846,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44205452783591737,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46392262013191704,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4788683279746835,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4620074085980068,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4410315572669587,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45128260721056757,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4784590874401742,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4517050281751602,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45515257483225263,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4526746870438075,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45801622590232055,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45087706778311704,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.467764190312091,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4796312832571184,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5016939610831098,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5583607776745416,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5599731061715353,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5555486080941244,
                "imagenes a comparar": [
                "./images/athenea6.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3911268614760892,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3844912226052455,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38157051864637054,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3763931945364967,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3865936337011684,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37700457259893133,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36480396751650623,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38386855005829784,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37867860933044745,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38765316038904735,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3596229676271121,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3895629039651886,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37378913014292986,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37679024983379267,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3794144562315533,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39297806275745,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3739489639797154,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3686122648292373,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4214388080402695,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37662985146123934,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3675189988229121,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3850105296939126,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3759112800192946,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3827115992966572,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3879073827916078,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4404458321169929,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4642968877948028,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5122387853475224,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.504155148632702,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5191458851298542,
                "imagenes a comparar": [
                "./images/athenea7.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41236004989506775,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4138605513326831,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41097018347554476,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39984786316824933,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4057263822365642,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39757586889121016,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.395118736382362,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39901211330725056,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3931101410662354,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4179123956446576,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4005168432668594,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4099161208274153,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4023195040228426,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40931728148023855,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41086450818643977,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4157583278606089,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3824106553547151,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.392761907624571,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42453750900102377,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40223464812217885,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4104943532044006,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41182291464796794,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4149716776016694,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4018124550059658,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4371450951208802,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.478262243694538,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4996301426922904,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5667985891371304,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5499970640432849,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5471398085339568,
                "imagenes a comparar": [
                "./images/athenea8.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4905748963761644,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49816950925849585,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48684619942605173,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4660400569249703,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4675912014321823,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4480946207995024,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46916967567054907,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4769251692228105,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45330894058647847,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49565115896871426,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4871426686936893,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4941670826614077,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.455491563725089,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4992518598761824,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5048864861266736,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47095774776543187,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4508071367283801,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4781025248926789,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48206008279088053,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46420107206551076,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4608793902643433,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4583593583764121,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46074402483701427,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4649067707705452,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4800512251123023,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4150592537319289,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.492996903913033,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4941040224949691,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5094181059012254,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5109732706672875,
                "imagenes a comparar": [
                "./images/athenea9.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4907545816187586,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49522435461886416,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4856241181591328,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4799835246248885,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49497117555795817,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47111933717223325,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4765814670890136,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47525880678667765,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4870086186008334,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4971589563509822,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4731741989110921,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.489202230693148,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47881474735358753,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48334324940296614,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4884974526820612,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4824591968867278,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47661000910607587,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47844885454243563,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.507960576728771,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4733772917118309,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4730305339183696,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4931688103727809,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4874322245098281,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4758809146938523,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4899317231178711,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42674652871026436,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5059884752898801,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.512885887793964,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5224093224536452,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5302672204778841,
                "imagenes a comparar": [
                "./images/athenea10.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4131243521430641,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44279498561946323,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45970552158928873,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45686297086283556,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4360963440294485,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4508838723615753,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.452769151740817,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4336242078908024,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4266121931710349,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44377722639703904,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4404742167149666,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46736245316647657,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43122398415922486,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44717198118283835,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42125867083154245,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4452066064788644,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45113723793504246,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45406288137089285,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41399882450559405,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4440688427399335,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44187889346202924,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4540103814216369,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43114212032938387,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4482320243580977,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.460202363355537,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4381801595826628,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45643536374733634,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4447246630498501,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5118960185266797,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5528365525387803,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5554356271051702,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5587775741460765,
                "imagenes a comparar": [
                "./images/athenea11.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35727730905039196,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3825677776936245,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.380353049470126,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37948586875617324,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3839420113137444,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36146945468210584,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3718306780650023,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36217548207486816,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.370044135327472,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3695373679792846,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35922561189165564,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3828554732981306,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3687943488533838,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3871728615472943,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37877960555475515,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37985908318456046,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38382974124954305,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39057298410999214,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3574529183219972,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35896697618321305,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3988859543075278,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.366925640396137,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3761531177148714,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37486639968140345,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3700976807901157,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3812248973742483,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3999186630616826,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4735875594208474,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4584533533098467,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.533072890773238,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5151199376057548,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5329716586405226,
                "imagenes a comparar": [
                "./images/athenea12.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41767539763575057,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4241514291409174,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41010852781540325,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.398466336479059,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43027295623903744,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3909269790810059,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3882832905197737,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40912706570234797,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38050786413329335,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3924604924214969,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3765202381602251,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4195681372701657,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4228488268274164,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4171437212689348,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3996697117028245,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40938586227637935,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41573408702446984,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4295391237837909,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39790136827868366,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.38683224884354495,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4083914568073916,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39410359461113137,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4196104852437359,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4054912071085635,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4165140218850036,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39167943440184444,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43999264827726026,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46870253084334323,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5048697058446823,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5353876834031279,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5290458089279705,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5316811973649668,
                "imagenes a comparar": [
                "./images/athenea13.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.33765789824674525,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35955475445556534,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37411958897216113,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37431771730903646,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36924506395804174,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3647828962403404,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36718311346393984,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35188902219259294,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36047144492243505,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35911600226788326,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3655955460547407,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3845650419734212,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3532805826562659,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3708414033378597,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3598735164242539,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36609868358614106,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.375505438687827,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3680940439681705,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.35268595903728955,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3556078437772598,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4066968196356462,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36098588586768915,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.34786035501872475,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.36961565971673643,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3632298179784929,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3752427739851317,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3732030982741101,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44938729165309343,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4077603764953375,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4627370050736614,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4637217857804701,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4702944811679493,
                "imagenes a comparar": [
                "./images/athenea14.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4406402056906014,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4550513123802591,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45513271618321616,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4528636050538839,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45994446612904505,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4361854608606713,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45501741673055013,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43079817394642084,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4437439222807586,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43493114004892613,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44179978642132783,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4644642669657011,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4582764939130357,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4580524442219766,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45410804135064,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45173082013034643,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4520900678205059,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4484532634900152,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42635415473753274,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4360053263188288,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45248766604975815,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4341204368176205,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46127749324275574,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45728275016503805,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4630569165447571,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4342646495060832,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47441015609836085,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4695107122506889,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49635228479513566,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5333145442758535,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5284276506081754,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5421587641196471,
                "imagenes a comparar": [
                "./images/athenea15.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40038246447848874,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42009034230878833,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43160766919472243,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42831442585397955,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4186216745337094,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40524195123815376,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4244354184980894,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3970384125566285,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4213654455365455,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4055771775890988,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4075578745304284,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.44032093878480955,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4135742320353453,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4199779008444069,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4141020377707861,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42252524448539397,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42789561651211655,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4143794664365252,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.39049637119790487,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4000611307389659,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43242034889552855,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40886876761941227,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41876507861206963,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42093942819904573,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.433215315784121,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41219594862748127,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.43581817248172916,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47777882736462113,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4587239284311613,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5301857412330073,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5203998468657415,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5237322972858939,
                "imagenes a comparar": [
                "./images/athenea16.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.46874262126043753,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.511752414251854,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4910310336519832,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4958406808327957,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4936111482661236,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49654706379973174,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4911198739942253,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49713558010873343,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48018296264379323,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4919281648974929,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49104621093563544,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4960414050084247,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4800797529651681,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5105787573937125,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48773249712923095,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.48945947641269666,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4892382100198334,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5129450032781001,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47943598066874143,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.47488316808242237,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5318755879812541,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49188880753849284,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.49041931543830275,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5087068578759218,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5020694930942059,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4992443765344996,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5084661462676404,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.488216825542554,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.549999071128639,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5613314656806311,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5698053126071713,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5725281669886404,
                "imagenes a comparar": [
                "./images/athenea17.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.2953500116440948,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.32779544848453745,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3527374667820935,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3366782325010602,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.32635423904825167,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3246053488347508,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3002357862522274,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.30407867627102364,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.31140838082637645,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3293880071607587,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3011012194926174,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3537856703948064,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3136583989540866,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3316434630492899,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.2892234729451217,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.31254312020136193,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.34730914070553975,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.34388026895592505,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3107070723916356,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3250778585707362,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3327759752555349,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.31670084253612174,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3191957513992836,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3111749617391955,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.31788260199824264,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.30592834283218534,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3332602068633552,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40259233892551904,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37842214157761295,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4271107494642541,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42294050655438814,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42521549766711675,
                "imagenes a comparar": [
                "./images/athenea18.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41188704964059,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42810241250200387,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_1.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3914611817757207,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_2.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40032130423050777,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4220814841021208,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_4.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4026987309724666,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_5.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3877995952800964,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_6.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4114310816769116,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_7.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40065662428012566,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_8.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4027378932532412,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_9.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3860959912955629,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_10.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.3937113951594868,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_11.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4079494308673781,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_12.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42009049323922093,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_13.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4200560902435357,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_14.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4008674729544041,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_15.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.40775776366006217,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_16.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.431297440417032,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_17.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4015150548756204,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_18.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.37794484868128864,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_19.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.45748036960460975,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_20.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4007154752132888,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_21.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42546935629920285,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_22.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42229107105349994,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_23.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.41076972352230373,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_24.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.42700075210093585,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_25.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4321006274502876,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaIPN4_26.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5258322923824629,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaTEC3.PNG"
                ]
            },
            {
                "similitud": False,
                "porcentaje": 0.4996792290393787,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaTEC3_1.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5136578353526203,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaTEC3_2.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5208094923247025,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaTEC3_3.PNG"
                ]
            },
            {
                "similitud": True,
                "porcentaje": 0.5307310010797354,
                "imagenes a comparar": [
                "./images/athenea19.PNG",
                "./images/atheneaTEC3_4.PNG"
                ]
            }
        ]
    }
}