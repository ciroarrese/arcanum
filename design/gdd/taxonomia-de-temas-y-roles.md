# Taxonomía de Temas y Roles

> **Status**: In Design
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-22
> **Last Verified**: 2026-10-22
> **Implements Pillar**: Regla Cero, Pilar 3 (Memoria Pura), Pilar 6 (No hay Carta Mala)
> **Creative Director Review (CD-GDD-ALIGN)**: skipped — Lean mode

## Summary

La Taxonomía es el diccionario común de la lectura. Tiene 19 temas agrupados en 5 familias, que siguen a los palos del tarot más los Arcanos Mayores, y tiene roles narrativos (origen, conflicto, desenlace). Con ese diccionario, las cartas, el cliente generado, las tiradas y los textos hablan el mismo idioma. Define también cuándo una lectura acierta exacto (mismo tema), a medias (misma familia) o no acierta. El jugador la ve en el tooltip de cada carta, como tema y familia.

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

> `systems-designer`, `game-designer` y `narrative-director` no fueron consultados — modo Lean. Revisar a mano antes de producción.

**Temas y familias**

1. Hay **5 familias fijas**: una por palo y una para los Arcanos Mayores. No se agregan familias nuevas, porque salen de la estructura del tarot (GDD §3.5).

   | Familia | Palo / elemento | Campo | Temas del MVP |
   |---|---|---|---|
   | Emoción | Copas / Agua | lo que se siente | amor, culpa, duelo, deseo |
   | Bienes | Oros / Tierra | lo que se tiene o se pierde | deuda, fortuna, enfermedad, hogar |
   | Conflicto | Espadas / Aire | lo que se enfrenta | traición, ley, violencia, engaño |
   | Ambición | Bastos / Fuego | lo que se busca | poder, rivalidad, fama, riesgo |
   | Destino | Arcanos Mayores | lo que no se controla | muerte, secreto, locura |

   Son 19 temas e incluyen los diez de ejemplo del GDD §3.2.
2. Cada tema pertenece a **exactamente una familia**. Una carta puede llevar temas de cualquier familia: un Cinco de Copas puede hablar de *deuda*.
3. Cada tema tiene un **identificador estable** (por ejemplo `traicion`), separado del nombre que se muestra, que se traduce. El identificador nunca se renombra ni se borra: si un tema deja de usarse, se marca como deprecado.
4. Los mapas pueden **agregar temas**, siempre dentro de una de las 5 familias. Ningún mapa cambia temas existentes.

**Comparación (la regla que usa la Resonancia)**

5. Comparar el tema leído con el tema verdadero da uno de tres resultados:
   - **exacto:** es el mismo tema;
   - **parcial:** son de la misma familia;
   - **ninguno:** son de familias distintas.

   El puntaje de cada resultado (2, 1 y 0 en el GDD §5.8) lo define Resonancia, no este documento.
6. El tema leído es el de **la palabra clave que el jugador elige** para la carta. Cada palabra clave derecha o invertida se asocia a **exactamente un tema**.

**Roles**

7. Roles del MVP: **origen**, **conflicto** y **desenlace**. Roles planificados para después del MVP *(provisorios hasta el GDD de Tiradas)*: **el otro**, **camino A** y **camino B**.
8. Cada posición de una tirada se traduce a **un rol o a "libre"**. Una posición libre no se compara contra la verdad, pero sus cartas cuentan para la gramática de combinación. Esto permite agregar tiradas grandes, como la Cruz Celta, sin inventar un rol por casillero.
9. El Generador asigna **un tema a cada rol activo**, porque todavía no sabe qué tirada se va a usar.

**Motivo de consulta**

10. El motivo tiene dos partes:
    - un **tema**, tomado de esta lista, que es de qué dice venir a hablar el cliente;
    - una **forma de pregunta**: *sí o no*, *situación general*, *dilema*, *vínculo* o *asunto grave*. La forma sugiere la tirada esperada (GDD §5.4). En el MVP solo existen *sí o no* y *situación general*.

    El tema del motivo puede no coincidir con la verdad: eso es el Doble Fondo, que lo decide el Generador.

### States and Transitions

| Estado de un tema | Significa | Transición |
|---|---|---|
| Activo | Lo pueden usar cartas, situaciones y textos | → Deprecado, si se deja de usar |
| Deprecado | No se generan situaciones nuevas con él; las partidas guardadas que lo tengan siguen funcionando | Fin; nunca vuelve a reutilizarse su identificador |

Fuera de este ciclo de vida, la taxonomía no cambia durante la partida: es un catálogo fijo de datos.

### Interactions with Other Systems

| Sistema | Qué recibe de la Taxonomía | Qué le devuelve o aporta |
|---|---|---|
| Base de Datos de Cartas | Lista de temas | Cada palabra clave, asociada a un tema |
| Generador de Situaciones | Temas, familias, roles activos y formas de pregunta | Un tema por rol, más el motivo (tema y forma) |
| Tiradas | Roles | La traducción de cada posición a un rol o a "libre" |
| Resonancia y Resolución | La regla de comparación (exacto, parcial, ninguno) | Nada; la consume |
| Gramática de Combinación | Familia de cada palo | Nada; la usa para el bono por palo dominante |
| Arquetipos y Pieles de Mapa | Temas | Los temas típicos de cada arquetipo y de sus secretos |
| Textos por Plantillas | Nombre visible de cada tema y rol | Nada; los usa para armar preguntas y sentencias |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD todavía.

## Edge Cases

1. **Una palabra clave sin tema, con dos temas, o un tema en dos familias.** Es un error de datos. El juego no arranca y nombra la carta o el tema mal cargado. Nunca se resuelve en silencio.
2. **La situación tiene un rol que la tirada no cubre** (por ejemplo, Carta Única frente a un cliente con origen, conflicto y desenlace). Solo se comparan los roles que la tirada cubre; los demás no suman ni restan. Qué rol cubre cada posición lo define el GDD de Tiradas.
3. **Una posición pide un rol que la situación no tiene** (roles posteriores al MVP, como "el otro"). La posición se trata como **libre**: no se compara, pero sus cartas cuentan para la gramática.
4. **Dos posiciones con el mismo rol** (por ejemplo, en la Cruz Celta). Las dos se comparan contra el mismo tema verdadero. Está permitido.
5. **El jugador no elige palabra clave para una carta.** El resultado es **ninguno**. No hay castigo extra.
6. **Una partida guardada con un tema deprecado.** Se carga y resuelve normal. El tema deja de aparecer solo en situaciones nuevas.
7. **Temas propios de un mapa.** Las cartas se comparten entre mapas, así que usan solo temas base. Cada tema de mapa declara un **tema base equivalente** (por ejemplo, *hiperinflación* → *deuda*). Leer el tema base contra la verdad del tema de mapa cuenta como **exacto**. Los textos muestran el nombre del tema de mapa.
8. **La familia Destino es heterogénea.** Que *muerte* contra *locura* cuente como parcial tiene menos sentido que *traición* contra *engaño*. Se acepta en el MVP y se mide en el prototipo; si se siente arbitrario, se revisa antes de sumar más temas a Destino.

## Dependencies

**Depende de:** ninguno (capa Foundation).

**Dependen de la Taxonomía:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Base de Datos de Cartas | Dura | Asocia cada palabra clave a un tema |
| Generador de Situaciones | Dura | Temas por rol, motivo (tema y forma de pregunta) |
| Tiradas | Dura | Traduce cada posición a un rol o a "libre" |
| Resonancia y Resolución | Dura | Regla de comparación exacto / parcial / ninguno |
| Arquetipos y Pieles de Mapa | Dura | Temas típicos de cada arquetipo y sus secretos |
| Textos por Plantillas | Dura | Nombres visibles de temas y roles |
| Gramática de Combinación | Blanda | Familia de cada palo, para el palo dominante |
| Preguntas Capciosas | Blanda, indirecta | Pregunta por temas a través del Generador y de Textos |

**Bidireccionalidad:** ninguno de estos sistemas tiene GDD todavía. La sección Dependencies de cada uno tiene que nombrar a la Taxonomía cuando se escriba. Resonancia y Gramática de Combinación se agregan como dependientes directos en `systems-index.md`.

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

> 📌 **UX Flag — Taxonomía de Temas y Roles:** antes de escribir las historias de implementación hay que hacer el spec del tooltip con `/ux-design`.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.2, §3.3 | Temas derivados de las palabras clave; temas públicos |
| GDD §3.5 | Palos y elementos → familias |
| GDD §5.3 | Motivo de consulta, separado en tema y forma de pregunta |
| GDD §5.4 | Tirada esperada según la forma de pregunta |
| GDD §5.8 | Match 0/1/2 → exacto / parcial / ninguno |
| D-08, D-37, D-39 | Significado público; desacople entre Generador y Tiradas; paleta de 1909 |

## Acceptance Criteria

Sin sección Formulas (la Taxonomía no define reglas numéricas): los criterios salen de Core Rules y Edge Cases. Los marcados *provisorio* dependen de un GDD que todavía no existe y se revisan cuando se escriba.

> Criterios revisados con `qa-lead` (modo Lean, sección de alto riesgo).

**Datos del catálogo**
- **AC-01** (R1) — GIVEN el catálogo del MVP, WHEN se carga, THEN hay exactamente 5 familias y 19 temas: Emoción `amor`, `culpa`, `duelo`, `deseo`; Bienes `deuda`, `fortuna`, `enfermedad`, `hogar`; Conflicto `traicion`, `ley`, `violencia`, `engano`; Ambición `poder`, `rivalidad`, `fama`, `riesgo`; Destino `muerte`, `secreto`, `locura`.
- **AC-02** (R3) — GIVEN dos tablas de nombres visibles de prueba (español y una segunda de prueba), WHEN se cambia de tabla, THEN el identificador de cada tema no cambia y su nombre visible sí.
- **AC-03** (R6, E1) — GIVEN un archivo de cartas con una palabra clave sin tema o con dos, WHEN se carga, THEN el juego no arranca y muestra un error que nombra la carta y la palabra clave.
- **AC-04** (R2, E1) — GIVEN un catálogo con un tema en dos familias, WHEN se carga, THEN el juego no arranca y muestra un error que nombra el tema.
- **AC-05** (R3, States) — GIVEN un tema nuevo con el mismo identificador que uno deprecado, WHEN se carga, THEN el juego no arranca y muestra un error que nombra el identificador.

**Comparación**
- **AC-06** (R5) — GIVEN leído `traicion` y verdadero `traicion`, WHEN se comparan, THEN el resultado es exacto.
- **AC-07** (R5) — GIVEN leído `engano` y verdadero `traicion`, WHEN se comparan, THEN el resultado es parcial.
- **AC-08** (R5) — GIVEN leído `amor` y verdadero `deuda`, WHEN se comparan, THEN el resultado es ninguno.
- **AC-09** (R5, E8; regresión) — GIVEN leído `muerte` y verdadero `locura`, WHEN se comparan, THEN el resultado es parcial.
- **AC-10** (R6) — GIVEN una carta cuyas palabras clave derecha e invertida tienen temas distintos, WHEN la invertida es la seleccionada, THEN el tema que entra a la comparación es el de la invertida.
- **AC-11** (E5) — GIVEN una posición comparable sin palabra clave seleccionada, WHEN se resuelve, THEN el resultado es ninguno.

**Roles y posiciones** *(provisorios hasta el GDD de Tiradas; usan tiradas de prueba)*
- **AC-12** (R8) — GIVEN una tirada de prueba con una posición libre, WHEN se resuelve, THEN esa posición no produce resultado de comparación y su carta está en la lista que recibe la Gramática.
- **AC-13** (E3) — GIVEN una posición con rol `el otro` contra una situación sin ese rol, WHEN se resuelve, THEN la posición no produce resultado de comparación y su carta está en la lista que recibe la Gramática.
- **AC-14** (E2) — GIVEN una tirada de prueba de una sola posición con rol `conflicto`, contra una situación con 3 roles, WHEN se resuelve, THEN hay exactamente un resultado de comparación, el de `conflicto`.
- **AC-15** (E4) — GIVEN una tirada de prueba con dos posiciones de rol `origen`, WHEN se resuelve, THEN ambas se comparan contra el mismo tema verdadero.

**Generación** *(provisorios hasta el GDD del Generador)*
- **AC-16** (R7, R9) — GIVEN 1.000 situaciones del MVP con semilla fija, WHEN se inspeccionan, THEN cada una tiene exactamente un tema para `origen`, `conflicto` y `desenlace`, y ningún otro rol.
- **AC-17** (R10) — GIVEN 1.000 clientes del MVP con semilla fija, WHEN se inspeccionan, THEN cada motivo tiene un tema del catálogo y una forma de pregunta que es *sí o no* o *situación general*.
- **AC-18** (States) — GIVEN un tema deprecado, WHEN se generan 1.000 situaciones con semilla fija, THEN ninguna lo usa.

**Ciclo de vida y mapas**
- **AC-19** (E6; *provisorio hasta Guardado*) — GIVEN una situación cargada cuyo tema verdadero está deprecado, WHEN se lee ese tema, THEN da exacto; WHEN se lee otro de su familia, THEN da parcial; y no hay error.
- **AC-20** (R4) — GIVEN un tema de mapa de prueba *hiperinflación* en la familia Bienes, con equivalente `deuda`, WHEN se carga, THEN se acepta; GIVEN uno sin familia o sin equivalente, THEN el juego no arranca y muestra un error que lo nombra.
- **AC-21** (R4) — GIVEN un mapa que cambia la familia de un tema base, WHEN se carga, THEN el juego no arranca y muestra un error que nombra el tema.
- **AC-22** (E7) — GIVEN leído `deuda` y verdadero *hiperinflación*, WHEN se comparan, THEN el resultado es exacto.
- **AC-23** (E7) — GIVEN una palabra clave de carta asociada a un tema de mapa, WHEN se carga, THEN el juego no arranca y muestra un error que nombra la carta.
- **AC-24** (E7; *provisorio hasta Textos por Plantillas*) — GIVEN una sentencia cuyo tema verdadero es *hiperinflación*, WHEN se arma el texto, THEN muestra el nombre del tema de mapa, no el de `deuda`.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| ¿Un parcial en Destino (*muerte* contra *locura*) se siente arbitrario? Umbral propuesto (a calibrar, sin fuente): se revisa si más del 30 % de los testers lo marca como injusto | Diseñador | Prototipo del núcleo |
| La exigencia "cada tema aparece en al menos una carta del nivel Aprendiz" | GDD de Cartas | Al diseñar Cartas |
| Roles posteriores al MVP (el otro, camino A y B) y su mapeo a posiciones | GDD de Tiradas | Al diseñar Tiradas |
| El motivo de consulta en el GDD maestro §5.3 sigue escrito como lista única | Diseñador | Próxima versión del GDD maestro |
