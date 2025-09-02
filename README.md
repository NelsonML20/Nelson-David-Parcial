# Nelson-David-Parcial
en este repositorio esta nuestro parcial del computo l

<img src="https://ugb.edu.sv/wp-content/uploads/2023/06/UGB_LOGOTIPO_HORIZONTAL.png">

Docente: **Willian Alexis Montes Girón**

ALUMNOS: **DAVID ALFONSO ALVARENGA BONILLA**

ALUMNOS: **NELSON JAVIER MEJIA LEMUS**


Preguntas 

1 ¿Qué ventajas tiene en comparación con poner todo el código en
un solo archivo o utilizar módulos?

Separar el código en módulos (por ejemplo, aparatos.py y main.py) tiene varias ventajas:

Organización y limpieza: El código está mejor estructurado. Las clases y funciones están separadas del programa principal, lo cual facilita la lectura y el mantenimiento.

Reutilización: Podemos reutilizar las clases en otros proyectos sin tener que copiar todo el código.

Escalabilidad: Si el proyecto crece (por ejemplo, se agregan tipos de aparatos o gráficos), es más fácil hacerlo en un sistema modular.

Pruebas más sencillas: Podemos probar las clases y funciones por separado sin afectar el resto del programa.

En cambio, si todo estuviera en un solo archivo, sería más difícil de mantener, menos legible y más propenso a errores.



2 ¿Cómo aplicaron la Programación Orientada a Objetos en su
solución? Describan el papel de las clases creadas.

La clase Aparato encapsula toda la lógica relacionada con un aparato: su nombre, potencia, horas de uso, consumo mensual en kWh y el costo mensual.

Cada objeto de esta clase representa un aparato específico (ej. refrigerador, televisor).

Utilizamos métodos para calcular el consumo (calcular_consumo), el costo (calcular_costo) y para mostrar la información (info).

Además, usamos un atributo de clase (lista_aparatos) para mantener un registro de todos los aparatos ingresados, similar a cómo se hizo en la clase Mascota de las capturas.

Esto nos permitió modelar los aparatos como objetos del mundo real, simplificar cálculos y mantener el código organizado y reutilizable.



3 ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo
en equipo? Den un ejemplo concreto

GitHub facilitó el trabajo colaborativo en varias formas:

Control de versiones: Cada integrante del equipo pudo hacer cambios en el código sin sobrescribir el trabajo de los demás.

Trabajo en paralelo: Por ejemplo, mientras una persona trabajaba en el módulo aparatos.py (definiendo la clase), otra trabajaba en main.py (haciendo pruebas y creando el menú de usuario).

Historial de cambios: Si cometíamos un error, podíamos volver a una versión anterior sin perder todo el avance.

Comentarios y revisiones: Usamos pull requests para revisar el código de otros compañeros antes de integrarlo al proyecto principal.

Ejemplo concreto: Un integrante del equipo encontró un error en el cálculo del costo y lo corrigió en una rama aparte. Después lo revisamos y lo fusionamos sin afectar el resto del proyecto. Esto hubiera sido muy difícil si estuviéramos trabajando todos sobre un mismo archivo sin control de versiones.
>>>>>>> 347087cc8c4a0c1043921ae90aeea709195209b2
