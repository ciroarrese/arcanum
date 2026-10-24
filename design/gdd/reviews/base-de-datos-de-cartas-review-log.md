# Review Log — Base de Datos de Cartas

## Review — 2026-10-24 — Verdict: NEEDS REVISION
Review mode: lean · Workflow: standard
Scope signal: L
Specialists: ninguno (lean)
Blocking items: 4 | Recommended: 9
Summary: La estructura y las cuentas de F2 a F4 verifican contra el conteo de Waite (`P_pos` ≈ 0,274, `P_cero` ≈ 0,38). El catálogo no se podía cargar de forma consistente: E2 contradecía a R6 y a la Taxonomía (`KW_SIN_TEMA`), y la cifra "14 de 72" no coincidía con el conteo (11 a 18 según el mazo). El riesgo de fondo, `P_cero` ≈ 0,38 contra el Pilar 6, es un costo aceptado en D-48 y no se relitigó, pero no tenía umbral falsable. Pasada lean: no sustituye una full.
Prior verdict resolved: First review
Findings:
- [BLOCKING] E2/R6: "elegir el tema más cercano" contradecía "nunca forzar" y el esquema no admitía orientación sin tema — corregido (campo `forzada`, orden de 4 pasos en E2, F2 solo sobre claras).
- [BLOCKING] E2/Open Questions: "14 de 72" falso; el conteo da 11 a 18, y 17 en Mayores + Copas — corregido.
- [BLOCKING] R3: `atribucion` sin definir para las 56 menores — corregido (decanato del *Book T* en 2 a 10, vacía en As y figuras; AC-04d).
- [BLOCKING] R4: ids `<1–3>` contra una perilla de máximo 4 — corregido (`<n>`, límites de la perilla, `orientaciones_con_una`, AC-05b/c).
- [RECOMMENDED] F3/F4: *invertir* citado como palanca sin número y sin umbral para el Pilar 6 — corregido (`P_pos_inv` ≈ 0,355 como cota, `P_cero_max` provisorio 0,30, AC-18e/f).
- [RECOMMENDED] F1: contrato de sorteo con un Generador sin diseñar — corregido (marcado como interfaz provisoria).
- [RECOMMENDED] R8: el 10 % repetido a mano — corregido (`Q_min`).
- [RECOMMENDED] AC-10: etiquetas de reglas equivocadas — corregido (R4; R6 lo cubre AC-11).
- [RECOMMENDED] AC-11: verificaba solo 78 de unas 400 palabras clave — corregido (MVP completo, todas las forzadas y muestra del 25 %).
- [RECOMMENDED] AC-09a ilegible, AC-15b sin receta, faltaban AC de `P_exacto` y de R7 con tema deprecado — corregido (AC-09a/c, AC-15b/d, AC-18b).
- [RECOMMENDED] Índice: línea de orden de diseño del Generador sin Cartas — corregido.
- [ADVISORY] Player Fantasy ausente — sin cambio.
- [NICE] Registro: Cartas no figura en `referenced_by` de los 23 temas — sin cambio.
Abierto tras las correcciones: el Dos de Copas invertida no tiene significado en Waite y E2 paso 4 no le da salida; `P_cero_max` es una propuesta a confirmar; falta rehacer la tabla por carta con los 23 temas.
Receipt: sin sello a propósito. El GDD se corrigió después de esta revisión, y un sello de la versión corregida haría pasar el documento nuevo por el que falló.
