# Organización del Proyecto Santiaguía
## Enfoque

La Santiaguía está enfocada principalmente en los estudiantes universitarios foráneos, que se encuentren confundidos o perdidos al intentar o querer vivir en Santiago.
Esta guía será difundida a través de las universidades.
Para lograr esto, se tiene pensado en informar al estudiante a través de una "wiki" que al principio va a tener al menos los siguientes temas:
- Transporte
- Seguridad
- Trámites
- Compras (víveres, mercadería)
- Hospedaje

Para lograr una buena mantención a largo plazo, se tendrá un sistema de autenticación, edición y colaboración de información incorporado en la wiki, de modo que estudiantes puedan curar y ayudar a mejorar los recursos de esta guía.
La recopilación de información inicial será a través de páginas o recursos ya existentes.
El aporte de información podrá ser hecho por cualquier persona (captcha), pero debe ser aprobada por curadores (plural).
Además, se podrá ver el historial de cambios de las páginas modificadas.

La página contará con un mapa que esté dividido en zonas, ya sea de seguridad, comercio y otros, con el fin de ayudar al estudiante a entender. Este mapa podrá ser mejorado por cualquier persona (captcha) y luego sus cambios ser aprobados por curadores.
En lo posible, se contará con un sistema de versiones para visualizar cambios a lo largo del tiempo.

---

## Programación
¿Cómo se va a hostear esto?
Yo Maxi estaba pensando en quizás, si es que todo sale bien y se ve con buen futuro el proyecto, pedir espacio a la Universidad para hostear y mantener la página en línea a través de ellos. Creo que como estudiantes es un poco obvio que no tenemos el dinero para mantener un servidor abierto jeje.
### Parte 1: Wiki
Literalmente vamos a reinventar la rueda (MediaWiki y otros framework de Wiki ya existen)
### Parte 2: Mapa
Podemos ocupar OpenStreetMap como mapa base y luego hacer un sistema que muestre la información de zonas sobre tal mapa, con capas que se puedan abrir y que muestre datos de cuándo fue añadido..
### API:
- OpenStreetMap
- Algún captcha
