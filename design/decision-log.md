# Registro de Decisiones — Arcanum Vulgaris

Decisiones de diseño tomadas, con su razón. Las preguntas abiertas viven en el GDD (§13).

| # | Fecha | Decisión | Razón |
| :---: | :--- | :--- | :--- |
| D-01 | 2026-10-20 | El juego se llama **Arcanum Vulgaris**. | "Arcanum" a secas choca con títulos existentes (búsqueda y marca). |
| D-02 | 2026-10-20 | Licencia del proyecto: **All rights reserved**. La plantilla CCGS conserva su MIT en `.claude/LICENSE-ClaudeCodeGameStudios`. | Proyecto comercial. |
| D-03 | 2026-10-20 | Partidas **largas** (horas o días) con guardado. Derrota permanente pero **nunca sorpresiva**. | Pedido del diseñador; la muerte instantánea tras horas de juego genera abandono. |
| D-04 | 2026-10-20 | Sistema de **Deudas de Sangre**: hilos de consecuencia escalables con al menos dos salidas; máximo 3 hilos activos. Reemplaza muertes instantáneas y la mora como sistema aparte. | Dar salida al jugador ante errores; la ruina se ve venir. |
| D-05 | 2026-10-20 | El **tarot real** es el núcleo: significados tradicionales y reglas reales de combinación. | Fantasía de "emulador de lector de cartas" con humor negro. |
| D-06 | 2026-10-20 | Escuelas: **Tarot Smith de 1909 (tradición RWS) + dignidades elementales** como base; **Marsella con lectura en línea** como mazo alternativo; mazo secreto inspirado en Lenormand. Thoth descartado. | Legibilidad de las 78 cartas, significados estandarizados, gramática sistémica, arte de dominio público. Thoth: riesgo de derechos de autor. |
| D-07 | 2026-10-20 | Reglas de combinación sistémicas: posición, orientación, dignidades elementales, palo dominante, peso de Mayores, números repetidos. | Profundidad sin escribir combinaciones una por una. |
| D-08 | 2026-10-20 | El significado individual de cada carta es **público** en el juego; las combinaciones y la lectura de contexto se aprenden jugando. | Accesible para quien no sabe tarot; el dominio está en la combinación. |
| D-09 | 2026-10-20 | Las cartas se **roban al azar**. | Fidelidad al tarot real y a la lectura en frío. |
| D-10 | 2026-10-20 | **Prestidigitación** como comodines limitados: ranuras, cargas por jornada y riesgo de detección. | Palanca de agencia frente al azar. |
| D-11 | 2026-10-20 | Entre partidas se conserva: conocimiento del jugador, mazos desbloqueados, Grados de Infamia, historial de Lectura Diaria. | Meta-progresión basada en conocimiento. |
| D-12 | 2026-10-20 | Entran las 5 propuestas de vida útil: prestidigitación, clientes por combinación, Grados de Infamia, mazos con gramática propia, Lectura Diaria. | Extender la vida útil más allá del dominio del conocimiento. |
| D-13 | 2026-10-20 | **Motor:** se elige después de cerrar los documentos base. | Elegir según requisitos reales (incluido el port a Switch). |

## Propuestas pendientes de confirmación
| # | Propuesta | Estado |
| :---: | :--- | :--- |
| P-01 | Tiradas variables según motivo: Carta Única (1), Tres Tiempos (3), Dos Caminos (5), El Vínculo (5), Cruz Celta (10). La tirada define la profundidad y el costo en UT. | Propuesta en GDD §5.4; a confirmar. |
| P-02 | Resolución por **Resonancia** (coincidencia de temas por posición × dignidades + bonos − contradicciones) e intención coherente con el estado real. | Propuesta en GDD §5.7; a confirmar. |
| P-03 | Etiqueta de género "Roguelite de deducción" en lugar de "Arcade Roguelike". | Aplicada en el Pitch; a confirmar. |
