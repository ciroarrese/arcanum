# Base de Datos de Cartas

> **Status**: Needs Revision — reescrito el 2026-10-24 (D-48) tras contar las 78 cartas contra Waite (1910); pendiente de `/design-review`
> **Creative Director Review (CD-GDD-ALIGN)**: NOT ASSESSED 2026-10-23 — omitida en modo lean
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-24
> **Last Verified**: 2026-10-23
> **Implements Pillar**: Pilar 3 (Memoria Pura: significado público), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909. Guarda los datos públicos de cada carta y 2 o 3 palabras clave por orientación, cada una con un tema de la Taxonomía y una fuente tradicional citada. Los temas salen de la tradición de 1909 y no se fuerzan: el mazo garantiza solo que cada tema exista en alguna carta y que ninguna familia desaparezca de un mazo. La verdad del cliente se sortea según lo que el mazo activo puede decir (D-48). El jugador ve este catálogo en el tooltip de cada carta.

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `Taxonomía de Temas y Roles`

## Overview

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909 (tradición Rider-Waite-Smith, arte de 1909 de dominio público). Guarda los datos públicos de cada carta:

- nombre;
- número;
- palo, o Arcano Mayor;
- elemento;
- palabras clave derechas e invertidas, cada una asociada a exactamente un tema de la Taxonomía (R7).

Es un catálogo fijo: se carga una vez y no cambia durante la partida.

Este sistema solo dice qué es cada carta y qué puede decir. Los otros sistemas toman de él lo que necesitan:

- **Mazo y Robo** baraja y reparte. De acá toma qué cartas forman cada Nivel de Mazo.
- **La Gramática** combina las cartas de la tirada. De acá lee el palo, el elemento y el número.
- **Interpretación** ofrece al jugador las palabras clave de la orientación que salió.
- **El Tapete** las muestra en el tooltip.
- **Resonancia** compara la lectura con la verdad. No toca este catálogo directamente: recibe los temas a través de Interpretación.

Además, el catálogo define qué cobertura de temas tiene que tener el mazo. De esa cobertura depende que una tirada le dé al jugador algo con qué trabajar (Pilar 6).

Sin este catálogo, la promesa de D-05 (tarot real, significados tradicionales) no tendría dónde vivir. Tampoco habría forma de conectar lo que sale en la mesa con la verdad del cliente, que la Taxonomía expresa en temas.

## Detailed Design

### Core Rules

> Redactado en modo lean, sin consultar a `systems-designer` ni a `writer`. Hay que revisarlo a mano antes de producción.

**El mazo**

1. El catálogo tiene exactamente las **78 cartas** del Smith 1909:
   - 22 Arcanos Mayores, numerados 0 a 21 en el orden de 1909 (la Fuerza es el 8 y la Justicia el 11);
   - 4 palos de 14 cartas: As a 10, más Sota (11), Caballero (12), Reina (13) y Rey (14).
2. Cada carta tiene un **identificador estable** con prefijo `carta.`: `carta.mayor_00` a `carta.mayor_21`, y `carta.<palo>_01` a `carta.<palo>_14`. Igual que en la Taxonomía (R4), un identificador nunca se renombra ni se borra, y el nombre visible sale de la tabla de idioma.
3. Campos de cada carta:

   | Campo | Valores | Nota |
   |---|---|---|
   | `id` | ver R2 | |
   | `arcano` | mayor / menor | |
   | `palo` | copas / oros / espadas / bastos; vacío en los Mayores | |
   | `numero` | 0–21 (Mayores), 1–14 (Menores) | Lo usa la Gramática para los números repetidos (§3.5.6) |
   | `elemento` | fuego / agua / aire / tierra / ninguno | Menores: Copas = agua, Oros = tierra, Espadas = aire, Bastos = fuego (coincide con R1 de la Taxonomía). Mayores: según la atribución de la Golden Dawn (§3.2); `ninguno` para las 7 planetarias hasta que se decida (Open Questions) |
   | `atribucion` | signo, planeta o elemento de la Golden Dawn | Dato público del tooltip; de acá sale `elemento` |
   | `arte` | referencia a la imagen de 1909 | Nunca la recoloración de 1971 (§3.1) |
   | `derecha`, `invertida` | 2 o 3 palabras clave cada una | R4 a R6 |

**Palabras clave**

4. Cada orientación tiene **2 o 3 palabras clave** (GDD §3.2). Cada una tiene:
   - un identificador `<id de carta>/<derecha|invertida>/<1–3>`;
   - un texto, que sale de la tabla de idioma;
   - **exactamente un tema base** (R7 de la Taxonomía);
   - una `fuente`, de la lista cerrada `waite_1910`, `book_t` o `mathers_1888`, y una `ubicacion` (página o sección, nunca vacía), para que R6 se pueda verificar.
5. **Sin cobertura forzada por carta.** Las palabras clave de una orientación pueden repetir familia y hasta tema: la variedad la da la tradición, no una regla (D-48). Cuando una orientación tiene más significados tradicionales que lugares, se eligen los que cubren familias distintas. Contadas las 78 cartas contra Waite (1910), una orientación tiene en promedio ~1,3 familias claras (Formulas).
6. **El texto manda sobre el tema.** Cada palabra clave es un significado tradicional de la carta (D-05), tomado de la tradición de 1909 (por ejemplo, *The Pictorial Key to the Tarot* de Waite, 1910, de dominio público). El tema se deriva del texto (§3.2). Nunca se inventa un significado para cumplir la cobertura (F2) ni para dar un tema a una orientación que la tradición deja sin ninguno (E2).

**Cobertura del mazo**

7. **Cada tema base activo aparece en al menos una palabra clave de las 78 cartas.** Un mazo concreto puede no tener algún tema (por ejemplo, *riesgo* no está en Mayores + Copas). Eso no rompe nada, porque el Generador solo sortea temas que el mazo activo contiene (F1, D-48).
8. **Los Mayores apuntan a cualquier familia.** La familia es del tema, no de la carta: los Mayores no van atados a Destino. Las "fuerzas fuera de tu control" de los Mayores las cubre la regla de peso de la Gramática (§3.5.5), no este catálogo. En cada mazo alcanzable (los 22 Mayores más cualquier combinación de palos, E1), cada familia aparece en al menos el **10 %** de las orientaciones (`q_f`, F2): ninguna familia puede desaparecer de un mazo.
9. Todos los datos de una carta son **públicos** (D-08, Pilar 3): nada de este catálogo es secreto ni se desbloquea.

**Validación**

10. Las reglas R1 a R8 y F2 se agregan al validador del catálogo (R13 de la Taxonomía). Un incumplimiento es un error de datos y el juego no arranca. Los sujetos de los errores siguen el formato de R13 de la Taxonomía: carta, orientación, palabra clave o mazo. Los códigos de error y sus casos se definen en las historias de implementación, no en este GDD.
11. **Informe de cobertura.** Para cada mazo alcanzable (E1), el validador produce un informe con `n_t` por tema, `c_f`, `q_f` y `u_f` por familia, los pesos de sorteo `p_t` (F1), y `P_exacto`, `P_pos`, `P_pos_inv` y `P_cero` (F3, F4). El informe no es una lista de errores. Sirve para calibrar, y de él lee el Generador los pesos `p_t` del mazo activo (D-48).

### States and Transitions

El catálogo no tiene estados: se carga una vez y no cambia durante la partida.

Entre versiones:

- Una carta nunca se borra ni cambia de identificador.
- El texto y el tema de una palabra clave **pueden** cambiar entre versiones. La partida guardada guarda la verdad del cliente, no las palabras clave, así que el cambio solo afecta a las lecturas que se hagan después.
- Una palabra clave puede seguir apuntando a un tema deprecado (Taxonomía, States).

### Interactions with Other Systems

| Sistema | Qué recibe de Cartas | Qué aporta o devuelve |
|---|---|---|
| Taxonomía de Temas y Roles | — | Los temas y familias que validan las palabras clave (R7) |
| Mazo y Robo | La lista de cartas por arcano y palo | Arma el mazo de cada Nivel de Mazo y reparte |
| Gramática de Combinación | `palo`, `elemento` y `numero` | Nada; los usa para dignidades, palo dominante y números repetidos |
| Interpretación y Sentencia | Las 2 o 3 palabras clave de la orientación que salió y su tema | La palabra clave elegida por posición |
| Generador de Situaciones | Los pesos `p_t` del mazo activo (R11, F1) | Sortea el tema verdadero de cada rol con esos pesos (D-48) |
| Tapete y Tooltips | Nombre, número, palo, `atribucion`, elemento, arte, y las palabras clave con su tema y familia | Nada; los muestra |
| Prestidigitación (indirecta, a través de Mazo y Robo) | La invertida de cada carta (para *invertir*) | Nada |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD salvo la Taxonomía.

## Formulas

Contadas las 78 cartas contra Waite (1910) —asignaciones claras, sin forzar; detalle en `design/balance/cobertura-cartas-waite.md`—, la tradición da en promedio **~1,3 familias por orientación**, y 14 de 72 orientaciones de un mazo Aprendiz no tienen ningún tema claro. Por eso el mazo no puede garantizar cobertura alta por posición, y la cobertura se resuelve del lado de la verdad: el Generador sortea lo que el mazo puede decir (F1). F2 la comprueba el validador; F1 es el contrato con el Generador; F3 y F4 son calibración.

Un **acierto de familia** es que la carta, en la orientación que salió, tenga una palabra clave de la familia de la verdad de su rol: es la condición para PARCIAL o EXACTO. Un **acierto exacto posible** pide una palabra clave del mismo tema.

**Variables**

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `N` | int | 36 (Aprendiz) a 78 | Mazo y Robo | Cartas del mazo activo |
| `O` | int | `2·N` | calculated | Orientaciones del mazo |
| `n_t` | int | 0 a `O` | calculated (catálogo) | Orientaciones del mazo con al menos una palabra clave del tema `t` |
| `c_f` | int | 0 a `O` | calculated (catálogo) | Orientaciones con al menos una palabra clave de la familia `f` |
| `q_f` | float | 0 a 1 | calculated | `c_f / O`: probabilidad de que una carta al azar, en una orientación al azar, tenga la familia `f` |
| `u_f` | float | 0 a 1 | calculated (catálogo) | Proporción de cartas cuya derecha y cuya invertida, juntas, cubren `f` |
| `p_t`, `p_f` | float | 0 a 1, suman 1 | calculated (F1) | Probabilidad de que la verdad de un rol sea el tema `t`; `p_f` = suma de `p_t` de la familia |
| `Q_min` | float | 0,10 | data file | Piso de `q_f` (Tuning Knobs) |

Supuestos: la orientación sale 50/50 y la carta es uniforme dentro del mazo.

**F1. Sorteo de la verdad según el mazo** (contrato con el Generador, D-48)

`p_t = n_t / Σ_s n_s`, sobre los temas activos del mazo activo

- **Rango:** `p_t` = 0 para un tema que el mazo no tiene, así que la verdad siempre es algo que el mazo puede decir.
- **Por qué:** con verdades uniformes, un tema ausente del mazo (*riesgo* en Mayores + Copas) daría clientes imposibles de acertar.
- **Ejemplo:** en Mayores + Copas, *culpa* (1 orientación, o 3 con vergüenza y confesión, en los otros palos) sale como verdad muy rara vez; los temas que la tradición repite salen seguido.
- **Lo que no cambia:** el Generador sigue sin conocer la tirada (D-37). El mazo activo se fija con el Nivel de Mazo al empezar la partida y cambia solo al sumar un palo en una Sede.

**F2. Piso por familia** (lo comprueba el validador)

`c_f ≥ ⌈Q_min · O⌉` para cada familia `f` y cada mazo alcanzable (E1)

- **Rango:** con 0,10: `c_f` ≥ 8 en un mazo de 36 cartas (`O` = 72) y ≥ 16 en el de 78 (`O` = 156).
- **Con los datos contados:** los 4 mazos Aprendiz lo cumplen. El mínimo es Destino en Mayores + Oros (9 de 72, `q` = 0,125).
- **Por qué solo un piso:** una banda con techo obligaría a forzar significados (R6). El piso evita que una familia desaparezca, y con eso que el PARCIAL deje de existir para esa familia.

**F3. Acierto posible por posición** (calibración)

`P_exacto = Σ_t p_t · n_t / O` · `P_pos = Σ_f p_f · q_f` · `P_pos_inv = Σ_f p_f · u_f` (con *invertir* en esa posición)

- **Rango:** de 0 a 1.
- **Con los datos contados** (Mayores + Copas): `q` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 (Emoción, Bienes, Conflicto, Ambición, Destino), `p_f` ≈ 0,23 / 0,20 / 0,23 / 0,21 / 0,13. Queda **`P_pos` ≈ 0,27**: en una posición hay acierto de familia posible algo más de 1 vez de cada 4.
- "Posible" es una cota superior: el jugador no conoce la verdad.

**F4. Tres Tiempos sin ningún acierto de familia** (calibración)

`P_cero ≈ (1 − P_pos)³`

- **Rango:** de 0 a 1.
- **Con los datos contados:** (1 − 0,274)³ ≈ **0,38**. Casi 4 de cada 10 Tres Tiempos no tienen ningún acierto de familia posible en ninguna posición, sin trucos.
- **Riesgo principal para el Pilar 6.** Las palancas que quedan son *invertir* (`P_pos_inv`), la Sentencia (Pilar 2) y un Generador que sobrepese los temas frecuentes (Open Questions). Se mide en el prototipo antes de tocar números.
- **Supuesto:** independencia entre posiciones. Si el Generador correlaciona los roles, el resultado cambia.

## Edge Cases

1. **Mazos de otro tamaño.** El nivel Aprendiz suma un palo en las Sedes 3, 5 y 7 (§3.4), así que en el MVP también hay mazos de 50 cartas. El piso F2 vale para **todo mazo alcanzable**: los 22 Mayores más cualquier combinación de 1 a 4 palos, que son 15 mazos. Al sumar un palo, el Generador recalcula `p_t` con el mazo nuevo para los clientes siguientes; los ya generados no cambian.
2. **Una orientación no tiene en Waite ningún significado con tema claro** (14 de 72 en un mazo Aprendiz). Primero se busca en otras fuentes de dominio público de la misma tradición: el *Book T* de la Golden Dawn, Mathers (1888). Si tampoco alcanza, se elige el significado tradicional más cercano a un tema y se anota en Open Questions; esa palabra clave queda marcada para la revisión de AC-11. Nunca se inventa un significado (R6).
3. **La misma palabra, el mismo tema o la misma familia en varias palabras clave de una carta.** Está permitido, en la misma orientación o entre derecha e invertida (R5).
4. **El mismo texto de palabra clave en varias cartas** (por ejemplo, *pérdida*). Está permitido: cada palabra clave tiene su propio identificador y su propio tema.
5. **Una palabra clave apunta a un tema deprecado.** Es válida (Taxonomía, States). Cuenta para `c_f` y `u_f`, porque su familia sigue dando acierto de familia contra verdades activas de esa familia. No cuenta para `n_t` de F1 ni para R7, que miran temas **activos**.
6. **Un Mayor con atribución planetaria.** Su `elemento` es `ninguno` hasta que se decida (Open Questions). Mientras tanto, la Gramática lo trata como neutro con cualquier vecina.
7. **La orientación que salió no tiene la familia de la verdad.** No hay acierto de familia posible en esa posición: el mejor resultado es NINGUNO. Cartas no lo compensa. Las palancas son *invertir* (`P_pos_inv`, F3) y la Sentencia (Pilar 2), y la frecuencia se calibra con F4.
8. **Falta el texto de una palabra clave en una tabla de idioma.** Es un error de datos del mismo tipo que `NOMBRE_FALTANTE` de la Taxonomía, con el identificador de la palabra clave como sujeto. El juego no arranca.

## Dependencies

**Depende de:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Taxonomía de Temas y Roles | Dura | Temas base, familias y el validador del catálogo (R7 y R13 de la Taxonomía) |

**Dependen de Cartas:**

| Sistema | Tipo | Qué usa |
|---|---|---|
| Mazo y Robo | Dura | Lista de cartas por arcano y palo, para armar los mazos de cada Nivel |
| Gramática de Combinación | Dura | `palo`, `elemento` y `numero` |
| Interpretación y Sentencia | Dura | Las 2 o 3 palabras clave de la orientación que salió y su tema |
| Tapete y Tooltips de Cartas | Dura | Todos los datos públicos de la carta y el arte |
| Prestidigitación | Blanda, indirecta | La invertida (*invertir*), a través de Mazo y Robo |
| Generador de Situaciones | Dura | Los pesos `p_t` del mazo activo, para sortear la verdad (F1, D-48). Hay que sumarla al índice |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Cartas en su tabla de dependientes.
- Los demás sistemas no tienen GDD todavía. La sección Dependencies de cada uno tiene que nombrar a Cartas cuando se escriba.
- El Generador depende de Cartas por F1: `systems-index.md` lo refleja (D-48).

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Palabras clave por orientación | 2 a 3 | Mínimo 1, máximo 4. Con más no se gana cobertura si la tradición no la tiene, y el tooltip se recarga | Volumen de contenido, legibilidad del tooltip |
| `Q_min` (piso de `q_f` por familia) | 0,10 | 0,05 a 0,12 con los datos contados (Destino en Mayores + Oros está en 0,125) | Que ninguna familia desaparezca de un mazo (F2) |

El validador lee estos valores del archivo de configuración; no los tiene fijos en el código. La forma del sorteo de F1 (proporcional a `n_t`) es una perilla del Generador, no de este catálogo.

## Visual/Audio Requirements

- El arte de cada carta es el escaneo de la edición de 1909 (Pamela Colman Smith), nunca la recoloración de 1971 (§3.1). La fuente de referencia de los escaneos la fija `/art-bible`, con validación legal previa a la producción de arte (§3.1).
- Una carta invertida es la misma imagen rotada 180°; no hay arte propio para la invertida.
- No hay sonido propio de este sistema.

## Game Feel

No aplica: el catálogo no se opera directamente. El feel de robar y dar vuelta una carta le corresponde a Mazo y Robo y al Tapete.

## UI Requirements

- El tooltip de una carta muestra sus datos públicos: nombre, número, palo o Arcano Mayor, atribución y elemento.
- Muestra también las palabras clave de **las dos orientaciones** (Pilar 3, §3.3), con la orientación que salió destacada. Cada palabra clave lleva su tema y su familia, con la marca de la familia (Taxonomía, UI Requirements).
- La `fuente` y la `ubicacion` no se muestran en el MVP; mostrarlas como cita es decisión de `/ux-design`.

> 📌 **UX Flag — Base de Datos de Cartas:** el tooltip muestra de 4 a 6 palabras clave con tema y familia. Antes de las historias del tooltip hay que hacer su spec con `/ux-design`, junto con el de la Taxonomía, incluida la legibilidad en Switch portátil.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.1, §3.2, §3.3 | Smith 1909 y restricciones legales; anatomía de la carta; datos públicos |
| GDD §3.4 | Niveles de Mazo; los palos que se suman en las Sedes 3, 5 y 7 (E1) |
| GDD §3.5 | Elemento, palo y número para la Gramática; peso de los Mayores |
| GDD §5.5, §9.2 | Interpretación por palabra clave; el truco *invertir* |
| D-05, D-06, D-08, D-09, D-18, D-22 | Tarot real; escuelas; significado público; robo al azar; 78 cartas; Nivel de Mazo |
| D-47 | `fuente`, informe de cobertura y sujetos de R13 |
| D-48 | Conteo de las 78 cartas contra Waite (1910); cobertura según la tradición; piso por familia; sorteo de la verdad según el mazo; 3 temas de resultado en la Taxonomía |
| Taxonomía R4, R7, R13, States | Identificadores; un tema por palabra clave; validador y formato de sujetos; temas deprecados |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_catalogo_valido` (78 cartas sintéticas con ids reales, textos centinela y `taxonomia_prueba`) y lo **muta en un solo punto**. AC-01 prueba que el fixture sin mutar pasa limpio.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "no contiene error de la regla X con sujeto S", nunca "no hay errores".
- Que el juego no arranque lo prueban AC-25a/b de la Taxonomía; que cada palabra clave tenga exactamente un tema, AC-03a–c de la Taxonomía. No se repiten acá.
- **Evidencia:** todos son Logic (test unitario en `[test root]/cartas/`), salvo los marcados Integration, UI o Config/Data. Los *provisorios* dependen de un GDD que no existe y no bloquean hasta que exista.

**Estructura**
- **AC-01** (R1–R11) — GIVEN `fixture_catalogo_valido`, WHEN se valida, THEN la lista está vacía.
- **AC-02a** (R1) — GIVEN el fixture sin `carta.copas_05`, WHEN se valida, THEN contiene error de R1 con sujeto `carta.copas_05`.
- **AC-02b** (R1) — GIVEN el fixture con `carta.mayor_09` de número 8, WHEN se valida, THEN contiene error de R1 con sujeto `carta.mayor_09`.
- **AC-03** (R2) — GIVEN el fixture con una carta de id `carta.copas_15`, WHEN se valida, THEN contiene error de R2 con sujeto `carta.copas_15`.
- **AC-04a** (R3) — GIVEN el fixture con `carta.copas_05` de elemento fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.copas_05`.
- **AC-04b** (R3) — GIVEN el fixture y la tabla `tabla_gd_prueba` (atribución → elemento, armada a mano y no derivada del catálogo), con `carta.mayor_04` de elemento agua cuando la tabla dice fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.mayor_04`. Control: un Mayor planetario con `ninguno` no da error de R3.
- **AC-04c** (R1, R3; Integration) — GIVEN los datos reales y `tabla_gd_prueba`, WHEN se cargan, THEN `carta.mayor_08` tiene atribución Leo y `carta.mayor_11` Libra; cada Mayor tiene el elemento de la tabla, y `ninguno` los 7 planetarios; cada palo tiene el elemento de R3.

**Palabras clave**
- **AC-05a** (R4) — GIVEN el fixture con 1 palabra clave en `carta.copas_05/derecha`, WHEN se valida, THEN contiene error de R4 con ese sujeto. Lo mismo con 4. Control: con 2 y con 3, no lo contiene.
- **AC-05b** (R4, Tuning Knobs) — GIVEN la configuración con máximo 4 palabras clave por orientación y `carta.copas_05/derecha` con 4, WHEN se valida, THEN no contiene error de R4 con ese sujeto.
- **AC-06** (R5) — GIVEN `carta.copas_05/derecha` con sus 3 palabras clave de la misma familia de `taxonomia_prueba`, WHEN se valida, THEN no contiene error con ese sujeto.
- *AC-07 se retiró el 2026-10-24 (D-48: no hay mínimo de familias por carta). Su número no se reutiliza.*
- **AC-08** (R7) — GIVEN el fixture donde `tema.locura` no aparece en ninguna palabra clave de las 78 cartas, WHEN se valida, THEN contiene error de R7 con sujeto `tema.locura`. Control: si aparece en una sola palabra clave de un palo, no lo contiene.
- **AC-09a** (E5) — GIVEN el fixture con `tema.traicion` deprecado y una palabra clave que lo usa y que lleva `c_Conflicto` del mazo `copas` de 7 a 8, WHEN se valida, THEN no contiene error de F2 con sujeto `copas/familia.conflicto`.
- **AC-09b** (E5, F1) — GIVEN `tema.traicion` deprecado y presente en palabras clave del mazo `copas`, WHEN se pide el informe, THEN `n_t` de `tema.traicion` no entra en los pesos `p_t`.
- **AC-10** (R3, R6) — GIVEN `carta.copas_05/derecha/1` sin `fuente`, con una `fuente` fuera de la lista o con `ubicacion` vacía (un caso cada uno), WHEN se valida, THEN contiene error de R6 con ese sujeto.
- **AC-11** (R6; Config/Data, revisión manual) — GIVEN los datos reales, WHEN se revisa la palabra clave 1 de la derecha de cada una de las 78 cartas, THEN su texto está en la `fuente` y la `ubicacion` citadas. El resultado queda en `production/qa/`.
- **AC-12** (E3) — GIVEN `carta.copas_05` con el mismo tema en la derecha y en la invertida, WHEN se valida, THEN no contiene error con sujeto `carta.copas_05`.
- **AC-13** (E4) — GIVEN el mismo texto en `carta.copas_05/derecha/1` y `carta.oros_05/derecha/1`, WHEN se valida, THEN no contiene error de identificador duplicado.
- **AC-14** (E8) — GIVEN la tabla `es_prueba` sin el texto de `carta.copas_05/derecha/2`, WHEN se valida, THEN contiene error con sujeto `carta.copas_05/derecha/2@es_prueba`.

**Cobertura**
- **AC-15a** (F2) — GIVEN el fixture mutado para que el mazo `copas` tenga `c_Destino` = 7, WHEN se valida, THEN contiene error de F2 con sujeto `copas/familia.destino`. Con 8, no lo contiene.
- **AC-15b** (F2, E1; parametrizado) — GIVEN, para cada uno de los 15 mazos alcanzables, el fixture mutado para que solo ese mazo quede bajo el piso en `familia.destino`, WHEN se valida, THEN contiene exactamente un error de F2, con el sujeto de ese mazo.
- **AC-15c** (F2; borde en enteros) — GIVEN el mazo `copas+oros+espadas+bastos` (`O` = 156), WHEN `c_Destino` vale 16, THEN no contiene error de F2; con 15, sí.
- *AC-16 se retiró el 2026-10-24 (D-48: sin piso de* invertir*). Su número no se reutiliza.*
- **AC-17** (Tuning Knobs) — GIVEN la configuración con `Q_min` = 0,15 y el mazo `copas` con `c_Destino` = 10, WHEN se valida, THEN contiene error de F2 (hace falta 11). Con 11, no lo contiene.

**Informe de cobertura (R11)**
- **AC-18a** (R11) — GIVEN el fixture, WHEN se pide el informe, THEN para cada mazo `n_t`, `c_f`, `q_f` = `c_f / O` y `u_f` coinciden con las cuentas del fixture.
- **AC-18b** (R11, F1) — GIVEN un mazo de prueba con `n_t` = 6, 3 y 1 para tres temas y 0 para el resto, WHEN se pide el informe, THEN `p_t` = 0,6 / 0,3 / 0,1 y 0 para los temas ausentes.
- **AC-18c** (R11, F3, F4) — GIVEN `q` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 y `p_f` = 0,23 / 0,20 / 0,23 / 0,21 / 0,13 (orden Emoción, Bienes, Conflicto, Ambición, Destino), WHEN se calcula, THEN `P_pos` = 0,276 ± 0,002 y `P_cero` = 0,380 ± 0,003.
- **AC-18d** (F1, D-48; *provisorio hasta el Generador*) — GIVEN un mazo activo sin ninguna palabra clave de `tema.riesgo`, WHEN el Generador sortea 1.000 verdades con un RNG simulado, THEN ninguna es `tema.riesgo`.

**Datos reales y otros**
- **AC-19** (R10; Integration) — GIVEN el catálogo, las cartas y las tablas de idioma reales, WHEN se valida, THEN la lista está vacía. Bloquea la historia de contenido, no la del validador.
- **AC-20** (R3; UI, *provisorio hasta `/art-bible`*) — GIVEN la fuente de referencia de los escaneos de 1909, WHEN se revisan las 78 `arte`, THEN todas apuntan a esa fuente, y una revisión manual con captura retenida en `production/qa/evidence/` confirma que ninguna es la recoloración de 1971.
- **AC-21** (States; Integration, *provisorio hasta Guardado*) — GIVEN una partida guardada, WHEN se carga con una versión del catálogo que cambió el texto de una palabra clave, THEN la verdad del cliente no cambia.
- Lo que muestra el tooltip (R9) lo prueban los AC de Tapete y Tooltips (`/ux-design`).

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| Elemento de los 7 Mayores con atribución planetaria (Mago, Sacerdotisa, Emperatriz, Rueda, Torre, Sol, Mundo): ¿neutro, el del planeta según otra tradición, o un elemento propio? | GDD de Gramática | Al diseñar la Gramática |
| Forma del sorteo de F1: ¿proporcional a `n_t`, o con sobrepeso (`n_t^k`, k > 1) para subir `P_pos`? ¿Los roles de una situación se sortean independientes o con afinidad (`afinidad_por_rol` de la Taxonomía)? | GDD del Generador | Al diseñar el Generador |
| **Riesgo del Pilar 6:** con la tradición, `P_cero` ≈ 0,38 en Tres Tiempos (F4). Medir en el prototipo si es jugable con *invertir* y la Sentencia, o si hace falta más palanca (sobrepeso del sorteo, más trucos, el Generador mirando la tirada). La meta de 0,15 de la versión anterior no se alcanza con datos tradicionales | Diseñador | Prototipo del núcleo |
| Orientaciones sin tema claro en Waite (E2): unas 14 por mazo Aprendiz. Buscarlas en el *Book T* y en Mathers antes de cargar los datos | Diseñador | Al escribir los datos de las 36 cartas del MVP |
| El conteo de D-48 lo hizo una sola lectura (diseñador más IA), con criterio de "asignación clara". Antes de cargar los datos, hace falta una segunda lectura independiente de las 36 cartas del MVP | Diseñador | Al escribir los datos |
| Traducción de las palabras clave del inglés de Waite al español rioplatense: ¿la `ubicacion` cita el original, y quién valida que la traducción no cambie el tema? | Diseñador, `/localize` | Al escribir los datos |
| Fuente de referencia de los escaneos de 1909 y validación legal | `/art-bible` | Antes de producir arte |
