# 📊 Dashboard de Candidatos - Power BI

> Dashboard interactivo profesional para análisis avanzado de candidatos y optimización de tasas de colocación

![Dashboard Preview](1.png)

## � **[VER DASHBOARD EN VIVO](https://anverpy.github.io/powerbi-candidatos/dashboard.html)** 
*👆 Haz clic para acceder al dashboard interactivo desde cualquier navegador*

## �🎯 Objetivo

Transformar datos de reclutamiento en insights accionables para mejorar la eficiencia del proceso de colocación de candidatos tecnológicos.

## 📈 Vista General del Dashboard

El dashboard proporciona una visión integral del pipeline de candidatos con métricas clave de rendimiento y análisis predictivo.

## 🔍 Dataset

### Características de los Datos
- **📊 Total de Registros**: 527 candidatos únicos
- **📅 Período de Análisis**: Enero - Septiembre 2025
- **🎯 Cobertura**: Proceso completo de reclutamiento
- **⚡ Actualización**: Datos generados sintéticamente para demo

### Dimensiones Analizadas
| Dimensión | Valores | Descripción |
|-----------|---------|-------------|
| 💻 **Tecnologías** | Power BI, Azure, Java, Python, React, C#, SQL | Stack tecnológico demandado |
| 🎖️ **Niveles** | Junior, Mid, Senior | Experiencia del candidato |
| 🌐 **Fuentes** | LinkedIn, Portal Empleo, Referral, Web Corp | Canal de reclutamiento |
| 👨‍💼 **Consultores** | María, Luis, Ana, Jorge | Responsable de seguimiento |

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
# Python 3.7+
pip install pandas datetime
```

### Ejecución
```bash
# Generar dataset
python gen_data.py

# Output: candidatos.csv listo para Power BI
```

## 📊 KPIs y Métricas Clave

### 🎯 Indicadores Principales
- **Tasa de Colocación Global**: % de candidatos exitosamente colocados
- **Tiempo Promedio de Colocación**: Días desde CV hasta colocación
- **Performance por Consultor**: Ranking de efectividad
- **ROI por Fuente**: Retorno de inversión por canal
- **Análisis de Tecnologías**: Demanda vs. disponibilidad

### 📐 Medidas DAX Implementadas

#### Tasa de Colocación
```dax
% Tasa Colocación = 
VAR _Total = [Total Candidatos]
VAR _Colocados = [Candidatos Colocados]
RETURN
    DIVIDE(_Colocados, _Total, 0)
```

#### Tiempo Promedio Colocación
```dax
Tiempo Promedio Colocación = 
AVERAGEX(
    FILTER(candidatos, candidatos[Estado] = "Colocado"),
    DATEDIFF(candidatos[Fecha_CV_Recibido], candidatos[Fecha_Colocacion], DAY)
)
```

#### Performance por Consultor
```dax
Ranking Consultor = 
RANKX(
    ALL(candidatos[Consultor]), 
    [% Tasa Colocación],
    ,DESC
)
```

## 🏗️ Arquitectura del Dashboard

### 📋 Estructura de Páginas
1. **🏠 Overview Dashboard**
   - KPIs ejecutivos
   - Tendencias temporales
   - Alertas y semáforos

2. **👥 Performance Consultores**
   - Ranking individual
   - Métricas comparativas
   - Goals vs. Actual

3. **💻 Análisis Tecnologías**
   - Demanda por skill
   - Tiempo colocación por tech
   - Proyecciones

4. **🌐 Fuentes de Reclutamiento**
   - ROI por canal
   - Volumen vs. calidad
   - Optimización de canales

5. **📅 Análisis Temporal**
   - Estacionalidad
   - Tendencias mensuales
   - Forecasting

### 🎨 Elementos Visuales
- **Cards dinámicas** con KPIs principales
- **Gráficos de líneas** para tendencias temporales
- **Matrices** para análisis multidimensional
- **Donut charts** para distribuciones
- **Gauges** para targets vs. actual
- **Mapas de calor** para correlaciones

## 🔧 Configuración Avanzada

### Relaciones del Modelo
```
Candidatos (1) ←→ (*) Calendario
Candidatos (1) ←→ (*) Tecnologías
Candidatos (1) ←→ (*) Consultores
```

### Segmentadores Recomendados
- 📅 Selector de fechas (rango)
- 💻 Multi-selector de tecnologías
- 👨‍💼 Filtro de consultores
- 🌐 Selector de fuentes

## 📱 Responsive Design

El dashboard está optimizado para:
- 🖥️ **Desktop**: Vista completa con drill-down
- 📱 **Mobile**: Cards principales y KPIs esenciales
- 📊 **Tablet**: Vista intermedia con navegación táctil

## 🔮 Roadmap

### Próximas Funcionalidades
- [ ] **Machine Learning**: Predicción de tiempo de colocación
- [ ] **Integración API**: Conexión directa con ATS
- [ ] **Alertas automáticas**: Notificaciones de anomalías
- [ ] **Benchmarking**: Comparación con estándares industria

## 🤝 Contribución

¿Mejoras o sugerencias? ¡Son bienvenidas!

1. Fork del proyecto
2. Crea tu feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub**

*Desarrollado con ❤️ para optimizar procesos de reclutamiento tecnológico*