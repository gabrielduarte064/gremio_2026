from dados import (
    JOGOS, JOGOS_CRONOLOGICOS, TABELA_GERAL, TABELA_GERAL_POS_GREMIO,
    PRIMEIRO_TIME_FORA_Z4, CAMPANHA_GERAL_2026, ARTILHEIROS_GERAL,
    ASSISTENCIAS_GERAL, ARTILHEIRO_BRASILEIRAO_GREMIO, DESTAQUE_RODADA_28,
)


def _pontos(v, e, d):
    return v * 3 + e * 1


def resumo_turno(turno_num):
    """Resumo estatístico (V/E/D, gols, aproveitamento) de um turno específico (1 ou 2)."""
    jogos = [j for j in JOGOS if j["turno"] == turno_num]
    v = sum(1 for j in jogos if j["resultado"] == "V")
    e = sum(1 for j in jogos if j["resultado"] == "E")
    d = sum(1 for j in jogos if j["resultado"] == "D")
    gf = sum(j["gf"] for j in jogos)
    ga = sum(j["ga"] for j in jogos)
    pts = _pontos(v, e, d)
    jogos_total = len(jogos)
    aproveitamento = round((pts / (jogos_total * 3)) * 100, 1) if jogos_total else 0
    return {
        "turno": turno_num,
        "jogos": jogos_total,
        "vitorias": v, "empates": e, "derrotas": d,
        "gf": gf, "ga": ga, "sg": gf - ga,
        "pontos": pts,
        "aproveitamento": aproveitamento,
        "media_gols_marcados": round(gf / jogos_total, 2) if jogos_total else 0,
        "media_gols_sofridos": round(ga / jogos_total, 2) if jogos_total else 0,
    }


def resumo_mandante_visitante():
    """Compara desempenho jogando em casa x fora, considerando todos os 28 jogos."""
    casa = [j for j in JOGOS if j["mandante"]]
    fora = [j for j in JOGOS if not j["mandante"]]

    def _sumario(lista):
        v = sum(1 for j in lista if j["resultado"] == "V")
        e = sum(1 for j in lista if j["resultado"] == "E")
        d = sum(1 for j in lista if j["resultado"] == "D")
        gf = sum(j["gf"] for j in lista)
        ga = sum(j["ga"] for j in lista)
        jogos_total = len(lista)
        pts = _pontos(v, e, d)
        aproveitamento = round((pts / (jogos_total * 3)) * 100, 1) if jogos_total else 0
        return {
            "jogos": jogos_total, "vitorias": v, "empates": e, "derrotas": d,
            "gf": gf, "ga": ga, "sg": gf - ga, "pontos": pts,
            "aproveitamento": aproveitamento,
        }

    return {"casa": _sumario(casa), "fora": _sumario(fora)}


def forma_recente(n=5):
    """Retorna os últimos N resultados em ordem cronológica (mais recente por último)."""
    ultimos = JOGOS_CRONOLOGICOS[-n:]
    return [
        {
            "rodada": j["rodada"], "data": j["data"], "adversario": j["adversario"],
            "mandante": j["mandante"], "gf": j["gf"], "ga": j["ga"],
            "resultado": j["resultado"],
        }
        for j in ultimos
    ]


def sequencia_atual():
    """Detecta a sequência atual (quantos jogos seguidos sem vencer, invicto, etc.)."""
    cronologicos_invertido = list(reversed(JOGOS_CRONOLOGICOS))
    sem_vencer = 0
    for j in cronologicos_invertido:
        if j["resultado"] == "V":
            break
        sem_vencer += 1

    invicto = 0
    for j in cronologicos_invertido:
        if j["resultado"] == "D":
            break
        invicto += 1

    return {"jogos_sem_vencer": sem_vencer, "jogos_invicto": invicto}


def maiores_goleadas():
    """Retorna as maiores vitórias e derrotas em saldo de gols."""
    vitorias = sorted(
        [j for j in JOGOS if j["resultado"] == "V"],
        key=lambda j: (j["gf"] - j["ga"]), reverse=True,
    )
    derrotas = sorted(
        [j for j in JOGOS if j["resultado"] == "D"],
        key=lambda j: (j["ga"] - j["gf"]), reverse=True,
    )
    return {
        "maior_vitoria": vitorias[0] if vitorias else None,
        "maior_derrota": derrotas[0] if derrotas else None,
    }


def comparativo_turnos():
    """Compara 1º x 2º turno lado a lado, incluindo variação percentual de aproveitamento."""
    t1 = resumo_turno(1)
    t2 = resumo_turno(2)
    variacao_aproveitamento = round(t2["aproveitamento"] - t1["aproveitamento"], 1)
    variacao_gols_marcados = round(t2["media_gols_marcados"] - t1["media_gols_marcados"], 2)
    variacao_gols_sofridos = round(t2["media_gols_sofridos"] - t1["media_gols_sofridos"], 2)
    return {
        "turno_1": t1,
        "turno_2": t2,
        "variacao_aproveitamento": variacao_aproveitamento,
        "variacao_gols_marcados": variacao_gols_marcados,
        "variacao_gols_sofridos": variacao_gols_sofridos,
        "melhorou": variacao_aproveitamento > 0,
    }


def situacao_rebaixamento():
    """Distância do Grêmio para a zona segura (1º time fora do Z-4)."""
    diff = PRIMEIRO_TIME_FORA_Z4["pontos"] - TABELA_GERAL["pontos"]
    return {
        "posicao_atual": TABELA_GERAL_POS_GREMIO,
        "pontos_gremio": TABELA_GERAL["pontos"],
        "referencia": PRIMEIRO_TIME_FORA_Z4["time"],
        "pontos_referencia": PRIMEIRO_TIME_FORA_Z4["pontos"],
        "distancia_pontos": diff,
        "jogos_restantes": 38 - TABELA_GERAL["jogos"],
    }


def gerar_todos_insights():
    """Agrega todos os cálculos num único dicionário para consumo do html_builder."""
    return {
        "tabela_geral": TABELA_GERAL,
        "posicao": TABELA_GERAL_POS_GREMIO,
        "campanha_geral_2026": CAMPANHA_GERAL_2026,
        "turno_1": resumo_turno(1),
        "turno_2": resumo_turno(2),
        "comparativo_turnos": comparativo_turnos(),
        "mandante_visitante": resumo_mandante_visitante(),
        "forma_recente": forma_recente(5),
        "sequencia_atual": sequencia_atual(),
        "goleadas": maiores_goleadas(),
        "rebaixamento": situacao_rebaixamento(),
        "artilheiros_geral": ARTILHEIROS_GERAL,
        "assistencias_geral": ASSISTENCIAS_GERAL,
        "artilheiro_brasileirao": ARTILHEIRO_BRASILEIRAO_GREMIO,
        "destaque_rodada_28": DESTAQUE_RODADA_28,
        "jogos_cronologicos": JOGOS_CRONOLOGICOS,
        "jogos_turno_1": [j for j in JOGOS if j["turno"] == 1],
        "jogos_turno_2": [j for j in JOGOS if j["turno"] == 2],
    }


if __name__ == "__main__":
    import json
    print(json.dumps(gerar_todos_insights(), indent=2, ensure_ascii=False))
