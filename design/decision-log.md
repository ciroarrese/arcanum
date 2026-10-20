# Registro de Decisiones — Arcanum Vulgaris

Decisiones de diseño tomadas, con su razón. Las preguntas abiertas viven en el GDD (§13).

| # | Fecha | Decisión | Razón |
| :---: | :--- | :--- | :--- |
| D-01 | 2026-10-20 | El juego se llama **Arcanum Vulgaris**. | "Arcanum" a secas choca con títulos existentes (búsqueda y marca). |
| D-02 | 2026-10-20 | Licencia del proyecto: **All rights reserved**. La plantilla CCGS conserva su MIT en `.claude/LICENSE-ClaudeCodeGameStudios`. | Proyecto comercial. |
| D-03 | 2026-10-20 | Partidas **largas** (horas o días) con guardado. Derrota permanente pero **nunca sorpresiva**. | Pedido del diseñador; la muerte instantánea tras horas de juego genera abandono. |
| D-04 | 2026-10-20 | Sistema de **Deudas de Sangre**: hilos de consecuencia escalables con al menos dos salidas; máximo 3 hilos activos. Reemplaza muertes instantáneas y la mora como sistema aparte. | Dar salida al jugador ante errores; la ruina se ve venir. |
| D-05 | 2026-10-20 | El **tarot real** es el núcleo: significados tradicionales y reglas reales de combinación. | Fantasía de "emulador de lector de cartas" con humor negro. |
| D-06 | 2026-10-20 | Escuelas: **Smith 1909 (tradición RWS) + dignidades elementales** como base; **Marsella con lectura en línea** como mazo alternativo; mazo secreto inspirado en Lenormand. Thoth descartado. | Legibilidad de las 78 cartas, significados estandarizados, gramática sistémica, arte de dominio público. Thoth: riesgo de derechos de autor. |
| D-07 | 2026-10-20 | Reglas de combinación sistémicas: posición, orientación, dignidades elementales, palo dominante, peso de Mayores, números repetidos. | Profundidad sin escribir combinaciones una por una. |
| D-08 | 2026-10-20 | El significado individual de cada carta es **público** en el juego; las combinaciones y la lectura de contexto se aprenden jugando. | Accesible para quien no sabe tarot; el dominio está en la combinación. |
| D-09 | 2026-10-20 | Las cartas se **roban al azar**. | Fidelidad al tarot real y a la lectura en frío. |
| D-10 | 2026-10-20 | **Prestidigitación** como comodines limitados: ranuras, cargas por jornada y riesgo de detección. | Palanca de agencia frente al azar. |
| D-11 | 2026-10-20 | Entre partidas se conserva: conocimiento del jugador, mazos desbloqueados, Grados de Infamia, historial de Lectura Diaria. | Meta-progresión basada en conocimiento. |
| D-12 | 2026-10-20 | Entran las 5 propuestas de vida útil: prestidigitación, clientes por combinación, Grados de Infamia, mazos con gramática propia, Lectura Diaria. | Extender la vida útil más allá del dominio del conocimiento. |
| D-13 | 2026-10-20 | **Motor:** se elige después de cerrar los documentos base. | Elegir según requisitos reales (incluido el port a Switch). |
| D-14 | 2026-10-20 | Tiradas variables según motivo: Carta Única (1), Tres Tiempos (3), Dos Caminos (5), El Vínculo (5), Cruz Celta (10). La tirada define la profundidad y el costo en UT. | Variar la lectura según el motivo y la situación del cliente. |
| D-15 | 2026-10-20 | Resolución por **Resonancia** (coincidencia de temas por posición × dignidades + bonos − contradicciones) e intención coherente con el estado real. | Conecta pistas, cartas e intención con una sola regla. |
| D-16 | 2026-10-20 | Género: **Roguelite de deducción** (se abandona "Arcade Roguelike"). | Coherente con partidas largas (D-03). |
| D-17 | 2026-10-20 | Trucos de prestidigitación iniciales (mirar, invertir, cambiar, forzar, preparar el mazo), 3 ranuras ampliables a 5. Nombres de mazos: **Smith 1909** (base) y **Petit Jeu de la Sibila** (secreto). | Confirmado por el diseñador; "Smith 1909" evita la marca "Rider-Waite". |
| D-18 | 2026-10-20 | El mazo base usa las **78 cartas**, con invertidas. | Las dignidades elementales necesitan los palos de los Arcanos Menores. |
| D-19 | 2026-10-20 | Época: **fines del siglo XX**. El escalado va de cosas muy simples a poder, riqueza y lujo. | Decisión del diseñador; escenario concreto en discusión. |
| D-20 | 2026-10-20 | Rango de fechas: **1985–1995**. | Evita celulares e internet masivos, que romperían la lectura en frío. |
| D-21 | 2026-10-20 | **Varios mapas** por escenario. Orden: **B** (EE. UU. años 80, MVP) → **A** (Latinoamérica 1985–1995) → **C** (Europa del Este 1989–1993). Comparten los sistemas centrales. | Información de sobra para el MVP en B; A y C amplían la vida útil. |
| D-22 | 2026-10-20 | **Nivel de Mazo** (Aprendiz 36 / Oficial 50 / Maestro 78 cartas) como curva de aprendizaje y selector de complejidad, disponible desde el inicio, con multiplicador de recompensa. | El jugador experto no queda obligado a empezar con pocas cartas. |
| D-23 | 2026-10-20 | **MVP:** Mapa B, Sedes 1–3, 5 arquetipos, Carta Única y Tres Tiempos, nivel Aprendiz, 3 trucos, Usurero + 1 hilo. | Validar el núcleo (leer cartas) antes de invertir en contenido. |
| D-24 | 2026-10-20 | Los mapas **se desbloquean jugando**: llegar a la Sede 8 del mapa anterior, sin necesidad de ganar. | Objetivo para el jugador nuevo; enseña los sistemas en el mapa más legible. |

