# EmprendeIA_ods 

## Estudiar No Es Suficiente
### La desconexión entre pobreza, educación y empleo digno en México

---

## Equipo

| Nombre | Descripción |
|--------|-------------|
| Alejandro Valentin Saldaña Mendez | Análisis de datos · Visualización |
| Eduardo Francisco Peñaloza Uribe  | Narrativa · Storytelling          |
| Tetsu Nicolas Osnaya Quevedo      | Desarrollo · Dashboard           | 

---

## ODS elegidos

| ODS | Nombre | Relación con el proyecto |
|-----|--------|--------------------------|
| **ODS 1** | Sin Pobreza | La pobreza extrema como barrera estructural que determina la escolaridad |
| **ODS 4** | Educación de Calidad | El rezago educativo como consecuencia medible de la pobreza |
| **ODS 8** | Trabajo Decente y Crecimiento Económico | La brecha salarial entre ocupaciones como condena para quienes no completan su educación |

---

## Pregunta central

> **¿Por qué en México estudiar más años no garantiza salir de la pobreza ni acceder a un empleo formal?**

Esta pregunta guía todo el tablero: exploramos si la relación Pobreza → Educación → Empleo funciona como se espera, o si hay una desconexión estructural que perpetúa el ciclo.

### Hallazgo analítico clave

Al correlacionar los datos de los 32 estados mexicanos encontramos que:

| Relación | Correlación (r) | p-valor | Interpretación |
|----------|:---:|:---:|---|
| Pobreza extrema vs Escolaridad promedio | **−0.82** | < 0.001 | **Muy fuerte**: a mayor pobreza extrema, menor escolaridad |
| Rezago educativo vs Escolaridad promedio | **−0.94** | < 0.001 | **Casi perfecta**: el rezago educativo medido por CONEVAL predice la escolaridad estatal |
| Pobreza vs Abandono Media Superior | −0.15 | 0.42 | **Nula**: el abandono escolar NO correlaciona con pobreza a nivel estatal |

Este descubrimiento nos obligó a pivotar: en lugar de medir el abandono escolar (variable confundida por el mercado laboral urbano), medimos la **escolaridad promedio** como indicador del daño acumulado que la pobreza causa en la educación. La brecha entre Chiapas (7.78 años) y Nuevo León (10.74 años) — casi **3 años de escolaridad** — es la evidencia central del tablero.

### Coherencia narrativa

El relato está estructurado como la historia de **Luis**, un joven mexicano cuya trayectoria de vida ilustra el ciclo sistémico. Está dividido en 3 Actos:

1. **Acto I — "Donde naciste ya decidió tu futuro" (ODS 1):** La pobreza como lotería geográfica. Mapa coroplético y comparativa de extremos.
2. **Acto II — "El puente que se rompe" (ODS 4):** Cómo la pobreza extrema predice la escolaridad (r = −0.82). Scatter plot con trendline y datos de UNICEF.
3. **Acto III — "Bienvenido al piso de abajo" (ODS 8):** La condena salarial: $40/hr en ocupaciones elementales vs $117/hr para directivos. El ciclo se reinicia.

### Potencial de impacto

Este tablero demuestra con datos tridimensionales que la pobreza extrema, el rezago educativo y la precarización laboral forman un ciclo que se auto-reproduce. Funciona como herramienta de divulgación para visibilizar ante formuladores de políticas públicas por qué las becas escolares por sí solas no solucionan el ciclo sin atacar la pobreza estructural.

---

## Justificación de la selección de datos

Elegimos la ENOE y el CONEVAL porque son las **únicas fuentes estadísticamente fiables** de cobertura nacional estandarizada.

- **Archivo CONEVAL `Concentrado_indicadores_de_pobreza_2020.xlsx`:** Contiene 16 indicadores de pobreza multidimensional por estado (pobreza general, extrema, moderada, rezago educativo, carencias sociales). Nuestro proyecto extrae pobreza, pobreza extrema y rezago educativo — tres dimensiones que no se habían cruzado antes en este formato.
- **ODS 4 — Escolaridad promedio:** Usamos el grado promedio de escolaridad por estado (Censo 2020) como indicador del daño acumulado. Descartamos el abandono escolar de Media Superior tras verificar que no correlaciona con pobreza a nivel estatal (r = −0.15), probablemente por la falacia ecológica y el efecto pull del mercado laboral en estados ricos.
- **ODS 8 — Año 2019:** Optamos por aislar los datos de desocupación al año 2019 porque los registros 2020+ presentaban colapsos estadísticos (NaN) por la paralización laboral COVID-19.

---

## Estructura del repositorio
```
EmprendeIA_ods/
├── datos/
│   ├── geo/         ← GeoJSON de estados de México
│   ├── ods1/        ← Datos CONEVAL de pobreza multidimensional
│   ├── ods4/        ← Datos SEP/INEGI de educación
│   └── ods8/        ← Datos INEGI ENOE de empleo e informalidad
├── scripts/         ← Scripts de limpieza y procesamiento
├── dashboard/       ← Tablero renderizado (HTML)
├── notebooks/       ← Notebook exploratorio
├── Tablero_ods_EmprendeIA.qmd  ← Código fuente del tablero
├── images/          ← Imágenes generadas con IA (fondos de sección)
├── landing.scss     ← Estilos del tablero
├── requirements.txt ← Dependencias de Python
├── License.txt      ← CC BY-SA 4.0
├── ai-log.md        ← Declaratoria de uso de IA (formato HackODS)
└── README.md
```

---

## Metadatos de los datos

### ODS 1 — Pobreza

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `Concentrado_indicadores_de_pobreza_2020.xlsx` | CONEVAL | Abril 2026 | Uso libre con atribución | % pobreza, % pobreza extrema, % rezago educativo por estado (2010, 2015, 2020) |
| `Líneas_de_Pobreza_por_Ingresos_mar2025.xlsx` | CONEVAL | Abril 2026 | Uso libre con atribución | Canasta básica mensual rural/urbano 1992–2025 |
| `1_1_1_a_sh_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | % población bajo $1.90 USD diarios por estado |
| `1_1_1_dc_637_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | Pobreza extrema total/urbano/rural 2018–2020 |

### ODS 4 — Educación

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `Educacion_05.xlsx` | INEGI Censo 2020 | Abril 2026 | Datos abiertos | **Grado promedio de escolaridad** por estado y sexo 2010–2020 |
| `Educacion_11.xlsx` | SEP / INEGI | Abril 2026 | Datos abiertos | Tasa de abandono escolar por nivel y estado 2000–2024 |
| `4_1_2_dc_1823_es.csv` | INEGI / Agenda 2030 | Abril 2026 | Datos abiertos | Índice de finalización primaria/secundaria/prepa por estado |
| `Educacion_03.xlsx` | INEGI | Abril 2026 | Datos abiertos | Asistencia escolar por estado 2020 |

### ODS 8 — Empleo

| Dataset | Fuente | Fecha descarga | Licencia | Variables clave |
|---------|--------|---------------|----------|-----------------|
| `8_5_1c_sh_es.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | **Ingreso medio por hora** por tipo de ocupación 2016–2024 |
| `8_5_2_2__sh_es.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de desocupación por estado, sexo y edad 1995–2020 |
| `Tabulado.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de informalidad trimestral 2022–2025 |
| `Tabulado__1_.csv` | INEGI ENOE | Abril 2026 | Datos abiertos | Tasa de desocupación mensual por sexo 2024–2026 |

---

## Fuentes oficiales y académicas

### Fuentes de datos
- CONEVAL: https://www.coneval.org.mx
- INEGI ENOE: https://www.inegi.org.mx/programas/enoe/15ymas/
- SEP: https://www.sep.gob.mx
- Agenda 2030 México: https://agenda2030.mx
- ONU ODS: https://unstats.un.org/sdgs/

### Fuentes citadas en el tablero
- CONEVAL, *Medición Multidimensional de la Pobreza 2020 y 2022*
- OCDE, *Economic Survey México 2026* — informalidad laboral al 56%
- UNICEF, *Country Office Annual Report México 2023* — solo 56 de 100 niños completan Media Superior
- El Colegio Mexiquense, *"Distribución espacial de la pobreza y rezago educativo en México"*, Economía, Sociedad y Territorio
- World Bank / UNICEF, *The State of Global Learning Poverty 2022*

---

## Cómo ejecutar el tablero

El tablero interactivo ya está renderizado en `dashboard/`. Para abrirlo directamente:

```bash
# Abrir el tablero renderizado (no requiere instalación)
open dashboard/Tablero_ods_EmprendeIA.html
```

Para renderizar desde la fuente:

```bash
# 1. Instalar dependencias de Python
pip install -r requirements.txt

# 2. Instalar Quarto CLI (https://quarto.org/docs/get-started/)
# 3. Renderizar
quarto render Tablero_ods_EmprendeIA.qmd
```

**Requisitos:** Python >= 3.10 · Quarto CLI · Dependencias en `requirements.txt`
