# ARCANUM VULGARIS
## Game Design Document (GDD) — Manual Operativo y Mecánico
**Versión:** 1.3 (Revisada — Dinámica de Fama, Reputación y Demografía Contextual)  
**Tesis de Diseño:** *No somos magos con poderes místicos; somos psicólogos callejeros, timadores perceptivos y manipuladores de la desesperación ajena. Las cartas son el vehículo para monetizar verdades deducidas, vender mentiras convenientes y moldear el destino de la ciudad.*

---

## 1. Regla Cero y Pilares Fundamentales
* **Regla Cero:** Ningún sistema del juego debe asumir la existencia de fuerzas sobrenaturales. Todo fenómeno en pantalla debe ser atribuible a la psicología del testimonio, el sesgo cognitivo, la puesta en escena teatral y la agudeza perceptiva del estafador.
* **Pilar 1 — La Verdad no es Mágica, es Observable:** El jugador extrae información mediante micro-detalles visuales y lenguaje corporal provocado por preguntas capciosas.
* **Pilar 2 — El Dilema de la Sentencia:** Descubrir la verdad es solo el comienzo; decidir si decirla, edulcorarla, mentir para cobrar una fortuna o extorsionar al cliente define la supervivencia.
* **Pilar 3 — Memoria Pura (Cero Libretas):** Un auténtico tarotista jamás toma notas frente al consultante. Toda deducción vive en la retención mental del jugador.
* **Pilar 4 — Gestión de Riesgo Probabilístico (Doble Fondo):** Nada es 100% seguro. Jugar a la fachada visible rinde ganancias bajas y seguras; apostar al secreto oculto multiplica el capital o precipita la ruina.
* **Pilar 5 — Tiranía del Tiempo y Gestión de Fila:** Atender a fondo a un pez gordo deja a la cola furiosa afuera; apurar a los clientes maximiza el volumen pero reduce la efectividad al mínimo.

---

## 2. Bucle de Juego Principal (Core Gameplay Loop)

```
[INICIO DE DÍA] ──► [GESTIÓN DE COLA (Mirilla)] ──► [MESA DE LECTURA]
                          │                              │
                          ├── Rechazo ──► Sanción        ├── Inspección Visual (3 capas)
                          └── Admisión                   ├── Preguntas Capciosas (Tells)
                                                         └── Tapete (3 cartas + Intención)
                                                                 │
[CIERRE NOCTURNO] ◄──────────────────────────────────────────────┘
  ├── Balance: Ingresos Brutos - Costos Fijos - Costos Variables
  ├── Control de Saldo / Días de Gracia (Morosidad Punitiva)
  ├── Evaluación de Ascenso (Dinero + Fama + Reputación)
  └── Trastienda: Artilugios, Insumos, Mazos e Informantes
```

---

## 3. Mecánicas Detalladas de Sesión

### 3.1. El Tiempo como Recurso Vital (La Vela Diaria)
El tiempo de la jornada se mide en **Unidades de Tiempo (UT)**, visualizadas mediante una vela de sebo que se derrite en la mesa.
* $UT_{	ext{Total}} = 100	ext{ UT}$ base (reducido por penalizaciones policiales o eventos).
* **Lectura Rápida (Express):** Consume de $15	ext{ a }20	ext{ UT}$. Cobro de honorarios base rápidos; mínima deducción.
* **Lectura Quirúrgica (Profunda):** Consume de $35	ext{ a }50	ext{ UT}$. Permite conectar pistas complejas, desarmar dobles fondos y cobrar propinas astronómicas.
* **Paciencia de la Fila:**
  $$P_{	ext{cliente}} = P_{	ext{base}} - (t_{	ext{espera}} 	imes \lambda_{	ext{arquetipo}})$$
  Si $P_{	ext{cliente}} \le 0$, el cliente se marcha furioso y aplica su penalización de rechazo barrial de inmediato.

### 3.2. Sistema de Detección: Ojos, Provocación y "Tells"
* **Las Tres Capas de la Mirada:**
  1. *Lo Tangible:* Objetos, roturas, manchas de barro o pólvora, boletos de tren, joyas de latón.
  2. *Lo Conductual:* Tics faciales, deglución forzada, respiración entrecortada, manos trémulas.
  3. *La Deducción Cruzada (Palacio Mental):* Síntesis mental de 2 o más pistas que revela secretos mayores (ej: infidelidad conyugal con socio comercial).
* **El Sonar de Preguntas Capciosas:**
  Lanzar una afirmación capciosa provoca al cliente. Si golpea su punto vulnerable, detona un *Tell Somático* animado durante una ventana crítica:
  $$T_{	ext{Tell}} = 2.5	ext{ s} + 	ext{Bonificador}_{	ext{Artilugios}} - 	ext{Resistencia}_{	ext{Arquetipo}}$$
* **Hurtboxes Somáticas:** El sprite cuenta con 4 áreas interactivas: *Ojos/Mirada*, *Cuello/Garganta*, *Pecho/Respiración*, *Manos/Bolsillos*. Cliquear dentro de la ventana confirma el rasgo a la memoria del jugador.
* **Fallo de Provocación:** Si se pregunta por un tema insensible, no hay tell y el Escepticismo del cliente sube en $+15$ pts.

### 3.3. El Tapete Deductivo y las 4 Intenciones Retóricas
El tapete dispone de tres receptáculos fijos: **Pasado** (El Origen/Pecado), **Presente** (El Conflicto Activo) y **Futuro** (La Sentencia/Consejo).

Al colocar un Arcano, el jugador selecciona una **Intención Retórica**:
1. **Acusar:** Desenmascara crímenes, traiciones o fraudes.
   * *Éxito:* Pánico severo; cobro extorsivo ($	imes 3$) o sumisión.
   * *Fallo:* Furia inmediata; agresión física o denuncia policial.
2. **Consolar:** Valida esperanzas o fantasías piadosas.
   * *Éxito:* Fe máxima; propinas extraordinarias ($+150\%$).
   * *Fallo:* Decepción; cobro exclusivo de tarifa base.
3. **Sembrar Paranoia:** Convence al cliente de amenazas y traiciones inminentes.
   * *Éxito:* Fidelización compulsiva; venta de amuletos de la trastienda.
   * *Fallo:* Escepticismo masivo y descrédito en la zona.
4. **Extorsionar:** Comercia el silencio del tarotista a cambio de favores.
   * *Éxito:* Inmunidad judicial, salvoconductos o favores políticos.
   * *Fallo:* El cliente envía sicarios para destruir la sede esa misma noche.

---

## 4. Matriz Paramétrica de Arquetipos y Doble Fondo
Probabilidad base de subversión: $P_{	ext{DF}} = 30\%$ (modificada por eventos del día).

| # | Arquetipo | Fachada Visible | Doble Fondo (Trampa Oculta) | Punto Ciego Vulnerable | Reacción al Rechazo / Desatención |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **El Indigente** | Pordiosero andrajoso, limosnas de cobre. | **Avaro Clandestino:** Ahorros en oro cosidos a los forros; busca saber si su escondite es seguro. | Salud y pérdida de su refugio | Barro y piedras contra la fachada (-Reputación). |
| **2** | **El Aristócrata** | Modales de seda, joyas, desprecio de clase. | **Heredero en Ruinas:** Joyas de latón y deudas colosales; busca golpes de suerte desesperados. | Deshonor público y ego | Acude al gabinete de un tarotista rival. |
| **3** | **El Sicario** | Rostro cortado, postura violenta y gélida. | **Devoto Culpable:** Busca una señal divina para no matar a un inocente. | Muerte violenta / Juicio divino | Patea la puerta; emboscada para cobrar peaje. |
| **4** | **La Viuda** | Luto riguroso, llanto contenido. | **Envenenadora Serial:** Viene a confirmar si los médicos forenses sospechan de la autopsia. | Descubrimiento legal / Condena | Difunde rumores de brujería y malas artes. |
| **5** | **El Policía** | Placa de bronce, libreta, tono autoritario. | **Cómplice Extorsionado:** Acorralado por una banda criminal rival; busca una salida desesperada. | Prisión y deshonor militar | Acta de inspección punitiva al día siguiente (-UT). |
| **6** | **El Jugador** | Ojos inyectados en sangre, humo, manos trémulas. | **Informante del Inframundo:** Paga con dossiers de inteligencia sobre futuros clientes de élite. | Ruina total inminente | Intento de hurto menor en la caja al salir. |
| **7** | **El Intelectual** | Escéptico, pedante, busca humillar al farsante. | **Ocultista Reprimido:** Aterrado por pesadillas lúcidas y visiones que su razón no explica. | Locura irracional / Miedo al ridículo | Columna satírica demoledora en la gaceta local. |
| **8** | **El Político** | Sonrisa ensayada, oratoria ambigua. | **Conspirador Acorralado:** Prepara o teme un golpe de estado; paga fortunas por saber de espías. | Traición de aliados cercanos | Clausura administrativa inmediata por edicto. |
| **9** | **El Obrero** | Ropa tiznada, manos encallecidas, sumiso. | **Saboteador Sindical:** Prepara un paro fabril y caza al delator infiltrado en su cuadrilla. | Despido y hambre familiar | Boicot gremial que vacía de clientes la cuadra. |
| **10** | **El Espejo** | Modales neutros, expresión completamente plana. | **Tarotista Rival / Infiltrado:** Viene a evaluar el truco, copiar métodos o tender una trampa. | Ser desenmascarado en público | Sabotaje nocturno a tus mazos o herramientas. |

---

## 5. Sistema Detallado de Economía, Balance y Colapso

### 5.1. La Moneda del Juego y Escala de Riqueza
La economía se expresa en **Monedas** (unidad estándar abstracta que representa el poder adquisitivo de la época). 
* $1	ext{ Moneda}$ en el Nivel 1 equivale al pan de un día.
* En el Nivel 8, una sola lectura de Estado puede mover miles de monedas.

### 5.2. Ecuación de Ingresos por Sesión
Los ingresos netos generados en una consulta particular ($I_{	ext{sesion}}$) se calculan mediante:
$$I_{	ext{sesion}} = (T_{	ext{base}} 	imes M_{	ext{intencion}} 	imes M_{	ext{DF}}) + 	ext{Propina}$$

Donde:
* **$T_{	ext{base}}$ (Tarifa Base):** Valor predeterminado por el estatus socioeconómico del cliente y el nivel de la sede en que se atiende.
* **$M_{	ext{intencion}}$ (Multiplicador de Intención Retórica):**
  * *Consolar (Éxito):* $1.0	imes$ a la tarifa base, pero habilita el multiplicador máximo de propina.
  * *Acusar (Éxito):* $3.0	imes$ (pago extorsivo por miedo al escándalo).
  * *Sembrar Paranoia (Éxito):* $1.5	imes$ base $+ 	ext{Venta Compulsiva de Amuleto}$ ($+50\%$ de tarifa fija adicional).
  * *Extorsionar (Éxito):* $5.0	imes$ a $10.0	imes$ (pago directo por rescate de secretos) o entrega de un pagaré/inmunidad.
  * *Cualquier Intención en Fallo:* $0	imes$ o tarifa de limosna ($0.2	imes$), con riesgo de daño o denuncia.
* **$M_{	ext{DF}}$ (Multiplicador de Doble Fondo):**
  * Si el jugador descubre y explota con éxito el Doble Fondo oculto del cliente, $M_{	ext{DF}} = 2.5	imes$ a $4.0	imes$.
  * *Ejemplo crítico:* Revelarle al Indigente que sabés del oro cosido en sus harapos no solo te da su tarifa, sino que le cobra $150$ monedas de oro antiguo de golpe.
* **Cálculo de la Propina ($	ext{Propina}$):**
  $$	ext{Propina} = T_{	ext{base}} 	imes \left(rac{	ext{Fe Resultante}}{100}
ight) 	imes K_{	ext{arquetipo}} 	imes K_{	ext{mazo}} 	imes K_{	ext{trastienda}}$$
  * Aristócratas y Políticos tienen $K_{	ext{arquetipo}} = 2.5$ a $4.0$ (propinas desmedidas ante adulaciones exitosas).
  * Obreros e Indigentes tienen $K_{	ext{arquetipo}} = 0.2$ a $0.5$ (dejan apenas centavos sueltos).

### 5.3. Tabla de Tarifas Base y Propinas por Arquetipo

| Arquetipo | Tarifa Base ($T_{	ext{base}}$) | Multiplicador Propina ($K_{	ext{arq}}$) | Recompensa Típica por Doble Fondo |
| :--- | :---: | :---: | :--- |
| **El Indigente** | 2 - 4 | $0.2	imes$ | +120 a 250 monedas (Oro cosido en harapos). |
| **El Obrero** | 6 - 10 | $0.5	imes$ | Salvoconducto sindical (Evita boicots). |
| **El Jugador** | 4 - 8 | $0.8	imes$ | Dossier de inteligencia sobre cliente VIP del día siguiente. |
| **El Sicario** | 15 - 25 | $1.2	imes$ | Contrato de protección (Anula asaltos por 3 días). |
| **La Viuda** | 20 - 35 | $1.8	imes$ | +200 a 400 monedas por complicidad de encubrimiento. |
| **El Intelectual** | 25 - 45 | $1.0	imes$ | Artículo elogioso (+15 Fama, +10% afluencia). |
| **El Policía** | 15 - 30 | $0.5	imes$ | Inmunidad judicial por 5 días (Anula multas). |
| **El Aristócrata** | 80 - 150 | $3.5	imes$ | Reliquia empeñable (Valor: +500 monedas). |
| **El Político** | 150 - 300 | $4.0	imes$ | Subvención municipal o contrata exclusiva (+1.500 monedas). |
| **El Espejo** | 50 - 100 | $0.0	imes$ | Desbloqueo de cartas prohibidas del rival. |

### 5.4. Estructura de Costos Diarios (La Asfixia Fija y Variable)
El dinero ganado durante el día es asediado cada noche en el Cierre de Caja por cuatro conceptos inexorables:

1. **Renta Fija de la Sede ($CF_{	ext{renta}}$):** El alquiler que cobra el dueño del local (escala desde 5 hasta 2.800 monedas).
2. **Peaje de Protección o Soborno Policial ($CF_{	ext{seguridad}}$):** 
   * En sedes bajas, la patota de la esquina exige un peaje para no quemarte la carpa.
   * En sedes altas, el comisario o inspector exige un sobre para no clausurar por fraude o salubridad.
   * Si no se paga: Riesgo inminente de redada o asalto nocturno.
3. **Consumibles de Sesión ($CV_{	ext{insumos}}$):**
   * *Velas de Sebo / Aceite de Ballena:* 1 unidad gastada por día obligatoria (Costo: 2 a 50 monedas según calidad de la sede).
   * *Dosis de Té con Solanáceas:* 3 monedas por cada cliente al que se le sirvió té para aflojarle la lengua.
   * *Carbón y Beleño para el Brasero:* 5 monedas por jornada activada.
4. **Información de Redes Previas ($CI_{	ext{espías}}$):**
   * Pago al pilluelo (2 monedas), cochero (15 monedas) o telegrafista (150 monedas) por dossiers previos.

#### Ecuación del Balance Diario
$$	ext{Balance}_{	ext{Final}} = 	ext{Saldo}_{	ext{Anterior}} + \sum I_{	ext{sesiones}} - (CF_{	ext{renta}} + CF_{	ext{seguridad}} + CV_{	ext{insumos}} + CI_{	ext{espías}})$$

---

### 5.5. Sistema de Colapso: Días de Gracia, Deuda y Morosidad Punitiva
Tener un balance menor a 0 al final del día no es Game Over instantáneo, pero inicia una espiral de agonía financiera estructurada en **3 Días de Gracia ($D_{	ext{Gracia}} = 3$)**:

```
[BALANCE NEGATIVO / SALDO 0]
             │
             ├── DÍA 1 EN MORA ──► Interés punitorio (+25%) + Estrés (-10 UT al día sig.)
             │
             ├── DÍA 2 EN MORA ──► Matón en la puerta (-30% Paciencia cola, -25% Afluencia)
             │
             ├── DÍA 3 EN MORA ──► Embargo de 1 Artilugio al azar + Ultimátum sangriento
             │
             └── DÍA 4 EN MORA ──► [GAME OVER: QUIEBRA, DESALOJO Y VIOLENCIA]
```

* **Día 1 de Morosidad (La Intimación del Usurero):**
  * Se aplica una tasa de interés punitorio del $+25\%$ diario sobre el monto adeudado.
  * Estrés nocturno del tarotista: La vela del día siguiente comienza con $10	ext{ UT}$ menos ($90	ext{ UT}$ de tiempo útil).
* **Día 2 de Morosidad (El Matón en la Puerta):**
  * Un cobrador de aspecto siniestro se instala en la entrada de la sede con un garrote.
  * *Efecto mecánico:* La presencia del matón reduce la paciencia de todos los clientes en la cola exterior en un $-30\%$. Los clientes de alta cuna (Aristócratas, Intelectuales) tienen un $25\%$ de probabilidad de huir aterrados sin siquiera consultar la mirilla.
* **Día 3 de Morosidad (Embargo Forzoso y Ultimátum):**
  * Al amanecer, los acreedores entran y confiscan un artilugio de trastienda al azar (la silla desbalanceada, la lámpara verde o un mazo secundario). Si no hay artilugios, rompen la mesa (-20% credibilidad).
  * El usurero deja un mensaje seco: *"Si al caer la noche no está el total de la deuda con intereses, no vas a necesitar otra vela"*.
* **Día 4 sin Pagar (Fin de Gracia): GAME OVER DEFINITIVO.**
  * La escena de muerte / derrota se adapta temáticamente a la sede actual:
    * *Sede 1 (Callejón):* Arrojado al río atado dentro de una alfombra raída.
    * *Sede 2-3 (Taberna/Boticario):* Te quiebran los dedos de la mano diestra y te arrojan al muladar municipal.
    * *Sede 4-5 (Feria/Barrio Rojo):* Linchamiento público o redada de la brigada de defraudaciones.
    * *Sede 6-7 (Distrito Artístico/Financiero):* Cárcel de deudores por decreto judicial irrevocable.
    * *Sede 8 (Penthouse):* "Suicidio" asistido: arrojado desde el balcón del piso 50.

### 5.6. Vías de Escape Desesperadas (Mecánicas de Rescate)
Si el jugador se encuentra en morosidad, dispone de tres decisiones extremas de rescate:
1. **El Préstamo Usurero Clandestino:**
   * Permite pedir prestado el monto exacto de la renta a un prestamista del hampa.
   * *Trampa:* Se debe devolver en exactamente 48 horas con un recargo del $+50\%$. Si no se paga, no hay días de gracia: se ejecuta el Game Over directo.
2. **Empeño de Parafernalia:**
   * Permite vender de urgencia los artilugios de trastienda al usurero local por el $30\%$ de su costo de compra para liquidar la deuda del día.
3. **La Tirada Suicida ("All-in"):**
   * Durante el Día 3 de morosidad, el jugador puede forzar una acusación o extorsión temeraria contra un cliente peligroso o rico, saltándose pasos de deducción. Si acierta, cancela toda su deuda de golpe; si falla, el cliente lo liquida en el acto sin esperar al Cierre de Caja.

---

### 5.7. Parámetros Económicos y Umbrales de Ascenso por Sede

| Nivel / Sede | Costo Mudanza | Fama Req. | Reputación Req. | Renta Diaria | Soborno / Peaje | Tarifa Media | Fila Base (Fama 0) | Fila Desbordada (Alta Fama) | Población Contextual Dominante |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Callejón del Ahorcado** | 0 | 0 | 0% | 5 | 2 | 4 - 8 | 2 - 3 | 7 - 9 | Mendigos, rateros, borrachos, peones portuarios. |
| **2. Sótano de Taberna** | 50 | 15 | 30% | 18 | 6 | 10 - 20 | 3 - 4 | 7 - 10 | Contrabandistas, marineros prófugos, tahúres de dados. |
| **3. Trastienda del Boticario** | 150 | 35 | 45% | 45 | 15 | 25 - 50 | 4 - 5 | 8 - 11 | Boticarios celosos, viudas envenenadoras, policías barriales. |
| **4. Carpa de Feria** | 350 | 55 | 55% | 90 | 30 | 40 - 80 | 5 - 6 | 9 - 12 | Comerciantes, feriantes, burgueses curiosos de incógnito. |
| **5. Salón del Barrio Rojo** | 800 | 70 | 65% | 200 | 70 | 80 - 160 | 6 - 7 | 10 - 13 | Madamas, usureros, sicarios profesionales, detectives corruptos. |
| **6. Estudio Distrito Artístico** | 1.800 | 85 | 75% | 450 | 150 | 180 - 350 | 6 - 8 | 10 - 14 | Intelectuales bohemios, artistas quebrados, herederos rebeldes. |
| **7. Gabinete Financiero** | 4.500 | 92 | 85% | 1.000 | 350 | 400 - 900 | 7 - 9 | 11 - 15 | Corredores de bolsa, jueces comisionados, directores de banco. |
| **8. Penthouse Internacional** | 12.000 | 98 | 92% | 2.800 | 1.000 | 1.200 - 3.500 | 8 - 10 | 12 - 16 | Ministros de guerra, diplomáticos extranjeros, magnates globales. |

---

## 6. Progresión Espacial: Las 8 Sedes del Inframundo

1. **Nivel 1 — El Callejón del Ahorcado:** Cajón de manzanas bajo toldo roto. Clientes marginales, borrachos y rateros. Amenaza: Frío entumecedor y rateros.
2. **Nivel 2 — El Sótano de la Taberna Portuaria:** Olor a cerveza y pescado. Clientes: Sicarios, Marineros, Contrabandistas. Amenaza: Cobro usurero del patrón de taberna.
3. **Nivel 3 — La Trastienda del Boticario:** Frascos de opio y hierbas secas. Clientes: Viudas, Médicos, Policías. Amenaza: Sospechas de tráfico de venenos.
4. **Nivel 4 — La Carpa de la Feria Itinerante:** Luces de gas y fanfarria. Clientes: Intelectuales curiosos, Aristócratas de incógnito. Amenaza: Inspectores de feria.
5. **Nivel 5 — El Salón Oculto del Barrio Rojo:** Terciopelo raído y opio. Clientes: Madamas, Prestamistas, Policías corruptos. Amenaza: Redadas y vendettas.
6. **Nivel 6 — El Estudio Bohemio del Distrito Artístico:** Libros antiguos y café turco. Clientes: Intelectuales, Artistas, El Espejo. Amenaza: Artículos venenosos en la prensa.
7. **Nivel 7 — El Gabinete Privado del Distrito Financiero:** Caoba, caja fuerte empotrada y coñac. Clientes: Banqueros, Especuladores, Jueces. Amenaza: Demandas judiciales y espionaje corporativo.
8. **Nivel 8 — El Penthouse Internacional:** Mármol, vista panorámica y custodia armada. Clientes: Ministros, Diplomáticos, Magnates. Amenaza: Atentados con explosivos y golpes de estado.

---

## 7. Arsenal de Trastienda, Mazos e Insumos

### 7.1. Artilugios Físicos de Puesta en Escena
* **Silla con Pata Trunca (-3mm):** Delata el momento exacto en que el cliente se inclina hacia adelante para mentir ($+30\%$ tiempo de detección de tell). Costo: 35 monedas.
* **Té de Cortesía con Solanáceas:** Dilata pupilas al máximo y reseca la garganta, facilitando la lectura de tics ($+1.3	ext{ s}$ a la ventana activa). Costo por dosis: 3 monedas.
* **Brasero de Beleño Aromático:** Ralentiza el crecimiento del Escepticismo en un $25\%$. Costo de instalación: 60 monedas; Costo de recarga: 5 monedas/día.
* **Reloj de Péndulo Desincronizado:** Desquicia a Intelectuales y Políticos (pierden $20\%$ de paciencia base). Costo: 90 monedas.
* **Pedal Crujidor Bajo Tarima:** Accionado con el talón; emite chasquidos lejanos para simular presencia fantasmal ante profecías fatales. Costo: 45 monedas.
* **Lámpara Focal Verde:** Ciega al cliente y deja al tarotista en penumbra total, ocultando dudas al manipular el mazo. Costo: 120 monedas.

### 7.2. Mazos Especializados
* **Tarot de Marsella Clásico:** Neutro, confiable, sin bonificaciones ni penalizaciones. Costo: Incluido de inicio.
* **Mazo del Hereje (Hueso y Tinta):** $+150\%$ al terror y cobro en cartas de desgracia; causa burla inmediata en Intelectuales. Costo: 180 monedas.
* **Mazo Veneciano (Filigrana de Oro):** Triplica las propinas de Aristócratas y Políticos; indigna a Obreros e Indigentes. Costo: 450 monedas.
* **Mazo Alquímico Hermético:** Anula el $80\%$ del escepticismo de Intelectuales; confunde a clientes pobres reduciendo su fe. Costo: 750 monedas.

---

## 8. Game Feel y Juiciness (Respuestas Sensoriales)
* **El Golpe del Arcano (*Card Slam*):** Audio contundente de madera pesada contra terciopelo con *screen shake* sutil (3px, 80ms).
* **Hitstop de Revelación Crítica:** Congelamiento visual de 150ms al ejecutar una deducción sinérgica de 3 pistas, con iluminación colapsando en haz cenital.
* **Tells Somáticos Vivos:** Dilatación física de pupilas en el sprite, sudor con brillo especular de un frame y crispación mandibular.
* **Atmósfera de Humo Volumétrico:** El humo del brasero o el querosene flota en capas 2D parallax y se disipa levemente al mover el cursor.
* **Feedback de Furia:** Al fallar contra un cliente peligroso, la mesa vibra, las cartas saltan y la llama de la vela titila violentamente.
* **Sonido de Monedas y Ruina:** Al cobrar, tintineo pesado de monedas metálicas cayendo en madera hueca; al entrar en morosidad, sonido seco de pestillo trancándose y respiración agitada en off.

---

## 9. Diagramas de Flujo y UI/UX

### 9.1. Diagrama de Navegación Global
```
[MENÚ PRINCIPAL]
       │
       ▼
[PANEL DE GESTIÓN MATUTINA] ──► Comprar Artilugios / Insumos / Sobornar Espías / Mazos
       │
       ▼
[INICIO DE JORNADA (Encendido de Vela)]
       │
       ├────────────────────────────────────────┐
       ▼                                        ▼
[VISTA MIRILLA (Cola Exterior)]           [SALA DE ESPERA (Paciencia)]
       │                                        │
       ├──────────► [Rechazar] ──► Sanción Directa de Arquetipo
       │
       ▼ [Hacer Pasar]
[MESA DE LECTURA]
  ├── Inspección Pasiva (Hover en Ropa / Objetos / Cara)
  ├── Provocación Capciosa (Pregunta ──► Disparo de Tell Somático de 2.5s)
  └── Colocación de Cartas (Pasado / Presente / Futuro + Intención Retórica)
       │
       ▼
[RESOLUCIÓN DE LA SESIÓN]
  ├── [Éxito]: Cobro de Honorarios + Propinas + Favores Políticos
  └── [Fallo]: Furia / Violencia / Pérdida de Reputación
       │
       ▼
[¿QUEDA VELA EN LA JORNADA?] ──► SI: Vuelve a [VISTA MIRILLA]
       │
       ▼ NO
[CIERRE DE CAJA NOCTURNO]
  ├── Balance: Ingresos Brutos - Renta de Sede - Peajes - Insumos - Espías
  ├── [Saldo <= 0]: ──► Incrementa Contador de Días de Gracia (D_Gracia + 1)
  │                         └── ¿Días de Gracia > 3? ──► [GAME OVER: QUIEBRA Y MUERTE]
  ├── [Muerte / Arresto Directo]: ────────────────────► [GAME OVER: FIN TRÁGICO]
  └── [Supervivencia Exitosa]:
        └── ¿Cumple Dinero + Fama + Reputación? ──► [OPCIÓN DE ASCENSO DE SEDE]
```

### 9.2. Mockup de HUD en Pantalla (Mesa de Lectura)
```
+-------------------------------------------------------------------------+
| [VELA: ||||||||||....]    [ORO: 420]    [FAMA: 45]    [REPUTACIÓN: 72%] |
| [MORA: DÍA 0/3]                                                         |
+-------------------------------------------------------------------------+
|                                                                         |
|                       [ SPRITE DEL CLIENTE ]                            |
|             (Hurtboxes interactivas: Ojos, Cuello, Manos)               |
|                                                                         |
|      [Tensión / Sospecha]                                               |
|      [||||||||............]                                             |
|                                                                         |
+-------------------------------------------------------------------------+
| [PREGUNTAS CAPCIOSAS]       |            TAPETE DE TERCIOPELO           |
| > ¿Familia y lealtades?     |  +----------+  +----------+  +----------+ |
| > ¿Deudas y oro oculto?     |  |  PASADO  |  | PRESENTE |  |  FUTURO  | |
| > ¿Crimen y sospechas?      |  | [Arcano] |  | [Arcano] |  | [Arcano] | |
|                             |  +----------+  +----------+  +----------+ |
|                             |   (Rueda de Intención: Acusar/Consolar)   |
+-----------------------------+-------------------------------------------+
| [MANO DE ARCANOS DISPONIBLES:  [El Loco]  [La Torre]  [El Diablo] ]     |
+-------------------------------------------------------------------------+
```

---

## 10. Condiciones de Victoria y Derrota
* **Derrota por Bancarrota:** Agotar los 3 Días de Gracia consecutivos con saldo en cero o deuda impagable al cierre nocturno.
* **Derrota por Muerte:** Reducir la paciencia de un Sicario o fallar una acusación directa en una sede sin protección.
* **Derrota por Prisión:** Acumular 3 actas de inspección o ser denunciado por un policía incorruptible.
* **Victoria:** Sobrevivir 7 jornadas consecutivas en el *Penthouse Internacional* (Nivel 8), orquestando el colapso bursátil y la cumbre diplomática mediante la última gran tirada.
