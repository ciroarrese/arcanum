# Review Log — Taxonomía de Temas y Roles

## Review — 2026-10-22 — Verdict: NEEDS REVISION
Review mode: lean · Workflow: standard
Scope signal: M
Specialists: ninguno (lean)
Blocking items: 1 | Recommended: 9
Summary: El diseño es coherente con los pilares y con el GDD maestro, y la comparación exacto / parcial / ninguno es implementable. Lo frenaba una regla de datos ambigua (la familia de los temas de mapa podía contradecir a su equivalente) y varias referencias cruzadas sin cerrar. Las revisiones se aplicaron en la misma sesión (D-42); falta una re-revisión que decida si se aprueba.
Prior verdict resolved: First review
Findings:
- [BLOCKING] Core Rules R4 / Edge Cases E7: la familia declarada por un tema de mapa podía contradecir a su equivalente — corregido: la familia se deriva del equivalente.
- [RECOMMENDED] Core Rules R9: "rol activo" sin definir — corregido.
- [RECOMMENDED] Cross-References: GDD maestro §5.3, §5.8, D-15 y §3.5 desfasados — anotado en Open Questions.
- [RECOMMENDED] Dependencies: faltaban Interpretación y Sentencia, Tapete y Tooltips, Inspección y Tells — corregido.
- [RECOMMENDED] Acceptance Criteria: AC con "el juego no arranca" — pasados al validador del catálogo y sumado AC-25.
- [RECOMMENDED] Open Questions: Carta Única cubre 1 de 3 roles, y falta definir la verdad de "sí o no" — anotado.
- [RECOMMENDED] Registry: los 19 temas no estaban registrados — registrados en entities.yaml.
- [RECOMMENDED] Core Rules R9: no se decía qué combinaciones de temas por rol son válidas — corregido (las define el Generador).
- [RECOMMENDED] Core Rules R1 / E8: `secreto` mal ubicado en Destino — movido a Conflicto.
- [RECOMMENDED] Header: faltan las consultas a systems-designer, game-designer y narrative-director — sigue abierto.
Receipt: sin sello a propósito. El documento se revisó después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.

## Review — 2026-10-22 — Verdict: NEEDS REVISION
Review mode: full · Workflow: standard
Scope signal: M
Specialists: game-designer, systems-designer, qa-lead, narrative-director, creative-director
Blocking items: 5 | Recommended: 8
Summary: La arquitectura (tema y rol separados, tiradas traducidas a roles, validador de datos) es correcta para una capa Foundation, así que el veredicto no es MAJOR. Fallaban cinco cosas locales que había que cerrar antes de cargar datos, porque R3 hace permanentes los ids y el esquema: Destino con 2 temas, un contrato de comparación ambiguo, un ciclo de vida que se contradecía, la colisión de namespaces y AC sin contrato de validador. Las revisiones se aplicaron el 2026-10-23 (D-43); falta una re-revisión que decida si se aprueba.
Prior verdict resolved: Yes — el bloqueante de la revisión lean (familia de los temas de mapa) estaba corregido.
Findings:
- [BLOCKING] Core Rules R1 / E8: Destino con 2 temas (parcial casi imposible; puntaje al azar 0,16 contra 0,32 en Conflicto) y umbral de "30 % de testers" sin base — corregido: enfermedad a Destino, trabajo a Bienes, mínimo 2 temas activos por familia, línea base calculada.
- [BLOCKING] Core Rules R5 / E3 / E4 / E7: "mismo tema" contradecía a E7, faltaban firma, orden de evaluación y SIN_COMPARACION — corregido (R6, R11).
- [BLOCKING] States / R4: deprecar un equivalente de mapa dejaba el juego sin arrancar; no se decía si las cartas podían ofrecer temas deprecados — corregido (DEPRECAR_CON_DEPENDIENTES, sin reactivación, válidos en cartas).
- [BLOCKING] Core Rules R3: colisión familia Conflicto / rol conflicto y esquema sin fijar con ids permanentes — corregido: prefijo por tipo.
- [BLOCKING] Acceptance Criteria: validador sin contrato, AC-05 y AC-25 mal formulados, AC-16..18 con semilla fija, R7 sin cubrir — corregido (R13, AC reescritos, AC-16..18 al Generador, AC-26..32 nuevos).
- [RECOMMENDED] Open Questions: Doble Fondo, coherencia entre roles, agregación y umbral de Resonancia, invariantes de Tiradas, palanca de Cartas, tells y catalog_version — anotados con dueño.
- [RECOMMENDED] Tuning Knobs: faltaba la sección — agregada.
- [RECOMMENDED] Vocabulario: glosario por tema, nota de Regla Cero, nombre visible de Destino y de locura, renombrar riesgo — anotado.
- [RECOMMENDED] E7: hiperinflación es del Mapa A y el MVP no tiene temas de mapa; ¿equivalente deuda o fortuna? — anotado.
- [RECOMMENDED] UI: la marca de familia confunde en cartas de otro palo; AC del tooltip — derivado a /ux-design.
- [RECOMMENDED] Header: nota "no consultados — modo Lean" desactualizada — corregido.
- [RECOMMENDED] Disputa sobre sacar secreto del catálogo: no se reabre D-42 sin un dato nuevo; queda como palanca si el prototipo muestra que Conflicto domina.
- [RECOMMENDED] AC-09 a provisorio, con un parcial por familia — corregido.
Receipt: sin sello a propósito. El documento se revisó después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.
