from datetime import datetime, timedelta
import pandas as pd
import random

# Semilla para reproducibilidad
random.seed(42)

# Generar tabla de candidatos
candidatos = []
tecnologias = ["Power BI", "Azure", "Java", "Python", "React", "C#", "SQL"]
niveles = ["Junior", "Mid", "Senior"]
fuentes = ["LinkedIn", "Portal Empleo", "Referral", "Web Corporativa"]
consultores = ["María", "Luis", "Ana", "Jorge"]

for i in range(1, 528):
    fecha_cv = datetime(2025, random.randint(1, 9), random.randint(1, 28))
    colocado = random.choice([True, False])
    fecha_colocacion = fecha_cv + timedelta(days=random.randint(5, 45)) if colocado else None
    candidatos.append({
        "ID_Candidato": f"CAND_{i:03}",
        "Fecha_CV_Recibido": fecha_cv.date(),
        "Fecha_Colocacion": fecha_colocacion.date() if fecha_colocacion else None,
        "Tecnologia": random.choice(tecnologias),
        "Nivel": random.choice(niveles),
        "Fuente": random.choice(fuentes),
        "Consultor": random.choice(consultores),
        "Estado": "Colocado" if colocado else "En espera"
    })

df_candidatos = pd.DataFrame(candidatos)

# Guardar como CSV para importar en Power BI
df_candidatos.to_csv("candidatos.csv", index=False)
