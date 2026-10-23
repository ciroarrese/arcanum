# Base de Datos de Cartas

> **Status**: Designed
> **Creative Director Review (CD-GDD-ALIGN)**: NOT ASSESSED 2026-10-23 — omitida en modo lean
> **Author**: Ciro + agentes
> **Last Updated**: 2026-10-23
> **Last Verified**: 2026-10-23
> **Implements Pillar**: Pilar 3 (Memoria Pura: significado público), Pilar 6 (No hay Carta Mala), D-05 (tarot real)

## Summary

La Base de Datos de Cartas es el catálogo de las 78 cartas del mazo Smith 1909. Guarda los datos públicos de cada carta y 3 palabras clave por orientación, cada una con un tema de la Taxonomía y una fuente tradicional citada. Además, fija la cobertura del mazo, para que una tirada casi siempre deje algo que leer: cada familia queda dentro de una banda en cada mazo alcanzable, hay un piso que hace útil al truco *invertir*, y los 22 Mayores cubren los 20 temas. El jugador la ve en el tooltip de cada carta.

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
   | `derecha`, `invertida` | 3 palabras clave cada una | R4 a R6 |

**Palabras clave**

4. Cada orientación tiene **exactamente 3 palabras clave**. El GDD §3.2 decía 2–3; se fija en 3 por la cobertura de R5. Cada una tiene:
   - un identificador `<id de carta>/<derecha|invertida>/<1–3>`;
   - un texto, que sale de la tabla de idioma;
   - **exactamente un tema base** (R7 de la Taxonomía);
   - una `fuente`, de la lista cerrada `waite_1910`, `book_t` o `mathers_1888`, y una `ubicacion` (página o sección, nunca vacía), para que R6 se pueda verificar.
5. **Cobertura por carta:**
   - Las palabras clave de una orientación son de **familias todas distintas entre sí** (3 con el valor actual).
   - La derecha y la invertida juntas cubren **al menos 4 familias**.

   En cada carta, una posición tiene acierto de familia posible en 3 de las 5 familias, y en 4 o 5 con el truco *invertir*, que es la palanca del Pilar 6 que pone el mazo. Además, en cada mazo alcanzable (E1), al menos el **75 %** de las cartas cubren cada familia entre su derecha y su invertida (`u_f`, Formulas): *invertir* tiene que servir para todas las familias, no solo en promedio.
6. **El texto manda sobre el tema.** Cada palabra clave es un significado tradicional de la carta (D-05), tomado de la tradición de 1909 (por ejemplo, *The Pictorial Key to the Tarot* de Waite, 1910, de dominio público). El tema se deriva del texto (§3.2). Si R5 obliga a una familia que la carta no tiene en la tradición, se cambia qué significado tradicional se elige. Nunca se inventa un significado para cumplir la cobertura.

**Cobertura del mazo**

7. Los 22 Arcanos Mayores **cubren por sí solos los 20 temas base activos**: cada tema aparece en al menos una palabra clave de un Mayor, derecha o invertida. Así, cualquier mazo Aprendiz (22 Mayores más un palo, el que elija Mazo y Robo) contiene todos los temas.
8. **Los Mayores apuntan a cualquier familia.** La familia es del tema, no de la carta: los Mayores no van atados a Destino. Las "fuerzas fuera de tu control" de los Mayores las cubre la regla de peso de la Gramática (§3.5.5), no este catálogo. En cada mazo alcanzable (los 22 Mayores más cualquier combinación de palos, E1), cada familia aparece en entre el **50 % y el 69 %** de las orientaciones (`q_f`, Formulas); en un mazo de 36 cartas, entre 36 y 50 de 72. Como los palos aportan pocas palabras clave de Destino, los Mayores cargan la mayor parte: unas 30 de sus 132.
9. Todos los datos de una carta son **públicos** (D-08, Pilar 3): nada de este catálogo es secreto ni se desbloquea.

**Validación**

10. Las reglas R1 a R8, F2 y F3 se agregan al validador del catálogo (R13 de la Taxonomía). Un incumplimiento es un error de datos y el juego no arranca. Los sujetos de los errores siguen el formato de R13 de la Taxonomía: carta, orientación, palabra clave o mazo. Los códigos de error y sus casos se definen en las historias de implementación, no en este GDD.
11. **Informe de cobertura.** Para cada mazo alcanzable (E1), el validador produce un informe con `c_f`, `q_f` y `u_f`, `P_pos` y `P_pos_inv` (F1), y `P_cero = (1 − P_pos)³` junto con el peor caso `max_f (1 − q_f)³` (F4). Recibe `p_f` como entrada; por defecto (*provisorio hasta el GDD del Generador*) usa el proporcional a los temas activos de cada familia: 0,20 / 0,20 / 0,25 / 0,20 / 0,15. El informe no es una lista de errores: sirve para calibrar y para que el Generador pueda leer `q_f`.

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
| Interpretación y Sentencia | Las 3 palabras clave de la orientación que salió y su tema | La palabra clave elegida por posición |
| Tapete y Tooltips | Nombre, número, palo, `atribucion`, elemento, arte, y las palabras clave con su tema y familia | Nada; los muestra |
| Prestidigitación (indirecta, a través de Mazo y Robo) | La invertida de cada carta (para *invertir*) | Nada |

**Interfaces provisorias:** ninguno de estos sistemas tiene GDD salvo la Taxonomía.

## Formulas

Ninguna de estas fórmulas es una regla de juego: son las condiciones de cobertura que el validador comprueba sobre el catálogo (F2, F3) y las cuentas con las que el diseño calibra (F1, F4). Un **acierto de familia** es que la carta, en la orientación que salió, tenga una palabra clave de la familia de la verdad de su rol: es la condición para que haya PARCIAL o EXACTO.

**Variables**

| Variable | Type | Range | Source | Description |
|---|---|---|---|---|
| `N` | int | 36 (Aprendiz) | Mazo y Robo | Cartas del mazo |
| `O` | int | `2·N` = 72 | calculated | Orientaciones del mazo |
| `c_f` | int | 0 a `O` | calculated (catálogo) | Orientaciones con una palabra clave de la familia `f`. Por R5 hay como mucho una por orientación, así que `Σ c_f = 3·O` = 216 |
| `q_f` | float | 0 a 1 | calculated | `c_f / O`: probabilidad de que una carta al azar, en una orientación al azar, tenga la familia `f` |
| `u_f` | float | 0 a 1 | calculated (catálogo) | Proporción de cartas del mazo cuya derecha y cuya invertida, juntas, cubren `f` |
| `p_f` | float | 0 a 1, `Σ p_f = 1` | Generador | Probabilidad de que la verdad de un rol sea de la familia `f` |
| `C_min`, `C_max` | int | 36, 50 | data file | Banda de `c_f` (Tuning Knobs) |
| `U_min` | float | 0,75 | data file | Piso de `u_f` (Tuning Knobs) |

Supuestos: la orientación sale 50/50 y la carta es uniforme dentro del mazo.

**F1. Acierto de familia por posición**

`P_pos = Σ_f p_f · q_f` (sin truco) · `P_pos_inv = Σ_f p_f · u_f` (con *invertir* en esa posición)

- **Rango:** sin truco, de 0 a 1. Con *invertir*, de 0,75 a 1, por el piso de F3.
- **Lectura:** si `p` o `q` es uniforme, `P_pos` = 0,6 exacto. Por eso **el promedio no sirve como métrica**: lo que importa es la familia más baja, `min q_f`, y de eso se encarga F2.
- **Ejemplo:** `p` = 0,20 / 0,20 / 0,25 / 0,20 / 0,15 (uniforme por tema) y `q` = 0,60 / 0,60 / 0,78 / 0,66 / 0,36. Queda `P_pos` = 0,621, que parece sano, pero una verdad de Destino tiene solo 36 % de acierto posible. F2 prohíbe ese mazo, porque `c_D` = 26 < 36.

**F2. Banda por familia** (la comprueba el validador)

`C_min ≤ c_f ≤ C_max` para cada familia `f` en cada mazo de 36 cartas. En todo mazo alcanzable (E1), en proporción y comparando en enteros para evitar redondeos: `c_f · 72 ≥ C_min · O` y `c_f · 72 ≤ C_max · O` (en el mazo de 78 cartas, `O` = 156, la banda es 78 a 108)

- **Rango:** con 36–50, `q_f` queda entre 0,50 y 0,69, es decir, 0,6 ± 0,1 alrededor del uniforme (43,2 en un mazo de 36).
- **Por qué piso y techo:** la cota de R5 (como mucho 1/3 de las palabras clave por familia) equivale a `q_f ≤ 1` y no limita nada. El piso evita que una familia escasa deje la verdad sin acierto; el techo, que una familia sea regalada.
- **Degeneración que evita:** R5 deja que un palo reparta sus 84 palabras clave 28/28/28 en 3 familias y ninguna en las otras 2. Esas 2 dependerían solo de los Mayores (`q` ≈ 0,37).
- **Ejemplo:** si un palo aporta 6 palabras clave de Destino, los Mayores necesitan al menos 30 para que `c_D` ≥ 36.

**F3. Piso de *invertir*** (lo comprueba el validador)

`u_f ≥ U_min` para cada familia `f` y cada mazo alcanzable (E1)

- **Rango:** con 0,75, *invertir* da acierto de familia posible en al menos 3 de cada 4 cartas para cualquier verdad.
- **Por qué:** "derecha + invertida cubren al menos 4 familias" garantiza el promedio (≥ 0,8), pero si todas las cartas dejan afuera la misma familia, *invertir* nunca la rescata.
- **Factibilidad:** las 36 cartas suman al menos 144 coberturas (4 cada una), así que el piso de 27 por familia es alcanzable.

**F4. Tres Tiempos sin ningún acierto de familia** (calibración)

`P_cero = Π_{i=1..3} (1 − q_{f_i})` (sin truco) · `P_cero_inv = Π_{i=1..3} (1 − u_{f_i})` (con *invertir* donde haga falta)

- **Rango:** de 0 a 1.
- **Ejemplo uniforme** (`q` = 0,6, `u` = 0,8): sin truco 0,4³ = **0,064**; con *invertir* 0,2³ = **0,008**.
- **Peor caso permitido por F2 y F3** (tres verdades de la familia con `q` = 0,5 y `u` = 0,75): sin truco 0,125; con *invertir* 0,016.
- **Supuesto:** independencia entre posiciones. Para las cartas es razonable: sacar 3 de 36 sin reposición mueve el resultado menos del 3 %. Para las verdades **no**: si el Generador repite familia entre roles, las posiciones se correlacionan y aparece el peor caso. Esto se mide en el prototipo por combinación de familias.
- "Posible" es una cota superior: el jugador no conoce la verdad.

## Edge Cases

1. **Mazos de otro tamaño.** El nivel Aprendiz suma un palo en las Sedes 3, 5 y 7 (§3.4), así que en el MVP también hay mazos de 50 cartas. La banda y el piso valen para **todo mazo alcanzable**: los 22 Mayores más cualquier combinación de 1 a 4 palos, que son 15 mazos. La banda se expresa en `q_f` (0,50 ≤ `q_f` ≤ 0,69) y el piso en `u_f` (≥ 0,75). En el mazo de 36 cartas, eso equivale a `c_f` entre 36 y 50.
2. **Una carta no tiene en la tradición significados de 3 familias distintas en una orientación.** Primero se buscan en otras fuentes de dominio público de la misma tradición: Waite (1910), el *Book T* de la Golden Dawn, Mathers (1888). Si tampoco alcanza, es un problema de datos que bloquea: el validador no admite excepciones, y el diseñador decide (Open Questions). Nunca se inventa un significado (R6).
3. **La misma palabra o el mismo tema en la derecha y en la invertida.** Está permitido, siempre que entre las dos orientaciones se cubran al menos 4 familias (R5). Dentro de una misma orientación no puede pasar, porque sus 3 palabras clave son de familias distintas.
4. **El mismo texto de palabra clave en varias cartas** (por ejemplo, *pérdida*). Está permitido: cada palabra clave tiene su propio identificador y su propio tema.
5. **Una palabra clave apunta a un tema deprecado.** Es válida (Taxonomía, States). Cuenta para `c_f` y `u_f`, porque su familia sigue dando acierto de familia contra verdades activas de esa familia. No cuenta para R7, que exige cubrir los temas **activos**.
6. **Un Mayor con atribución planetaria.** Su `elemento` es `ninguno` hasta que se decida (Open Questions). Mientras tanto, la Gramática lo trata como neutro con cualquier vecina.
7. **La orientación que salió no tiene la familia de la verdad.** No hay acierto de familia posible en esa posición: el mejor resultado es NINGUNO. Cartas no lo compensa. Las palancas son *invertir* (F3) y la Sentencia (Pilar 2), y la frecuencia se calibra con F4.
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
| Interpretación y Sentencia | Dura | Las 3 palabras clave de la orientación que salió y su tema |
| Tapete y Tooltips de Cartas | Dura | Todos los datos públicos de la carta y el arte |
| Prestidigitación | Blanda, indirecta | La invertida (*invertir*), a través de Mazo y Robo |
| Generador de Situaciones | Blanda, *provisoria* | Las `q_f` del mazo, si se decide que el Generador no favorezca familias escasas (Open Questions). Hoy el índice no la lista |

**Bidireccionalidad:**

- La Taxonomía ya nombra a Cartas en su tabla de dependientes.
- Los demás sistemas no tienen GDD todavía. La sección Dependencies de cada uno tiene que nombrar a Cartas cuando se escriba.
- Si el Generador termina leyendo `q_f`, hay que sumar Cartas a sus dependencias en `systems-index.md`.

## Tuning Knobs

| Perilla | Valor actual | Rango seguro | Qué afecta |
|---|---|---|---|
| Palabras clave por orientación | 3 | 3 a 4. Con 2 no se cumple R5 (3 familias); con 4 la cobertura por posición sube a 0,8, pero pasa de 468 a 624 palabras clave y se aparta del §3.2 | Cobertura por posición (F1), volumen de contenido, legibilidad del tooltip |
| Familias mínimas entre derecha e invertida | 4 | 4 a 5. Con 5, cada carta toca todas las familias, lo que tensiona D-05 | Cuánto rescata *invertir* por carta |
| `C_min` / `C_max` (banda por familia, en un mazo de 36) | 36 / 50 (`q_f` de 0,50 a 0,69) | `C_min` de 30 a 40, `C_max` de 46 a 56; siempre `C_min` < 43,2 < `C_max`. Cuanto más angosta la banda, más difícil escribir los datos | Peor caso de acierto de familia (F1, F4) |
| `U_min` (piso de *invertir* por familia) | 0,75 | 0,6 a 0,8. Arriba de 0,8 hacen falta cartas que cubran las 5 familias, porque con 4 por carta el promedio es exactamente 0,8 | Peor caso con *invertir* (F3, F4) |

El validador lee todos estos valores del archivo de configuración; no los tiene fijos en el código.

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

> 📌 **UX Flag — Base de Datos de Cartas:** el tooltip muestra 6 palabras clave con tema y familia. Antes de las historias del tooltip hay que hacer su spec con `/ux-design`, junto con el de la Taxonomía, incluida la legibilidad en Switch portátil.

## Cross-References

| Fuente | Qué se toma |
|---|---|
| GDD §3.1, §3.2, §3.3 | Smith 1909 y restricciones legales; anatomía de la carta; datos públicos |
| GDD §3.4 | Niveles de Mazo; los palos que se suman en las Sedes 3, 5 y 7 (E1) |
| GDD §3.5 | Elemento, palo y número para la Gramática; peso de los Mayores |
| GDD §5.5, §9.2 | Interpretación por palabra clave; el truco *invertir* |
| D-05, D-06, D-08, D-09, D-18, D-22 | Tarot real; escuelas; significado público; robo al azar; 78 cartas; Nivel de Mazo |
| D-47 | Cobertura, `fuente`, informe de cobertura y sujetos de R13 |
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
- **AC-05a** (R4) — GIVEN el fixture con 2 palabras clave en `carta.copas_05/derecha`, WHEN se valida, THEN contiene error de R4 con ese sujeto. Lo mismo con 4.
- **AC-05b** (R4, Tuning Knobs) — GIVEN la configuración con 4 palabras clave por orientación y `carta.copas_05/derecha` con 4 palabras de 4 familias distintas, WHEN se valida, THEN no contiene error de R4 con ese sujeto.
- **AC-06** (R5) — GIVEN `carta.copas_05/derecha` con dos temas de la misma familia de `taxonomia_prueba`, WHEN se valida, THEN contiene error de R5 con ese sujeto. Control: con 3 familias distintas, no lo contiene.
- **AC-07** (R5) — GIVEN `carta.copas_05` cuya derecha e invertida suman 3 familias, WHEN se valida, THEN contiene error de R5 con sujeto `carta.copas_05`. Control: con 4 familias, no lo contiene.
- **AC-08** (R7) — GIVEN el fixture donde `tema.locura` solo aparece en un palo, WHEN se valida, THEN contiene error de R7 con sujeto `tema.locura`.
- **AC-09a** (E5) — GIVEN el fixture con `tema.traicion` deprecado y una palabra clave que lo usa y que lleva `c_Conflicto` del mazo `copas` de 35 a 36, WHEN se valida, THEN no contiene error de F2 con sujeto `copas/familia.conflicto`.
- **AC-09b** (E5) — GIVEN `tema.traicion` deprecado y ausente de los Mayores, WHEN se valida, THEN no contiene error de R7 con sujeto `tema.traicion`.
- **AC-10** (R3, R6) — GIVEN `carta.copas_05/derecha/1` sin `fuente`, con una `fuente` fuera de la lista o con `ubicacion` vacía (un caso cada uno), WHEN se valida, THEN contiene error de R6 con ese sujeto.
- **AC-11** (R6; Config/Data, revisión manual) — GIVEN los datos reales, WHEN se revisa la palabra clave 1 de la derecha de cada una de las 78 cartas, THEN su texto está en la `fuente` y la `ubicacion` citadas. El resultado queda en `production/qa/`.
- **AC-12** (E3) — GIVEN `carta.copas_05` con el mismo tema en la derecha y en la invertida y 4 familias en total, WHEN se valida, THEN no contiene error de R5 con sujeto `carta.copas_05`.
- **AC-13** (E4) — GIVEN el mismo texto en `carta.copas_05/derecha/1` y `carta.oros_05/derecha/1`, WHEN se valida, THEN no contiene error de identificador duplicado.
- **AC-14** (E8) — GIVEN la tabla `es_prueba` sin el texto de `carta.copas_05/derecha/2`, WHEN se valida, THEN contiene error con sujeto `carta.copas_05/derecha/2@es_prueba`.

**Cobertura**
- **AC-15a** (F2) — GIVEN el fixture mutado para que el mazo `copas` tenga `c_Destino` = 35, WHEN se valida, THEN contiene error de F2 con sujeto `copas/familia.destino`. Bordes: con 36 y con 50 no lo contiene; con 51 sí.
- **AC-15b** (F2, E1; parametrizado) — GIVEN, para cada uno de los 15 mazos alcanzables, el fixture mutado para que solo ese mazo viole la banda en `familia.destino`, WHEN se valida, THEN contiene exactamente un error de F2, con el sujeto de ese mazo.
- **AC-15c** (F2; borde en enteros) — GIVEN el mazo `copas+oros+espadas+bastos` (`O` = 156), WHEN `c_Destino` vale 78 y 108, THEN no contiene error de F2; con 77 y con 109, sí.
- **AC-16** (F3) — GIVEN el mazo `copas` con `c_Destino` dentro de la banda y 26 cartas que cubren Destino, WHEN se valida, THEN contiene error **de F3** con sujeto `copas/familia.destino`. Con 27, no lo contiene.
- **AC-17** (Tuning Knobs) — GIVEN la configuración con `C_min` = 37 y el mazo `copas` con `c_Destino` = 36, WHEN se valida, THEN contiene error de F2. GIVEN `U_min` = 0,8 y 28 cartas que cubren Destino, THEN contiene error de F3; con 29, no.

**Informe de cobertura (R11)**
- **AC-18a** (R11) — GIVEN el fixture, WHEN se pide el informe, THEN para cada mazo `q_f` = `c_f / O` y `u_f` coinciden con las cuentas del fixture.
- **AC-18b** (R11, F1) — GIVEN `q` = 0,60 / 0,60 / 0,78 / 0,66 / 0,36 y `p` = 0,20 / 0,20 / 0,25 / 0,20 / 0,15 (orden Emoción, Bienes, Conflicto, Ambición, Destino), WHEN se calcula, THEN `P_pos` = 0,621 ± 0,001.
- **AC-18c** (R11, F4) — GIVEN `q` uniforme 0,6 y `u` uniforme 0,8, WHEN se calcula, THEN `P_cero` = 0,064 y `P_cero_inv` = 0,008 (± 0,001), y el peor caso es 0,064.
- **AC-18d** (R11; *provisorio hasta el Generador*) — GIVEN ningún `p_f` de entrada, WHEN se calcula, THEN usa `p` = 0,20 / 0,20 / 0,25 / 0,20 / 0,15.

**Datos reales y otros**
- **AC-19** (R10; Integration) — GIVEN el catálogo, las cartas y las tablas de idioma reales, WHEN se valida, THEN la lista está vacía. Bloquea la historia de contenido, no la del validador.
- **AC-20** (R3; UI, *provisorio hasta `/art-bible`*) — GIVEN la fuente de referencia de los escaneos de 1909, WHEN se revisan las 78 `arte`, THEN todas apuntan a esa fuente, y una revisión manual con captura retenida en `production/qa/evidence/` confirma que ninguna es la recoloración de 1971.
- **AC-21** (States; Integration, *provisorio hasta Guardado*) — GIVEN una partida guardada, WHEN se carga con una versión del catálogo que cambió el texto de una palabra clave, THEN la verdad del cliente no cambia.
- Lo que muestra el tooltip (R9) lo prueban los AC de Tapete y Tooltips (`/ux-design`).

## Open Questions

| Pregunta | Responsable | Cuándo |
|---|---|---|
| Elemento de los 7 Mayores con atribución planetaria (Mago, Sacerdotisa, Emperatriz, Rueda, Torre, Sol, Mundo): ¿neutro, el del planeta según otra tradición, o un elemento propio? | GDD de Gramática | Al diseñar la Gramática |
| ¿El Generador lee `q_f` del mazo para no favorecer familias escasas? ¿Cuál es el `p_f` real que reemplaza al proporcional de R11? | GDD del Generador | Al diseñar el Generador |
| Medir en el prototipo `P_cero` real por combinación de familias (F4), con el Generador real. Meta tentativa: ninguna combinación de verdades supera 0,15 sin truco | Diseñador | Prototipo del núcleo |
| Cartas sin significados tradicionales de 3 familias distintas en una orientación (E2): cuántas son y qué se decide en cada caso | Diseñador | Al escribir los datos de las 36 cartas del MVP |
| Traducción de las palabras clave del inglés de Waite al español rioplatense: ¿la `ubicacion` cita el original, y quién valida que la traducción no cambie el tema? | Diseñador, `/localize` | Al escribir los datos |
| Fuente de referencia de los escaneos de 1909 y validación legal | `/art-bible` | Antes de producir arte |
