# Patrón de diseño de sedes y mesas

Cada sede son tres capas que se apilan: **fondo** (el entorno, con la luz de la
hora), **cliente** (ver `patron-personajes.md`) y **mesa** (primer plano). Estilo:
el mismo de los personajes (D-48). Referencia aprobada: `assets/art/sede1/`.

## Fondos

1. Vista en primera persona desde la silla del tarotista, cámara a la altura de los ojos sentado, horizonte a media altura, perspectiva de un punto, 16:9.
2. Escena vacía: sin gente, sin mesa, nada en primer plano.
3. **El centro, detrás del cliente, es tranquilo y de tono medio:** ni muy oscuro (el cliente se funde) ni muy claro (compite con la cara).
4. **Lo que identifica a la sede va a un costado**, nunca en el centro, porque el cliente lo tapa.
5. Ese elemento tiene que seguir visible con la mesa delante. Preferentemente, del lado opuesto a la vela (la vela va a la derecha).
6. Paleta apagada de los 80, sin neón (D-41).

## Ciclo de horas (D-49)

Cada fondo tiene **6 versiones**, una por hora de la jornada, generadas reiluminando la misma imagen:

| Archivo | Hora |
|---|---|
| `-1-madrugada` | Antes del amanecer |
| `-2-manana` | Mañana |
| `-3-mediodia` | Mediodía |
| `-4-siesta` | Primeras horas de la tarde |
| `-5-tarde` | Tarde dorada |
| `-6-noche` | Noche |

- Las 6 versiones tienen que estar alineadas píxel a píxel: el motor pasa de una a otra con un fundido. Comprobar con un fundido 50/50 que no aparezcan líneas dobles.
- El motor tiñe al cliente y a la mesa con la luz de cada hora.
- **Al mediodía y en la siesta el cielo puede quedar más claro que la cara:** el motor baja el cielo o sube la luz del cliente para que la cara y la mesa sigan siendo lo más claro.
- Cuánto dura cada tramo lo define el GDD del Reloj de Vela.

## Variantes de entorno (D-51)

- Hasta **2 variantes** por sede: el mismo lugar con otra composición o decorado.
- La variante se elige al empezar la partida, a partir de la **semilla** (RNG con Semilla), para que la Lectura Diaria muestre el mismo entorno a todos y los bugs se puedan reproducir.
- Las variantes difieren solo en el decorado: ninguna tiene más o menos pistas.

## Arco entre sedes (D-50)

Como cada sede pasa por todas las horas, el arco de lúgubre a luminoso (Sede 1 a 8)
lo cargan los **materiales y objetos**, no la luz: frazada y lata en la Sede 1,
terciopelo y bronce en la Sede 3, mármol y plata en la Sede 8. Al mediodía, la
Sede 1 se sigue viendo pobre.

## Mesas

1. La mesa es una capa con fondo transparente; su borde lejano es una línea horizontal que coincide con la línea de manos del cliente.
2. El paño deja un espacio central despejado para las cartas de la tirada.
3. **Sin vela y sin dinero:** la mesa trae solo el lugar donde van. La vela es otra capa, porque se anima a medida que se consume. Vela a la derecha, dinero a la izquierda.
4. Los agujeros del paño no pueden ser transparentes: dejan ver lo que hay debajo, no el fondo. `tools/art/fill_holes.py` rellena los agujeros encerrados. Los que tocan el borde del fleco se retocan a mano.
5. Recraft dibuja las mesas como objetos sueltos vistos desde arriba. Funcionan escaladas al ancho de pantalla, con el frente cortado por el borde inferior.

## Producción pendiente

- **Resolución:** los originales salen a 1376 × 768. Escalar al doble (2752 × 1536) después de aprobar, para 1080p y 4K, con margen para el parallax.
- **Parallax:** cada fondo es una imagen plana. Hay que elegir entre recortar capas o usar un mapa de profundidad (2.5D). Las dos opciones sirven para las 6 horas de una variante porque están alineadas. Probarlo con la Sede 1 antes de generar más sedes.

## Prompts compartidos

**Fondos:**
```
First-person view from a seated tarot reader, camera at seated eye level looking straight ahead, horizon at the middle of the image, one-point perspective, 16:9. Empty scene: no people, no table, no furniture in the lower third. The central area behind where a seated client's head would be is calm and low in detail. Seinen manga illustration with black ink lineart of varying weight, bold widely spaced cross-hatching, two to three flat muted color tones per surface, subtle warm paper texture. Muted 1980s palette, no neon, no text, no readable signs except where specified.
```

**Mesas:**
```
A tabletop seen from the seated reader's point of view, matching a first-person camera at seated eye level, 16:9, the table filling only the lower third of the image; its far edge is a straight horizontal line, everything above it is plain flat off-white for background removal. Clear empty space in the center of the table surface for three tarot cards in a row. An empty spot on the right for a candle and an empty spot on the left for a money container: no candle, no money, no cards, no hands, no people. Holes or gaps in the cloth are filled with what is underneath, never see-through. Seinen manga illustration with black ink lineart of varying weight, bold widely spaced cross-hatching, two to three flat muted color tones, subtle warm paper texture. Muted 1980s palette, no neon, no text.
```
