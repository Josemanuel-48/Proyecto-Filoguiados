# Sistema de Monitorización AGV — Documento de Entrega

*Borrador de trabajo. Se irá completando sección por sección, en el orden pedido por el curso. Antes de la entrega final se convertirá a PDF/Word.*

---

## 1. Objetivos del proyecto

El proyecto nace de una necesidad detectada en el entorno real de producción: actualmente, la detección de paradas de los AGVs en su recorrido depende en gran medida de la comunicación manual entre los operarios de planta y la oficina de monitorización — son los propios operarios quienes, al no ver llegar un carro, avisan para que se compruebe su ubicación. Este proceso reactivo introduce un tiempo de respuesta variable y depende del factor humano, retrasando la detección de incidencias.

Esta demora tiene un impacto directo en la producción: si un AGV se detiene y la incidencia no se detecta a tiempo, el material que transporta no llega a la línea correspondiente, pudiendo derivar en paradas de la propia línea de producción por falta de material — un problema con un coste mucho mayor que la simple parada del carro en sí.

El objetivo principal del Sistema de Monitorización AGV es automatizar esta detección: registrar cada parada del recorrido con su ubicación (sensor/segmento), duración y momento exacto, y ofrecer una visualización clara y centralizada (a través de un panel de control accesible mediante login) que permita detectar de un vistazo qué segmentos superan un umbral de tiempo considerado anómalo, sin depender de que alguien note la incidencia manualmente.

Con ello se busca reducir el tiempo de reacción ante paradas, minimizar el riesgo de paradas de producción por falta de material, facilitar el análisis histórico de qué tramos del recorrido son más problemáticos, y sentar una base software que en el futuro podría ampliarse con avisos físicos (sonoros o luminosos) en la propia planta.

---

## 2. Stack tecnológico y alternativas evaluadas

El framework elegido para el desarrollo del proyecto es Django. La decisión responde a dos razones principales:

En primer lugar, una razón práctica: de las opciones vistas durante la formación (Django, Flask, Tkinter), Django es el framework en el que se ha adquirido un dominio real y suficiente para desarrollar un proyecto completo con garantías, frente a un conocimiento más superficial de las otras alternativas. Se ha priorizado construir algo sólido y bien entendido de principio a fin, antes que arriesgar la viabilidad del proyecto explorando una tecnología nueva bajo la presión de un plazo de entrega.

En segundo lugar, una razón técnica: Django resuelve de un solo golpe tres de los cuatro requisitos mínimos exigidos por el curso — framework web, programación orientada a objetos (los modelos de datos son clases que heredan de `models.Model`) y sistema de login/control de accesos (incluido de fábrica, sin necesidad de programarlo desde cero). Tkinter, al ser una librería de interfaces de escritorio y no un framework web, quedó descartada al no encajar con el enfoque de aplicación accesible desde navegador. Flask, aunque también viable, se descartó por ser un framework más minimalista que habría requerido construir a mano funcionalidades (como el sistema de autenticación) que Django ya trae integradas.

---

## 3. Explicación y esquema de la base de datos

El sistema utiliza una única tabla, `RegistroParada`, que almacena cada parada detectada durante el recorrido de los AGVs:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | INTEGER (autoincremental) | Clave primaria, generada automáticamente por Django. |
| `id_carro` | CharField | Identificador del AGV que ha sufrido la parada (ej. "Carro_1"). |
| `sensor` | CharField | Segmento/tramo del recorrido donde se ha detectado la parada (ej. "Segmento_3"). |
| `duracion` | IntegerField | Duración de la parada, en segundos. |
| `hora` | DateTimeField | Fecha y hora exactas en que se registró la parada. |

El campo `id` es autoincremental y actúa como clave primaria en lugar de cualquier otro campo del modelo. La razón es que, al circular varios AGVs simultáneamente, dos paradas de carros distintos podrían coincidir exactamente en fecha y hora — por lo que ningún campo por sí solo garantiza unicidad. El `id` autoincremental, generado automáticamente por Django, resuelve esto sin necesidad de gestión manual: cada parada queda identificada de forma única independientemente de que coincida con otra en cualquier otro dato.

Por otro lado, el archivo `db.sqlite3` (donde Django almacena físicamente los datos) se ha excluido del control de versiones mediante `.gitignore`. El motivo principal no es que los datos sean sensibles (son datos simulados de prueba), sino que es un archivo binario: Git no puede mostrar qué ha cambiado línea a línea entre versiones, por lo que cada modificación de datos "ensuciaría" el historial de commits repitiendo el archivo entero. Si en algún momento fuera necesario mostrar datos de ejemplo sin subir el binario, la alternativa contemplada es exportar datos concretos a un archivo de *fixtures* (formato JSON que Django puede cargar).

---

## 4. Explicación de los requisitos de la aplicación

*Pendiente de redactar.*

---

## 5. Manual de instalación

*Pendiente de redactar.*

---

## 6. Conclusiones y evolutivos del proyecto

*Pendiente de redactar — se escribe al final, cuando el proyecto esté más cerca de cerrarse.*
