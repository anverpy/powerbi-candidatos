# Dashboard de Candidatos - Power BI

## Descripción
Dashboard interactivo para análisis de candidatos y tasas de colocación.

## Datos
- 527 candidatos generados
- Período: Enero-Septiembre 2025
- Tecnologías: Power BI, Azure, Java, Python, React, C#, SQL

## Archivos
- `gen_data.py`: Script generador de datos
- `candidatos.csv`: Dataset de candidatos
- Dashboard Power BI con análisis de KPIs

## Ejecutar
```bash
python gen_data.py
```

## KPIs Principales
- % Tasa de Colocación
- Tiempo Promedio de Colocación
- Performance por Consultor
- Análisis por Tecnología

## Medidas DAX Implementadas
```dax
% Tasa Colocación = 
VAR _Total = [Total Candidatos]
VAR _Colocados = [Candidatos Colocados]
RETURN
    DIVIDE(_Colocados, _Total, 0)
```

## Estructura del Dashboard
1. **Overview**: KPIs generales y tendencias
2. **Performance Consultores**: Análisis individual
3. **Análisis Tecnologías**: ¿Cuáles colocan mejor?
4. **Fuentes de Reclutamiento**: ROI por canal
5. **Detalle Temporal**: Análisis de estacionalidad