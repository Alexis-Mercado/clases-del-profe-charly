# Metodologías Ágiles

## 1. Introducción y Panorama General

### Resumen Ejecutivo
El término **“ágil”** (Agile) hace referencia a un conjunto de filosofías, valores y principios de gestión y desarrollo de software que priorizan la adaptabilidad, la entrega temprana de valor incremental y la colaboración continua con el cliente por encima de la planificación rígida y los procesos burocráticos. 

El movimiento ágil surge formalmente a finales de los años 90 y principios de los 2000 (culminando en la publicación del *Manifesto Ágil* en 2001) como una respuesta crítica a los modelos de desarrollo tradicionales (como el modelo en cascada o *Waterfall*). Estos enfoques tradicionales fallaban recurrentemente en entornos complejos debido a su incapacidad para gestionar los cambios de requisitos a mitad del proyecto, generando costosos retrasos y productos desalineados con las necesidades reales de los usuarios.

Este documento cubrirá de manera exhaustiva los fundamentos teóricos y prácticos de la agilidad, desglosando los marcos de trabajo más utilizados en la industria tecnológica: **Scrum**, **Kanban** y la metodología de innovación centrada en el usuario **Design Thinking**, detallando sus roles, artefactos, eventos, métricas de flujo y su articulación dentro del ciclo de vida del desarrollo de software (SDLC).

### Principios Ágiles y su Impacto
El marco conceptual ágil se sustenta en 4 valores fundamentales y 12 principios rectores que transforman la dinámica de los equipos de trabajo:

* **Valores clave:**
  1. *Individuos e interacciones* sobre procesos y herramientas.
  2. *Software funcionando* sobre documentación exhaustiva.
  3. *Colaboración con el cliente* sobre negociación de contratos.
  4. *Respuesta ante el cambio* sobre seguir un plan estricto.

* **Impacto en la gestión del trabajo:**
  * **Transparencia y visibilidad:** Las tareas y bloqueos se hacen públicos y accesibles para todo el equipo.
  * **Mitigación temprana de riesgos:** Al trabajar en ciclos cortos (iteraciones), los errores se detectan y corrigen semanas antes de la entrega final.
  * **Empoderamiento del equipo:** Se otorga autonomía a los desarrolladores para autoorganizarse y tomar decisiones técnicas.

### Panorama de Marcos Ágiles
* **Scrum:** Un marco estructurado basado en iteraciones de duración fija (*Sprints*), ideal para productos complejos donde los requisitos evolucionan constantemente y se requiere entregar incrementos funcionales regulares.
* **Kanban:** Un enfoque de gestión visual del flujo de trabajo basado en la mejora continua y la limitación del trabajo en proceso (*WIP*), óptimo para entornos operativos o de soporte con alta variabilidad y entradas continuas de tareas.
* **Design Thinking:** Una metodología de resolución creativa de problemas centrada profundamente en la empatía con el usuario. Se utiliza antes o en paralelo a Scrum/Kanban para asegurar que se está construyendo el producto correcto (*"building the right thing"*).

### Ventajas, Limitaciones y Trade-offs

| Dimensión | Beneficios / Ventajas | Limitaciones | Trade-offs típicos |
| :--- | :--- | :--- | :--- |
| **Scrum** | Estructura clara, entregas predecibles, fuerte alineación de equipo. | Rigidez en los Sprints; sobrecarga de reuniones si no se facilitan bien. | Se sacrifica la flexibilidad a corto plazo dentro del Sprint a cambio de estabilidad temporal. |
| **Kanban** | Máxima flexibilidad, visibilidad de cuellos de botella, sin ciclos rígidos. | Requiere disciplina estricta para no saturar el tablero; menor previsibilidad a largo plazo. | Se sacrifica la predictibilidad de fechas fijas a cambio de optimizar el tiempo de ciclo continuo. |
| **Design Thinking** | Evita desperdiciar recursos construyendo soluciones no deseadas; alta empatía. | Puede percibirse como abstracto o lento si no se acotan los tiempos de investigación. | Se invierte más tiempo inicial en exploración a cambio de reducir drásticamente el riesgo de fracaso comercial. |

---

## 2. Scrum: Profundización

### Conceptos Base
Scrum es un marco de trabajo ligero que ayuda a las personas, equipos y organizaciones a generar valor a través de soluciones adaptativas para problemas complejos. Su propósito fundamental es romper proyectos grandes en piezas manejables entregadas en ciclos cortos llamados *Sprints* (de 1 a 4 semanas).

* **Cuándo usar Scrum:** 
  * Cuando el producto es complejo y los requerimientos cambian con frecuencia.
  * Cuando se requiere una retroalimentación constante del cliente o usuario final.
  * Cuando el equipo puede trabajar de manera colaborativa y multifuncional.

### Roles en Scrum
* **Product Owner (PO):**
  * *Responsabilidades:* Es el máximo responsable de maximizar el valor del producto. Gestiona, prioriza y aclara los elementos del *Product Backlog*, sirviendo de puente entre los stakeholders y el equipo técnico.
  * *Errores frecuentes:* Asumir un rol pasivo, cambiar prioridades a mitad de un Sprint en curso, o actuar como intermediario inaccesible.
* **Scrum Master (SM):**
  * *Responsabilidades:* Facilita los eventos de Scrum, ayuda al equipo a eliminar impedimentos y promueve la adopción de las prácticas y valores ágiles. Es un líder servidor.
  * *Errores frecuentes:* Actuar como "jefe" o gestor de tareas del equipo en lugar de facilitador, o ignorar los conflictos interpersonales.
* **Development Team (Equipo de Desarrollo):**
  * *Responsabilidades:* Profesionales multifuncionales (analistas, desarrolladores, testers, diseñadores) encargados de crear el incremento utilizable de producto en cada Sprint. Son totalmente autoorganizados.
  * *Errores frecuentes:* Trabajar en silos individuales sin colaborar, aceptar compromisos excesivos de trabajo por presión externa.

### Artefactos y Criterios de Calidad
* **Product Backlog:** Lista emergente y ordenada de todo lo necesario para mejorar el producto. Es la única fuente de requisitos para el trabajo a realizar.
* **Sprint Backlog:** El conjunto de elementos del Product Backlog seleccionados para el Sprint actual, junto con el plan para entregarlos.
* **Increment (Incremento):** Concreción de un paso hacia el objetivo del producto. Cada incremento debe ser sumable y usable, cumpliendo estrictamente con la *Definition of Done*.
* **Criterios de aceptación vs. Definition of Done (DoD):**
  * *Criterios de aceptación:* Son las condiciones específicas que una historia de usuario particular debe cumplir para que el PO la apruebe (ej. *"el botón de pago debe validar tarjetas VISA y Mastercard"*).
  * *Definition of Done (DoD):* Es el estándar de calidad compartido por todo el equipo que aplica a **todas** las historias del incremento (ej. código revisado por pares, pruebas unitarias aprobadas al 80%, sin errores críticos en CI/CD).

### Eventos de Scrum
| Evento | Objetivo | Duración sugerida | Antipatrón típico |
| :--- | :--- | :--- | :--- |
| **Sprint Planning** | Planificar el trabajo del ciclo seleccionando elementos del Backlog y definiendo el *Sprint Goal*. | Máximo 8 horas para un Sprint de 1 mes (proporcional). | Salir de la reunión sin un objetivo claro o planificar basándose en deseos y no en la capacidad real. |
| **Daily Scrum** | Sincronizar las actividades del día anterior y planificar el trabajo de las siguientes 24 horas para el equipo de desarrollo. | Exactamente 15 minutos. | Convertirlo en un reporte de estatus individual dirigido al jefe o Scrum Master en lugar de una sesión de coordinación de equipo. |
| **Sprint Review** | Inspeccionar el incremento de producto con los stakeholders y adaptar el Product Backlog si es necesario. | Máximo 4 horas para un Sprint de 1 mes. | Presentar una simple presentación de PowerPoint en lugar de mostrar software funcionando en un entorno real. |
| **Sprint Retrospective** | Planificar formas de aumentar la calidad y la efectividad del equipo, revisando personas, procesos y herramientas. | Máximo 3 horas para un Sprint de 1 mes. | Que sea una sesión de quejas sin planes de acción concretos o dejar de hacerla por falta de tiempo. |

### Métricas en Scrum
* **Velocity (Velocidad):** Cantidad de trabajo (medida en Story Points) que un equipo completa de manera exitosa en un Sprint.
  * *Cómo interpretarla:* Sirve como métrica de predictibilidad histórica a mediano plazo.
  * *Cómo no usarla:* **Nunca** debe usarse como una herramienta de medición de productividad individual o para comparar la eficiencia entre diferentes equipos.
* **Burndown Chart:** Gráfico que muestra la cantidad de trabajo restante en el Sprint o en el proyecto frente al tiempo transcurrido.
  * *Cómo interpretarla:* Permite ver si el equipo va a ritmo de cumplir el objetivo del Sprint o si se desvía.
  * *Cómo no usarla:* No debe manipularse para ocultar retrasos reales ante la gerencia.
* **Work in Progress (WIP):** Número de tareas iniciadas pero no terminadas.
  * *Cómo interpretarla:* Un WIP alto indica multitarea ineficiente y cuellos de botella.
  * *Cómo no usarla:* Ignorarla permitiendo que cada desarrollador abra múltiples tareas al mismo tiempo.

---

## 3. Kanban: Profundización

### Fundamentos y Prácticas
Kanban es un método de gestión de flujo de valor basado en la mejora evolutiva y el principio de "empezar con lo que haces ahora". Sus 6 prácticas esenciales son:
1. **Visualizar el flujo de trabajo:** Reflejar las tareas en un tablero físico o digital transparente.
2. **Limitar el trabajo en proceso (WIP):** Restringir la cantidad de tareas simultáneas para obligar a terminar antes de empezar algo nuevo.
3. **Gestionar el flujo:** Monitorear, medir y optimizar el movimiento de los elementos a través del tablero.
4. **Hacer las políticas explícitas:** Definir reglas claras de cuándo un trabajo puede pasar de una columna a otra (criterios de "pase").
5. **Implementar bucles de retroalimentación:** Realizar reuniones periódicas de revisión de operaciones.
6. **Mejorar colaborativamente (evolucionar experimentalmente):** Usar modelos científicos y métricas para ajustar el proceso.

### Tablero Kanban y Límites WIP
Propuesta de columnas para un equipo de desarrollo de software:
`[ Backlog ] -> [ Por Hacer (WIP: 6) ] -> [ En Desarrollo (WIP: 3) ] -> [ Code Review (WIP: 2) ] -> [ Testing (WIP: 2) ] -> [ Hecho (Done) ]`

* *Razonamiento de límites WIP:* Si el equipo consta de 5 personas, permitir más de 3 tareas simultáneas en desarrollo genera saturación y pérdida de enfoque (multitarea ineficiente). Los límites estrictos en *Code Review* y *Testing* evitan que se acumulen tareas sin revisar.

### Métricas de flujo
* **Lead Time:** Tiempo total que transcurre desde que una solicitud es creada en el backlog hasta que se entrega completamente al usuario final.
* **Cycle Time:** Tiempo que tarda una tarea desde que el equipo comienza a trabajar activamente en ella hasta que se finaliza.
* **Throughput:** Cantidad de elementos de trabajo completados por unidad de tiempo (ej. tareas terminadas por semana).
* **Diagrama de Flujo Acumulado (CFD):** Gráfico de áreas apiladas que muestra el volumen de trabajo en cada estado del tablero a lo largo del tiempo. 
  * *Lectura:* Si las bandas paralelas crecen desproporcionadamente en una fase intermedia (ej. Testing), indica un cuello de botella evidente que requiere intervención inmediata.

### Políticas y Clases de Servicio
Las clases de servicio categorizan el trabajo según su urgencia y costo de retraso:
* **Expédito (Urgente / Hotfix):** Errores críticos en producción. Salta las colas normales y tiene prioridad absoluta (rompe temporalmente el límite WIP normal bajo reglas estrictas).
* **Fecha fija (Fixed Date):** Tareas atadas a un lanzamiento normativo o legal obligatorio.
* **Estándar (Standard):** Funcionalidades regulares del producto con flujo normal.
* **Intangible (Intangible):** Refactorizaciones técnicas o mejoras de documentación sin fecha de entrega rígida.

### Cuándo usar Kanban vs. Otros Enfoques
Kanban es ideal para **entornos orientados a servicios, soporte técnico, mantenimiento de software o flujos operativos continuos** caracterizados por una alta variabilidad en la llegada de requerimientos imprevistos, donde las iteraciones fijas de Scrum resultan restrictivas.

---

## 4. Design Thinking: Profundización

### Visión General y Encaje con el Desarrollo de Software
Design Thinking es un enfoque de innovación centrado en las personas que utiliza la sensibilidad y los métodos del diseñador para hacer coincidir las necesidades de los usuarios con lo que es tecnológicamente factible y comercialmente viable. En el desarrollo de software, se acopla en las fases iniciales de descubrimiento (*Discovery*) para mitigar el riesgo de construir un sistema técnicamente impecable que nadie necesita.

### Fases de Design Thinking
1. **Empatizar:**
   * *Objetivo:* Comprender profundamente las necesidades, emociones y frustraciones de los usuarios reales.
   * *Técnicas:* Entrevistas en profundidad, observación de campo, mapas de empatía.
   * *Entregable mínimo:* Perfiles de usuario y mapas de empatía documentados.
2. **Definir:**
   * *Objetivo:* Sintetizar los hallazgos para formular un problema claro y enfocado en el usuario (*Point of View*).
   * *Técnicas:* Definición de declaraciones de problemas, arquetipos de usuarios (User Personas).
   * *Entregable mínimo:* Declaración clara del problema a resolver.
3. **Idear:**
   * *Objetivo:* Generar una gran cantidad de ideas creativas sin filtros iniciales.
   * *Técnicas:* Lluvia de ideas (*Brainstorming*), Crazy Eights, bocetos rápidos.
   * *Entregable mínimo:* Banco de soluciones candidatas priorizadas.
4. **Prototipar:**
   * *Objetivo:* Construir representaciones tangibles y económicas de las ideas seleccionadas.
   * *Técnicas:* Wireframes en papel, maquetas de baja fidelidad en Figma o descripciones textuales de flujos.
   * *Entregable mínimo:* Prototipo interactivo navegable de baja fidelidad.
5. **Probar:**
   * *Objetivo:* Evaluar el prototipo con usuarios reales para recoger feedback y ajustar la solución.
   * *Técnicas:* Pruebas de usabilidad, matrices de retroalimentación.
   * *Entregable mínimo:* Informe de hallazgos y lista de mejoras identificadas.

### Mini-caso Práctico: Aplicación de Delivery para Adultos Mayores
* **Problema:** Los adultos mayores de 70 años experimentan altos niveles de frustración y abandono al intentar pedir medicamentos o víveres a domicilio en aplicaciones de entrega comerciales debido a tipografías minúsculas, procesos de pago confusos y exceso de opciones publicitarias.
* **Fase 1 (Empatizar):** Se entrevista a 5 adultos mayores, observando que necesitan fuentes grandes, asistencia por voz y botones grandes de un solo toque.
* **Fase 2 (Definir):** *"Los adultos mayores independientes necesitan una interfaz radicalmente simplificada y asistida por voz para pedir suministros esenciales sin fricción digital."*
* **Fase 3 (Idear):** Se generan ideas como una pantalla inicial con solo 3 botones grandes (Supermercado, Farmacia, Llamar a Asistente) y opción de dictado por voz.
* **Fase 4 (Prototipar - Baja fidelidad en texto):**
  ```text
  +-----------------------------------+
  |          ASISTENTE SALUD          |
  |                                   |
  |  [ 🛒 PEDIR VÍVERES Y MEDICINAS ] |
  |                                   |
  |  [ 📞 LLAMAR A FAMILIAR / AYUDA ] |
  |                                   |
  |  ( 🎤 Toca aquí y di qué necesitas) |
  +-----------------------------------+
  ```
* **Fase 5 (Probar):** Se somete el prototipo de papel y baja fidelidad a prueba con 3 usuarios de la tercera edad, validando que el botón de voz reduce el tiempo de interacción en un 70%.

### Relación con SDLC y Agilidad
Design Thinking opera en el espacio del **Problema** (asegurando construir el producto correcto), mientras que Scrum y Kanban operan en el espacio de la **Solución** (construyendo el producto correctamente). Las historias de usuario generadas en el backlog de Scrum se alimentan directamente de los prototipos validados en Design Thinking.

---

## 5. Conclusiones

La adopción de marcos ágiles como Scrum y Kanban, combinados con una sólida mentalidad de diseño centrada en el usuario mediante Design Thinking, transforma radicalmente la eficiencia operativa y la efectividad del desarrollo tecnológico. En un contexto académico o profesional, estas metodologías eliminan la incertidumbre ciega, fomentan la adaptabilidad frente a cambios del mercado y garantizan que los equipos tecnológicos entreguen soluciones con un impacto real y medible.

---

## 6. Referencias

1. Beck, K., et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org/
2. Sutherland, J., & Schwaber, K. (2020). *La Guía de Scrum: Las reglas del juego para Scrum*. Scrum.org.
3. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.
4. Brown, T. (2008). *Design Thinking*. Harvard Business Review, 86(6), 84.
5. Kniberg, H., & Skelton, M. (2015). *Kanban and Scrum: making the most of both*. InfoQ Enterprise Software Development Series.