"""Simulación Monte Carlo de la economía del MVP (Mapa B, Sedes 1-3).

Uso: python3 tools/balance/economia_mvp.py [--runs N] [--seed S]

Modela jornadas de 100 UT con lecturas de Carta Única y Tres Tiempos, y mide
cuántas jornadas tarda un jugador (novato, medio, experto) en mudarse de sede y
cuántas veces cae en el hilo del Usurero. Los valores salen de
design/balance/economia-mvp.md; si cambian allí, cambian aquí.
"""

import argparse
import random
import statistics

UT_JORNADA = 100
UT_PREGUNTA = 5
UT_TIRADA = {"unica": 10, "tres": 20}

# Por sede: tarifa base, costos fijos diarios, mudanza a la siguiente,
# requisitos de Fama y Reputación para mudarse, arquetipos presentes (peso).
SEDES = {
    1: dict(tarifa=4, renta=5, peaje=2, vela=2, mudanza=100, fama_req=20, rep_req=0.30,
            pob={"vagabundo": 5, "estibador": 3, "apostador": 2}),
    2: dict(tarifa=10, renta=18, peaje=6, vela=4, mudanza=350, fama_req=45, rep_req=0.45,
            pob={"estibador": 3, "apostador": 4, "viuda": 2, "detective": 1}),
    3: dict(tarifa=25, renta=45, peaje=15, vela=8, mudanza=None, fama_req=None, rep_req=None,
            pob={"viuda": 4, "detective": 3, "apostador": 2, "estibador": 1}),
}

# Factor de estatus (multiplica la tarifa de la sede), K de propina y botín del Doble Fondo.
ARQUETIPOS = {
    "vagabundo": dict(estatus=0.5, k_propina=0.2, botin=(25, 40)),
    "estibador": dict(estatus=1.0, k_propina=0.5, botin=(0, 0)),     # salvoconducto sindical
    "apostador": dict(estatus=0.8, k_propina=0.8, botin=(0, 0)),     # dossier VIP
    "viuda": dict(estatus=1.5, k_propina=1.8, botin=(60, 100)),
    "detective": dict(estatus=1.2, k_propina=0.5, botin=(0, 0)),     # inmunidad
}

P_DOBLE_FONDO = 0.30
M_DF = (2.5, 4.0)

# Perfiles de jugador: probabilidad de acertar la lectura, de detectar el Doble
# Fondo cuando existe, de elegir Tres Tiempos en vez de Carta Única, preguntas por
# sesión y calidad (cuánto paga una lectura exitosa según su Resonancia).
PERFILES = {
    "novato": dict(p_exito=0.45, p_detecta_df=0.20, p_tres=0.5, preguntas=2, calidad=0.9),
    "medio": dict(p_exito=0.60, p_detecta_df=0.40, p_tres=0.6, preguntas=2, calidad=1.0),
    "experto": dict(p_exito=0.75, p_detecta_df=0.60, p_tres=0.7, preguntas=3, calidad=1.3),
}

# Reparto de intenciones al acertar: (multiplicador, peso).
INTENCIONES = {"consolar": (1.0, 5), "acusar": (3.0, 2), "paranoia": (2.0, 2), "extorsionar": (5.0, 1)}
M_FALLO = 0.2
CREDULIDAD_EXITO = 60   # Credulidad final típica tras una lectura exitosa
BONO_TRES = 0.15        # Tres Tiempos suma probabilidad de acierto frente a Carta Única

FAMA_POR_CLIENTE = 1
FAMA_POR_EXITO = 2
VENTANA_REPUTACION = 10
DIAS_MAX = 120


def elegir(pesos, rng):
    claves = list(pesos)
    return rng.choices(claves, weights=[pesos[k] for k in claves])[0]


def sesion(sede, perfil, rng):
    """Devuelve (ut, ingreso, exito)."""
    s, p = SEDES[sede], PERFILES[perfil]
    arq = ARQUETIPOS[elegir(s["pob"], rng)]
    tirada = "tres" if rng.random() < p["p_tres"] else "unica"
    ut = p["preguntas"] * UT_PREGUNTA + UT_TIRADA[tirada]
    t_base = s["tarifa"] * arq["estatus"]
    p_exito = min(0.95, p["p_exito"] + (BONO_TRES if tirada == "tres" else 0))
    if rng.random() >= p_exito:
        return ut, t_base * M_FALLO, False
    mult = INTENCIONES[elegir({k: v[1] for k, v in INTENCIONES.items()}, rng)][0]
    ingreso = (t_base * mult + t_base * CREDULIDAD_EXITO / 100 * arq["k_propina"]) * p["calidad"]
    if rng.random() < P_DOBLE_FONDO and rng.random() < p["p_detecta_df"]:
        ingreso = ingreso * rng.uniform(*M_DF) + rng.uniform(*arq["botin"])
    return ut, ingreso, True


def partida(perfil, rng):
    sede, saldo, fama, historial = 1, 0.0, 0, []
    dias_por_sede, dia_entrada, usurero = {}, 0, 0
    for dia in range(1, DIAS_MAX + 1):
        ut = UT_JORNADA
        while ut >= UT_PREGUNTA * 2 + UT_TIRADA["unica"]:
            gasto, ingreso, exito = sesion(sede, perfil, rng)
            if gasto > ut:
                break
            ut -= gasto
            saldo += ingreso
            fama += FAMA_POR_CLIENTE + (FAMA_POR_EXITO if exito else 0)
            historial = (historial + [exito])[-VENTANA_REPUTACION:]
        s = SEDES[sede]
        saldo -= s["renta"] + s["peaje"] + s["vela"]
        if saldo < 0:
            usurero += 1
        rep = sum(historial) / len(historial) if historial else 0
        if s["mudanza"] and saldo >= s["mudanza"] and fama >= s["fama_req"] and rep >= s["rep_req"]:
            saldo -= s["mudanza"]
            dias_por_sede[sede] = dia - dia_entrada
            dia_entrada, sede = dia, sede + 1
        if sede == 3 and 3 not in dias_por_sede:
            dias_por_sede[3] = None
            return dias_por_sede, usurero, dia
    return dias_por_sede, usurero, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    print(f"{'perfil':<8} {'días S1':>8} {'días S2':>8} {'día llega S3':>13} {'días en negativo':>17} {'no llega':>9}")
    for perfil in PERFILES:
        s1, s2, llegada, neg, fallidas = [], [], [], [], 0
        for _ in range(args.runs):
            dps, usurero, dia = partida(perfil, rng)
            neg.append(usurero)
            if dia is None:
                fallidas += 1
                continue
            s1.append(dps[1]); s2.append(dps[2]); llegada.append(dia)
        med = lambda xs: f"{statistics.median(xs):.0f}" if xs else "-"
        print(f"{perfil:<8} {med(s1):>8} {med(s2):>8} {med(llegada):>13} {statistics.mean(neg):>17.1f} {fallidas / args.runs:>8.0%}")


if __name__ == "__main__":
    main()
