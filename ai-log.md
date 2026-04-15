# Registro Estratégico de Uso de IA

## Herramientas Utilizadas
- Claude / ChatGPT (como buscador de documentación de sintaxis)
- GitHub Copilot (autocompletado básico)

## Filosofía de Uso
En "Estudiar No Es Suficiente", tomé la decisión estricta de utilizar la Inteligencia Artificial **únicamente como un asistente de sintaxis y tipografía**. Toda la investigación, estructuración sociológica, análisis de datos con Pandas y el *storytelling* (la narrativa que conecta la pobreza con el abandono escolar y el empleo precario) son decisiones e ideas 100% mías.

Si la tarea requería pensar, cruzar datos, decidir qué contar o analizar cómo funciona el sistema educativo de México, lo hice yo. Si la decisión era recordar de memoria la documentación técnica para pintar el borde de una gráfica, usé la IA para mayor velocidad.

## Registro Específico de Tareas:

1. **Sintaxis de Mapas Coropléticos en Plotly**
   - *El problema:* Necesitaba mapear la pobreza por estados (ODS 1) pero no recordaba exactamente cómo cargar un `.json` geográfico dentro de un `px.choropleth`.
   - *Cómo usé la IA:* En lugar de buscar horas en foros, le pregunté a Claude la sintaxis base para que Plotly leyera el `featureidkey`.
   - *Mi aportación:* Yo programé el pre-filtrado de Pandas, elegí la paleta `Reds` para denotar urgencia y ajusté manualmente los hiperparámetros del `update_layout` para alinear todo al diseño oscuro (`plotly_dark`).

2. **Resolución de Bugs en Quarto Dashboards**
   - *El problema:* Al intentar maquetar mi proyecto interactivo con Quarto nativo, tenía un error donde me daba doble renderizado de los gráficos.
   - *Cómo usé la IA:* Utilicé ChatGPT para investigar por qué estaban colisionando mis variables de Python dentro de las etiquetas de bloque de Markdown. Me explicó que simplemente debía devolver la variable al final de la celda de Jupyter en lugar de usar comandos extra de visualización. 
   - *Mi aportación:* Corregí limpia y manualmente mi archivo `.qmd` reacomodando mis bloques de sintaxis usando columnas y _valueboxes_ nativos.

3. **Autocompletado de CSS/Markdown**
   - *El problema:* Generar estructura repetitiva (como las pestañas del *"Fase I, Fase II, Fase III"*).
   - *Cómo usé la IA:* GitHub Copilot me daba el autocompletado del etiquetado Markdown cada que empezaba a escribir mis encabezados nivel 1 y 2.

## Qué NO hizo la IA:
- **La selección teórica de variables socioeconómicas** (navegación manual por CONEVAL, SEP e INEGI).
- **El descubrimiento sistemático:** La hipótesis fundamental y comprobación de que el "ODS 1 provoca el fracaso del ODS 4, lo que estanca a los jóvenes en el fracaso del ODS 8" fue concebida, investigada y demostrada enteramente por mí.
- **La redacción de los paneles laterales y conclusión:** Todo el texto crítico y periodístico de mi tablero es completamente manual. La IA nunca escribió mi guion ni mi conclusión de la historia sobre "la lotería del código postal".
