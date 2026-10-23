# Taxonomía de Temas y Roles

> **Status**: In Review
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-23
> **Last Verified**: 2026-10-23
> **Implements Pillar**: Regla Cero, Pilar 3 (Memoria Pura), Pilar 6 (No hay Carta Mala)
> **Creative Director Review (CD-GDD-ALIGN)**: `/design-review` full del 2026-10-22, NEEDS REVISION; revisado el 2026-10-23 (D-43), pendiente de re-revisión

## Summary

La Taxonomía es el diccionario común de la lectura. Tiene 20 temas agrupados en 5 familias, que siguen a los palos del tarot más los Arcanos Mayores, y tiene roles narrativos (origen, conflicto, desenlace). Con ese diccionario, las cartas, el cliente generado, las tiradas y los textos hablan el mismo idioma. Define también cuándo una lectura acierta exacto (mismo tema), a medias (misma familia) o no acierta. El jugador la ve en el tooltip de cada carta, como tema y familia.

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `None`

## Overview

La Taxonomía de Temas y Roles es el vocabulario cerrado que comparten todos los sistemas de la lectura. Tiene dos listas:

- **Temas:** etiquetas mecánicas como *traición*, *deuda*, *culpa* o *poder*, que dicen **de qué** habla algo.
- **Roles narrativos:** *origen*, *conflicto*, *desenlace*, *el otro*, *caminos*, que dicen **qué lugar ocupa** ese algo en la historia del cliente.

Cada sistema usa ese vocabulario a su manera:

- Cada carta declara sus temas, derivados de sus palabras clave (GDD §3.2).
- El Generador de Situaciones produce la verdad oculta del cliente como temas por rol.
- Cada tirada traduce sus posiciones a roles.
- Las preguntas y los textos se arman con las mismas palabras.

La Resonancia compara la lectura con la verdad usando las reglas de comparación entre temas que define este documento.

El jugador no maneja la taxonomía como sistema: la percibe a través de lo que habilita. Ve los temas de cada carta en el tooltip, que es conocimiento público (Pilar 3, GDD §3.3). Lee las posiciones de la tirada como preguntas ("¿de dónde viene esto?", "¿qué lo traba?"). Y descubre que lo que dice el cliente, lo que sale en las cartas y lo que paga la sentencia hablan el mismo idioma.

Sin este vocabulario, cada sistema tendría su propio lenguaje. El Generador tendría que conocer cada tirada, porque la tirada se elige después de generar al cliente (D-37). Y no habría forma de decir si una lectura "acertó".

## Detailed Design

### Core Rules

> Revisado en `/design-review` full con `game-designer`, `systems-designer`, `qa-lead`, `narrative-director` y `creative-director` (2026-10-22). Las decisiones que salieron de esa revisión están en D-43.

**Temas y familias**

1. Hay **5 familias fijas**: una por palo y una para los Arcanos Mayores. No se agregan familias nuevas, porque salen de la estructura del tarot (GDD §3.5).

   | Familia | Palo / elemento | Campo | Temas del MVP |
   |---|---|---|---|
   | Emoción | Copas / Agua | lo que se siente | amor, culpa, duelo, deseo |
   | Bienes | Oros / Tierra | lo que se tiene o se pierde | deuda, fortuna, hogar, trabajo |
   | Conflicto | Espadas / Aire | lo que se enfrenta | traición, ley, violencia, engaño, secreto |
   | Ambición | Bastos / Fuego | lo que se busca | poder, rivalidad, fama, riesgo |
   | Destino | Arcanos Mayores | lo que le pasa al cliente y no controla | muerte, locura, enfermedad |

   Son 20 temas e incluyen los diez de ejemplo del GDD §3.2. La frontera entre Conflicto y Destino es una sola, y es el criterio de D-42: lo que el cliente controla o hace va en Conflicto, y lo que le pasa va en Destino. Por eso *secreto* va en Conflicto (el cliente lo esconde, el Doble Fondo) y *enfermedad* va en Destino (D-43). *Trabajo* (empleo, despido, cierre de fábrica) completa Bienes.
2. Cada tema pertenece a **exactamente una familia**: en los datos, la familia es un campo único del tema. Una carta puede llevar temas de cualquier familia: un Cinco de Copas puede hablar de *deuda*.
3. **Mínimo por familia:** cada familia tiene al menos **2 temas activos**, porque con uno solo el resultado parcial no puede darse. El objetivo de diseño es 3 o más. El validador rechaza un catálogo por debajo del mínimo.

**Identificadores**

4. Todo lo que define este catálogo tiene un **identificador estable**, separado del nombre que se muestra (que sale de la tabla de idioma y se traduce). El identificador lleva el prefijo de su tipo, de modo que dos tipos distintos nunca chocan:

   | Tipo | Prefijo | Ejemplo |
   |---|---|---|
   | Familia | `familia.` | `familia.conflicto` |
   | Tema base | `tema.` | `tema.traicion` |
   | Rol | `rol.` | `rol.conflicto` |
   | Forma de pregunta | `forma.` | `forma.si_o_no` |
   | Tema de mapa | `mapa_<mapa>.` | `mapa_a.hiperinflacion` |

   Después del prefijo, el identificador usa solo `[a-z0-9_]`, sin tildes ni eñes. Cada identificador es único en todo el catálogo. Nunca se renombra ni se borra: si un tema deja de usarse, se marca como deprecado (ver States).
5. Los mapas pueden **agregar temas**. Ningún mapa cambia un tema base existente, en ningún campo. Cada tema de mapa declara un **tema base equivalente**, que tiene que existir y ser un tema base activo (no otro tema de mapa). El tema de mapa **no declara familia**: toma la de su equivalente. Varios temas de mapa pueden compartir el mismo equivalente.

**Comparación (la regla que usa la Resonancia)**

6. La comparación es una función pura:

   `comparar(leído: tema base | nada, verdadero: tema base o de mapa) → EXACTO | PARCIAL | NINGUNO`

   Primero, si el verdadero es un tema de mapa, se reemplaza por su equivalente base. Después:
   - **EXACTO:** el leído y el verdadero son el mismo tema base;
   - **PARCIAL:** son temas distintos de la misma familia;
   - **NINGUNO:** son de familias distintas, o no hay leído.

   Si cualquiera de los dos identificadores no existe en el catálogo, o si el leído es un tema de mapa, la función **falla con error**: nunca devuelve NINGUNO en silencio.

   El puntaje de cada resultado (2, 1 y 0 en el GDD §5.8) lo define Resonancia, no este documento.
7. El tema leído es el de **la palabra clave que el jugador elige** para la carta. Cada palabra clave derecha o invertida se asocia a **exactamente un tema base**.

**Roles**

8. Roles del MVP: **origen**, **conflicto** y **desenlace**. Roles planificados para después del MVP *(provisorios hasta el GDD de Tiradas)*: **el otro**, **camino A** y **camino B**.
9. Cada posición de una tirada se traduce a **un rol o a "libre"**. Una posición libre no se compara contra la verdad, pero sus cartas cuentan para la gramática de combinación. Esto permite agregar tiradas grandes, como la Cruz Celta, sin inventar un rol por casillero.
10. El Generador asigna **un tema a cada rol activo**, porque todavía no sabe qué tirada se va a usar. Un rol es **activo** si el catálogo lo marca como producido por el Generador en la build actual. Es un dato del catálogo, como el estado de los temas. En el MVP los activos son origen, conflicto y desenlace; los roles planificados existen como identificadores pero no están activos. El catálogo tiene al menos un rol activo.

    La Taxonomía **no restringe qué temas van juntos** en una situación: si dos roles pueden repetir tema o si los temas deben ser coherentes entre sí lo define el Generador (ver Open Questions).

**Resolución de una posición**

11. Cada posición de la tirada produce **un resultado propio**, siguiendo estos pasos en orden:
    1. Se toma el rol de la posición, o "libre".
    2. Si la posición es libre, o si la situación no contiene ese rol, el resultado es **SIN_COMPARACION** y se termina acá.
    3. Si el jugador no eligió palabra clave, el resultado es **NINGUNO**.
    4. Si eligió, el tema leído es el de esa palabra clave (R7), y el resultado es `comparar(leído, tema verdadero del rol)` (R6).

    La resolución devuelve una lista con un resultado por posición, en el orden de la tirada: (posición, rol o libre, resultado). SIN_COMPARACION no es lo mismo que NINGUNO: la primera no entra en ninguna cuenta y la segunda vale cero. Cómo se agregan los resultados (por ejemplo, dos posiciones con el mismo rol) lo define Resonancia.

**Motivo de consulta**

12. El motivo tiene dos partes:
    - un **tema**, tomado de esta lista, que es de qué dice venir a hablar el cliente;
    - una **forma de pregunta**: *sí o no*, *situación general*, *dilema*, *vínculo* o *asunto grave*. La forma sugiere la tirada esperada (GDD §5.4). Las cinco existen como identificadores; en el MVP solo están activas *sí o no* y *situación general*.

    El tema del motivo puede no coincidir con la verdad: eso es el Doble Fondo, que lo decide el Generador (ver Open Questions).

**Validador del catálogo**

13. Los errores de datos los detecta el **validador del catálogo**, una función pura:

    `validar_catalogo(catálogo, cartas, mapas, tablas de idioma, catálogo anterior opcional) → lista de errores`

    Cada error es `{código, sujeto, detalle}`: el código identifica la regla rota y el sujeto es el identificador mal cargado (tema, carta y orientación, mapa, etc.). Los tests verifican el código y el sujeto, nunca el texto del mensaje. Con el catálogo anterior, el validador revisa también lo que no puede cambiar entre versiones (ids borrados o reactivados). Códigos:

    | Código | Regla |
    |---|---|
    | `ID_VACIO`, `ID_DUPLICADO`, `ID_FORMATO` | R4 |
    | `TEMA_SIN_FAMILIA`, `FAMILIA_INEXISTENTE` | R2 |
    | `FAMILIA_BAJO_MINIMO` | R3 |
    | `NOMBRE_FALTANTE` | Falta el nombre visible de un identificador en una tabla de idioma |
    | `KW_SIN_TEMA`, `KW_TEMA_INEXISTENTE`, `KW_TEMA_DE_MAPA` | R7, E7 |
    | `MAPA_SIN_EQUIVALENTE`, `MAPA_EQUIV_INEXISTENTE`, `MAPA_EQUIV_ES_DE_MAPA`, `MAPA_EQUIV_DEPRECADO`, `MAPA_DECLARA_FAMILIA`, `MAPA_SOBREESCRIBE_BASE` | R5 |
    | `SIN_ROLES_ACTIVOS` | R10 |
    | `ROL_INEXISTENTE` | E3: una tirada nombra un rol que no está en el catálogo |
    | `ID_ELIMINADO`, `ID_REACTIVADO`, `DEPRECAR_CON_DEPENDIENTES` | States |

    Si la lista no está vacía, el juego no pasa del arranque y muestra los errores (E1).

### States and Transitions

| Estado de un tema | Significa | Transición |
|---|---|---|
| Activo | Lo pueden usar cartas, situaciones y textos | → Deprecado, si se deja de usar y ningún tema de mapa lo tiene como equivalente |
| Deprecado | No se generan situaciones nuevas con él. Las partidas guardadas que lo tengan siguen funcionando, y las cartas pueden seguir ofreciéndolo como palabra clave | Fin: nunca vuelve a Activo y su identificador nunca se reutiliza |

Un tema base con temas de mapa que lo tienen como equivalente no se puede deprecar: primero hay que cambiar o deprecar esos temas de mapa. El validador lo rechaza con `DEPRECAR_CON_DEPENDIENTES`.

Fuera de este ciclo de vida, la taxonomía no cambia durante la partida: es un catálogo fijo de datos que se carga una vez.

### Interactions with Other Systems

| Sistema | Qué recibe de la Taxonomía | Qué le devuelve o aporta |
|---|---|---|
| Base de Datos de Cartas | Lista de temas | Cada palabra clave, asociada a un tema |
| Interpretación y Sentencia | Tema de cada palabra clave | La palabra clave elegida por posición, que define el tema leído (R7) |
| Tapete y Tooltips de Cartas | Nombre visible y familia de cada tema, y su marca | Nada; los muestra en el tooltip |
| Generador de Situaciones | Temas, familias, roles activos y formas de pregunta activas | Un tema por rol, más el motivo (tema y forma) |
| Tiradas | Roles | La traducción de cada posición a un rol o a "libre" |
| Resonancia y Resolución | `comparar` y la lista de resultados por posición (R6, R11) | Nada; la consume |
| Gramática de Combinación | Familia de cada palo | Nada; la usa para el bono por palo dominante |
| Arquetipos y Pieles de Mapa | Temas | Los temas típicos de cada arquetipo y de sus secretos |
| Textos por Plantillas | Nombre visible de cada tema y rol | Nada; los usa para armar preguntas y sentencias |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD todavía.

## Edge Cases

1. **Datos mal cargados** (una palabra clave sin tema o con un tema que no existe, un tema sin familia, un identificador vacío o repetido). Es un error de datos: el validador lo devuelve con su código (R13), el juego no arranca y nombra lo que está mal cargado. Nunca se resuelve en silencio.
2. **La situación tiene un rol que la tirada no cubre** (por ejemplo, Carta Única frente a un cliente con origen, conflicto y desenlace). Solo se comparan los roles que la tirada cubre; los demás no suman ni restan. Qué rol cubre cada posición lo define el GDD de Tiradas.
3. **Una posición pide un rol que la situación no contiene** (un rol no activo, como "el otro" en el MVP). La posición da **SIN_COMPARACION** (R11, paso 2), aunque el jugador no haya elegido palabra clave: no se compara, pero sus cartas cuentan para la gramática. Un rol que **no existe** en el catálogo (por ejemplo, un error de tipeo como `rol.orijen`) no es este caso: es un error de datos (`ROL_INEXISTENTE`).
4. **Dos posiciones con el mismo rol** (por ejemplo, en la Cruz Celta). Cada una produce su propio resultado contra el mismo tema verdadero. Está permitido. Cómo se combinan esos resultados lo define Resonancia.
5. **El jugador no elige palabra clave en una posición comparable.** El resultado es **NINGUNO**. No hay castigo extra.
6. **Una partida guardada con un tema deprecado.** Se carga y resuelve normal: las cartas pueden seguir ofreciéndolo, así que el exacto sigue siendo posible. El tema deja de aparecer solo en situaciones nuevas.
7. **Temas propios de un mapa.** Las cartas se comparten entre mapas, así que usan solo temas base. Para comparar, un tema de mapa se reemplaza por su equivalente (R6). Por ejemplo, con `mapa_a.hiperinflacion` → `tema.deuda` (familia Bienes): leer `deuda` da **EXACTO**, leer otro tema de Bienes da **PARCIAL** y leer uno de otra familia da **NINGUNO**. Los textos muestran el nombre del tema de mapa. Mecánicamente, un tema de mapa se comporta igual que su equivalente; lo que agrega es texto. El Mapa B del MVP no declara temas de mapa: esta lógica se prueba con datos de prueba (*hiperinflación* es del Mapa A).
8. **Las familias no tienen el mismo tamaño** (4/4/5/4/3). Si las cartas y la verdad tuvieran los temas repartidos de forma uniforme, leer un tema al azar daría un puntaje esperado de (n + 1) / 20 por posición, donde n es el tamaño de la familia del tema leído: 0,30 en Conflicto, 0,25 en Emoción, Bienes y Ambición, y 0,20 en Destino. Al azar, una posición da exacto el 5 % de las veces (20/400) y parcial el 15,5 % (62/400). Es la línea base con la que se calibra Resonancia. El sesgo real depende también de cómo reparten las familias las Cartas y el Generador, así que se vuelve a medir en el prototipo con los datos reales (ver Open Questions). Revisar la asignación es barato, porque las cartas y las situaciones referencian temas por identificador.

## Dependencies

**Depende de:** ninguno (capa Foundation).

**Dependen de la Taxonomía:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Base de Datos de Cartas | Dura | Asocia cada palabra clave a un tema |
| Interpretación y Sentencia | Dura | El tema de la palabra clave elegida es el tema leído |
| Tapete y Tooltips de Cartas | Blanda | Nombre visible, familia y marca de cada tema |
| Generador de Situaciones | Dura | Temas por rol, motivo (tema y forma de pregunta) |
| Tiradas | Dura | Traduce cada posición a un rol o a "libre" |
| Resonancia y Resolución | Dura | `comparar` y la lista de resultados por posición |
| Arquetipos y Pieles de Mapa | Dura | Temas típicos de cada arquetipo y sus secretos |
| Textos por Plantillas | Dura | Nombres visibles de temas y roles |
| Gramática de Combinación | Blanda | Familia de cada palo, para el palo dominante |
| Preguntas Capciosas | Blanda, indirecta | Pregunta por temas a través del Generador y de Textos |
| Inspección y Tells | Blanda, indirecta | Los tells apuntan a los temas de la verdad, a través del Generador |

**Bidireccionalidad:** ninguno de estos sistemas tiene GDD todavía. La sección Dependencies de cada uno tiene que nombrar a la Taxonomía cuando se escriba. En `systems-index.md` figuran como dependientes directos todos los de tipo dura o blanda; los indirectos llegan por el Generador.

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Asignación de tema a familia | Tabla de R1 (4/4/5/4/3) | Toda familia con 2 o más temas activos | Probabilidad de parcial por familia y línea base de E8 |
| Mínimo de temas activos por familia | 2 (objetivo de diseño: 3) | 2 o más; con 1 no hay parcial posible | Lo que acepta el validador |
| Roles activos | origen, conflicto, desenlace | Al menos 1 | Cuántos temas genera el Generador por situación |
| Formas de pregunta activas | sí o no, situación general | Al menos 1 | Tiradas esperadas disponibles |

## Visual/Audio Requirements

- Cada familia tiene una marca visual propia, la misma en el tooltip, el tapete y cualquier texto: el símbolo de su palo (copa, oro, espada, basto) o, para Destino, el de los Arcanos Mayores.
- La marca no depende solo del color, por accesibilidad.
- El color de cada familia sale de la paleta de las cartas de 1909 (D-39). El detalle se define en `/art-bible`.
- No hay sonido propio de este sistema.

## Game Feel

No aplica: la Taxonomía no se opera directamente. El feel del acierto exacto o parcial le corresponde a Resonancia.

## UI Requirements

- El tooltip de cada carta muestra, para la palabra clave derecha y la invertida, **el tema y su familia**: por ejemplo, "*engaño* · Conflicto" con la marca de la familia.
- El nombre del tema que se ve sale de la tabla de idioma, nunca del identificador interno.
- Los roles no se muestran con su nombre técnico. El jugador ve el nombre de la posición de la tirada ("Pasado", "Presente"); el rol queda detrás.

> 📌 **UX Flag — Taxonomía de Temas y Roles:** antes de escribir las historias de implementación hay que hacer el spec del tooltip con `/ux-design`. Los criterios de aceptación del tooltip (con captura retenida) se escriben ahí.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.2, §3.3 | Temas derivados de las palabras clave; temas públicos |
| GDD §3.5 | Palos y elementos → familias |
| GDD §5.3 | Motivo de consulta, separado en tema y forma de pregunta |
| GDD §5.4 | Tirada esperada según la forma de pregunta |
| GDD §5.8 | Match 0/1/2 → exacto / parcial / ninguno |
| D-08, D-37, D-39 | Significado público; desacople entre Generador y Tiradas; paleta de 1909 |
| D-42, D-43 | Criterio Conflicto/Destino; decisiones de la revisión full |

## Acceptance Criteria

Sin sección Formulas (la Taxonomía no define reglas numéricas): los criterios salen de Core Rules, States y Edge Cases. Los marcados *provisorio* dependen de un GDD que todavía no existe y se revisan cuando se escriba.

Convenciones de prueba:
- Los errores de datos se prueban contra el validador (R13): cada AC verifica que la lista **contiene** un error con ese código y ese sujeto, nunca el texto. Que el juego no arranque se prueba una sola vez (AC-25a y AC-25b).
- Los AC de nombres visibles usan **tablas de idioma de prueba con nombres centinela** (por ejemplo `«A:amor»`), nunca la tabla real, para que mostrar un identificador se pueda detectar.
- Los AC-16 a AC-18 se retiraron: probaban al Generador y pasan a su GDD (ver Open Questions). Sus números no se reutilizan.

**Datos del catálogo**
- **AC-01** (R1) — GIVEN el catálogo base, WHEN se carga, THEN hay exactamente 5 familias y 20 temas base activos: `familia.emocion` `amor`, `culpa`, `duelo`, `deseo`; `familia.bienes` `deuda`, `fortuna`, `hogar`, `trabajo`; `familia.conflicto` `traicion`, `ley`, `violencia`, `engano`, `secreto`; `familia.ambicion` `poder`, `rivalidad`, `fama`, `riesgo`; `familia.destino` `muerte`, `locura`, `enfermedad` (todos con prefijo `tema.`). Este AC cambia a propósito cada vez que cambia el catálogo.
- **AC-02a** (R4) — GIVEN las tablas de idioma de prueba A y B, con nombres centinela distintos entre sí y distintos del identificador, WHEN se pide el nombre visible de cada tema con cada tabla, THEN devuelve el de esa tabla, nunca el identificador, y el conjunto de identificadores del catálogo es el mismo con las dos.
- **AC-02b** (R13) — GIVEN una tabla de idioma a la que le falta el nombre de `tema.deuda`, WHEN se valida, THEN la lista contiene `NOMBRE_FALTANTE` con sujeto `tema.deuda`.
- **AC-03a** (R7, E1) — GIVEN una carta con una palabra clave sin tema, WHEN se valida, THEN la lista contiene `KW_SIN_TEMA` con sujeto la carta y su orientación.
- **AC-03b** (R7, E1) — GIVEN una carta con una palabra clave que apunta a `tema.inexistente`, WHEN se valida, THEN la lista contiene `KW_TEMA_INEXISTENTE` con sujeto la carta y su orientación.
- **AC-04** (R2, E1) — GIVEN un tema sin familia y otro cuya familia es `familia.sombra`, WHEN se valida, THEN la lista contiene `TEMA_SIN_FAMILIA` para el primero y `FAMILIA_INEXISTENTE` para el segundo.
- **AC-05a** (R4) — GIVEN un catálogo con dos temas de identificador `tema.deuda` (en cualquier estado), WHEN se valida, THEN la lista contiene `ID_DUPLICADO` con sujeto `tema.deuda`.
- **AC-05b** (R4, States) — GIVEN un catálogo anterior con `tema.deuda` deprecado y uno nuevo donde `tema.deuda` no está, WHEN se valida, THEN la lista contiene `ID_ELIMINADO` con sujeto `tema.deuda`.
- **AC-05c** (States) — GIVEN un catálogo anterior con `tema.deuda` deprecado y uno nuevo con `tema.deuda` activo, WHEN se valida, THEN la lista contiene `ID_REACTIVADO` con sujeto `tema.deuda`.
- **AC-25a** (E1, R13) — GIVEN un catálogo de prueba inválido, WHEN corre la secuencia de arranque sin pantalla, THEN devuelve "no arrancó", el menú principal nunca se alcanza y los errores que devuelve son los mismos que da `validar_catalogo`. Control: con un catálogo válido, arranca y se llega al menú principal.
- **AC-25b** (E1; UI) — GIVEN el mismo catálogo inválido, WHEN se lanza el juego real, THEN la pantalla de error lista el código y el sujeto de cada error. Evidencia: captura retenida en `production/qa/evidence/`.
- **AC-26** (R8, R10, R12) — GIVEN el catálogo base, WHEN se carga, THEN los roles activos son `rol.origen`, `rol.conflicto`, `rol.desenlace`; `rol.el_otro`, `rol.camino_a`, `rol.camino_b` existen e inactivos; las formas activas son `forma.si_o_no`, `forma.situacion_general`; y `forma.dilema`, `forma.vinculo`, `forma.asunto_grave` existen e inactivas.
- **AC-27** (R4) — GIVEN un identificador vacío y otro con mayúsculas o tildes (`tema.Traición`), WHEN se valida, THEN la lista contiene `ID_VACIO` y `ID_FORMATO`, cada uno con su sujeto.
- **AC-28** (R3) — GIVEN un catálogo de prueba donde `familia.destino` tiene un solo tema activo, WHEN se valida, THEN la lista contiene `FAMILIA_BAJO_MINIMO` con sujeto `familia.destino`.
- **AC-29** (R10) — GIVEN un catálogo de prueba sin roles activos, WHEN se valida, THEN la lista contiene `SIN_ROLES_ACTIVOS`.

**Comparación**
- **AC-06** (R6) — GIVEN leído `tema.traicion` y verdadero `tema.traicion`, WHEN se comparan, THEN el resultado es EXACTO.
- **AC-07** (R6) — GIVEN leído `tema.engano` y verdadero `tema.traicion`, y también al revés, WHEN se comparan, THEN los dos resultados son PARCIAL.
- **AC-08** (R6) — GIVEN leído `tema.amor` y verdadero `tema.deuda`, WHEN se comparan, THEN el resultado es NINGUNO.
- **AC-09** (R6, E8; *provisorio*: cambia si se revisa la asignación de familias) — GIVEN los pares leído/verdadero `muerte`/`locura`, `enfermedad`/`muerte`, `culpa`/`amor`, `hogar`/`trabajo` y `fama`/`poder`, WHEN se comparan, THEN los cinco dan PARCIAL (uno por familia, junto con AC-07).
- **AC-10** (R7) — GIVEN una carta con palabra clave derecha de tema `tema.traicion` e invertida de tema `tema.amor`, WHEN se selecciona la derecha y después la invertida, THEN el tema leído es `tema.traicion` y después `tema.amor`.
- **AC-11** (R11, E5) — GIVEN una posición con rol activo presente en la situación y sin palabra clave elegida, WHEN se resuelve, THEN el resultado es NINGUNO.
- **AC-30** (R6) — GIVEN un leído o un verdadero que no existe en el catálogo, o un leído que es un tema de mapa, WHEN se llama a `comparar`, THEN falla con error y no devuelve ningún resultado.

**Roles y posiciones** *(provisorios hasta el GDD de Tiradas; usan tiradas de prueba)*
- **AC-12** (R9, R11) — GIVEN una tirada de prueba con una posición libre, WHEN se resuelve, THEN esa posición da SIN_COMPARACION y su carta está en la lista que recibe la Gramática.
- **AC-13** (E3, R11) — GIVEN una posición con rol `rol.el_otro` contra una situación sin ese rol, con y sin palabra clave elegida, WHEN se resuelve, THEN en los dos casos da SIN_COMPARACION y su carta está en la lista que recibe la Gramática.
- **AC-14** (E2) — GIVEN una tirada de prueba de una sola posición con rol `rol.conflicto`, contra una situación con 3 roles, WHEN se resuelve, THEN la lista tiene exactamente un resultado distinto de SIN_COMPARACION, el de `rol.conflicto`.
- **AC-15** (E4) — GIVEN una tirada de prueba con dos posiciones de rol `rol.origen`, verdadero `tema.traicion` y leídos `tema.engano` y `tema.amor`, WHEN se resuelve, THEN la lista tiene dos entradas de `rol.origen`, con PARCIAL y NINGUNO.
- **AC-31** (E3) — GIVEN una tirada de prueba con una posición de rol `rol.orijen`, WHEN se valida, THEN la lista contiene `ROL_INEXISTENTE` con sujeto `rol.orijen`.

**Ciclo de vida y mapas**
- **AC-19a** (E6, States) — GIVEN un catálogo de prueba con `tema.traicion` deprecado, WHEN se compara leído `tema.traicion` contra verdadero `tema.traicion`, THEN da EXACTO.
- **AC-19b** (E6, States) — GIVEN el mismo catálogo, WHEN se compara leído `tema.engano` contra verdadero `tema.traicion`, THEN da PARCIAL.
- **AC-19c** (States) — GIVEN el mismo catálogo y una carta con una palabra clave de tema `tema.traicion`, WHEN se valida, THEN la lista no contiene ningún error.
- **AC-19d** (E6; *provisorio hasta Guardado*) — GIVEN una partida guardada con verdadero `tema.traicion` activo, WHEN el catálogo nuevo lo marca deprecado y se carga la partida, THEN las comparaciones dan los mismos resultados que antes.
- **AC-20a** (R5) — GIVEN el tema de mapa de prueba `mapa_a.hiperinflacion` con equivalente `tema.deuda`, WHEN se valida, THEN no hay errores y su familia es `familia.bienes`.
- **AC-20b..f** (R5) — GIVEN un tema de mapa sin equivalente, uno con equivalente `tema.inexistente`, uno cuyo equivalente es otro tema de mapa, uno cuyo equivalente está deprecado y uno que declara familia (aunque sea la misma que la del equivalente), WHEN se valida, THEN la lista contiene, respectivamente, `MAPA_SIN_EQUIVALENTE`, `MAPA_EQUIV_INEXISTENTE`, `MAPA_EQUIV_ES_DE_MAPA`, `MAPA_EQUIV_DEPRECADO` y `MAPA_DECLARA_FAMILIA`, cada uno con el tema de mapa como sujeto.
- **AC-21** (R5) — GIVEN un archivo de mapa con una entrada de identificador `tema.deuda` (cualquier campo distinto: familia, estado o nombre), WHEN se valida, THEN la lista contiene `MAPA_SOBREESCRIBE_BASE` con sujeto `tema.deuda`.
- **AC-22** (E7, R6) — GIVEN verdadero `mapa_a.hiperinflacion` (equivalente `tema.deuda`), WHEN se compara contra leído `tema.deuda`, `tema.fortuna` y `tema.amor`, THEN los resultados son EXACTO, PARCIAL y NINGUNO.
- **AC-23** (E7) — GIVEN una palabra clave de carta asociada a `mapa_a.hiperinflacion`, WHEN se valida, THEN la lista contiene `KW_TEMA_DE_MAPA` con sujeto la carta y su orientación.
- **AC-24a** (E7) — GIVEN una tabla de idioma de prueba con `«MAPA:Hiperinflación»` y `«BASE:Deuda»`, WHEN se pide el nombre visible de `mapa_a.hiperinflacion`, THEN es `«MAPA:Hiperinflación»`.
- **AC-24b** (E7; *provisorio hasta Textos por Plantillas*) — GIVEN una plantilla de sentencia con el tema verdadero `mapa_a.hiperinflacion` y la misma tabla de prueba, WHEN se arma el texto, THEN contiene `«MAPA:Hiperinflación»` y no contiene `«BASE:Deuda»`.
- **AC-32** (States) — GIVEN un catálogo anterior con `mapa_a.hiperinflacion` → `tema.deuda` y uno nuevo donde `tema.deuda` pasa a deprecado sin cambiar el tema de mapa, WHEN se valida, THEN la lista contiene `DEPRECAR_CON_DEPENDIENTES` con sujeto `tema.deuda`.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| ¿El reparto de familias (4/4/5/4/3) produce un sesgo que se note? Medir en el prototipo, con las cartas y el Generador reales, el puntaje esperado al azar por familia y la frecuencia de "tirada sin jugada útil" por familia verdadera. Meta: ninguna familia a más de ±15 % del promedio. Si Conflicto domina, la primera palanca es *secreto* (dato nuevo para revisar D-42) | Diseñador | Prototipo del núcleo |
| **Doble Fondo:** ¿contra qué rol se compara el tema del motivo? ¿La fachada puede ser de la misma familia que la verdad? (Daría parcial, y el Pilar 4 pide que la fachada rinda poco y seguro.) ¿Todos los clientes tienen Doble Fondo? ¿Qué pasa si la verdad de un rol es *secreto*? | GDD del Generador | Al diseñar el Generador |
| **Coherencia entre roles:** con 20 temas y 3 roles hay 8.000 tríos y muchos no cuentan una historia. El Generador tiene que dar una garantía mínima de coherencia antes del prototipo. Si la pide, la afinidad de cada tema con cada rol (alta / posible / evitar) puede vivir en este catálogo como dato | GDD del Generador | Al diseñar el Generador |
| **AC del Generador (ex AC-16 a AC-18):** cada situación tiene un tema por rol activo y ningún otro rol; el motivo tiene un tema activo y una forma activa; un tema deprecado nunca entra a los candidatos. Escribirlos como contrato sobre la lista de candidatos con un RNG simulado, sin semilla fija. Definir también cómo reparte las familias | GDD del Generador | Al diseñar el Generador |
| **Agregación y umbral:** cómo se combinan varias posiciones del mismo rol (suma, máximo o promedio); qué pasa si la lista no tiene ningún resultado comparable (0/0); el umbral se calibra contra la línea base de E8, porque sin castigo por error adivinar siempre conviene; ¿el feedback distingue "deduje mal" de "no tenía la carta"? | GDD de Resonancia | Al diseñar Resonancia |
| Carta Única cubre un solo rol de tres. ¿Qué rol cubre "Respuesta"? ¿Qué es la verdad de una pregunta *sí o no*, si la verdad se expresa en temas? Toda tirada tiene que tener al menos una posición con rol activo. ¿Las posiciones libres son una falsa elección para el jugador? | GDD de Tiradas | Al diseñar Tiradas |
| Roles posteriores al MVP (el otro, camino A y B) y su mapeo a posiciones | GDD de Tiradas | Al diseñar Tiradas |
| La exigencia "cada tema aparece en al menos una carta del nivel Aprendiz". ¿"Una palabra clave = un tema" deja poca palanca de lector (Pilar 6)? ¿Hace falta un tema secundario que puntúe como máximo parcial? Destino representa a los 22 Arcanos Mayores pero tiene 3 temas: ¿cuántas cartas la llevan? | GDD de Cartas | Al diseñar Cartas |
| ¿Qué señal observable distingue a cada tema de los de su familia? Si los tells no separan temas dentro de una familia, el exacto es azar | GDD de Inspección y Tells | Al diseñar Tells |
| Guardar la versión del catálogo en la partida, para detectar cambios de familia entre versiones | GDD de Guardado | Al diseñar Guardado |
| La marca de la familia es el símbolo de un palo: en una carta de otro palo (Cinco de Copas con *deuda*) puede leerse como el palo de la carta. Resolverlo en el spec del tooltip | `/ux-design`, `/art-bible` | Antes de las historias del tooltip |
| Vocabulario: glosario de una línea por tema (deseo/amor, poder/rivalidad, engaño/traición, hogar); nota de Regla Cero ("los temas describen la situación del cliente, nunca una fuerza"); nombre visible de Destino y de *locura*; renombrar *riesgo*, que es una actitud y no un asunto (*apuesta* choca con el "apostar" del Pilar 4). ¿El equivalente de *hiperinflación* es *deuda* o *fortuna*? | Diseñador | Antes de escribir los datos del catálogo |
| El GDD maestro está desfasado con esta Taxonomía en cinco puntos:<br>- El motivo de consulta (§5.3) sigue escrito como lista única y mezcla temas con cosas que no lo son: *dinero* (¿`fortuna` o `deuda`?), *salud* (`enfermedad`), *peligro* (¿`riesgo` o `violencia`?) y *decisión*, que es una forma de pregunta.<br>- §5.3, §5.8 y D-15 hablan de "temas por posición", y desde D-37 son temas por rol.<br>- §3.5 llama "la sentencia" al Futuro, y el rol es `desenlace`; "sentencia" ya es la intención retórica.<br>- *Enfermedad* pasó a Destino y se sumó *trabajo* (D-43). | Diseñador | Próxima versión del GDD maestro |
