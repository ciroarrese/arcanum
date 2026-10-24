# Base de Datos de Cartas

> **Status**: In Review — reescrito el 2026-10-24 (D-48); `/design-review` lean (NEEDS REVISION) y full (NEEDS REVISION) del 2026-10-24, las dos corregidas el mismo día; pendiente de re-revisión
> **Creative Director Review (CD-GDD-ALIGN)**: NEEDS REVISION 2026-10-24 (revisión full), corregida
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-24
> **Last Verified**: 2026-10-24
> **Implements Pillar**: Pilar 3 (Memoria Pura: significado público), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909. Guarda los datos públicos de cada carta y de 2 a 3 palabras clave por orientación (1 en unas pocas excepciones), cada una con un tema de la Taxonomía y una fuente tradicional citada. Los temas salen de la tradición de 1909 y no se fuerzan: el mazo garantiza solo que cada tema exista en alguna carta y que ninguna familia desaparezca de un mazo. La verdad del cliente se sortea según lo que el mazo activo puede decir (D-48). El jugador ve este catálogo en el tooltip de cada carta.

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

> Revisado en modo full el 2026-10-24 (`game-designer`, `systems-designer`, `qa-lead`, `creative-director`). Sin consultar a `writer`: los textos de las palabras clave se revisan con AC-11.

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
   | `atribucion` | Mayores: signo, planeta o elemento de la Golden Dawn. Menores 2 a 10: signo y planeta del decanato según el *Book T*. As y figuras (Sota, Caballero, Reina, Rey): vacía | Dato público del tooltip. En los Mayores de acá sale `elemento`; en los Menores `elemento` sale siempre del palo, nunca del decanato. La tabla de decanatos se verifica contra el *Book T* al cargar los datos (Open Questions) |
   | `arte` | referencia a la imagen de 1909 | Nunca la recoloración de 1971 (§3.1) |
   | `derecha`, `invertida` | de 2 a 3 palabras clave cada una (1 en las excepciones de R4) | R4 a R6 |

**Palabras clave**

4. Cada orientación tiene **de 2 a 3 palabras clave** (GDD §3.2). Los límites salen de la perilla de Tuning Knobs, no del código. **Excepción:** las orientaciones de una lista cerrada `orientaciones_con_una` (un archivo de datos) pueden tener **1 sola**. Entran ahí solo cuando ninguna fuente de la lista da más de un significado para esa orientación (E2). Cada palabra clave tiene:
   - un identificador `<id de carta>/<derecha|invertida>/<n>`, con `n` de 1 hasta el máximo de la perilla;
   - un texto, que sale de la tabla de idioma;
   - **exactamente un tema base** (R7 de la Taxonomía);
   - una `fuente`, de la lista cerrada `waite_1910`, `book_t` o `mathers_1888`, y una `ubicacion` (página o sección, nunca vacía), para que R6 se pueda verificar;
   - `forzada` (sí / no, por defecto no): sí cuando el tema es el más cercano disponible porque la tradición no da uno claro (R6, E2);
   - `debilitada` (sí / no, por defecto no): sí solo en la palabra clave de una orientación sin ninguna fuente, que se lee como su derecha debilitada (E2 paso 4). Lleva el tema de una palabra clave de la derecha, va con `forzada` = sí, cita como `fuente` la que documenta la práctica y solo puede estar en una orientación de `orientaciones_con_una`.
5. **Sin cobertura forzada por carta.** Las palabras clave de una orientación pueden repetir familia y hasta tema: la variedad la da la tradición, no una regla (D-48). Cuando una orientación tiene más significados tradicionales que lugares, se eligen los que cubren familias distintas y, a igual familia, temas distintos: cada tema más es una elección más para el jugador (Pilar 6). Contadas las 78 cartas contra Waite (1910), una orientación tiene en promedio ~1,3 familias claras (Formulas).
6. **El texto manda sobre el tema.** Cada palabra clave es un significado tradicional de la carta (D-05), tomado de la tradición de 1909 (por ejemplo, *The Pictorial Key to the Tarot* de Waite, 1910, de dominio público). El tema se deriva del texto (§3.2). Nunca se inventa un significado para cumplir la cobertura (F2). Cuando el significado es real pero ningún tema encaja con claridad, se asigna el tema más cercano y la palabra clave se marca `forzada` (E2). Marcar como clara una que no lo es incumple esta regla, y lo revisa AC-11. Una palabra clave `forzada` se puede leer y da EXACTO o PARCIAL como cualquier otra, pero en el sorteo (F1) pesa `w_forz`, no hace sorteable a un tema por sí sola, y no cuenta para el piso F2 ni para R7.

**Cobertura del mazo**

7. **Cada tema base activo aparece en al menos una palabra clave clara de las 78 cartas.** Un mazo concreto puede no tener algún tema (por ejemplo, *riesgo* no está en Mayores + Copas). Eso no rompe nada, porque el Generador solo sortea temas que el mazo activo dice con claridad (F1, D-48). Un tema con una sola orientación clara en las 78 cartas (hoy, *culpa*) es frágil: si una relectura de los datos la reclasifica, R7 falla. El informe lo marca (R11).
8. **Los Mayores apuntan a cualquier familia.** La familia es del tema, no de la carta: los Mayores no van atados a Destino. Las "fuerzas fuera de tu control" de los Mayores las cubre la regla de peso de la Gramática (§3.5.5), no este catálogo. En cada mazo alcanzable (los 22 Mayores más cualquier combinación de palos, E1), cada familia aparece en al menos `Q_min` de las orientaciones (`q_f`, F2; hoy 10 %), contando solo palabras clave claras: ninguna familia puede desaparecer de un mazo.
9. Todos los datos de una carta son **públicos** (D-08, Pilar 3): nada de este catálogo es secreto ni se desbloquea.

**Validación**

10. Las reglas R1 a R8 (incluidas la lista de excepciones de R4 y los campos `forzada` y `debilitada`), F2 y `MAZO_SIN_VERDADES` (F1) se agregan al validador del catálogo (R13 de la Taxonomía). Un incumplimiento es un error de datos y el juego no arranca. Los sujetos de los errores siguen el formato de R13 de la Taxonomía: carta, orientación, palabra clave o mazo. Los códigos de error y sus casos se definen en las historias de implementación, no en este GDD.
11. **Informe de cobertura.** Para cada mazo alcanzable (E1), el validador produce un informe con:
    - por tema: `n_t^clara`, `n_t^forz`, `n_t`, `n_t⁺` y `p_t` (F1), con los temas frágiles (R7) marcados;
    - por familia: `c_f`, `c_f⁺`, `q_f`, `u_f`, `p_f` y `P_fallo_f` (F3), con la marca de `P_fallo_max`;
    - por mazo: la cantidad de palabras clave `forzada`, las orientaciones sin elección (todas sus palabras clave del mismo tema, o una sola), `P_exacto`, `P_pos`, `P_pos⁺`, `P_pos_inv`, `P_cero` (F3, F4) y `V_prior` (F5), con las marcas de F4 (progresión) y F5.

    El informe no es una lista de errores, y ninguna marca impide arrancar el juego. Sirve para calibrar, y de él lee el Generador los pesos `p_t` del mazo activo (D-48). Cumple siempre `q_f ≤ u_f ≤ 2·q_f`.
12. **Interfaz** (amplía R13 de la Taxonomía). Todas son funciones puras, sin estado:
    - `validar_catalogo` recibe además, de Cartas: `config` (las perillas de Tuning Knobs), `orientaciones_con_una` y el oráculo `atribuciones_gd`, un archivo de datos con una fila por Mayor y por decanato, cada una con su cita del *Book T*, armado desde la fuente y no desde el catálogo;
    - `informe_cobertura(cartas, catálogo, config) → informe por mazo alcanzable` (R11);
    - F1, F3, F4 y F5 se pueden llamar con entradas arbitrarias, incluso mazos que no son alcanzables, para probarlas;
    - `acierto_posible(carta, orientación, tema verdadero, catálogo) → EXACTO | PARCIAL | NINGUNO`: el mejor resultado que permite alguna palabra clave de esa orientación. Es la consulta que necesitan Tiradas y Resonancia para la "carta muda" (E7);
    - `MAZO_SIN_VERDADES`: el mazo no tiene ningún tema sorteable (F1). Sujeto: el mazo, en el formato de R13 sin familia (`copas+oros`).

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
| Interpretación y Sentencia | Las palabras clave de la orientación que salió (de 1 a 3) y su tema | La palabra clave elegida por posición |
| Tiradas y Resonancia | `acierto_posible` (R12) | Deciden qué pasa con una carta muda (E7) |
| Generador de Situaciones | Los pesos `p_t` del mazo activo (R11, F1) | Sortea el tema verdadero de cada rol con esos pesos (D-48) |
| Tapete y Tooltips | Nombre, número, palo, `atribucion`, elemento, arte, y las palabras clave con su tema y familia | Nada; los muestra |
| Prestidigitación (indirecta, a través de Mazo y Robo) | La invertida de cada carta (para *invertir*) | Nada |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD salvo la Taxonomía. En particular, el sorteo de F1 es un contrato provisorio con el Generador: este puede filtrar o reescalar `p_t` (por arquetipo, por coherencia entre roles, por `afinidad_por_rol`, ver Open Questions de la Taxonomía). Lo único que Cartas garantiza es que la verdad sorteada sea decible por el mazo activo.

## Formulas

Contadas las 78 cartas contra Waite (1910) —asignaciones claras, sin forzar; detalle en `design/balance/cobertura-cartas-waite.md`—, la tradición da en promedio **~1,3 familias por orientación**, y entre 11 y 18 de las 72 orientaciones de un mazo Aprendiz no tienen ningún tema claro (17 en Mayores + Copas). Por eso el mazo no puede garantizar cobertura alta por posición, y la cobertura se resuelve del lado de la verdad: el Generador sortea lo que el mazo puede decir (F1). F2 la comprueba el validador; F1 es el contrato con el Generador; F3 a F5 son calibración y salen en el informe (R11).

Un **acierto de familia** es que la carta, en la orientación que salió, tenga una palabra clave de la familia de la verdad de su rol: es la condición para PARCIAL o EXACTO. Un **acierto exacto posible** pide una palabra clave del mismo tema. `acierto_posible` (R12) da el mejor de los dos para una orientación y una verdad.

**Variables**

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `N` | int | 36 (Aprendiz) a 78 | Mazo y Robo | Cartas del mazo activo |
| `O` | int | `2·N` | calculated | Orientaciones del mazo |
| `n_t^clara` | int | 0 a `O` | calculated (catálogo) | Orientaciones con al menos una palabra clave **clara** del tema `t` |
| `n_t^forz` | int | 0 a `O` | calculated (catálogo) | Orientaciones con una palabra clave forzada del tema `t` y ninguna clara de `t` |
| `n_t`, `n_t⁺` | float, int | 0 a `O` | calculated | `n_t = n_t^clara + w_forz · n_t^forz` (peso de sorteo, F1); `n_t⁺ = n_t^clara + n_t^forz` (orientaciones donde el exacto es posible) |
| `c_f`, `c_f⁺` | int | 0 a `O` | calculated (catálogo) | Orientaciones con al menos una palabra clave clara de la familia `f`; `c_f⁺`, contando también las forzadas |
| `q_f` | float | 0 a 1 | calculated | `c_f / O`: probabilidad de que una carta al azar, en una orientación al azar, tenga la familia `f` con una palabra clave clara |
| `u_f` | float | 0 a 1 | calculated (catálogo) | Proporción de cartas cuya derecha o cuya invertida tiene una palabra clave clara de `f`. Siempre `q_f ≤ u_f ≤ 2·q_f` |
| `p_t` | float | 0 a 1, suman 1 | calculated (F1) | Probabilidad de que la verdad de un rol sea el tema `t` |
| `p_f` | float | 0 a 1, suman 1 | calculated (F1) | `Σ p_t` de los temas de la familia `f`. Es el único `p_f` que usan F3 a F5 |
| `T_m` | int | 1 a 23 | calculated | Temas sorteables del mazo (F1) |
| `w_forz` | float | 0 a 1 | data file | Peso de una forzada en el sorteo (Tuning Knobs) |
| `Q_min` | float | 0,10 | data file | Piso de `q_f`, guardado en milésimos (`q_mil` = 100) |
| `P_fallo_max`, `V_prior_max` | float | — | data file | Umbrales de las marcas del informe (F3, F5); sin fijar hasta el prototipo |

Supuestos: la orientación sale 50/50 y la carta es uniforme dentro del mazo.

**F1. Sorteo de la verdad según el mazo** (contrato con el Generador, D-48)

`p_t = n_t / Σ_s n_s`, sobre los temas **sorteables** del mazo activo: activos y con `n_t^clara` ≥ 1

- **Rango:** `p_t` = 0 para un tema que el mazo no tiene o que solo tiene como forzada. La verdad siempre es algo que el mazo dice con al menos un significado claro.
- **Degeneración:** si `Σ_s n_s` = 0 (ningún tema sorteable, por ejemplo un mazo cuyas claras apuntan todas a temas deprecados), el validador da `MAZO_SIN_VERDADES` con el mazo como sujeto (R12). F1 nunca divide por cero.
- **Por qué las forzadas pesan menos:** el jugador puede leerlas y dan EXACTO, así que cuentan. Pero un tema que la tradición no dice con claridad no tiene que decidir qué verdad le toca al cliente (R6, D-48). Con `w_forz` = 0,5, cuentan la mitad.
- **Ejemplo:** *culpa* tiene 1 sola orientación clara en las 78 cartas (Ocho de Bastos invertida). En Mayores + Bastos es sorteable, con `n_t` = 1, y sale como verdad muy rara vez. En Mayores + Espadas solo aparece como forzada (vergüenza y confesión), así que ahí `p` = 0. En Mayores + Copas no aparece.
- **Lo que no cambia:** el Generador sigue sin conocer la tirada (D-37). El mazo activo se fija con el Nivel de Mazo al empezar la partida y cambia solo al sumar un palo en una Sede.
- **Interfaz provisoria:** el Generador puede componer `p_t` con otras restricciones (Interactions). La forma proporcional tiene un costo, que mide F5: cuanto más concentra `p_t`, más rinde memorizar frecuencias en vez de deducir.

**F2. Piso por familia** (lo comprueba el validador, en enteros)

`c_f · 1000 ≥ q_mil · O` para cada familia `f` y cada mazo alcanzable (E1), con `q_mil` = `Q_min` en milésimos

- **Por qué en enteros:** `⌈0,07 · 100⌉` en coma flotante da 8 y no 7. Con enteros no hay redondeo.
- **Rango:** con `q_mil` = 100, `c_f` ≥ 8 con `O` = 72, ≥ 10 con 100, ≥ 13 con 128 y ≥ 16 con 156.
- **Con los datos contados:** los 15 mazos lo cumplen. El mínimo es Destino en Mayores + Oros (9 de 72, `q` = 0,125). `c_f` cuenta solo palabras clave claras, que es lo que se contó: las forzadas no ayudan a cumplir el piso (R6).
- **Por qué solo un piso:** una banda con techo obligaría a forzar significados (R6). El piso evita que una familia desaparezca, y con eso que el PARCIAL deje de existir para esa familia.

**F3. Acierto posible por posición** (calibración)

`P_exacto = Σ_t p_t · n_t⁺ / O` · `P_pos = Σ_f p_f · q_f` · `P_pos⁺ = Σ_f p_f · c_f⁺ / O` · `P_pos_inv = Σ_f p_f · u_f` · `P_fallo_f = 1 − q_f`

- **Rango:** de 0 a 1. `P_pos` cuenta solo claras y `P_pos⁺` también forzadas: el valor real queda entre las dos.
- **Con los datos contados** (Mayores + Copas): `q` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 (Emoción, Bienes, Conflicto, Ambición, Destino). El conteo todavía no tiene `n_t` por tema, así que el `p_f` de F1 no se puede calcular. Con la aproximación `p_f` ≈ parte de cada familia en `Σ c_f` (22/95, 19/95…), **`P_pos` ≈ 0,274**: acierto de familia posible algo más de 1 vez de cada 4. Se recalcula con el `p_f` de F1 cuando esté la tabla por carta (Open Questions).
- **Por familia:** `P_fallo_f` es la probabilidad de que una posición no tenga acierto posible cuando la verdad es de `f`. En Mayores + Copas, Destino da **0,83**, contra 0,69 a 0,74 en las otras familias: el riesgo se concentra en los clientes de Destino. El informe marca la familia con `P_fallo_f` > `P_fallo_max`. Hasta que el prototipo fije el umbral, muestra el valor y no marca.
- **Con *invertir*:** `P_pos_inv` supone que el jugador invierte solo cuando conviene, y eso exige conocer la verdad. Es una cota **superior** del acierto, y `(1 − P_pos_inv)³` una cota **inferior** de `P_cero`. No hay cifra: el único detalle por carta del conteo es anterior a D-48, y su `u_f` no es compatible con los `q_f` de ahora (Destino: `u` 0,08 < `q` 0,17). Se calcula cuando esté la tabla por carta con los 23 temas.
- "Posible" es una cota superior: el jugador no conoce la verdad.

**F4. Tres Tiempos sin ningún acierto de familia** (calibración)

`P_cero ≈ (1 − P_pos)³`

- **Rango:** de 0 a 1.
- **Con los datos contados** (aproximación de F3): 0,38 en Mayores + Copas y Mayores + Oros, 0,378 en Mayores + Espadas, 0,392 en Mayores + Bastos, y **0,403 en el mazo de 4 palos**. Casi 4 de cada 10 Tres Tiempos no tienen ningún acierto de familia posible en ninguna posición, sin trucos. D-48 acepta ese costo.
- **La progresión empeora:** sumar palos en las Sedes 3, 5 y 7 sube `P_cero`. El informe marca un mazo de 2 o más palos cuando su `P_cero` es mayor que el de algún mazo Aprendiz que contiene, o sea, cuando la progresión desde ese Aprendiz empeora el Pilar 6. Hoy marca, por lo menos, el de 4 palos (0,403 contra 0,378). Cómo se compensa es una pregunta de Prestidigitación (Open Questions).
- **Palancas:** *invertir*, la relectura de una carta muda (P3 de la revisión del 2026-10-24, en Tiradas y Resonancia), la Sentencia (Pilar 2) y la forma del sorteo del Generador. Se miden en el prototipo.
- **Supuestos:** independencia entre posiciones y carta con reposición. Sacar sin reponer cambia `P_cero` en menos de 0,01 con 36 cartas, así que no se corrige. Lo que sí lo cambia es que el Generador correlacione los roles.

**F5. Ventaja del prior** (calibración)

`V_prior = T_m · max_t p_t`

- **Rango:** de 1 (todas las verdades igual de probables) a `T_m` (una sola verdad posible).
- **Qué mide:** cuánto más probable es la verdad más frecuente del mazo que una al azar. El catálogo es público (Pilar 3), así que un jugador puede aprender esas frecuencias y elegir siempre el tema más común en vez de deducir. Eso choca con el Pilar 1. `V_prior` cerca de 1 deja el mérito en la observación.
- **El trade-off:** subir `P_pos` concentrando el sorteo (`n_t^k`, k > 1) sube `V_prior`. Toda forma de sorteo del Generador se mide contra `P_cero` y contra `V_prior` a la vez. El informe marca el mazo con `V_prior` > `V_prior_max`; el umbral lo fija el prototipo.
- **Con los datos contados:** no se puede calcular hasta tener `n_t` por tema.

## Edge Cases

1. **Mazos de otro tamaño.** El nivel Aprendiz suma un palo en las Sedes 3, 5 y 7 (§3.4), así que en el MVP también hay mazos de 50 cartas. El piso F2 vale para **todo mazo alcanzable**: los 22 Mayores más cualquier combinación de 1 a 4 palos, que son 15 mazos. Al sumar un palo, el Generador recalcula `p_t` con el mazo nuevo para los clientes siguientes; los ya generados no cambian.
2. **Una orientación no tiene en Waite ningún significado con tema claro** (entre 11 y 18 de 72 en un mazo Aprendiz; 17 en Mayores + Copas). En este orden:
   1. se busca en otras fuentes de dominio público de la misma tradición: el *Book T* de la Golden Dawn y Mathers (1888);
   2. si hay un significado real pero ningún tema encaja con claridad, se asigna el tema más cercano y la palabra clave se marca `forzada` = sí (R6). Cuenta para el sorteo (F1) y no para el piso (F2), y AC-11 las revisa todas;
   3. si ninguna fuente da más de un significado para la orientación, entra en `orientaciones_con_una` con 1 palabra clave (R4);
   4. si ninguna fuente da siquiera un significado (hoy, el Dos de Copas invertida, que Waite no trata; antes hay que verificar Mathers), la orientación se lee como su **derecha debilitada**: entra en `orientaciones_con_una` con 1 palabra clave `debilitada`, con el tema de una palabra clave de la derecha, `forzada` = sí y como `fuente` la que documenta esa práctica (R4). Si ninguna fuente de la lista documenta la práctica, la carta no pasa AC-19 hasta que se agregue una (Open Questions). Nunca se inventa un significado (R6).
3. **La misma palabra, el mismo tema o la misma familia en varias palabras clave de una carta.** Está permitido, en la misma orientación o entre derecha e invertida (R5).
4. **El mismo texto de palabra clave en varias cartas** (por ejemplo, *pérdida*). Está permitido: cada palabra clave tiene su propio identificador y su propio tema.
5. **Una palabra clave apunta a un tema deprecado.** Es válida (Taxonomía, States). Cuenta para `c_f`, `c_f⁺` y `u_f`, porque su familia sigue dando acierto de familia contra verdades activas de esa familia. No cuenta para `n_t` de F1 ni para R7, que miran temas **activos**. Si una familia de un mazo queda cubierta solo por temas deprecados, cumple F2 pero tiene `p_f` = 0: el informe lo muestra. Si el mazo entero queda sin temas sorteables, es `MAZO_SIN_VERDADES` (R12).
6. **Un Mayor con atribución planetaria.** Su `elemento` es `ninguno` hasta que se decida (Open Questions). Mientras tanto, la Gramática lo trata como neutro con cualquier vecina.
7. **La orientación que salió no tiene la familia de la verdad.** No hay acierto de familia posible en esa posición (una **carta muda**): el mejor resultado es NINGUNO. Cartas no lo compensa, pero lo informa: `acierto_posible` (R12) dice si la orientación es muda para una verdad. La palanca acordada es **releer esa carta pagando UT** (decisión de la revisión full del 2026-10-24); la regla vive en Tiradas y Resonancia. Las otras palancas son *invertir* (`P_pos_inv`, F3) y la Sentencia (Pilar 2), y la frecuencia se calibra con F3 (por familia) y F4.
8. **Falta el texto de una palabra clave en una tabla de idioma.** Es un error de datos del mismo tipo que `NOMBRE_FALTANTE` de la Taxonomía, con el identificador de la palabra clave como sujeto. El juego no arranca. Lo mismo con el nombre visible de una carta (sujeto `<id de carta>@<tabla>`).
9. **Un tema aparece en un mazo solo como forzada.** Se puede leer y da EXACTO, pero no es sorteable en ese mazo: `p_t` = 0 (F1). Por ejemplo, *culpa* en Mayores + Espadas.

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
| Interpretación y Sentencia | Dura | Las palabras clave de la orientación que salió (de 1 a 3) y su tema |
| Tiradas, Resonancia y Resolución | Blanda | `acierto_posible` (R12), para la relectura de una carta muda (E7) |
| Tapete y Tooltips de Cartas | Dura | Todos los datos públicos de la carta y el arte |
| Prestidigitación | Blanda, indirecta | La invertida (*invertir*), a través de Mazo y Robo |
| Generador de Situaciones | Dura | Los pesos `p_t` del mazo activo, para sortear la verdad (F1, D-48) |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Cartas en su tabla de dependientes.
- Los demás sistemas no tienen GDD todavía. La sección Dependencies de cada uno tiene que nombrar a Cartas cuando se escriba.
- El Generador depende de Cartas por F1: `systems-index.md` lo refleja (D-48).

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Palabras clave por orientación | mínimo 2, máximo 3 | Mínimo 1 a 2, máximo 3 a 4. Con más no se gana cobertura si la tradición no la tiene, y el tooltip se recarga | Volumen de contenido, legibilidad del tooltip |
| `orientaciones_con_una` | lista cerrada (dato) | Solo orientaciones que ninguna fuente de la lista puede completar a 2 (E2). Cada entrada anota las fuentes que se buscaron | Volumen de contenido, cota de `P_pos` |
| `Q_min` (piso de `q_f` por familia) | 0,10 (se guarda en milésimos) | 0,05 a 0,11 con los datos contados. En 0,12 Destino en Mayores + Oros (9 de 72) pasa sin ningún margen, con un conteo de una sola lectura | Que ninguna familia desaparezca de un mazo (F2) |
| `w_forz` (peso de una forzada en F1) | 0,5 | 0 a 1. Con 0 las forzadas no generan verdades; con 1 pesan como claras y el mazo "dice" temas que la tradición no dice con claridad | Distribución de verdades, `V_prior` |
| `P_fallo_max` | sin fijar | Lo fija el prototipo | Solo la marca por familia del informe (F3) |
| `V_prior_max` | sin fijar | Lo fija el prototipo | Solo la marca del informe (F5) |

El validador lee estos valores del archivo de configuración; no los tiene fijos en el código. Un valor fuera del rango seguro no es un error de configuración: el rango es una guía de calibración. La forma del sorteo de F1 (proporcional a `n_t`) es una perilla del Generador, no de este catálogo.

## Visual/Audio Requirements

- El arte de cada carta es el escaneo de la edición de 1909 (Pamela Colman Smith), nunca la recoloración de 1971 (§3.1). La fuente de referencia de los escaneos la fija `/art-bible`, con validación legal previa a la producción de arte (§3.1).
- Una carta invertida es la misma imagen rotada 180°; no hay arte propio para la invertida.
- No hay sonido propio de este sistema.

## Game Feel

No aplica: el catálogo no se opera directamente. El feel de robar y dar vuelta una carta le corresponde a Mazo y Robo y al Tapete.

## UI Requirements

- El tooltip de una carta muestra sus datos públicos: nombre, número, palo o Arcano Mayor, atribución y elemento.
- Muestra también las palabras clave de **las dos orientaciones** (Pilar 3, §3.3), con la orientación que salió destacada. Cada palabra clave lleva su tema y su familia, con la marca de la familia (Taxonomía, UI Requirements).
- La `fuente` y la `ubicacion` no se muestran en el MVP; mostrarlas como cita es decisión de `/ux-design`. También lo es si se marcan las palabras clave `forzada` o `debilitada`.

> 📌 **UX Flag — Base de Datos de Cartas:** con las perillas actuales, el tooltip muestra de 3 a 6 palabras clave con tema y familia (hasta 8 con el máximo de 4 por orientación). Antes de las historias del tooltip hay que hacer su spec con `/ux-design`, junto con el de la Taxonomía, incluida la legibilidad en Switch portátil.

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
| Revisión full del 2026-10-24 (`reviews/base-de-datos-de-cartas-review-log.md`) | Peso de las forzadas en F1, marcas por familia y de progresión, relectura de la carta muda, derecha debilitada |
| Taxonomía R4, R7, R13, States | Identificadores; un tema por palabra clave; validador y formato de sujetos; temas deprecados |

## Acceptance Criteria

Convenciones de prueba:
- Todo AC parte de `fixture_catalogo_valido` (78 cartas sintéticas con ids reales, textos centinela y `taxonomia_prueba`) y lo **muta en un solo punto**. Las excepciones lo dicen: AC-15b y AC-15e redistribuyen una familia entera, y AC-17 cambia configuración y datos a la vez. AC-01 prueba que el fixture sin mutar pasa limpio.
- Cada error se verifica por la regla de la que es (con el código que fije la historia) y por su sujeto en formato R13 de la Taxonomía. Los controles dicen "ningún error de la regla X cuyo sujeto empiece por S", nunca "no hay errores".
- Que el juego no arranque lo prueban AC-25a/b de la Taxonomía; que cada palabra clave tenga exactamente un tema, AC-03a–c de la Taxonomía. No se repiten acá.
- Las funciones de R12 aceptan entradas arbitrarias: los AC del informe pueden usar mazos de prueba que no son alcanzables.
- **Evidencia:** todos son Logic (test unitario en `[test root]/cartas/`), salvo los marcados Integration. Los *provisorios* dependen de un GDD que no existe y no bloquean hasta que exista.

**Estructura**
- **AC-01** (R1–R8, R10, F2) — GIVEN `fixture_catalogo_valido`, WHEN se valida, THEN la lista está vacía.
- **AC-02a** (R1) — GIVEN el fixture sin `carta.copas_05`, WHEN se valida, THEN contiene error de R1 con sujeto `carta.copas_05`.
- *AC-02b se retiró el 2026-10-24: era ambiguo entre R1 y R3; el caso pasó a AC-04e. Su número no se reutiliza.*
- **AC-03** (R2; parametrizado) — GIVEN el fixture con una carta de id `carta.copas_15`, `carta.mayor_22`, `carta.copas_5` o `carta.copos_05` (un caso cada uno), WHEN se valida, THEN contiene error de R2 con ese sujeto. Con dos cartas de id `carta.copas_05`, contiene error de R2 con sujeto `carta.copas_05`.
- **AC-04a** (R3) — GIVEN el fixture con `carta.copas_05` de elemento fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.copas_05`.
- **AC-04b** (R3) — GIVEN el fixture y `tabla_atribuciones_prueba` (atribución → elemento, armada a mano y no derivada del catálogo), con `carta.mayor_04` de elemento agua cuando la tabla dice fuego, WHEN se valida, THEN contiene error de R3 con sujeto `carta.mayor_04`. Control: un Mayor planetario con `ninguno` no da ningún error de R3 cuyo sujeto empiece por su id.
- **AC-04c** (R3, R12; Integration) — GIVEN los datos reales y el oráculo `atribuciones_gd` (R12), WHEN se cargan, THEN las 22 atribuciones de los Mayores y los 36 decanatos de los Menores 2 a 10 coinciden con el oráculo; `carta.mayor_08` tiene Leo y `carta.mayor_11` Libra; los 7 planetarios tienen elemento `ninguno`, y cada palo el elemento de R3.
- **AC-04d** (R3; parametrizado) — GIVEN el fixture y `tabla_atribuciones_prueba`, con `carta.copas_05` sin decanato, o con `carta.copas_01`, `_11`, `_12`, `_13` o `_14` con decanato (un caso cada uno), WHEN se valida, THEN contiene error de R3 con sujeto esa carta. Control: `carta.copas_05` con el decanato de la tabla no da ningún error de R3 cuyo sujeto empiece por `carta.copas_05`.
- **AC-04e** (R3; parametrizado) — GIVEN el fixture con `carta.mayor_09` de número 8, un Mayor con palo, un Menor sin palo, un `elemento` o un `arcano` fuera de la lista, o un `arte` vacío (un caso cada uno), WHEN se valida, THEN contiene error de R3 con sujeto esa carta.

**Palabras clave**
- **AC-05a** (R4) — GIVEN el fixture con 1 palabra clave en `carta.copas_05/derecha`, que no está en `orientaciones_con_una`, WHEN se valida, THEN contiene error de R4 con ese sujeto. Lo mismo con 4. Control: con 2 y con 3, no lo contiene.
- **AC-05b** (R4, Tuning Knobs) — GIVEN la configuración con máximo 4 palabras clave por orientación y `carta.copas_05/derecha` con 4, la cuarta con id `carta.copas_05/derecha/4`, WHEN se valida, THEN no contiene error de R4 con ese sujeto ni de identificador.
- **AC-05c** (R4, E2) — GIVEN `carta.copas_02/invertida` en `orientaciones_con_una` con 1 palabra clave, WHEN se valida, THEN no contiene error de R4 con ese sujeto. Con 0, sí. Con 2, no (la lista permite 1, no obliga).
- **AC-05d** (R4; parametrizado) — GIVEN `orientaciones_con_una` con una entrada `carta.copas_15/derecha` (no existe), una entrada repetida, o una entrada sin las fuentes buscadas (un caso cada uno), WHEN se valida, THEN contiene error de R4 con sujeto la entrada en formato R13 de la Taxonomía.
- **AC-05e** (R4; parametrizado) — GIVEN el fixture con una palabra clave de id `carta.copas_05/derecha/0`, con `carta.copas_05/derecha/1` y `/3` sin `/2`, o con id `carta.copas_05/derechaa/1` (un caso cada uno), WHEN se valida, THEN contiene error de R4 con sujeto ese id (en el hueco, la orientación).
- **AC-06** (R5) — GIVEN `carta.copas_05/derecha` con sus 3 palabras clave de la misma familia de `taxonomia_prueba`, WHEN se valida, THEN no contiene ningún error cuyo sujeto empiece por `carta.copas_05`.
- *AC-07 se retiró el 2026-10-24 (D-48: no hay mínimo de familias por carta). Su número no se reutiliza.*
- **AC-08** (R7) — GIVEN el fixture donde `tema.locura` no aparece en ninguna palabra clave de las 78 cartas, WHEN se valida, THEN contiene error de R7 con sujeto `tema.locura`. Control: si aparece en una sola palabra clave clara, no lo contiene; si aparece solo en palabras clave forzadas, sí.
- **AC-09a** (E5) — GIVEN el fixture con `tema.traicion` deprecado y el mazo `copas` con `c_Conflicto` = 8, donde una de esas orientaciones tiene como única palabra clave de Conflicto una de `tema.traicion` (sin ella `c_Conflicto` sería 7), WHEN se valida, THEN no contiene error de F2 con sujeto `copas/familia.conflicto`.
- **AC-09b** (E5, F1) — GIVEN un mazo de prueba con `n_t^clara` = 2 para `tema.amor`, 2 para `tema.deuda` y 4 para `tema.traicion` deprecado, WHEN se pide el informe, THEN `p_traicion` = 0 y `p_amor` = `p_deuda` = 0,5.
- **AC-09c** (E5, R7) — GIVEN `tema.locura` deprecado y sin ninguna palabra clave, WHEN se valida, THEN no contiene error de R7 con sujeto `tema.locura`.
- **AC-09d** (E5) — GIVEN un mazo de prueba con una orientación cuya única palabra clave de Conflicto es clara y de `tema.traicion` deprecado, WHEN se pide el informe, THEN esa orientación cuenta en `c_Conflicto` y en `c_Conflicto⁺`, su carta cuenta en `u_Conflicto`, y `n_traicion` no entra en `p_t`.
- **AC-10** (R4) — GIVEN `carta.copas_05/derecha/1` sin `fuente`, con una `fuente` fuera de la lista o con `ubicacion` vacía (un caso cada uno), WHEN se valida, THEN contiene error de R4 con ese sujeto. Que el texto salga de la fuente citada (R6) no lo puede juzgar el validador: lo cubre AC-11.
- **AC-11** (R6; Integration, revisión documentada; bloquea la historia de contenido) — GIVEN los datos reales, WHEN un revisor que no cargó los datos compara cada palabra clave con el original inglés en su `ubicacion`, para (a) todas las palabras clave de las cartas que carga la build del MVP, (b) todas las `forzada` = sí y (c) una muestra de al menos el 25 % de las demás, sorteada con una semilla anotada, THEN hay 0 fallas en (a) y (b), y una sola falla en (c) obliga a revisar el 100 %. Es falla: el significado no está en la `ubicacion`; la traducción cambia el tema asignado; una `forzada` tiene un tema claro en alguna fuente, o una clara no lo tiene. El resultado queda en `production/qa/`.
- **AC-11b** (R4) — GIVEN `carta.copas_05/derecha/1` con `forzada` o `debilitada` fuera de {sí, no} (un caso cada uno), WHEN se valida, THEN contiene error de R4 con ese sujeto. Control: sin los campos (por defecto no), no lo contiene.
- **AC-12** (E3) — GIVEN `carta.copas_05` con el mismo tema en la derecha y en la invertida, WHEN se valida, THEN no contiene ningún error cuyo sujeto empiece por `carta.copas_05`.
- **AC-13** (E4) — GIVEN el mismo texto en `carta.copas_05/derecha/1` y `carta.oros_05/derecha/1`, WHEN se valida, THEN no contiene error de identificador duplicado.
- **AC-14** (E8) — GIVEN la tabla `es_prueba` sin el texto de `carta.copas_05/derecha/2`, WHEN se valida, THEN contiene el error de nombre faltante (el mismo tipo que `NOMBRE_FALTANTE` de la Taxonomía) con sujeto `carta.copas_05/derecha/2@es_prueba`.
- **AC-14b** (E8) — GIVEN las tablas `es_prueba` y `en_prueba`, y `en_prueba` sin el nombre visible de `carta.copas_05`, WHEN se valida, THEN contiene ese error con sujeto `carta.copas_05@en_prueba`, y ninguno con sujeto `carta.copas_05@es_prueba`.

**Cobertura**
- **AC-15a** (F2; parametrizado por familia) — GIVEN, para cada una de las 5 familias, el fixture mutado para que el mazo `copas` tenga `c_f` = 7, WHEN se valida, THEN contiene error de F2 con sujeto `copas/<familia>`. Con 8, no lo contiene.
- **AC-15b** (F2, E1; parametrizado, redistribuye una familia) — GIVEN, para cada uno de los 15 mazos alcanzables, el fixture con `c_Destino` por bloque (Mayores / copas / oros / espadas / bastos) según la receta de su tamaño, WHEN se valida, THEN contiene exactamente un error de F2 de `familia.destino`, con el sujeto de ese mazo en el orden canónico de R13 (nunca `oros+copas/...`). Recetas, con el mazo objetivo formado por los palos del valor más bajo (se permutan los palos para los demás mazos del mismo tamaño):
  - 1 palo (objetivo `copas`): 7 / 0 / 3 / 3 / 3;
  - 2 palos (objetivo `copas+oros`): 7 / 1 / 1 / 4 / 4;
  - 3 palos (objetivo `copas+oros+espadas`): 6 / 2 / 2 / 2 / 4;
  - 4 palos: 7 / 2 / 2 / 2 / 2.
- **AC-15c** (F2; borde) — GIVEN el mazo `copas+oros+espadas+bastos` (`O` = 156), WHEN `c_Destino` vale 16, THEN no contiene error de F2; con 15, sí.
- **AC-15d** (F2, R6) — GIVEN el mazo `copas` con 7 orientaciones con palabra clave clara de Destino y 1 palabra clave `forzada` de Destino en otra orientación, WHEN se valida, THEN contiene error de F2 con sujeto `copas/familia.destino`. Con 8 claras, no.
- **AC-15e** (F2; aritmética entera, redistribuye una familia) — GIVEN `Q_min` = 0,07 y el mazo `copas+oros` (`O` = 100), WHEN `c_Destino` vale 7, THEN no contiene error de F2; con 6, sí. Con `Q_min` = 0,10: 10 no, 9 sí.
- *AC-16 se retiró el 2026-10-24 (D-48: sin piso de* invertir*). Su número no se reutiliza.*
- **AC-17** (Tuning Knobs; configuración y datos) — GIVEN la configuración con `Q_min` = 0,15 y el mazo `copas` con `c_Destino` = 10, WHEN se valida, THEN contiene error de F2 (hace falta 11). Con 11, no lo contiene. Un valor fuera del rango seguro no es un error de configuración.

**Informe de cobertura y funciones de R12**
- **AC-18a** (R11, R12) — GIVEN `fixture_informe_chico`: carta A con derecha [*amor* clara, *deuda* forzada] e invertida [*amor* clara, *duelo* clara]; carta B con derecha [*deuda* clara] e invertida [*muerte* forzada]; `w_forz` = 0,5. WHEN se pide el informe, THEN `O` = 4; `c` = Emoción 2, Bienes 1, Destino 0; `c⁺` = Emoción 2, Bienes 2, Destino 1; `u` = Emoción 0,5, Bienes 0,5, Destino 0; forzadas = 2; `n` = *amor* 2, *duelo* 1, *deuda* 1,5, *muerte* 0,5 (no sorteable); `p` = 0,444 / 0,222 / 0,333 / 0 (± 0,001); `P_pos` = 0,417 y `P_pos⁺` = 0,500 (± 0,001).
- **AC-18b** (R11, F1) — GIVEN un mazo de prueba de 10 cartas (`O` = 20), todas sus palabras clave claras, con `n_t` = 6, 3 y 1 para tres temas y 0 para el resto, WHEN se pide el informe, THEN `p_t` = 0,6 / 0,3 / 0,1 y 0 para los temas ausentes, y `P_exacto` = 0,23.
- **AC-18c** (F3, F4) — GIVEN `q` = 0,31 / 0,26 / 0,31 / 0,28 / 0,17 y `p_f` = 0,23 / 0,20 / 0,23 / 0,21 / 0,13 (orden Emoción, Bienes, Conflicto, Ambición, Destino), WHEN se calcula, THEN `P_pos` = 0,276 ± 0,002, `P_cero` = 0,380 ± 0,003 y `P_fallo_Destino` = 0,83.
- *AC-18d se retiró el 2026-10-24: sortear 1.000 verdades es una prueba del Generador; la parte de Cartas (`p_t` = 0 sin palabras clave) la cubren AC-18a y AC-18b. Su número no se reutiliza.*
- **AC-18e** (R11; invariante) — GIVEN el informe de los 15 mazos del fixture, WHEN se revisa, THEN para cada mazo y familia vale `q_f ≤ u_f ≤ 2·q_f`. Control: el chequeo del informe reporta un informe armado a mano con `q_Destino` = 0,17 y `u_Destino` = 0,08.
- **AC-18f** (F3, F4; marcas) — GIVEN `P_fallo_max` = 0,80, WHEN se pide el informe, THEN una familia con `P_fallo` = 0,80 no se marca y una con 0,8001 sí. Con `P_fallo_max` sin fijar, ninguna se marca. GIVEN un mazo de 2 palos con `P_cero` = 0,39 que contiene mazos Aprendiz con 0,38 y 0,40, THEN se marca; con 0,38, no. Ningún caso produce un error de datos.
- **AC-18g** (F1, `w_forz`) — GIVEN `fixture_informe_chico`, WHEN `w_forz` vale 0 o 1, THEN `p` (*amor*, *duelo*, *deuda*) da 0,5 / 0,25 / 0,25 o 0,4 / 0,2 / 0,4. En los dos casos *muerte* tiene `p` = 0; con una palabra clave clara de *muerte* en B, `p_muerte` > 0.
- **AC-18h** (F5) — GIVEN un mazo de prueba con `p` = 0,5 / 0,25 / 0,25 (`T_m` = 3), WHEN se calcula, THEN `V_prior` = 1,5; con `p` uniforme, 1. Con `V_prior_max` = 1,5 no se marca; con 1,4999, sí.
- **AC-18i** (R11, E1) — GIVEN el fixture, WHEN se pide el informe, THEN tiene exactamente 15 entradas, una por mazo alcanzable, con la clave en el formato de mazo de R13.
- **AC-18j** (R11) — GIVEN el fixture con `tema.culpa` en una sola orientación clara de las 78 cartas y `carta.copas_05/derecha` con sus palabras clave todas de un mismo tema, WHEN se pide el informe, THEN marca `tema.culpa` como frágil y cuenta `carta.copas_05/derecha` entre las orientaciones sin elección.
- **AC-22** (R12, F1) — GIVEN un mazo de prueba donde todas las palabras clave claras son de temas deprecados, WHEN se valida, THEN contiene `MAZO_SIN_VERDADES` con el mazo como sujeto, y el informe no divide por cero.
- **AC-23** (R12) — GIVEN una orientación con *amor* (clara) y *deuda* (forzada), WHEN se consulta `acierto_posible` con verdad *amor*, *deuda*, *duelo* y *muerte*, THEN da EXACTO, EXACTO, PARCIAL y NINGUNO.
- **AC-24** (E2 paso 4) — GIVEN `carta.copas_02/invertida` en `orientaciones_con_una` con una palabra clave `debilitada` = sí, `forzada` = sí, el tema de una palabra clave de `carta.copas_02/derecha` y una `fuente` de la lista, WHEN se valida, THEN no contiene ningún error cuyo sujeto empiece por `carta.copas_02/invertida`. Con `forzada` = no, con otro tema o con la orientación fuera de la lista (un caso cada uno), contiene error de R4.

**Datos reales y otros**
- **AC-19** (R10; Integration) — GIVEN el catálogo, las cartas y las tablas de idioma reales, WHEN se valida, THEN la lista está vacía. Bloquea la historia de contenido, no la del validador.
- **AC-20** (R3; Integration, *provisorio hasta `/art-bible`*) — GIVEN el manifiesto de la fuente de escaneos que fije `/art-bible` (un hash por imagen), WHEN se comparan las 78 `arte`, THEN el hash de cada una coincide con el de su carta en el manifiesto. Que esa fuente no sea la recoloración de 1971 lo decide `/art-bible` con su validación legal.
- **AC-21** (States; Integration, *provisorio hasta Guardado*) — GIVEN una partida guardada con verdad *traición* en un rol, WHEN se carga con una versión del catálogo que cambió el tema de una palabra clave de *traición* a *engaño*, THEN la verdad del cliente sigue siendo *traición*.
- Lo que muestra el tooltip (R9) lo prueban los AC de Tapete y Tooltips (`/ux-design`). E6 y E7 los prueban la Gramática y Resonancia.

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| Elemento de los 7 Mayores con atribución planetaria (Mago, Sacerdotisa, Emperatriz, Rueda, Torre, Sol, Mundo): ¿neutro, el del planeta según otra tradición, o un elemento propio? | GDD de Gramática | Al diseñar la Gramática |
| Forma del sorteo de F1: ¿proporcional a `n_t`, o con sobrepeso (`n_t^k`, k > 1) para subir `P_pos`? ¿Los roles de una situación se sortean independientes o con afinidad (`afinidad_por_rol` de la Taxonomía)? | GDD del Generador | Al diseñar el Generador |
| **Riesgo del Pilar 6:** con la tradición, `P_cero` ≈ 0,38 en Tres Tiempos y 0,40 en 78 cartas (F4), y 0,83 de fallo por posición con verdad de Destino (F3). Medir en el prototipo si es jugable con *invertir*, la relectura de una carta muda y la Sentencia, y fijar `P_fallo_max` y `V_prior_max`. Con F1 proporcional, `P_pos` ronda 0,26 a 0,28, y llegar a `P_cero` 0,15 pediría `P_pos` ≈ 0,47: si hace falta, la palanca viene de trucos o de la forma del sorteo, siempre medida contra `V_prior` (F5) | Diseñador | Prototipo del núcleo |
| **Relectura de una carta muda pagando UT** (E7): costo en UT, cuántas por tirada, y si la carta nueva sale del mismo mazo | GDD de Tiradas y de Resonancia | Al diseñarlos |
| **La progresión del mazo empeora `P_cero`** (F4): compensarlo con más trucos por Sede (preferido en la revisión) o con el multiplicador de recompensa de D-22 | GDD de Prestidigitación | Al diseñar Prestidigitación |
| ¿Qué fuente de la lista documenta la lectura de una invertida como "derecha debilitada" (E2 paso 4)? Si ninguna, ¿se suma una a la lista cerrada de `fuente`? Sin eso, la regla es un significado inventado con otro nombre | Diseñador | Antes de cargar los datos |
| Orientaciones sin tema claro en Waite (E2): de 11 a 18 por mazo Aprendiz (17 en Mayores + Copas). Buscarlas en el *Book T* y en Mathers antes de cargar los datos; las que queden van `forzada` | Diseñador | Al escribir los datos de las 36 cartas del MVP |
| **Dos de Copas invertida:** Waite no la trata. Verificar primero Mathers (1888) y el *Book T* (una lectura de la revisión recuerda en Mathers algo como "crossed desires, obstacles", sin verificar); si no dan nada, va como derecha debilitada (E2 paso 4) | Diseñador | Antes de cargar los datos |
| Tabla de decanatos del *Book T* para los Menores 2 a 10 (36 valores) y si las figuras llevan atribución propia. Hoy las figuras no la llevan | Diseñador | Al escribir los datos |
| Rehacer la tabla por carta de `design/balance/cobertura-cartas-waite.md` con los 23 temas y con `n_t` por tema: sin ella no se pueden calcular el `p_f` de F1, `P_pos_inv` (F3) ni `V_prior` (F5) | Diseñador | Antes de cargar los datos |
| Registro: agregar `w_forz` (lo usa el Generador) y anotar la excepción de 1 en `palabras_clave_por_orientacion` | `/consistency-check` | Antes del GDD del Generador |
| El conteo de D-48 lo hizo una sola lectura (diseñador más IA), con criterio de "asignación clara". Antes de cargar los datos, hace falta una segunda lectura independiente de las 36 cartas del MVP | Diseñador | Al escribir los datos |
| Traducción de las palabras clave del inglés de Waite al español rioplatense: ¿la `ubicacion` cita el original, y quién valida que la traducción no cambie el tema? | Diseñador, `/localize` | Al escribir los datos |
| Fuente de referencia de los escaneos de 1909 y validación legal | `/art-bible` | Antes de producir arte |
