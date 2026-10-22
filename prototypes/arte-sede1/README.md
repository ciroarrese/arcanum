# Prototipo de arte — Sede 1 (La Boca del Subte)

Prueba descartable del método "3D como andamio, arte final en 2D" (ver `design/gdd/game-concept.md`, Visual Identity Anchor).

- `sede1_blockout.py` — arma la Sede 1 en Blender por código (volúmenes, cámara en primera persona, luz) y la renderiza con Cycles.
- `sede1_render.png` — render de referencia (128 muestras).
- `sede1_render_gris.png` — test de legibilidad: escala de grises + desenfoque. La cara del cliente y la mesa deben ser lo más claro del cuadro.
- `cartas/` — tres cartas de la edición de 1909 de Pamela Colman Smith (dominio público; escaneos de Wikimedia Commons), reducidas.

## Resultado (2026-10-22)

- Composición y arco de luz: funcionan. Cada render tarda entre 30 y 60 s en CPU; reiluminar es cambiar valores.
- Test de legibilidad: **casi pasa**. Cara 74, globo verde 79, mesa 54 (luminancia media 0-255, desenfoque gaussiano de radio 18). La regla no se cumple sola: hay que medirla en cada sede.
- Geometría: primitiva (bloques y cilindros). Sirve de guía, no de arte.
- **Sin probar:** el paso a 2D (pintar o generar con IA sobre el render). Es el eslabón que valida el método.

Script de prototipo: no sigue los estándares de código del juego.
