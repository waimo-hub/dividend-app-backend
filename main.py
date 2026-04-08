from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PlanInput(BaseModel):
    objetivo_mensual: float
    capital_inicial: float
    aporte_mensual: float
    yield_anual: float = 0.04

@app.post("/calcular")
def calcular_plan(data: PlanInput):
    capital = data.capital_inicial
    mes = 0

    while True:
        dividendos = capital * data.yield_anual / 12

        if dividendos >= data.objetivo_mensual:
            return {
                "meses": mes,
                "años": round(mes / 12, 1),
                "capital_final": round(capital, 2),
                "ingreso_mensual": round(dividendos, 2)
            }

        capital += data.aporte_mensual + dividendos
        mes += 1