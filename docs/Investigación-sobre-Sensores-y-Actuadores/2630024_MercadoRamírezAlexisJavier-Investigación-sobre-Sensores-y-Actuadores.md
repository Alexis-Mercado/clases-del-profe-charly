# Sensores y Actuadores en Sistemas Mecatrónicos

---

## 1. Conceptos básicos

### ¿Qué es un sensor?
Un sensor es un dispositivo que capta magnitudes físicas o químicas del entorno (como temperatura, luz, presión o distancia) y las transforma en señales eléctricas comprensibles para un sistema de control o procesamiento. Su función principal es permitir que la máquina "perciba" su entorno.

### ¿Qué es un actuador?
Un actuador es un componente capaz de transformar una fuente de energía (eléctrica, neumática o hidráulica) en una acción física o mecánica sobre el entorno. Representa los "músculos" del sistema, encargados de ejecutar movimientos, fuerzas o cambios de estado.

### ¿Cuál es la diferencia entre un sensor y un actuador?
La diferencia radica en el sentido del flujo de información y energía. El **sensor** funciona de entrada: recibe un estímulo físico del entorno y lo convierte en una señal de datos para el sistema. El **actuador** funciona de salida: recibe una orden eléctrica del sistema de control y genera un cambio físico o mecánico en el entorno.

### ¿Qué función tienen dentro de un sistema mecatrónico?
En la mecatrónica, los sensores y actuadores son los elementos de interacción directa con el mundo físico. Los sensores miden el estado actual del proceso y retroalimentan al controlador, mientras que los actuadores ejecutan las correcciones y comandos necesarios para que el sistema cumpla su objetivo de manera autónoma.

---

### Ejemplo de sistema: Puerta automática deslizante

* **Sensor:** Un sensor de presencia por infrarrojos o microondas que detecta la cercanía física de una persona u objeto.
* **Actuador:** Un motor eléctrico de corriente directa o motor paso a paso acoplado a un mecanismo de poleas que abre y cierra las hojas de la puerta.
* **Acciones:**
  * **Sensor detecta:** La presencia de un usuario frente a la entrada.
  * **Actuador realiza:** El giro del motor para deslizar y abrir la puerta de manera controlada.

---

## 2. Investigación de sensores

| Tipo de sensor | Variable que mide | Principio de funcionamiento | Ejemplo | Aplicación |
| :--- | :--- | :--- | :--- | :--- |
| **Temperatura** | Temperatura ambiente o de contacto | Variación de la resistencia eléctrica en función del calor (como en los termistores NTC/PTC) o generación de voltaje por efecto Seebeck (termopares). | Termistor NTC 10k | Control térmico en sistemas de climatización o impresoras 3D. |
| **Luz** | Intensidad lumínica / fotones | Variación de la conductividad eléctrica de un semiconductor al recibir radiación lumínica (fotorresistencia o LDR). | Fotorresistencia LDR GL5528 | Sistemas de iluminación automática exterior o control de brillo de pantallas. |
| **Proximidad** | Presencia u objeto cercano sin contacto | Generación de un campo electromagnético o capacitivo; si un objeto interrumpe o altera el campo, cambia la salida. | Sensor inductivo LJ12A3-4-Z/BX | Detección de piezas metálicas en líneas de producción automatizadas. |
| **Distancia** | Distancia espacial a un objeto | Emisión de un pulso físico (ultrásonico o láser) y medición del tiempo de retorno del eco (tiempo de vuelo). | Sensor ultrasónico HC-SR04 | Sistemas anticolisión en robots móviles y medición de niveles de llenado. |
| **Presión** | Fuerza ejercida por fluidos o gases por unidad de área | Deformación de un elemento elástico (diafragma) que altera galgas extensiométricas en su interior, variando su resistencia. | Transductor de presión MPX5700AP | Monitoreo de presión en sistemas neumáticos o neumáticos médicos. |
| **Humedad** | Humedad relativa del aire o suelo | Cambio en la capacidad dieléctrica o conductividad eléctrica de un polímero higroscópico al absorber vapor de agua. | Sensor DHT11 | Invernaderos automatizados y estaciones meteorológicas domésticas. |
| **Posición** | Ángulo de giro o posición lineal | Interrupción óptica de un disco ranurado (encoder) o variación de un campo magnético (efecto Hall). | Encoder rotativo incremental E6B2-CWZ6C | Control de posición angular en ejes de motores y brazos robóticos. |
| **Velocidad o movimiento** | Velocidad de giro o desplazamiento | Conteo de pulsos por unidad de tiempo emitidos por un encoder o sensor de efecto Hall magnético. | Sensor magnético KY-003 | Tacómetros industriales y control de velocidad en motores síncronos. |
| **Fuerza o peso** | Fuerza mecánica, tensión o peso de carga | Deformación mecánica microscópica de una celda que altera la resistencia eléctrica de sus galgas internas (puente de Wheatstone). | Celdas de carga HX711 (tipo barra) | Básculas digitales comerciales e industriales. |

---

## 3. Clasificación de sensores

### Sensores analógicos vs. digitales
* **Característica distintiva:** La naturaleza de la señal de salida frente a la variable física medida.
* **Sensor analógico:** Entrega una señal eléctrica continua (voltaje o corriente) que varía de forma proporcional e infinita dentro de un rango determinado (ej. de 0 a 5V). Requiere un conversor analógico-digital (ADC) para ser leída por un microcontrolador.
* **Sensor digital:** Entrega pulsos o valores discretos en formato binario (niveles lógicos de 0 y 1 o protocolos de comunicación digital como I2C / SPI). No sufre degradación por ruido eléctrico a largas distancias.

### Sensores de contacto vs. sin contacto
* **Característica distintiva:** El requerimiento de interacción física directa con el objeto a medir.
* **Sensor de contacto:** Requiere tocar físicamente el objeto para realizar la medición o activación (ej. un interruptor de límite o *switch* mecánico). Su desgaste mecánico es mayor debido a la fricción constante.
* **Sensor sin contacto:** Mide a distancia utilizando campos electromagnéticos, luz, ultrasonido o infrarrojos. Ofrece mayor vida útil al no existir fricción mecánica ni desgaste por abrasión.

### Sensores activos vs. pasivos
* **Característica distintiva:** La necesidad o no de una fuente de alimentación externa para generar la señal de respuesta.
* **Sensor activo:** Requiere una fuente de energía externa para excitar el transductor y generar su señal (ej. un sensor ultrasónico que necesita voltaje para emitir la onda).
* **Sensor pasivo:** Genera su propia señal eléctrica directamente a partir de la energía de la variable física que mide, sin requerir energía de excitación externa (ej. un termopar que genera voltaje por diferencia de temperatura o una celda fotovoltaica).

---

## 4. Investigación de actuadores

| Actuador | Energía utilizada | Movimiento | Ventaja | Limitación | Aplicación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Motor DC** | Eléctrica (Corriente Continua) | Rotatorio continuo (en ambos sentidos) | Alto torque a altas velocidades y facilidad de control de velocidad mediante PWM. | Poca precisión angular sin un sistema de retroalimentación externo. | Tracción de vehículos de juguete o ventiladores portátiles. |
| **Servomotor** | Eléctrica | Rotatorio limitado y controlado con precisión angular exacta (ej. 0° a 180°) | Incorpora un lazo cerrado interno que asegura alta precisión de posición. | Rango de giro mecánico limitado por topes físicos internos. | Articulaciones de brazos robóticos y timones de aeromodelos. |
| **Motor paso a paso** | Eléctrica (pulsos discretos) | Rotatorio fraccionado en pasos discretos y precisos | Excelente control de posición y retención estática sin perder el paso en lazo abierto. | Menor torque a altas velocidades y consumo constante de corriente en reposo. | Extrusores e impresoras 3D, máquinas CNC. |
| **Solenoide** | Eléctrica | Lineal (empuje o tracción corta) | Respuesta muy rápida y diseño compacto y robusto. | Recorrido de desplazamiento físico muy corto y limitado. | Cerrojos eléctricos de puertas y válvulas hidráulicas/neumáticas. |
| **Cilindro neumático** | Neumática (aire comprimido) | Lineal de alta fuerza | Gran fuerza de empuje con alta velocidad y componentes limpios de bajo mantenimiento. | Requiere compresor de aire y una instalación ruidosa con control de velocidad menos fluido. | Expulsión de piezas en líneas de bandas transportadoras. |
| **Cilindro hidráulico** | Hidráulica (aceite a alta presión) | Lineal de fuerza extrema | Capacidad para mover cargas de toneladas con gran precisión de empuje constante. | Sistema complejo, costoso, voluminoso y con riesgo de fugas de fluido. | Maquinaria pesada, retroexcavadoras y prensas industriales. |

---

## 5. Comparación de actuadores

### Motor DC vs. Servomotor
* **Diferencia:** El motor DC convencional gira continuamente a velocidad variable gobernada por voltaje, mientras que el servomotor combina un motor DC, una caja reductora y un circuito de control con potenciómetro para posicionarse exactamente en un ángulo específico.
* **Situación de elección:** Se elegiría un **motor DC** para accionar las ruedas de un carro robotizado donde se requiere velocidad y desplazamiento continuo sin importar el ángulo exacto. Se elegiría un **servomotor** para controlar el timón de dirección de ese mismo robot, donde se requiere posicionar las ruedas con un ángulo preciso y mantenerlas firmes.

### Servomotor vs. Motor paso a paso
* **Diferencia:** El servomotor utiliza un sistema de control en lazo cerrado con realimentación de posición (generalmente limitada a un ángulo de 180° o 360° continuos en versiones especiales), mientras que el motor paso a paso se mueve mediante pulsos discretos en lazo abierto permitiendo giros completos ilimitados con alta resolución de paso.
* **Situación de elección:** Se elegiría un **servomotor** para mover la cámara de vigilancia de un sistema de seguridad en un ángulo de paneo rápido y controlado. Se elegiría un **motor paso a paso** para mover el eje de una impresora 3D o máquina de grabado, donde se requieren giros repetitivos continuos con una precisión milimétrica por cada revolución.

### Actuador neumático vs. Actuador hidráulico
* **Diferencia:** El actuador neumático utiliza aire comprimido, lo que lo hace rápido, limpio y adecuado para cargas moderadas. El actuador hidráulico utiliza aceite a presiones mucho más elevadas, lo que le permite desarrollar fuerzas inmensas para cargas pesadas.
* **Situación de elección:** Se elegiría un **actuador neumático** para desplazar rápidamente una caja ligera en una línea de empaque industrial. Se elegiría un **actuador hidráulico** para el brazo de una excavadora o grúa de construcción que debe levantar toneladas de tierra o materiales pesados.

---

## 6. Sensores y actuadores en un sistema real

### Sistema seleccionado: Brazo robótico industrial

#### Elementos identificados:
* **Sensores:**
  1. **Encoder óptico:** Mide los giros y la posición angular exacta de cada articulación del brazo.
  2. **Sensor de corriente:** Detecta sobrecargas o atascos en los motores previniendo daños mecánicos.
  3. **Sensor táctil/de fuerza en la pinza (*gripper*):** Detecta la presión ejercida sobre el objeto sujetado para evitar aplastarlo.
* **Actuadores:**
  1. **Servomotores o motores de corriente alterna con reductor:** Mueven las articulaciones principales (hombro, codo y base).
  2. **Cilindro neumático o solenoide de pinza:** Abre y cierra el efector final (pinza) para tomar y soltar piezas.

---

### Diagrama de relación del sistema

```
[ Usuario / Consigna ] 
         │
         ▼
[ Controlador (PLC / Microcontrolador) ] ◄── (Retroalimentación) ── [ Sensores (Encoders, Fuerza) ]
         │
         ▼ 
      (Señales de control)
[ Actuadores (Servomotores, Solenoides) ]
         │
         ▼
[ Entorno Físico (Movimiento del Brazo y Piezas) ]
```

---

## 7. Selección de componentes

1. **Detectar si una persona se encuentra frente a una puerta automática:**
   * **Componente:** Sensor infrarrojo pasivo (PIR) o sensor de presencia ultrasónico/microondas.
   * **Razón:** Permite identificar sin contacto la presencia de cuerpos en movimiento dentro del área de cobertura de la entrada.
2. **Medir la temperatura dentro de un salón:**
   * **Componente:** Sensor de temperatura digital (como el LM35 o DHT22).
   * **Razón:** Ofrecen una lectura lineal precisa y estable de la temperatura ambiente para sistemas de climatización.
3. **Detectar el nivel de agua de un depósito:**
   * **Componente:** Sensor de nivel ultrasónico o sensor de boya magnética por contacto.
   * **Razón:** Miden con precisión la altura o presencia del líquido sin requerir mediciones complejas de presión.
4. **Mover una rueda de un robot móvil:**
   * **Componente:** Motor de corriente directa (DC con reductor).
   * **Razón:** Proporciona tracción continua, velocidad variable y buen torque para desplazamiento sobre el suelo.
5. **Controlar con precisión el ángulo de una pequeña articulación robótica:**
   * **Componente:** Servomotor (como el SG90 o MG996R).
   * **Razón:** Su circuitería interna de control por PWM permite fijar y mantener una posición angular exacta de manera sencilla.
6. **Empujar una pieza en una línea de producción:**
   * **Componente:** Cilindro neumático de doble efecto.
   * **Razón:** Ofrece una fuerza de empuje lineal rápida, confiable y de alta velocidad ideal para procesos de manufactura.
7. **Medir la distancia entre un robot y una pared:**
   * **Componente:** Sensor de distancia ultrasónico (HC-SR04) o sensor láser ToF (Time-of-Flight).
   * **Razón:** Calculan de forma inmediata la distancia mediante tiempo de vuelo con excelente resolución.
8. **Detectar si una habitación está iluminada:**
   * **Componente:** Fotorresistencia (LDR) o sensor de luz digital (como el TSL2561).
   * **Razón:** Modifican su resistencia eléctrica o entregan un valor directamente proporcional a los niveles de luz ambiental detectados.

---

## Reflexión final

Analizar un sistema mecatrónico permite comprender la estrecha sinergia entre el cálculo lógico, la medición física y la ejecución mecánica. 

* **Diferencia entre medir y actuar:** Medir una variable representa un proceso pasivo o de adquisición de información donde el sistema capta el estado del entorno sin alterarlo bruscamente. En contraste, realizar una acción física implica un despliegue de energía para modificar el entorno y generar un cambio tangible.
* **Necesidad de sensores y actuadores:** Un sistema mecatrónico no puede funcionar de manera autónoma solo con procesamiento informático. Los sensores actúan como los sentidos que informan lo que sucede, el microcontrolador procesa los datos y toma decisiones, y los actuadores ejecutan la respuesta física. Sin esta triada, el sistema carecería de la capacidad de interactuar y adaptarse al mundo real.
* **Componente más interesante:** El **servomotor** resulta fascinante debido a la integración inteligente de la electrónica de control en lazo cerrado dentro de un actuador mecánico, logrando mantener posiciones estables y milimétricas a pesar de perturbaciones externas.

---

## Referencias

* Ogata, K. (2010). *Ingeniería de Control Moderna* (5ª ed.). Pearson Educación.
* Bolton, W. (2016). *Mechatronics: Electronic Control Systems in Mechanical and Electrical Engineering* (6ª ed.). Pearson.
* SparkFun Electronics. (2025). *Hojas de datos y guías técnicas de sensores y actuadores*. https://www.sparkfun.com
* Texas Instruments. (2024). *Manuales de aplicación de transductores y amplificadores de señal*. https://www.ti.com