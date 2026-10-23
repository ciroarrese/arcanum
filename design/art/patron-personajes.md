# Patrón de diseño de personajes

Reglas que cumple todo cliente del juego para que el elenco se vea como un solo
juego. Estilo de referencia: `assets/art/personajes/vagabundo-variante-viejo.png`
(D-48). Generación con Recraft; cada personaje se genera **neutro primero** y las
facetas (tells) se hacen editando esa imagen, nunca desde cero.

## A. Dibujo (igual para todos)

1. Tinta negra de manga seinen, con grosor de línea variable: más grueso en el contorno, fino en los detalles.
2. Sombras con rayado de trazo grueso y espaciado, más 2 o 3 tonos de color plano.
3. Textura sutil de papel cálido en todo el dibujo.
4. La cara lleva poco rayado: nada de sombreado sobre los ojos, las mejillas ni la frente (son las zonas de los tells).
5. Ojos medianos y detallados, con iris visible y el blanco del ojo legible.

## B. Encuadre y composición

6. Formato vertical 3:4. La cabeza y los hombros ocupan la mitad superior.
7. **Línea de manos fija:** en la pose neutra, las dos manos van apoyadas, abiertas y planas, a la misma altura cerca del borde inferior. No se dibuja mesa ni línea de mesa: la mesa de cada sede es otra capa y tapa ese borde.
8. Fondo liso blanco roto (para recortar) o transparente.
9. Luz neutra y frontal. La luz de la sede y de la hora la aplica el motor.

## C. Personaje

10. Edad real del arquetipo o la variante, con rasgos de edad concretos.
11. Ojos siempre despejados: nada de velos, sombreros bajos ni anteojos oscuros. Los anteojos transparentes se permiten.
12. Nada fijo que se parezca a un tell (rubor, nariz roja, sudor, pupilas dilatadas), salvo que sea parte de la fachada del arquetipo (por ejemplo, la lágrima medida de la Viuda).
13. La suciedad y el desgaste son del personaje, no del estilo: un senador se ve limpio con el mismo dibujo.
14. La fachada no delata el secreto. La pista del Doble Fondo aparece solo en su faceta.
15. Época legible (1985–1995): al menos una prenda o accesorio del período. Paleta apagada de los 80: sin neón, sin colores fluorescentes ni de alta visibilidad (D-41).
16. La pose neutra es quieta. Los gestos (pañuelo a la cara, mano al cuello) son facetas.

## D. Facetas

Una imagen por zona de tell (GDD §5.2), editando solo esa zona de la neutra:
ojos/mirada, cuello/garganta, pecho/respiración, manos/bolsillos, más una de
tensión alta. Antes de aceptar una faceta, compararla con la neutra: si cambió
algo fuera de la zona, se rehace.

## Plantilla de prompt

El bloque de estilo no cambia nunca. Si se usa una imagen de contexto con el
estilo, alcanza con los bloques de personaje y pose.

```
[PERSONAJE]
Front-facing portrait of [WHO, AGE], New Carthage, USA, [YEAR 1985-1995], seated, looking straight at the viewer. Close framing: head and shoulders fill the upper half of the image.
[FACE AND AGE DETAILS]. [OUTFIT, at least one clearly 1980s item]. [CONDITION: worn and dirty / neat and clean / expensive].
Expression: [NEUTRAL FACADE], small pupils, relaxed shoulders, hands still.

[POSE — no cambiar]
No table, no table edge line, no furniture, no props in front of the character. Both forearms extended forward with both hands resting flat and open at the same horizontal line at the bottom edge of the image, as if on an invisible table surface; nothing drawn below it.

[ESTILO — no cambiar]
Style: seinen manga illustration with black ink lineart of varying weight, bold widely spaced cross-hatching for shadows on clothes and hair, light hatching on the face that never covers the eyes or cheeks, two to three flat muted color tones, subtle warm paper texture. Medium-sized detailed eyes with clearly visible whites and irises, eyes fully uncovered. Muted 1980s palette, no neon, no fluorescent or high-visibility colors. Neutral even front lighting. Plain flat off-white background. No permanent blush, no red nose, no sweat, no text.
```

## Cómo evaluar un personaje

1. **Consistencia:** neutra y facetas muestran a la misma persona.
2. **Legibilidad:** reducida a ~300 px de alto, cada tell se distingue de la neutra.
3. **Valores:** en gris y desenfocada, la cara y las manos son lo más claro.
4. **Elenco:** al lado de otro personaje aprobado, parecen del mismo juego.
5. **Rechazo:** no genera rechazo (criterio que descartó la caricatura de D-40).

## Resolución

Los originales salen de Recraft a 896 × 1200. Alcanzan para 1080p; para 4K se
escalan después de aprobados.
