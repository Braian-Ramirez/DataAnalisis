import time
import psutil

# Función para contar palabras en una lista de líneas
def contar_palabras(lista):
    cache = []  # O(1) - Operación de tiempo constante
    contador_palabras = {}  # O(1) - Operación de tiempo constante

    for linea in lista:  # O(n), donde n es la cantidad de líneas en 'lista'
        for palabra in linea.split():  # O(m), donde m es la cantidad de palabras en una línea
            if palabra in cache:  # O(k), donde k es el tamaño de 'cache'
                contador_palabras[palabra] += 1  # O(1) - Operación de tiempo constante
            else:
                cache.append(palabra)  # O(1) - Operación de tiempo constante
                contador_palabras[palabra] = 1  # O(1) - Operación de tiempo constante

    return contador_palabras  # O(1) - Operación de tiempo constante

# Función para obtener las cinco palabras más usadas
def palabras_mas_usadas(documento):
    cinco_mayores = dict(sorted(documento.items(), key=lambda item: item[1], reverse=True)[:5])  # O(m log m), donde m es la cantidad de palabras únicas
    return cinco_mayores  # O(1) - Operación de tiempo constante

# Función para buscar la posición de una palabra en el documento
def buscar_palabra(documento):
    cache = []  # O(1) - Operación de tiempo constante
    indice = {}  # O(1) - Operación de tiempo constante

    for contador_linea, linea in enumerate(documento):  # O(n), donde n es la cantidad de líneas en 'documento'
        for palabra in linea.split():  # O(m), donde m es la cantidad de palabras en una línea
            if palabra in cache:  # O(k), donde k es el tamaño de 'cache'
                indice[palabra].append(contador_linea)  # O(1) - Operación de tiempo constante
            else:
                indice[palabra] = [contador_linea]  # O(1) - Operación de tiempo constante
                cache.append(palabra)  # O(1) - Operación de tiempo constante

    return indice  # O(1) - Operación de tiempo constante
#La complejidad del algoritmo es de O (n*m) donde n es la contidad de lineas y m la contidad de palabras en una linea,
# esta complejidad aplica para las funciones contar_palabras y buscar_palabra debido a sus bucles anidados
# La función palabras_mas_usadas cuenta con una complejidad O(m log m) debido a la operación de ordenación.


documento = [
    "La programación en Python es clave para el trabajo con datos",
    "Los programadores en Java tienen un alto interés en pasar a Python",
    "La optimización de algoritmos es fundamental en el desarrollo de software",
    "Las bases de datos relacionales son esenciales para muchas aplicaciones",
    "El paradigma de programación funcional gana popularidad",
    "La seguridad informática es un tema crucial en el desarrollo de aplicaciones web",
    "Los lenguajes de programación modernos ofrecen abstracciones poderosas",
    "La inteligencia artificial está transformando diversas industrias",
    "El aprendizaje automático es una rama clave de la ciencia de datos",
    "Las interfaces de usuario intuitivas mejoran la experiencia del usuario",
    "La calidad del código es esencial para mantener un proyecto exitoso",
    "La agilidad en el desarrollo de software permite adaptarse a cambios rápidamente",
    "Las pruebas automatizadas son cruciales para garantizar la estabilidad del software",
    "La modularización del código facilita la colaboración en equipos de programadores",
    "El control de versiones es necesario para rastrear cambios en el código",
    "La documentación clara es fundamental para que otros entiendan el código",
    "La programación orientada a objetos promueve la reutilización de código",
    "La resolución de problemas es una habilidad esencial en la programación",
    "La optimización prematura puede llevar a código complicado y difícil de mantener",
    "El diseño de interfaces de usuario atractivas mejora la usabilidad de las aplicaciones",
    "El código limpio es esencial para facilitar el mantenimiento",
    "Los patrones de diseño son soluciones probadas para problemas comunes",
    "Las pruebas unitarias garantizan el correcto funcionamiento de las partes del código",
    "El desarrollo ágil prioriza la entrega continua de valor al cliente",
    "Los comentarios en el código deben ser claros y útiles",
    "La recursividad es una técnica poderosa en la programación",
    "Las bibliotecas de código abierto aceleran el desarrollo de software",
    "La virtualización permite una mejor utilización de los recursos de hardware",
    "La seguridad en la programación web es fundamental para prevenir ataques",
    "Los principios SOLID son fundamentales para el diseño de software robusto",
    "La arquitectura de microservicios permite escalar componentes individualmente",
    "La refactorización mejora la calidad del código sin cambiar su comportamiento",
    "Los sistemas distribuidos presentan desafíos en la sincronización de datos",
    "El enfoque DevOps une el desarrollo y las operaciones para una entrega eficiente",
    "Las bases de datos NoSQL son útiles para manejar datos no estructurados",
    "La agilidad en el desarrollo permite adaptarse a cambios del mercado",
    "Las buenas prácticas en el control de versiones facilitan la colaboración",
    "La programación concurrente mejora la eficiencia en sistemas multiusuario",
    "Los marcos de trabajo MVC separan la lógica de la interfaz de usuario",
    "La interacción entre aplicaciones se logra a través de APIs",
    "El machine learning permite a las máquinas aprender de los datos",
    "La analítica de datos ayuda a tomar decisiones basadas en información",
    "El diseño responsivo garantiza una experiencia consistente en diferentes dispositivos",
    "Las pruebas de carga verifican el rendimiento de las aplicaciones",
    "El enfoque centrado en el usuario mejora la usabilidad de las aplicaciones",
    "La programación reactiva es útil para manejar flujos de datos asincrónicos",
    "Los contenedores facilitan la implementación y el despliegue de aplicaciones",
    "La gestión de dependencias es esencial para administrar las bibliotecas externas",
    "La integración continua automatiza la verificación de cambios en el código",
    "El aprendizaje profundo es una rama avanzada del machine learning",
    "La depuración es una habilidad crucial para encontrar y corregir errores",
    "La criptografía protege la información sensible en aplicaciones",
    "El desarrollo full-stack abarca tanto el frontend como el backend",
    "Las pruebas de seguridad ayudan a identificar vulnerabilidades en el software",
    "La agilidad cultural es clave para adoptar prácticas ágiles de manera efectiva",
    "La infraestructura como código permite automatizar la gestión de servidores",
    "Los patrones arquitectónicos guían la estructura general de una aplicación",
    "El análisis predictivo utiliza datos históricos para predecir tendencias",
    "Las interfaces API REST son ampliamente utilizadas para comunicarse con aplicaciones",
    "El rendimiento de las aplicaciones es esencial para brindar una buena experiencia",
    "La virtualización de servidores reduce costos y facilita la administración",
    "La ingeniería de software implica la aplicación de métodos sistemáticos",
    "El código autodocumentado es claro y fácil de entender para otros programadores",
    "La integración de sistemas conecta diferentes aplicaciones para trabajar juntas",
    "Las metodologías ágiles promueven la adaptación y la colaboración continua",
    "El monitoreo de aplicaciones permite identificar y resolver problemas en tiempo real",
    "El análisis de datos masivos (big data) abre oportunidades para obtener insights",
    "El diseño de interfaces de usuario es crucial para la experiencia del usuario",
    "La seguridad en el desarrollo es un proceso constante de mitigación de riesgos"
    ]
start_time = time.time()
menria_inicio = psutil.virtual_memory().used
resultado = contar_palabras(documento)
resultado2= palabras_mas_usadas(resultado)
resultado3 = buscar_palabra(documento)
print(f"estas son todas las palabras que contiene el documento con el número de veces que aparacen en el mismo:\n{resultado}")
print(f"estas son las cinco palrabras más usadas en el documento:\n{resultado2}")
print(f"lista de las palabras con su indice en cual aparecen:\n{resultado3}")
end_time = time.time()
memoria_final = psutil.virtual_memory().used
print(f"el tiempo de ejecución del algoritmmo es de: {end_time-start_time} segundos")
print(f"el espacio en memoria consumido durante la ejecución del algoritmo es de: {memoria_final-menria_inicio} bytes")
