# AI Log — Equipo EmprendeIA

## Herramientas utilizadas
- **Claude** (claude.ai) — Consultas de sintaxis y documentación
- **Claude Code** (CLI / Anthropic) — Auditoría de datos, verificación estadística, investigación de fuentes
- **GitHub Copilot** (VS Code) — Autocompletado básico de código
- **ChatGPT 4o** — Búsqueda de documentación de sintaxis

## Filosofía de uso

Nuestro criterio fue estricto: **si la tarea requiere pensar, cruzar datos, decidir qué contar o interpretar el sistema educativo de México, la hacemos nosotros.** La IA se usó exclusivamente como acelerador mecánico (sintaxis, documentación, verificación) y como auditor externo (revisión de datos, búsqueda de errores).

La hipótesis fundamental — que la pobreza condiciona la educación y esto condena al empleo precario — fue concebida, investigada y demostrada enteramente por el equipo. La narrativa de "La Historia de Luis" fue redactada por el equipo. La IA revisó y criticó, pero no creó contenido narrativo original.

**Regla interna:** si la decisión afecta la historia que contamos, la tomamos nosotros. Si la decisión es sobre cómo pintar un borde o qué función de Plotly usar, la IA puede ayudar.

## Registro de uso

### 2026-04-08 | Claude | Sintaxis de mapas coropléticos en Plotly
- **Tarea:** Necesitábamos mapear la pobreza por estados (ODS 1) y no recordábamos cómo cargar un GeoJSON dentro de `px.choropleth`.
- **Prompt:** "¿Cuál es la sintaxis base para que Plotly lea un GeoJSON con `featureidkey`?"
- **Resultado:** Devolvió la estructura base de `px.choropleth` con `geojson`, `locations` y `featureidkey`.
- **Decisión:** Aceptamos la estructura base. Nosotros programamos el pre-filtrado de Pandas, elegimos la paleta `Reds` para denotar urgencia, y ajustamos manualmente los hiperparámetros del `update_layout` para el diseño oscuro.

### 2026-04-09 | ChatGPT | Resolución de bug en Quarto Dashboards
- **Tarea:** El render de Quarto daba doble renderizado de los gráficos. No entendíamos por qué.
- **Prompt:** "Tengo un error en Quarto donde mis gráficos de Plotly se renderizan dos veces dentro de bloques markdown. ¿Por qué?"
- **Resultado:** Explicó que debíamos retornar la variable al final de la celda de Jupyter en lugar de usar comandos extra de visualización.
- **Decisión:** Aceptamos el diagnóstico. Corregimos manualmente el archivo `.qmd` reacomodando los bloques y usando columnas y valueboxes nativos.

### 2026-04-09 | GitHub Copilot | Autocompletado de Markdown
- **Tarea:** Generar estructura repetitiva de etiquetas Markdown para las pestañas del tablero.
- **Resultado:** Copilot autocompletaba los encabezados nivel 1 y 2 al empezar a escribir.
- **Decisión:** Aceptamos el autocompletado por ser puramente mecánico.

### 2026-04-14 | Claude Code | Auditoría de integridad de datos
- **Tarea:** Verificar que los valores mostrados en el tablero coincidieran con los datos fuente. Sospechábamos de un dato hardcodeado.
- **Prompt:** "Lee, analiza y evalúa el proyecto. Verifica los datos del dashboard contra las fuentes originales."
- **Resultado:** Identificó que el valor `$59 MXN/hr` para ocupaciones elementales estaba hardcodeado y era incorrecto — el dato real en `8.5.1c_sh_es.csv` es `$39.66 MXN/hr`. También detectó que la correlación central del proyecto (pobreza vs abandono Media Superior) era estadísticamente nula (r = −0.15, p = 0.42).
- **Decisión:** Corregimos el dato de salario a su valor real calculado. El descubrimiento de la correlación nula fue un punto de inflexión — nos obligó a replantear el eje analítico completo del proyecto (ver siguiente entrada).

### 2026-04-14 | Claude Code | Exploración de variables alternativas en CONEVAL
- **Tarea:** Ante la correlación nula de pobreza vs abandono, necesitábamos encontrar variables que SÍ se correlacionaran estadísticamente. El archivo CONEVAL tiene 145 columnas y solo estábamos usando 1.
- **Prompt:** "Extrae TODOS los indicadores del archivo Concentrado_indicadores_de_pobreza_2020.xlsx y calcula correlaciones contra las variables educativas."
- **Resultado:** Descubrió que el archivo CONEVAL contenía "rezago educativo" y "pobreza extrema" por estado. Al correlacionar pobreza extrema con escolaridad promedio obtuvo **r = −0.82, p < 0.001** — una relación muy fuerte que sí sostiene nuestra tesis.
- **Decisión:** Adoptamos la escolaridad promedio como variable central de ODS 4, reemplazando el abandono escolar. Esta fue una decisión analítica del equipo basada en los resultados que la IA nos presentó — nosotros interpretamos por qué funciona mejor (la escolaridad captura el efecto acumulado de las barreras, mientras que el abandono está confundido por el pull del mercado laboral en estados ricos).

### 2026-04-14 | Claude Code | Búsqueda de fuentes citables
- **Tarea:** Necesitábamos fuentes académicas e institucionales que respaldaran la correlación pobreza-educación para el contexto narrativo.
- **Prompt:** "Busca estudios del CONEVAL, OCDE, UNICEF y artículos académicos sobre la relación pobreza-rezago educativo en México."
- **Resultado:** Encontró el estudio de El Colegio Mexiquense sobre distribución espacial de pobreza y rezago educativo, el reporte OCDE México 2026 (informalidad 56%), y el dato UNICEF (56 de 100 niños completan Media Superior).
- **Decisión:** Incorporamos las fuentes que verificamos manualmente consultando las URLs. Descartamos fuentes que no pudimos verificar. La selección final de qué citar y cómo integrarlo en la narrativa fue nuestra.

### 2026-04-14 | Claude Code | Rediseño de arquitectura del tablero
- **Tarea:** Convertir el dashboard con tabs en una landing page con scroll narrativo estilo Apple, integrando la historia de Luis con los datos.
- **Prompt:** "Construye la landing page según el blueprint de diseño UX que aprobamos."
- **Resultado:** Generó el archivo `.qmd` con formato HTML, 8 secciones scroll, animaciones CSS con Intersection Observer, y las gráficas Plotly embebidas. Requirió dos iteraciones porque Quarto inyectaba wrappers de dashboard que rompían el layout.
- **Decisión:** El diseño conceptual (qué secciones, qué historia contar en cada una, el wireframe completo) fue nuestro. Claude Code implementó el código CSS/HTML/Python según nuestras especificaciones. Revisamos el resultado visual y pedimos ajustes.

### 2026-04-14 | Claude Code | Auditoría UX/UI y mejoras visuales
- **Tarea:** Evaluar el tablero como un producto digital y aplicar mejoras de experiencia de usuario.
- **Prompt:** "Haz un análisis como UX/UI Product Designer del proyecto actual."
- **Resultado:** Identificó 8 problemas de usabilidad (grids rotos por Plotly, fondos no transparentes, falta de separación visual entre secciones, etc.) y los corrigió en `landing.scss`. Incluyó fixes de CSS Grid, glassmorphism en tarjetas, y un chevron animado.
- **Decisión:** Nosotros priorizamos las mejoras a implementar. La IA ejecutó las correcciones CSS/HTML según nuestra aprobación. Verificamos cada cambio visualmente.

### 2026-04-14 | Claude Code | Generación de prompts para imágenes con IA
- **Tarea:** Crear un prompt por cada sección del tablero para generar imágenes con un modelo de IA generativa.
- **Prompt:** "Por cada sección genera un prompt para generar una imagen con IA. ¿Qué estilo de imagen me recomiendas?"
- **Resultado:** Propuso dirección artística (fotografía documental con iluminación cinematográfica, paleta desaturada) y entregó 9 prompts optimizados para Gemini, uno por sección.
- **Decisión:** El equipo eligió la dirección artística y el modelo (Gemini). Los prompts fueron generados por la IA pero revisados y ajustados por el equipo antes de ejecutarlos. Las imágenes se generaron manualmente por el equipo.

### 2026-04-14 | Claude Code | Integración de imágenes y animaciones avanzadas
- **Tarea:** Integrar las 9 imágenes generadas como fondos de sección y mejorar el sistema de animaciones para un scrollytelling más inmersivo.
- **Prompt:** "Integra las imágenes en la landing page" y "Mejora la animación de todo. Piensa en Apple como referencia."
- **Resultado:** Integró las imágenes con overlays CSS oscuros calibrados por sección. Reemplazó el sistema de animaciones con easing `cubic-bezier` estilo Apple, animaciones direccionales (`slide-left`, `slide-right`), blur reveal para títulos, clip-path wipe para gráficas, counter animation para números estadísticos, y parallax en fondos.
- **Decisión:** La selección de imágenes, la dirección artística y la verificación visual fueron del equipo. La IA implementó la integración técnica (CSS backgrounds con gradient overlays) y el código de animaciones según nuestras indicaciones de referencia (Apple).

## Lo que NO hizo la IA

- **La selección teórica de ODS y variables socioeconómicas.** La navegación por CONEVAL, SEP e INEGI, la decisión de cruzar ODS 1, 4 y 8, y la hipótesis de que forman un ciclo sistémico fue investigada y formulada por el equipo.
- **La interpretación de la correlación nula.** Cuando Claude Code reportó r = −0.15, fuimos nosotros quienes entendimos que el abandono escolar no era la variable correcta (por la falacia ecológica y el pull del mercado laboral) y decidimos pivotar a escolaridad promedio.
- **La narrativa de "La Historia de Luis."** Todo el texto narrativo del tablero — la historia personal, las metáforas ("la lotería del código postal", "el puente que se rompe"), los paneles laterales y la conclusión — es producto del trabajo intelectual del equipo. La IA criticó y señaló inconsistencias, pero no escribió prosa narrativa.
- **La decisión editorial de qué datos mostrar y qué omitir.** Por ejemplo, decidimos aislar ODS 8 al año 2019 porque los registros 2020+ tenían colapsos estadísticos por COVID-19. Esa decisión requirió explorar los datos y entender el contexto — no se la delegamos a la IA.
- **El diseño conceptual del tablero.** La arquitectura de 3 Actos, el wireframe de la landing page, la elección de tipografía, paleta de colores y la estructura del scroll fueron decisiones del equipo.
- **La dirección artística de las imágenes.** El equipo eligió el estilo visual (fotografía documental cinematográfica), seleccionó el modelo generativo (Gemini), ejecutó la generación, y revisó/descartó resultados. La IA propuso prompts base que el equipo refinó.
- **La verificación visual de cada cambio.** Cada mejora UX, integración de imagen y ajuste de animación fue verificada manualmente por el equipo antes de aceptarse.
