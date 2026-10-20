# ARCANUM VULGARIS
## Game Design Document (GDD) — Manual Operativo y Mecánico
**Versión:** 1.8 (Ediciones de mazo; Tiempo por acción, métricas del cliente, Fama/Reputación, voces en gibberish; Integra Mapa B "New Carthage"; Mapas por época, Nivel de Mazo; Tarot real como núcleo, tiradas variables, prestidigitación, Deudas de Sangre y meta-progresión)
**Versión anterior:** 1.3 (ver historial de git)
**Tesis de Diseño:** *No somos magos con poderes místicos; somos psicólogos callejeros, timadores perceptivos y manipuladores de la desesperación ajena. Las cartas son el vehículo para monetizar verdades deducidas, vender mentiras convenientes y moldear el destino de la ciudad.*

> **Estado del documento:** documento maestro en construcción. Las secciones marcadas con **[PENDIENTE]** todavía no tienen decisión tomada; ver §13. Las decisiones tomadas y su razón están en `design/decision-log.md`.

---

## 1. Regla Cero y Pilares Fundamentales
* **Regla Cero:** Ningún sistema del juego debe asumir la existencia de fuerzas sobrenaturales. Todo fenómeno en pantalla debe ser atribuible a la psicología del testimonio, el sesgo cognitivo, la puesta en escena teatral y la agudeza perceptiva del estafador. Las cartas no predicen nada: funcionan porque **el cliente cree** en su significado.
* **Pilar 1 — La Verdad no es Mágica, es Observable:** El jugador extrae información mediante micro-detalles visuales y lenguaje corporal provocado por preguntas capciosas.
* **Pilar 2 — El Dilema de la Sentencia:** Descubrir la verdad es solo el comienzo; decidir si decirla, edulcorarla, mentir para cobrar una fortuna o extorsionar al cliente define la supervivencia.
* **Pilar 3 — Memoria Pura sobre el Cliente:** Un auténtico tarotista jamás toma notas frente al consultante. Todo lo que el jugador observa y deduce **sobre el cliente** vive en su memoria. *El significado de las cartas, en cambio, es público y consultable en todo momento* (ver §3.3): lo que se aprende es cómo combinarlas y aplicarlas.
* **Pilar 4 — Gestión de Riesgo Probabilístico (Doble Fondo):** Nada es 100% seguro. Jugar a la fachada visible rinde ganancias bajas y seguras; apostar al secreto oculto multiplica el capital o precipita la ruina.
* **Pilar 5 — Tiranía del Tiempo y Gestión de Fila:** Atender a fondo a un pez gordo deja a la cola furiosa afuera; apurar a los clientes maximiza el volumen pero reduce la efectividad al mínimo.
* **Pilar 6 — No hay Carta Mala, hay Lector Malo:** Las cartas salen al azar. El mérito del jugador es hacer que cualquier tirada juegue a su favor mediante interpretación, combinación y trucos de mano. El azar siempre deja al menos una palanca de acción.

---

## 2. Estructura de Partida y Género
* **Género:** Roguelite de deducción psicológica y gestión de riesgo.
* **Duración de partida:** larga — horas o días de juego, con guardado del progreso.
* **Derrota:** permanente, pero **nunca sorpresiva**. Las amenazas graves se anuncian y escalan como Deudas de Sangre (§8), con salidas disponibles. El jugador ve venir su ruina.
* **Única muerte instantánea:** la Tirada Suicida (§8.4), que el jugador elige conscientemente.
* **Época:** fines del siglo XX, **1985–1995** (antes de celulares e internet masivos).
* **Mapas:** el juego tiene varios mapas (escenarios), cada uno con sus 8 sedes, su población y sus reglas propias. Se elige al empezar la partida. Orden de producción:
  1. **Mapa B — Metrópolis estadounidense ficticia, años 80** (MVP): época yuppie, Wall Street, telepredicadores, líneas de videntes en TV; la victoria encaja con el crac bursátil de 1987.
  2. **Mapa A — Ciudad latinoamericana ficticia, 1985–1995** (expansión): transición democrática, hiperinflación como mecánica propia, sindicatos, intentos de golpe.
  3. **Mapa C — Ciudad portuaria de Europa del Este, 1989–1993** (expansión): caída del Muro, mafias, privatizaciones, videntes en TV estatal.
* **Desbloqueo:** llegar a la Sede 8 de un mapa (sin necesidad de ganar) desbloquea el siguiente. El Mapa B está disponible desde el inicio.
* **Adaptaciones por mapa:** `design/mapas/`.
* **Los mapas comparten** el sistema de tarot, las tiradas, la Resonancia, la prestidigitación y las Deudas de Sangre. **Cambian:** sedes, arte, variantes de arquetipos, eventos, escenas de derrota y una regla propia por mapa.
* **Al perder se conserva:** solo el conocimiento del jugador, los mazos desbloqueados, los Grados de Infamia alcanzados y el historial de Lecturas Diarias (§10).

---

## 3. El Sistema de Tarot (Núcleo del Juego)

### 3.1. Escuelas Adoptadas
| Rol | Escuela | Gramática de combinación |
| :--- | :--- | :--- |
| **Mazo base** | Smith 1909: 78 cartas, con invertidas (tradición Rider-Waite-Smith; arte original de Pamela Colman Smith, de dominio público) | **Dignidades elementales** de la Golden Dawn + reglas de combinación sistémicas (§3.5). |
| **Mazo alternativo (desbloqueable)** | Tarot de Marsella | **Lectura en línea:** las cartas se leen como frase; la dirección de la mirada de las figuras y la adyacencia modifican el sentido. |
| **Mazo secreto (desbloqueable)** | Inspirado en Lenormand (36 cartas) | **Pares fijos:** cada par adyacente forma una frase. |

**Restricciones legales:** no usar las marcas "Rider-Waite" ni "Rider" (marcas de U.S. Games Systems). Usar solo el arte de 1909, no la edición recoloreada de 1971. Descartado el Tarot Thoth por riesgo de derechos de autor sobre el arte. Validar con asesoría legal antes de producir arte.

### 3.2. Anatomía de una Carta
Cada carta tiene datos **públicos** en el juego:
* Nombre, número, palo (o Arcano Mayor).
* **Elemento** (Fuego, Agua, Aire, Tierra; los Mayores según su atribución astrológica de la Golden Dawn).
* **Palabras clave derechas** (2–3) y **palabras clave invertidas** (2–3).
* **Temas** asociados (etiquetas mecánicas como *traición, deuda, muerte, amor, poder, culpa, secreto, fortuna, enfermedad, ley*), derivados de sus palabras clave.

### 3.3. Conocimiento Público vs. Conocimiento Aprendido
* **Público (tooltip siempre disponible):** significado individual de cada carta, derecha e invertida, su elemento y sus temas.
* **Aprendido (nunca explicado por el juego):** cómo se combinan las cartas entre sí, qué combinaciones resuenan con cada tipo de situación, y cómo leer el contexto del cliente. Este es el conocimiento que el jugador acumula entre partidas.

### 3.4. Nivel de Mazo (Selector de Complejidad)
Al empezar la partida, el jugador elige cuántas cartas usa. Sirve como curva de aprendizaje para el novato y como selector de dificultad para el experto, que no queda obligado a empezar con pocas cartas.

| Nivel | Cartas al inicio | Crecimiento durante la partida | Multiplicador de recompensa |
| :--- | :--- | :--- | :---: |
| **Aprendiz** | 36: los 22 Arcanos Mayores + 1 palo | Se suma un palo al llegar a las Sedes 3, 5 y 7 | ×1.0 |
| **Oficial** | 50: los 22 Arcanos Mayores + 2 palos | Se suman los palos restantes en las Sedes 3 y 5 | ×1.25 |
| **Maestro** | 78: el mazo completo | — | ×1.5 |

* Todos los niveles están disponibles desde la primera partida.
* El multiplicador de recompensa (valores a calibrar) existe para que elegir más cartas convenga, no solo sea más difícil.
* El Nivel de Mazo es un eje **independiente** de los Grados de Infamia (§10.3): el Nivel de Mazo mide complejidad; el Grado mide dureza.
* La Lectura Diaria (§10.4) usa un Nivel de Mazo fijo para que el ranking sea justo.

### 3.5. Reglas de Combinación (Gramática del Mazo Base)
Todas son reglas reales de la práctica del tarot, aplicadas de forma sistémica:
1. **Posición:** cada casillero de la tirada pregunta algo distinto (ej.: Pasado = el origen; Presente = el conflicto; Futuro = la sentencia).
2. **Orientación:** derecha o invertida cambia la palabra clave disponible.
3. **Dignidades elementales:** cada carta es reforzada o debilitada por sus vecinas.
   * Mismo elemento: refuerzo fuerte.
   * Elementos amigos (Fuego + Aire, Agua + Tierra): refuerzo.
   * Elementos neutros (Fuego + Tierra, Agua + Aire): sin cambio.
   * Elementos hostiles (Fuego + Agua, Aire + Tierra): debilitamiento.
4. **Palo dominante:** si un palo domina la tirada, tiñe toda la lectura (Copas = emociones, Oros = dinero, Espadas = conflicto, Bastos = ambición).
5. **Peso de los Arcanos Mayores:** muchos Mayores = "fuerzas fuera de tu control"; da credibilidad ante temas graves.
6. **Números repetidos:** dos o más cartas del mismo número refuerzan su significado numérológico.

---

## 4. Bucle de Juego Principal (Core Gameplay Loop)

```
[INICIO DE DÍA] ──► [GESTIÓN DE COLA (Mirilla)] ──► [MESA DE LECTURA]
                          │                              │
                          ├── Rechazo ──► Abre/agrava    ├── 1. Inspección Visual (3 capas)
                          │              Deuda de Sangre ├── 2. Preguntas Capciosas (Tells)
                          └── Admisión                   ├── 3. Elección de Tirada (según motivo)
                                                         ├── 4. Robo al azar de cartas
                                                         ├── 5. Trucos de Prestidigitación (opcional)
                                                         ├── 6. Interpretación por posición
                                                         └── 7. Sentencia (Intención Retórica)
                                                                 │
[CIERRE NOCTURNO] ◄──────────────────────────────────────────────┘
  ├── Balance: Ingresos Brutos - Costos Fijos - Costos Variables
  ├── Avance de Deudas de Sangre activas
  ├── Evaluación de Ascenso (Dinero + Fama + Reputación)
  └── Trastienda: Artilugios, Trucos, Insumos, Mazos e Informantes
```

---

## 5. Mecánicas Detalladas de Sesión

### 5.1. El Tiempo como Recurso Vital (La Vela Diaria)
El tiempo de la jornada se mide en **Unidades de Tiempo (UT)**, visualizadas mediante una vela de sebo que se derrite en la mesa.
* $UT_{\text{Total}} = 100\ \text{UT}$ base (reducido por penalizaciones o Deudas de Sangre).
* La profundidad de la lectura ya no es una elección binaria (Express/Profunda): **la define la tirada elegida** (§5.4). Cada tirada tiene su costo en UT.
* **Paciencia de la Fila:**
  $$P_{\text{cliente}} = P_{\text{base}} - (t_{\text{espera}} \times \lambda_{\text{arquetipo}})$$
  Si $P_{\text{cliente}} \le 0$, el cliente se marcha furioso y abre o agrava una Deuda de Sangre según su arquetipo.
* **Tiempo por acción:** la vela no se consume sola; cada acción descuenta UT. Valores iniciales a calibrar:
  * Inspección pasiva (hover sobre el cliente): gratis.
  * Pregunta capciosa: 5 UT.
  * Truco de prestidigitación: 2 UT.
  * Tirada: según §5.4.
* **Lo único en tiempo real** son las ventanas de los tells (§5.2). Mientras el jugador interpreta las cartas, el reloj no corre: pensar la lectura nunca se castiga.

### 5.2. Sistema de Detección: Ojos, Provocación y "Tells"
* **Las Tres Capas de la Mirada:**
  1. *Lo Tangible:* Objetos, roturas, manchas de barro o pólvora, boletos de tren, joyas de latón.
  2. *Lo Conductual:* Tics faciales, deglución forzada, respiración entrecortada, manos trémulas.
  3. *La Deducción Cruzada (Palacio Mental):* Síntesis mental de 2 o más pistas que revela secretos mayores (ej.: infidelidad conyugal con socio comercial).
* **El Sonar de Preguntas Capciosas:**
  Lanzar una afirmación capciosa provoca al cliente. Si golpea su punto vulnerable, detona un *Tell Somático* animado durante una ventana crítica:
  $$T_{\text{Tell}} = 2.5\ \text{s} + \text{Bonificador}_{\text{Artilugios}} - \text{Resistencia}_{\text{Arquetipo}}$$
* **Hurtboxes Somáticas:** El sprite cuenta con 4 áreas interactivas: *Ojos/Mirada*, *Cuello/Garganta*, *Pecho/Respiración*, *Manos/Bolsillos*.
  * **Cliquear un tell no guarda nada:** el juego no registra qué pista viste. Es una acción sobre el cliente: nota que lo descubriste, su **Tensión** sube y se abre una **pregunta de seguimiento** sobre ese tema. Recordar qué significaba sigue siendo tarea del jugador (Pilar 3).
* **Fallo de Provocación:** Si se pregunta por un tema insensible, no hay tell y la Credulidad del cliente baja $15$ pts.

### 5.3. La Situación del Cliente (Generación Combinatoria)
Cada cliente se genera combinando:

$$\text{Situación} = \text{Arquetipo} \times \text{Secreto} \times \text{Motivo} \times \text{Urgencia}$$

* **Arquetipo:** uno de los 10 de §6 (define fachada, tarifa, resistencia y reacciones).
* **Secreto:** la fachada visible o un Doble Fondo, elegido de un pool por arquetipo (objetivo: ~15 secretos totales combinables, no uno fijo por arquetipo).
* **Motivo de consulta:** qué viene a preguntar (amor, dinero, decisión, culpa, salud, peligro, traición, poder…). **Define la tirada esperada** (§5.4).
* **Urgencia:** baja, media o alta (afecta paciencia, tarifa y gravedad de las consecuencias).

La Situación produce un conjunto de **temas ocultos por posición**, que la lectura del jugador debe acertar.

### 5.4. Las Tiradas
La cantidad de cartas depende del **motivo** del cliente, de su **estatus** (lo que puede pagar) y del **tiempo** disponible en la vela.

| Tirada | Cartas | Posiciones | Costo UT | Motivo que la pide | Disponibilidad |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Carta Única** | 1 | Respuesta | 10 | Pregunta urgente de sí/no | Desde el inicio |
| **Tres Tiempos** | 3 | Pasado · Presente · Futuro | 20 | Situación general | Desde el inicio |
| **Dos Caminos** | 5 | Situación · Camino A · Camino B · Resultado A · Resultado B | 30 | Decisión o dilema | Desbloqueable en la partida |
| **El Vínculo** | 5 | Consultante · El Otro · Lo que une · Lo que separa · Desenlace | 30 | Amor, sociedad, traición | Desbloqueable en la partida |
| **Cruz Celta** | 10 | Las 10 posiciones clásicas | 45 | Clientes VIP, asuntos graves | Sedes altas |

**Reglas:**
* El motivo del cliente sugiere una tirada. Usar la **tirada esperada** da un bono de Credulidad; usar otra la baja, salvo que el jugador la justifique con una buena lectura.
* **Más cartas = más información y más riesgo:** más combinaciones posibles a favor, pero también más cartas contradictorias que explicar, más tiempo gastado y más oportunidades de que el cliente note un truco.

### 5.5. Robo, Prestidigitación e Interpretación
1. **Robo:** el mazo se baraja y las cartas caen al azar en las posiciones, derechas o invertidas.
2. **Trucos de Prestidigitación (comodines):** el jugador puede alterar la tirada con trucos comprados en la trastienda (§9.2). Son limitados:
   * Máximo de **3 ranuras de truco** equipadas (ampliable a 5 con mejoras).
   * Cada truco tiene **cargas por jornada**.
   * Cada uso tiene un **riesgo de detección** que depende del arquetipo (alto en El Espejo y El Intelectual, bajo en El Indigente y El Obrero) y de los artilugios activos (la Lámpara Focal Verde lo reduce).
   * Ser descubierto: la Credulidad cae al mínimo, se pierde la tarifa y se abre una Deuda de Sangre de descrédito.
3. **Interpretación:** por cada posición, el jugador elige qué palabra clave de la carta enfatizar (de las públicas, según su orientación) y la conecta con lo que dedujo del cliente.

### 5.6. La Sentencia: Las 4 Intenciones Retóricas
Tras interpretar la tirada, el jugador elige una **Intención Retórica** para la lectura completa:
1. **Acusar:** Desenmascara crímenes, traiciones o fraudes.
   * *Éxito:* Pánico severo; cobro extorsivo ($\times 3$) o sumisión.
   * *Fallo:* Furia; abre una Deuda de Sangre de violencia o denuncia.
2. **Consolar:** Valida esperanzas o fantasías piadosas.
   * *Éxito:* Fe máxima; propinas extraordinarias ($+150\%$).
   * *Fallo:* Decepción; cobro exclusivo de tarifa base.
3. **Sembrar Paranoia:** Convence al cliente de amenazas y traiciones inminentes.
   * *Éxito:* Fidelización compulsiva; venta de amuletos de la trastienda.
   * *Fallo:* la Credulidad del cliente se desploma; abre una Deuda de Sangre de descrédito en la zona.
4. **Extorsionar:** Comercia el silencio del tarotista a cambio de favores.
   * *Éxito:* Inmunidad judicial, salvoconductos o favores políticos (pueden saldar Deudas de Sangre).
   * *Fallo:* Abre una Deuda de Sangre grave con el cliente (empieza en etapa 2).

### 5.7. Métricas del Cliente y del Tarotista

**Del cliente** (reemplazan a Fe, Escepticismo y Credibilidad de la v1.3):

| Métrica | Escala | Cuándo existe | Qué hace |
| :--- | :---: | :--- | :--- |
| **Paciencia** | 0 a 100 | Solo en la fila | Baja con la espera (§5.1). En 0 el cliente se va y abre o agrava una Deuda de Sangre. |
| **Credulidad** | -100 a +100 | En la mesa | De escepticismo total (-100) a fe ciega (+100). Sube con aciertos y puesta en escena; baja con preguntas fallidas, tiradas inadecuadas y trucos descubiertos. Modifica el umbral de la Resonancia y, si es positiva, la propina. |
| **Tensión** | 0 a 100 | En la mesa | Los nervios del cliente. Sube con preguntas que golpean y tells cliqueados. Más Tensión = tells más largos y visibles; en 100 el cliente estalla en furia y la sesión termina en fallo. |

**Del tarotista:**
* **Fama:** cuánta gente sabe que existís. Controla **cuántos** clientes hacen fila. Sube con cada cliente atendido, rumores, prensa y también con escándalos; baja lentamente con días sin atender.
* **Reputación:** porcentaje de lecturas exitosas sobre las últimas N lecturas. Controla **qué clase** de clientes llega: más Reputación atrae arquetipos más ricos y peligrosos.

### 5.8. Resolución: la Resonancia
El éxito de la lectura se calcula con la **Resonancia** ($R$): qué tan bien encaja lo que el jugador dijo con la verdad oculta del cliente.

$$R = \sum_{p \in \text{posiciones}} \left( \text{Match}_p \times D_p \right) + B_{\text{combinación}} + B_{\text{tirada}} - \text{Contradicciones}$$

Donde:
* $\text{Match}_p$: coincidencia entre el tema de la palabra clave elegida en la posición $p$ y el tema oculto de esa posición (0 = nada, 1 = parcial, 2 = exacto).
* $D_p$: modificador por dignidades elementales de la carta en $p$ (ej.: 1.5 refuerzo fuerte, 1.25 refuerzo, 1.0 neutro, 0.5 debilitada).
* $B_{\text{combinación}}$: bonos por palo dominante, peso de Mayores y números repetidos cuando coinciden con la situación.
* $B_{\text{tirada}}$: bono por usar la tirada esperada para el motivo.
* $\text{Contradicciones}$: penalización por cartas cuyo sentido choca con la narrativa elegida y que el jugador no reinterpretó.

**Resultado:**
* Si $R \ge U_{\text{arquetipo}}$ (umbral del arquetipo, modificado por la Credulidad) **y** la intención es coherente con el estado real del cliente → **Éxito**.
* Si $R$ alcanza el umbral pero la intención no es coherente (ej.: Acusar a un inocente) → **Fallo de intención**.
* Si $R < U_{\text{arquetipo}}$ → **Fallo de lectura**.

Todos los valores numéricos de esta sección son **perillas de ajuste** a calibrar en prototipo.

---

## 6. Matriz Paramétrica de Arquetipos y Doble Fondo
Probabilidad base de subversión: $P_{\text{DF}} = 30\%$ (modificada por eventos del día).

> **Arquetipos de sistema:** la tabla usa nombres genéricos. Cada mapa les da su propia piel (nombre, fachada, secretos); la población de cada sede son variantes de estos 10 arquetipos más 2 arquetipos exclusivos por mapa. Pieles del Mapa B: `design/mapas/mapa-b-new-carthage.md` §4.
>
> **Nota v1.4:** el Doble Fondo de cada arquetipo ya no es único. La columna "Doble Fondo" muestra el ejemplo original; cada arquetipo tendrá un pool de secretos posibles (§5.3). La columna "Reacción al Rechazo" pasa a ser la **primera etapa de la Deuda de Sangre** que abre ese arquetipo (§8).

| # | Arquetipo | Fachada Visible | Doble Fondo (ejemplo) | Punto Ciego Vulnerable | Deuda de Sangre que abre (etapa 1) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **El Indigente** | Pordiosero andrajoso, limosnas de cobre. | **Avaro Clandestino:** Ahorros en oro cosidos a los forros; busca saber si su escondite es seguro. | Salud y pérdida de su refugio | Barro y piedras contra la fachada (-Reputación). |
| **2** | **El Aristócrata** | Modales de seda, joyas, desprecio de clase. | **Heredero en Ruinas:** Joyas de latón y deudas colosales; busca golpes de suerte desesperados. | Deshonor público y ego | Acude al gabinete de un tarotista rival. |
| **3** | **El Sicario** | Rostro cortado, postura violenta y gélida. | **Devoto Culpable:** Busca una señal divina para no matar a un inocente. | Muerte violenta / Juicio divino | Patea la puerta; emboscada para cobrar peaje. |
| **4** | **La Viuda** | Luto riguroso, llanto contenido. | **Envenenadora Serial:** Viene a confirmar si los médicos forenses sospechan de la autopsia. | Descubrimiento legal / Condena | Difunde rumores de brujería y malas artes. |
| **5** | **El Policía** | Placa de bronce, libreta, tono autoritario. | **Cómplice Extorsionado:** Acorralado por una banda criminal rival; busca una salida desesperada. | Prisión y deshonor militar | Acta de inspección punitiva al día siguiente (-UT). |
| **6** | **El Jugador** | Ojos inyectados en sangre, humo, manos trémulas. | **Informante del Inframundo:** Paga con dossiers de inteligencia sobre futuros clientes de élite. | Ruina total inminente | Intento de hurto menor en la caja al salir. |
| **7** | **El Intelectual** | Escéptico, pedante, busca humillar al farsante. | **Ocultista Reprimido:** Aterrado por pesadillas lúcidas y visiones que su razón no explica. | Locura irracional / Miedo al ridículo | Columna satírica demoledora en la gaceta local. |
| **8** | **El Político** | Sonrisa ensayada, oratoria ambigua. | **Conspirador Acorralado:** Prepara o teme una traición o conspiración (en el Mapa B: una investigación federal); paga fortunas por saber de espías. | Traición de aliados cercanos | Inspección administrativa (escala a clausura). |
| **9** | **El Obrero** | Ropa tiznada, manos encallecidas, sumiso. | **Saboteador Sindical:** Prepara un paro fabril y caza al delator infiltrado en su cuadrilla. | Despido y hambre familiar | Boicot gremial que vacía de clientes la cuadra. |
| **10** | **El Espejo** | Modales neutros, expresión completamente plana. | **Tarotista Rival / Infiltrado:** Viene a evaluar el truco, copiar métodos o tender una trampa. | Ser desenmascarado en público | Sabotaje nocturno a tus mazos o herramientas. |

---

## 7. Sistema Detallado de Economía y Balance
> **[PENDIENTE] Rebalanceo completo (§13):** la v1.3 tiene inconsistencias conocidas que se conservan aquí hasta decidir: (a) un solo Doble Fondo del Indigente (120–250) paga entre 15 y 25 días de la Sede 1 o las mudanzas a las Sedes 2 y 3; (b) la tarifa base por arquetipo (§7.3) contradice la tarifa media por sede (§7.6); (c) calibrar Fama y Reputación (§5.7) contra la tabla de sedes.

### 7.1. La Moneda del Juego y Escala de Riqueza
La economía se expresa en **Monedas** (unidad estándar abstracta que representa el poder adquisitivo de la época).
* $1\ \text{Moneda}$ en el Nivel 1 equivale al pan de un día.
* En el Nivel 8, una sola lectura de Estado puede mover miles de monedas.

### 7.2. Ecuación de Ingresos por Sesión
$$I_{\text{sesion}} = (T_{\text{base}} \times M_{\text{intencion}} \times M_{\text{DF}}) + \text{Propina}$$

Donde:
* **$T_{\text{base}}$ (Tarifa Base):** Valor predeterminado por el estatus socioeconómico del cliente y el nivel de la sede en que se atiende.
* **$M_{\text{intencion}}$ (Multiplicador de Intención Retórica):**
  * *Consolar (Éxito):* $1.0\times$ a la tarifa base, pero habilita el multiplicador máximo de propina.
  * *Acusar (Éxito):* $3.0\times$ (pago extorsivo por miedo al escándalo).
  * *Sembrar Paranoia (Éxito):* $1.5\times$ base $+$ Venta Compulsiva de Amuleto ($+50\%$ de tarifa fija adicional).
  * *Extorsionar (Éxito):* $5.0\times$ a $10.0\times$ (pago directo por rescate de secretos) o entrega de un pagaré/inmunidad.
  * *Cualquier Intención en Fallo:* $0\times$ o tarifa de limosna ($0.2\times$).
* **$M_{\text{DF}}$ (Multiplicador de Doble Fondo):** si el jugador descubre y explota con éxito el Doble Fondo, $M_{\text{DF}} = 2.5\times$ a $4.0\times$.
* **Propina:**
  $$\text{Propina} = T_{\text{base}} \times \frac{\max(0,\ \text{Credulidad}_{\text{final}})}{100} \times K_{\text{arquetipo}} \times K_{\text{mazo}} \times K_{\text{trastienda}}$$

### 7.3. Tabla de Tarifas Base y Propinas por Arquetipo

| Arquetipo | Tarifa Base ($T_{\text{base}}$) | Multiplicador Propina ($K_{\text{arq}}$) | Recompensa Típica por Doble Fondo |
| :--- | :---: | :---: | :--- |
| **El Indigente** | 2 - 4 | $0.2\times$ | +120 a 250 monedas (Oro cosido en harapos). |
| **El Obrero** | 6 - 10 | $0.5\times$ | Salvoconducto sindical (Evita boicots). |
| **El Jugador** | 4 - 8 | $0.8\times$ | Dossier de inteligencia sobre cliente VIP del día siguiente. |
| **El Sicario** | 15 - 25 | $1.2\times$ | Contrato de protección (Anula asaltos por 3 días). |
| **La Viuda** | 20 - 35 | $1.8\times$ | +200 a 400 monedas por complicidad de encubrimiento. |
| **El Intelectual** | 25 - 45 | $1.0\times$ | Artículo elogioso (+15 Fama, +10% afluencia). |
| **El Policía** | 15 - 30 | $0.5\times$ | Inmunidad judicial por 5 días (Anula multas). |
| **El Aristócrata** | 80 - 150 | $3.5\times$ | Reliquia empeñable (Valor: +500 monedas). |
| **El Político** | 150 - 300 | $4.0\times$ | Subvención municipal o contrata exclusiva (+1.500 monedas). |
| **El Espejo** | 50 - 100 | $0.0\times$ | Desbloqueo de cartas prohibidas del rival. |

### 7.4. Estructura de Costos Diarios
> Los nombres de insumos e informantes son los del **Mapa B**; cada mapa los adapta a su época.

1. **Renta Fija de la Sede ($CF_{\text{renta}}$):** de 5 a 2.800 monedas según sede.
2. **Peaje de Protección o Soborno Policial ($CF_{\text{seguridad}}$):** en sedes bajas, la patota de la esquina; en sedes altas, el comisario o inspector. Si no se paga, abre una Deuda de Sangre.
3. **Consumibles de Sesión ($CV_{\text{insumos}}$):**
   * *Velas* (de supermercado en sedes bajas, aromáticas importadas en sedes altas): 1 por día obligatoria (2 a 50 monedas según la sede).
   * *Té de la Casa* ("relajante"): 3 monedas por cliente.
   * *Sahumerio de pachulí:* 5 monedas por jornada activada.
4. **Información de Redes Previas ($CI_{\text{espías}}$):** lustrabotas (2), taxista (15) o técnico de la telefónica (150) por dossiers previos. Revisar la basura del cliente es gratis pero cuesta UT del día siguiente.

#### Ecuación del Balance Diario
$$\text{Balance}_{\text{Final}} = \text{Saldo}_{\text{Anterior}} + \sum I_{\text{sesiones}} - (CF_{\text{renta}} + CF_{\text{seguridad}} + CV_{\text{insumos}} + CI_{\text{espías}})$$

Un balance negativo al cierre abre la Deuda de Sangre **"El Usurero"** (§8.3).

### 7.5. Parámetros Económicos y Umbrales de Ascenso por Sede

Valores económicos comunes a todos los mapas; nombres de sede del **Mapa B**. Población, amenazas y escenas de derrota de cada sede: `design/mapas/mapa-b-new-carthage.md` §3.

| Nivel / Sede (Mapa B) | Costo Mudanza | Fama Req. | Reputación Req. | Renta Diaria | Soborno / Peaje | Tarifa Media | Fila Base (Fama 0) | Fila Desbordada (Alta Fama) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. La Boca del Subte** | 0 | 0 | 0% | 5 | 2 | 4 - 8 | 2 - 3 | 7 - 9 |
| **2. La Lavandería 24 Horas** | 50 | 15 | 30% | 18 | 6 | 10 - 20 | 3 - 4 | 7 - 10 |
| **3. El Local de la Galería** | 150 | 35 | 45% | 45 | 15 | 25 - 50 | 4 - 5 | 8 - 11 |
| **4. El Stand del Paseo Marítimo** | 350 | 55 | 55% | 90 | 30 | 40 - 80 | 5 - 6 | 9 - 12 |
| **5. El Reservado del Club Velvet** | 800 | 70 | 65% | 200 | 70 | 80 - 160 | 6 - 7 | 10 - 13 |
| **6. El Estudio de Radio AM** | 1.800 | 85 | 75% | 450 | 150 | 180 - 350 | 6 - 8 | 10 - 14 |
| **7. La Oficina del Piso 30** | 4.500 | 92 | 85% | 1.000 | 350 | 400 - 900 | 7 - 9 | 11 - 15 |
| **8. El Penthouse y el Show de Medianoche** | 12.000 | 98 | 92% | 2.800 | 1.000 | 1.200 - 3.500 | 8 - 10 | 12 - 16 |

---

## 8. Deudas de Sangre (Consecuencias Escalables)
Reemplaza a las muertes instantáneas y castigos irreversibles de la v1.3. Toda ofensa grave —rechazar o desatender a un cliente peligroso, fallar una intención, ser descubierto haciendo trampa, no pagar un peaje o cerrar el día en negativo— abre un **hilo de consecuencia** visible.

### 8.1. Anatomía de un Hilo
* **Acreedor:** quién lo abrió (el Político, la banda del Sicario, el Usurero, el gremio obrero…).
* **Etapas:** 3 o 4, que escalan con el paso de los días o ante nuevas ofensas al mismo acreedor. Cada etapa tiene un efecto mecánico creciente.
* **Salidas (al menos dos por hilo):**
  * **Pagar:** dinero, artilugios o favores acumulados.
  * **Devolver el favor:** cumplir un encargo del acreedor (ej.: hacerle una lectura falsa a un rival suyo).
  * **Desviar:** cargarle el problema a otro cliente o facción. Cierra este hilo pero **abre otro**.

### 8.2. Límite y Game Over
* **Máximo 3 hilos activos.** Si se abre un cuarto, o si un hilo llega a su etapa final, se ejecuta el **Game Over** temático de la sede actual. Cada mapa define sus escenas; en el **Mapa B**:
  * *Sede 1 (La Boca del Subte):* Arrojado al río desde el muelle, envuelto en una alfombra.
  * *Sede 2 (La Lavandería):* Te quiebran los dedos de la mano diestra y te tiran a un contenedor.
  * *Sede 3 (El Local de la Galería):* Incendio "accidental" del local con vos adentro.
  * *Sede 4 (El Stand del Paseo Marítimo):* Redada por fraude postal y telefónico; cárcel estatal.
  * *Sede 5 (El Club Velvet):* Desaparecido en el baúl de un auto de lujo.
  * *Sede 6 (El Estudio de Radio AM):* Desenmascarado en vivo; demanda colectiva y ruina pública.
  * *Sede 7 (La Oficina del Piso 30):* Prisión federal por fraude de valores.
  * *Sede 8 (El Penthouse):* "Suicidio" desde el balcón del piso 50.
* El HUD muestra siempre los hilos activos y su etapa: **la ruina nunca es sorpresiva**.

### 8.3. Hilo Especial: "El Usurero" (Morosidad)
Se abre cuando el balance diario cierra en negativo. Conserva las etapas de morosidad de la v1.3:

```
[BALANCE NEGATIVO]
       │
       ├── ETAPA 1 ──► Interés punitorio (+25% diario) + Estrés (-10 UT al día siguiente)
       ├── ETAPA 2 ──► Matón en la puerta (-30% Paciencia de la cola; 25% de fuga de clientes de alta cuna)
       ├── ETAPA 3 ──► Embargo de 1 artilugio al azar (o rotura de la mesa: -20% credibilidad) + Ultimátum
       └── ETAPA 4 ──► [GAME OVER: QUIEBRA, DESALOJO Y VIOLENCIA]
```

**Salidas del Usurero:**
1. **Pagar** la deuda con intereses.
2. **Préstamo Clandestino:** pedir prestado el monto exacto a un prestamista del hampa. Cierra este hilo pero abre el hilo "Prestamista" con plazo de 48 horas y recargo del $+50\%$, que empieza en etapa 3.
3. **Empeño de Parafernalia:** vender artilugios al usurero por el $30\%$ de su costo.

### 8.4. La Tirada Suicida ("All-in")
Disponible con cualquier hilo en etapa 3. El jugador fuerza una acusación o extorsión temeraria contra un cliente peligroso o rico, saltándose pasos de deducción.
* **Acierto:** cancela ese hilo de golpe.
* **Fallo:** el cliente lo liquida en el acto. **Única muerte instantánea del juego**, y siempre elegida por el jugador.

---

## 9. Arsenal de Trastienda, Trucos y Mazos

### 9.1. Artilugios Físicos de Puesta en Escena
Artilugios del **Mapa B** (costos a calibrar en el rebalanceo):
* **Silla con Pata Trunca (-3mm):** Delata el momento exacto en que el cliente se inclina hacia adelante para mentir ($+30\%$ tiempo de detección de tell). Costo: 35 monedas.
* **Parlante Escondido** con cinta de ruidos: simula presencia "fantasmal" ante profecías fatales. Costo: 45 monedas.
* **Reloj Digital que Parpadea 12:00:** Desquicia a Escépticos y Senadores (pierden $20\%$ de paciencia base). Costo: 90 monedas.
* **Luz Negra y Reflector:** Encandila al cliente y deja al tarotista en penumbra; reduce el riesgo de detección de los trucos. Costo: 120 monedas.
* **El Audífono:** un cómplice en la sala de espera escucha las charlas de la fila y te las sopla: pistas extra en la mirilla. Riesgo de detección alto con el Escéptico.
* **Grabador de Casete** bajo la mesa: las sesiones grabadas mejoran el éxito de Extorsionar. Si te lo encuentran, abre una Deuda de Sangre.
* **Circuito Cerrado** en la sala de espera: ves el comportamiento de los clientes que esperan.

Los insumos de sesión (Té de la Casa, Sahumerio) están en §7.4.

### 9.2. Trucos de Prestidigitación (Comodines)
Se compran en la trastienda y se equipan en las ranuras de truco (máximo 3, ampliable a 5). Cada uno tiene cargas por jornada y riesgo de detección. Lista inicial propuesta (valores a calibrar):

| Truco | Efecto | Riesgo de detección |
| :--- | :--- | :--- |
| **Mirada al Fondo** | Ver la próxima carta del mazo antes de robarla. | Bajo |
| **Inversión de Muñeca** | Invertir una carta ya sobre el tapete. | Medio |
| **Cambio de Manga** | Reemplazar una carta del tapete por una al azar del mazo. | Medio |
| **Carta Forzada** | Elegir la carta exacta de una posición (una por jornada). | Alto |
| **Mazo Preparado** | Antes de barajar, fijar el palo dominante de la tirada. | Alto |

### 9.3. Mazos
Los mazos son el principal tipo de partida desbloqueable: cambian la gramática de combinación, no solo los números.

| Mazo | Gramática | Desbloqueo |
| :--- | :--- | :--- |
| **Smith 1909** | Dignidades elementales (§3.5). | Incluido de inicio. |
| **Tarot de Marsella** | Lectura en línea: miradas y adyacencia. | Desbloqueable. |
| **Petit Jeu de la Sibila** *(inspirado en Lenormand)* | Pares fijos adyacentes. | Secreto. |

**Ediciones de mazo:** los mazos de modificadores de la v1.3 pasan a ser **ediciones** que se compran dentro de una partida. Una edición conserva los significados y la gramática del mazo en uso, pero cambia cómo reaccionan los arquetipos. No forman parte del MVP.
* **Edición del Hereje (Hueso y Tinta):** $+150\%$ al terror y cobro en cartas de desgracia; causa burla inmediata en Intelectuales. Costo: 180 monedas.
* **Edición Veneciana (Filigrana de Oro):** Triplica las propinas de Aristócratas y Políticos; indigna a Obreros e Indigentes. Costo: 450 monedas.
* **Edición Alquímica Hermética:** Anula el $80\%$ de la Credulidad negativa de Intelectuales; confunde a clientes pobres reduciendo su Credulidad. Costo: 750 monedas.

---

## 10. Meta-progresión y Vida Útil

### 10.1. Qué se Conserva entre Partidas
* **Conocimiento del jugador:** combinaciones, lectura de contexto y de arquetipos. No se guarda en el juego; vive en la cabeza del jugador.
* **Mazos desbloqueados** (§9.3).
* **Grados de Infamia** alcanzados (§10.3).
* **Historial de Lecturas Diarias** (§10.4).

### 10.2. Profundidad Combinatoria
La situación de cada cliente se genera por combinación (§5.3) y las cartas salen al azar (§5.5). Ninguna lectura es igual a otra; el conocimiento se aplica, no se memoriza.

### 10.3. Grados de Infamia (Dificultad Ascendente)
Cada victoria desbloquea el siguiente Grado, que agrega una regla más dura a todas las partidas (ej.: menor Credulidad inicial, menos ranuras de truco, hilos que escalan más rápido, menos UT). "Ser el mejor tarotista" se mide por el **Grado más alto vencido**.

### 10.4. Lectura Diaria
Una partida corta con semilla compartida, igual para todos los jugadores ese día, con ranking global.

---

## 11. Game Feel y Juiciness (Respuestas Sensoriales)

### 11.1. Diálogos y Voces
* **Ningún personaje habla con voz real.** Todo el diálogo aparece en **cuadros de texto** acompañados de **balbuceo ininteligible** (*vocal gibberish*): sílabas sin sentido que imitan el ritmo del habla.
* El balbuceo es **expresivo**: cada arquetipo tiene su timbre, y la **Tensión** del cliente modifica tono, velocidad y pausas. Un cambio en el balbuceo puede ser una pista más.
* Ventajas: no hay grabación ni actuación de voz, la localización es solo de texto y todo el diálogo está siempre escrito (accesibilidad).

### 11.2. Respuestas Sensoriales
* **El Golpe del Arcano (*Card Slam*):** Audio contundente de madera pesada contra terciopelo con *screen shake* sutil (3px, 80ms).
* **Hitstop de Revelación Crítica:** Congelamiento visual de 150ms al ejecutar una deducción sinérgica de 3 pistas, con iluminación colapsando en haz cenital.
* **Tells Somáticos Vivos:** Dilatación física de pupilas en el sprite, sudor con brillo especular de un frame y crispación mandibular.
* **Atmósfera de Humo Volumétrico:** El humo del brasero o el querosene flota en capas 2D parallax y se disipa levemente al mover el cursor.
* **Feedback de Furia:** Al fallar contra un cliente peligroso, la mesa vibra, las cartas saltan y la llama de la vela titila violentamente.
* **Sonido de Monedas y Ruina:** Al cobrar, tintineo pesado de monedas cayendo en madera hueca; al abrirse una Deuda de Sangre, sonido seco de pestillo trancándose y respiración agitada en off.
* **Truco de Manos:** Al usar un truco, la cámara se acerca a las manos y el tiempo se ralentiza; si el cliente lo detecta, corte seco y silencio.

---

## 12. Diagramas de Flujo y UI/UX

### 12.1. Diagrama de Navegación Global
```
[MENÚ PRINCIPAL]
       │
       ├── [NUEVA PARTIDA] ── Elección de Mazo + Grado de Infamia
       ├── [CONTINUAR PARTIDA]
       └── [LECTURA DIARIA]
       │
       ▼
[PANEL DE GESTIÓN MATUTINA] ──► Comprar Artilugios / Trucos / Insumos / Espías / Mazos
       │                        Gestionar Deudas de Sangre (pagar, cumplir favores, desviar)
       ▼
[INICIO DE JORNADA (Encendido de Vela)]
       │
       ├────────────────────────────────────────┐
       ▼                                        ▼
[VISTA MIRILLA (Cola Exterior)]           [SALA DE ESPERA (Paciencia)]
       │
       ├──────────► [Rechazar] ──► Abre/agrava Deuda de Sangre del arquetipo
       │
       ▼ [Hacer Pasar]
[MESA DE LECTURA]
  ├── Inspección Pasiva (Hover en Ropa / Objetos / Cara)
  ├── Provocación Capciosa (Pregunta ──► Tell Somático)
  ├── Elección de Tirada
  ├── Robo al azar ──► Trucos de Prestidigitación (opcional)
  ├── Interpretación por posición
  └── Sentencia (Intención Retórica)
       │
       ▼
[RESOLUCIÓN (Resonancia)]
  ├── [Éxito]: Cobro de Honorarios + Propinas + Favores
  └── [Fallo]: Furia / Descrédito ──► Abre/agrava Deuda de Sangre
       │
       ▼
[¿QUEDA VELA EN LA JORNADA?] ──► SI: Vuelve a [VISTA MIRILLA]
       │
       ▼ NO
[CIERRE DE CAJA NOCTURNO]
  ├── Balance diario (negativo ──► Hilo "El Usurero")
  ├── Avance de etapas de Deudas de Sangre
  │     └── ¿4 hilos activos o un hilo en etapa final? ──► [GAME OVER]
  └── ¿Cumple Dinero + Fama + Reputación? ──► [OPCIÓN DE ASCENSO DE SEDE]
```

### 12.2. Mockup de HUD en Pantalla (Mesa de Lectura)
```
+-------------------------------------------------------------------------+
| [VELA: ||||||||||....]    [ORO: 420]    [FAMA: 45]    [REPUTACIÓN: 72%] |
| [DEUDAS: Usurero ●●○○ | Político ●○○○ | — ]   [TRUCOS: ■ ■ □]          |
+-------------------------------------------------------------------------+
|                       [ SPRITE DEL CLIENTE ]                            |
|             (Hurtboxes interactivas: Ojos, Cuello, Pecho, Manos)        |
|  [CREDULIDAD: -|----●-----|+]   [TENSIÓN: ||||||........]              |
+-------------------------------------------------------------------------+
| [PREGUNTAS CAPCIOSAS]       |   TAPETE — TIRADA: TRES TIEMPOS           |
| > ¿Familia y lealtades?     |  +----------+  +----------+  +----------+ |
| > ¿Deudas y oro oculto?     |  |  PASADO  |  | PRESENTE |  |  FUTURO  | |
| > ¿Crimen y sospechas?      |  | La Torre |  | 3 Espadas|  | El Sol ↓ | |
|                             |  +----------+  +----------+  +----------+ |
|                             |  (Tooltip: elemento + palabras clave)     |
|                             |  (Sentencia: Acusar / Consolar /          |
|                             |   Paranoia / Extorsionar)                 |
+-----------------------------+-------------------------------------------+
```

---

## 13. Preguntas Abiertas
Decisiones pendientes que bloquean o condicionan otras partes del diseño:
1. **Mapas A y C:** escribir su adaptación cuando se cierre el MVP.
2. **Economía:** números de las Sedes 1–3 para el MVP ahora; rebalanceo completo (tarifas por arquetipo vs. por sede, recompensas de Doble Fondo, Sedes 4–8) con datos del prototipo.
3. **Victoria del Mapa B:** diseñar en detalle la tirada final del Lunes Negro.

---

## 14. Condiciones de Victoria y Derrota
* **Derrota por Deudas de Sangre:** abrir un cuarto hilo activo o que un hilo llegue a su etapa final. Incluye la quiebra (hilo "El Usurero"), la prisión (hilos de policías y políticos) y la violencia (hilos de sicarios y bandas).
* **Derrota por Tirada Suicida:** fallar un "All-in" (§8.4).
* **Victoria (Mapa B — el Lunes Negro):** en la Sede 8, sobrevivir 7 jornadas de euforia bursátil que terminan en el crac. La última gran tirada es una Cruz Celta para el magnate más poderoso de la ciudad; su decisión define quién se hunde. Se gana sobreviviendo al Lunes Negro con la fortuna por encima de un umbral y sin hilos en etapa final. Detalle: `design/mapas/mapa-b-new-carthage.md` §7. **[PENDIENTE: diseño detallado de la tirada final]**
* **Victoria en otros mapas:** cada mapa define su propio clímax.
* **Victoria en Grado de Infamia:** desbloquea el siguiente Grado (§10.3).

---

## 15. Alcance del MVP
Versión mínima para validar que leer cartas es divertido, en el Mapa B:
* **Sedes:** 1 a 3.
* **Arquetipos:** 5.
* **Tiradas:** Carta Única y Tres Tiempos.
* **Nivel de Mazo:** Aprendiz.
* **Trucos:** 3.
* **Deudas de Sangre:** El Usurero + 1 hilo de arquetipo.
* **Fuera del MVP:** Cruz Celta y demás tiradas, mazos alternativos, Grados de Infamia, Lectura Diaria, Sedes 4–8, Mapas A y C.

Detalle del recorte: `design/mapas/mapa-b-new-carthage.md` §8.

