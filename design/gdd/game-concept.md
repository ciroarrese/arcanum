# Game Concept: Arcanum Vulgaris

*Created: 2026-10-22 · Updated: 2026-10-23 (arte: D-48 a D-51)*
*Status: Draft*

> **Este documento es una síntesis.** La fuente de verdad del diseño es
> `design/ARCANUM_VULGARIS_GDD.md` (v1.9); las decisiones y su razón, en
> `design/decision-log.md`. Acá no se copian valores numéricos (tarifas, UT,
> umbrales): se citan las secciones. Si algo de este documento contradice al GDD
> maestro, gana el GDD maestro y este documento se corrige.

---

## Elevator Pitch

> Un roguelite de deducción donde sos un tarotista estafador que lee cartas de
> tarot reales y los tells de sus clientes para vaciarles la billetera y
> sobrevivir, en una metrópolis estadounidense de 1987 que corre hacia el crac.

Fuente: Pitch §1; GDD §2.

---

## Core Identity

| Aspect | Detail |
| ---- | ---- |
| **Genre** | Roguelite de deducción psicológica, lectura de tarot y gestión de riesgo y tiempo (D-16) |
| **Platform** | PC (Steam, Steam Deck) y Nintendo Switch (Pitch, Ficha Técnica) |
| **Target Audience** | Ver Target Player Profile |
| **Player Count** | Un jugador |
| **Session Length** | 30–60 min, unas 3–5 jornadas *(hipótesis; la jornada se estima en 8–12 min, `design/balance/economia-mvp.md` §4, a medir en el prototipo)* |
| **Monetization** | Premium, USD 14.99–19.99, con expansiones de mapas (Pitch, Ficha Técnica) |
| **Estimated Scope** | Large — **[A DEFINIR]**: el timeline se fija con datos del prototipo del núcleo |
| **Comparable Titles** | *Papers, Please*, *Balatro*, *Return of the Obra Dinn* (también *Inscryption*, *Strange Horticulture*) |

---

## Core Fantasy

Sos un psicólogo callejero, no un mago. Las cartas no predicen nada: funcionan
porque el cliente cree en ellas. El poder está en ver lo que el otro esconde,
decidir qué verdad o qué mentira venderle y cobrarla, mientras subís de una
manta en la vereda a un penthouse donde le leés el destino a la gente que maneja
la ciudad. (GDD, Tesis de Diseño; Pitch §2)

---

## Unique Hook

Es como *Papers, Please*, **y además** el documento que inspeccionás es una
tirada de tarot real, que salió al azar, y la tenés que hacer coincidir con un
secreto que dedujiste mirando la cara del cliente.

El significado de cada carta es público. Lo que se domina jugando es combinarlas
(dignidades elementales, palo dominante, peso de los Mayores) y aplicarlas a cada
cliente (GDD §3.3, §3.5; D-05, D-08).

---

## Player Experience Analysis (MDA Framework)

### Target Aesthetics (What the player FEELS)

*Orden aprobado como hipótesis (2026-10-22).*

| Aesthetic | Priority | How We Deliver It |
| ---- | ---- | ---- |
| **Challenge** | 1 | Deducir el secreto con tells fugaces y la memoria como única libreta; leer una tirada al azar con la gramática real |
| **Fantasy** | 2 | El estafador de lectura en frío, con humor negro; la ciudad de los 80 |
| **Discovery** | 3 | Las combinaciones que no explica el juego; los Doble Fondo; los mazos desbloqueables |
| **Narrative** | 4 | Situaciones combinatorias (arquetipo × secreto × motivo × urgencia); Deudas de Sangre que escalan |
| **Expression** | 5 | La sentencia: acusar, consolar, sembrar paranoia o extorsionar |
| **Sensation** | 6 | Golpe de la carta, hitstop de revelación, vela y humo (GDD §11.2) |
| **Fellowship** | N/A | Un jugador; la Lectura Diaria compite por ranking, no socializa |
| **Submission** | N/A | El juego presiona a propósito (tiempo, fila, deudas) |

### Key Dynamics (Emergent player behaviors)

- Provocar tells con preguntas para decidir si apostar al secreto o a la fachada.
- Elegir la tirada según el motivo y el tiempo que queda en la vela.
- Reinterpretar una carta contradictoria en lugar de esconderla con un truco, o al revés.
- Rechazar o atender a un cliente peligroso midiendo la Deuda de Sangre que abriría.
- Aprender combinaciones entre partidas y llevarlas en la cabeza (D-11).

### Core Mechanics (Systems we build)

1. Inspección y tells provocados por preguntas capciosas (GDD §5.2).
2. Tiradas de tarot real con robo al azar, gramática de combinación y prestidigitación (GDD §3.5, §5.4, §5.5).
3. Sentencia con 4 intenciones retóricas y resolución por Resonancia (GDD §5.6, §5.8).
4. Jornada con vela por acción, fila con paciencia y cierre de caja (GDD §5.1, §7).
5. Deudas de Sangre: consecuencias que escalan con salidas (GDD §8).

---

## Player Motivation Profile

### Primary Psychological Needs Served

| Need | How This Game Satisfies It | Strength |
| ---- | ---- | ---- |
| **Autonomy** | A quién atender, qué tirada usar, qué intención elegir, verdad o mentira | Core |
| **Competence** | Leer mejor la tirada y al cliente; el pago por calidad premia investigar (D-36) | Core |
| **Relatedness** | Clientes con historia propia y el mundo de la sede; sin vínculos sociales reales | Minimal |

### Player Type Appeal (Bartle Taxonomy)

- [x] **Explorers** (primario) — How: entender un sistema de combinación real que el juego no explica.
- [x] **Achievers** (secundario) — How: sedes, mazos desbloqueables y Grados de Infamia (GDD §10.3).
- [ ] **Socializers** — no apunta.
- [x] **Killers/Competitors** (terciario) — How: ranking de la Lectura Diaria (GDD §10.4; Full Vision).

### Flow State Design

- **Onboarding curve**: Nivel de Mazo Aprendiz (36 cartas), Carta Única y Tres Tiempos, significados siempre consultables (GDD §3.3, §3.4).
- **Difficulty scaling**: más cartas por Nivel de Mazo, tiradas más grandes, sedes con clientes más poderosos; Grados de Infamia para expertos.
- **Feedback clarity**: el juego muestra por qué resonó o no una lectura (mitigación de riesgo de Resonancia, `systems-index.md`).
- **Recovery from failure**: la derrota nunca es sorpresiva; las Deudas de Sangre avisan y tienen salidas (D-03, D-04). Perder la partida conserva el conocimiento y los desbloqueos.

---

## Core Loop

### Moment-to-Moment (30 seconds)
Mirar al cliente, lanzar una pregunta capciosa y atrapar el tell en su ventana de
2–3 segundos; robar, mirar las cartas e interpretar una posición. (GDD §5.2, §5.5)

### Short-Term (5-15 minutes)
Una jornada: elegir clientes por la mirilla, leer a cada uno y sentenciar,
mientras la vela se consume por acción. Cierre nocturno con balance, deudas y
trastienda. (GDD §4)

### Session-Level (30-120 minutes)
Varias jornadas hasta juntar dinero, Fama y Reputación para mudarse de sede, o
hasta cerrar o desactivar un hilo de Deuda de Sangre. El guardado al cierre de
cada jornada da un corte natural (D-03).

### Long-Term Progression
Subir las 8 sedes de un mapa hasta la victoria (en el Mapa B, el Lunes Negro);
desbloquear mapas al llegar a la Sede 8 (D-24), mazos y Grados de Infamia. El
progreso real es lo que el jugador aprende (GDD §10).

### Retention Hooks
- **Curiosity**: el próximo Doble Fondo; el mazo de Marsella y el secreto con gramática propia; los Mapas A y C.
- **Investment**: una partida larga con guardado; la sede ganada.
- **Social**: la Lectura Diaria con semilla compartida (Full Vision).
- **Mastery**: combinaciones, Grados de Infamia, Nivel de Mazo Maestro (78 cartas).

---

## Game Pillars

La Regla Cero y los 6 pilares del GDD maestro §1, sin cambios. Se conservan los
seis (la plantilla sugiere 3–5) porque el resto del diseño los cita por número.

### Regla Cero: Nada es Sobrenatural
Ningún sistema asume fuerzas sobrenaturales; todo se explica por psicología,
sesgo, puesta en escena y percepción. Las cartas funcionan porque el cliente cree.

*Design test*: si un efecto solo se explica con magia (una carta que "acierta"
sola), se descarta o se reescribe como sesgo, puesta en escena o percepción.

### Pilar 1: La Verdad no es Mágica, es Observable
El jugador saca información de microdetalles visuales y del lenguaje corporal que
provocan sus preguntas.

*Design test*: entre darle al jugador un dato directo ("culpa 70 %") o una señal
que tiene que observar o provocar, gana la señal.

### Pilar 2: El Dilema de la Sentencia
Descubrir la verdad es el comienzo; decidir si decirla, edulcorarla, mentir o
extorsionar define la supervivencia.

*Design test*: si una intención retórica domina en todas las situaciones, se
rebalancea hasta que la verdad y la mentira tengan cada una su caso rentable.

### Pilar 3: Memoria Pura sobre el Cliente
Lo que el jugador observa del cliente vive en su memoria. El significado de las
cartas es público y consultable.

*Design test*: si una función guarda o vuelve a mostrar algo que el jugador ya vio
del cliente, no entra; si muestra el significado de las cartas, sí.

### Pilar 4: Gestión de Riesgo Probabilístico (Doble Fondo)
Jugar a la fachada rinde poco y seguro; apostar al secreto multiplica o arruina.

*Design test*: la fachada siempre rinde poco y seguro, y apostar al secreto
siempre lleva riesgo visible; nunca hay apuesta garantizada.

### Pilar 5: Tiranía del Tiempo y Gestión de Fila
Atender a fondo a un pez gordo enfurece a la fila; apurarse baja la efectividad.

*Design test*: entre una acción gratis y una que cuesta UT, cuesta UT, salvo
interpretar las cartas, que nunca corre el reloj (D-28).

### Pilar 6: No hay Carta Mala, hay Lector Malo
Las cartas salen al azar; el mérito es hacer que cualquier tirada juegue a favor.

*Design test*: si una tirada puede dejar al jugador sin jugada útil, se agrega una
palanca (otra palabra clave, una reinterpretación, un truco) antes que reducir el
azar.

### Anti-Pillars (What This Game Is NOT)

- **NOT magia real ni muerte sorpresiva**: rompe la Regla Cero y D-03; tras horas de partida, una muerte sin aviso provoca abandono.
- **NOT tarot como combate numérico**: el tarot no es un deckbuilder de daño; si las cartas se vuelven números, se pierde la lectura (Pitch §2).
- **NOT notas sobre el cliente ni voces grabadas**: las notas rompen el Pilar 3; las voces encarecen producción y localización (D-31).
- **NOT identidad neón/synthwave**: es el cliché saturado de los 80; la identidad viene del tarot y de la mesa (`mapa-b-new-carthage.md` §9).

---

## Visual Identity Anchor

**Dirección: "La Mesa del Otro Lado"** — propuesta por el art-director (veredicto
STRONG, 2026-10-22) a partir de la referencia de construcción de mundo de
*ReStory*; actualizada el 2026-10-23 con el estilo y la producción aprobados
(D-48 a D-51). Reglas de detalle: `design/art/patron-personajes.md` y
`design/art/patron-sedes.md`.

**Regla visual:** la luz siempre cae sobre la mesa y sobre la cara del cliente;
lo que cambia de sede en sede es todo lo que queda fuera de ese círculo.

**Principios:**
1. **El círculo de lámpara (legibilidad).** La cara del cliente y la mesa son la
   zona más clara del cuadro en las 8 sedes, incluido el Penthouse.
   *Design test:* captura en gris y desenfocada; si lo más claro no es la cara y
   la mesa, falla.
2. **La misma pluma.** Clientes, sedes y mesas comparten la tinta de manga seinen,
   el rayado y la textura de papel; las cartas de 1909 conviven por el contorno de
   tinta y el color plano.
   *Design test:* cliente, fondo y una carta juntos; si parecen de dos juegos, falla.
3. **La interfaz es un objeto.** Vela, caja y herramientas existen sobre la mesa y
   cambian de material con la sede.
   *Design test:* si un dato de la interfaz flota sin objeto que lo sostenga,
   falla (salvo menús fuera de partida).

**Invariante en todas las sedes:** encuadre en primera persona, mesa en el tercio
inferior, cliente frontal al centro con el fondo de tono medio detrás, el elemento
que identifica la sede a un costado, el círculo de luz, el trazo y la posición de
cada objeto de interfaz (vela a la derecha, dinero a la izquierda).
**Variable:** la luz según la hora de la jornada (6 versiones por fondo, D-49), la
variante de entorno elegida por la semilla (hasta 2 por sede, D-51), materiales,
objetos y vestuario del cliente.

**Filosofía de color:** la luz cambia con la hora de la jornada, de la madrugada a
la noche, en todas las sedes. El arco de lúgubre (Sede 1) a luminoso (Sede 8) lo
cargan los **materiales y objetos** (D-50): frazada y lata abajo, mármol, oro viejo
y plata arriba; el lujo se marca con material y reflejo, no con saturación. Paleta
apagada de los 80, sin neón. Al mediodía el motor cuida que el cielo no supere a
la cara. La cabina de neón de la Sede 4 se ve desde adentro: el cartel tiñe el
fondo, nunca la cara.

**Personajes (D-48):** ilustración de manga seinen con tinta de grosor variable,
rayado y textura de papel; reemplaza la caricatura editorial (D-40), que generaba
rechazo. Edad real, ojos medianos y siempre despejados, sin rasgos fijos que se
confundan con tells; el estilo no embellece a nadie y la suciedad es del
personaje, no del dibujo. Cada cliente es una imagen neutra con las manos en una
línea fija (la mesa es otra capa) y una faceta por tell. Referencia de estilo:
`assets/art/personajes/vagabundo-variante-viejo.png`.

**Producción:** arte 2D generado con Recraft. Cada fondo se aprueba una vez y se
reilumina para las 6 horas, alineado píxel a píxel para el fundido en el motor.
Clientes, fondo y mesa son capas separadas. El boceto 3D por script
(`prototypes/arte-sede1/`) queda como guía opcional de composición. La Sede 1
está aprobada (`assets/art/sede1/`). **Pendiente:** escalar los originales al
doble y elegir cómo hacer el parallax (capas recortadas o mapa de profundidad).

---

## Inspiration and References

| Reference | What We Take From It | What We Do Differently | Why It Matters |
| ---- | ---- | ---- | ---- |
| *Papers, Please* | Inspección bajo presión de tiempo con dilema moral | El "documento" es una tirada al azar que se interpreta, no se valida | Valida que la inspección tensa sostiene un juego |
| *Balatro* | Azar de cartas con palancas del jugador | No hay puntaje: la carta se lee contra un secreto | Valida el público de cartas con azar y dominio |
| *Return of the Obra Dinn* | Deducción sin que el juego confirme a medias | La deducción es en vivo y cara a cara | Valida la deducción pura como placer |
| *ReStory* | Construcción del mundo: primera persona sobre una mesa, cliente enfrente, interfaz diegética | Manga seinen con tinta y rayado, no anime limpio; el fondo cambia con la hora | Referencia visual del anchor |

**Non-game inspirations**: el tarot de Pamela Colman Smith (1909); la lectura en
frío y el mentalismo; el Wall Street de 1987 y el crac del Lunes Negro; los
telepredicadores y las líneas de videntes de la TV de los 80; el manga seinen y la
historieta de tinta de la época.

---

## Target Player Profile

*Aprobado como hipótesis (2026-10-22).*

| Attribute | Detail |
| ---- | ---- |
| **Age range** | 20–40 |
| **Gaming experience** | Mid-core |
| **Time availability** | Sesiones de 30–60 min; partidas largas con guardado |
| **Platform preference** | PC y Steam Deck; Switch en portátil |
| **Current games they play** | *Balatro*, *Papers, Please*, *Inscryption* |
| **What they're looking for** | Deducción tensa con humor negro y un sistema real para dominar |
| **What would turn them away** | Tener que saber tarot de antemano (no hace falta: el significado está en pantalla); muertes injustas |

---

## Technical Considerations

| Consideration | Assessment |
| ---- | ---- |
| **Recommended Engine** | **Sin elegir** (D-13). Candidato fuerte: Unity, por el soporte de Switch; se decide con `/setup-engine` y datos verificados |
| **Key Technical Challenges** | Generador de situaciones coherentes y deducibles; plantillas de texto que sobrevivan la traducción; tells legibles en Switch portátil; azar reproducible con semilla |
| **Art Style** | 2D en capas (fondo por hora, cliente, mesa), manga seinen con tinta, rayado y color plano; parallax pendiente de definir |
| **Art Pipeline Complexity** | Medium (custom 2D asistido por IA) |
| **Audio Needs** | Moderate: balbuceo expresivo por arquetipo, sin voces (D-31), feedback sensorial (GDD §11) |
| **Networking** | Ninguno en partida; ranking online de la Lectura Diaria (Full Vision) |
| **Content Volume** | 78 cartas (36 en el MVP); 10 arquetipos + 2 por mapa; ~15 secretos; 5 tiradas; 8 sedes por mapa, 3 mapas |
| **Procedural Systems** | Situación del cliente por combinación (GDD §5.3); robo al azar; RNG con semilla |

---

## Risks and Open Questions

### Design Risks
- El Generador de Situaciones no produce situaciones coherentes y deducibles: la deducción se siente arbitraria.
- La Resonancia no se siente justa ni explicable.
- La Taxonomía de Temas y Roles mal cortada contamina cartas, situaciones y textos.
- Deudas de Sangre en espiral de muerte.

### Technical Risks
- Plantillas de texto que se rompen al traducir (género, número, concordancia).
- Rendimiento y legibilidad en Switch portátil.

### Market Risks
- El nicho del tarot puede alejar a quien no lo conoce; mitigación: significados públicos (D-08).
- Comparación directa con *Papers, Please* y *Balatro*.

### Scope Risks
- 1 persona: ~60 sesiones de diseño para el MVP (D-38).
- Contenido de cartas: 78 × palabras clave derechas e invertidas × temas; el MVP usa 36.
- Consistencia de estilo entre clientes generados con IA (mitigación: patrón de personajes).
- Volumen de fondos: 6 horas × hasta 2 variantes × 8 sedes por mapa.

### Open Questions
- Parallax: capas recortadas o mapa de profundidad → prueba con la Sede 1 antes de generar más sedes.
- Duración de cada tramo de luz de la jornada → GDD del Reloj de Vela.
- Motor → `/setup-engine` después de este documento.
- Timeline por tier → con datos del prototipo del núcleo.
- Pendientes del GDD §13: Mapas A y C, rebalanceo de economía, tirada final del Lunes Negro.

---

## MVP Definition

**Core hypothesis**: leer cartas de tarot reales a clientes generados por
combinación es divertido, y la deducción se siente justa.

**Required for MVP** (D-23, GDD §15):
1. Mapa B, Sedes 1–3, 5 arquetipos.
2. Carta Única y Tres Tiempos, Nivel de Mazo Aprendiz (36 cartas).
3. Tells y preguntas, sentencia y Resonancia con pago por calidad.
4. 3 trucos de prestidigitación.
5. Deudas de Sangre: El Usurero + 1 hilo de arquetipo.

El MVP termina al alcanzar la Sede 3 y sobrevivir N jornadas (D-26).

**Explicitly NOT in MVP**: Cruz Celta y demás tiradas, mazos alternativos,
Grados de Infamia, Lectura Diaria, Sedes 4–8, Mapas A y C.

### Scope Tiers (if budget/time shrinks)

| Tier | Content | Features | Timeline |
| ---- | ---- | ---- | ---- |
| **MVP** | Mapa B, Sedes 1–3, 5 arquetipos, 36 cartas | Núcleo de lectura y supervivencia diaria | [A DEFINIR] |
| **Vertical Slice** | MVP + Informantes, escenas de derrota y victoria | Audio, tutorial, menú | [A DEFINIR] |
| **Alpha** | Mapa B completo | Regla de Mapa, meta-progresión | [A DEFINIR] |
| **Full Vision** | Mapas A y C, mazos alternativos | Lectura Diaria, servicios de plataforma | [A DEFINIR] |

---

## Next Steps

- [ ] Escalar el arte aprobado y probar el parallax con la Sede 1
- [ ] Diseñar el núcleo de lectura (`/design-system`): Taxonomía → Cartas → Tiradas → Generador → Resonancia
- [ ] Prototipo del núcleo (`/prototype`)
- [ ] Elegir motor (`/setup-engine`)
- [ ] Art Bible (`/art-bible`), a partir de `design/art/`
- [ ] Revisar este documento con `/design-review` en una sesión nueva
