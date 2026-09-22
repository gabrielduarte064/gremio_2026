import json
import os

_DIR = os.path.dirname(os.path.abspath(__file__))
_ARQ_JOGOS_JSON = os.path.join(_DIR, "dados_jogos.json")
_ARQ_TABELA_JSON = os.path.join(_DIR, "dados_tabela.json")


# JOGOS DO GRÊMIO NO BRASILEIRÃO 2026 (Rodadas 1 a 28)

JOGOS = [
    # ---- 1º TURNO (Rodadas 1-19) ----
    {"rodada": 1,  "data": "28/01/2026", "mandante": False, "adversario": "Fluminense",         "gf": 1, "ga": 2, "turno": 1},
    {"rodada": 2,  "data": "04/02/2026", "mandante": True,  "adversario": "Botafogo",            "gf": 5, "ga": 3, "turno": 1},
    {"rodada": 3,  "data": "11/02/2026", "mandante": False, "adversario": "São Paulo",           "gf": 0, "ga": 2, "turno": 1},
    {"rodada": 4,  "data": "25/02/2026", "mandante": True,  "adversario": "Atlético-MG",         "gf": 2, "ga": 1, "turno": 1},
    {"rodada": 5,  "data": "12/03/2026", "mandante": True,  "adversario": "Red Bull Bragantino",  "gf": 1, "ga": 1, "turno": 1},
    {"rodada": 6,  "data": "16/03/2026", "mandante": False, "adversario": "Chapecoense",         "gf": 1, "ga": 1, "turno": 1},
    {"rodada": 7,  "data": "19/03/2026", "mandante": True,  "adversario": "Vitória",             "gf": 2, "ga": 0, "turno": 1},
    {"rodada": 8,  "data": "22/03/2026", "mandante": False, "adversario": "Vasco da Gama",       "gf": 1, "ga": 2, "turno": 1},
    {"rodada": 9,  "data": "02/04/2026", "mandante": False, "adversario": "Palmeiras",           "gf": 1, "ga": 2, "turno": 1},
    {"rodada": 10, "data": "05/04/2026", "mandante": True,  "adversario": "Remo",                "gf": 0, "ga": 0, "turno": 1},
    {"rodada": 11, "data": "11/04/2026", "mandante": False, "adversario": "Internacional",       "gf": 0, "ga": 0, "turno": 1},
    {"rodada": 12, "data": "18/04/2026", "mandante": False, "adversario": "Cruzeiro",            "gf": 0, "ga": 2, "turno": 1},
    {"rodada": 13, "data": "26/04/2026", "mandante": True,  "adversario": "Coritiba",            "gf": 1, "ga": 0, "turno": 1},
    {"rodada": 14, "data": "02/05/2026", "mandante": False, "adversario": "Athletico-PR",        "gf": 0, "ga": 0, "turno": 1},
    {"rodada": 15, "data": "10/05/2026", "mandante": True,  "adversario": "Flamengo",            "gf": 0, "ga": 1, "turno": 1},
    {"rodada": 16, "data": "17/05/2026", "mandante": False, "adversario": "Bahia",               "gf": 1, "ga": 1, "turno": 1},
    {"rodada": 17, "data": "23/05/2026", "mandante": True,  "adversario": "Santos",              "gf": 3, "ga": 2, "turno": 1},
    {"rodada": 18, "data": "30/05/2026", "mandante": True,  "adversario": "Corinthians",         "gf": 1, "ga": 3, "turno": 1},
    {"rodada": 19, "data": "17/07/2026", "mandante": False, "adversario": "Mirassol",            "gf": 1, "ga": 2, "turno": 1},

    # ---- 2º TURNO (Rodadas 20-28, até 20/09/2026) ----
    {"rodada": 20, "data": "26/07/2026", "mandante": True,  "adversario": "Fluminense",          "gf": 1, "ga": 1, "turno": 2},
    {"rodada": 22, "data": "08/08/2026", "mandante": True,  "adversario": "São Paulo",           "gf": 2, "ga": 1, "turno": 2},
    {"rodada": 23, "data": "16/08/2026", "mandante": False, "adversario": "Atlético-MG",         "gf": 0, "ga": 3, "turno": 2},
    {"rodada": 24, "data": "23/08/2026", "mandante": False, "adversario": "Red Bull Bragantino",  "gf": 0, "ga": 1, "turno": 2},
    {"rodada": 25, "data": "30/08/2026", "mandante": True,  "adversario": "Chapecoense",         "gf": 3, "ga": 1, "turno": 2},
    {"rodada": 26, "data": "07/09/2026", "mandante": False, "adversario": "Vitória",             "gf": 0, "ga": 1, "turno": 2},
    {"rodada": 27, "data": "12/09/2026", "mandante": True,  "adversario": "Vasco da Gama",       "gf": 1, "ga": 2, "turno": 2},
    {"rodada": 21, "data": "16/09/2026", "mandante": False, "adversario": "Botafogo",            "gf": 2, "ga": 3, "turno": 2},  # partida remarcada
    {"rodada": 28, "data": "20/09/2026", "mandante": True,  "adversario": "Palmeiras",           "gf": 0, "ga": 0, "turno": 2},
]


def resultado(jogo):
    """Retorna 'V', 'E' ou 'D' do ponto de vista do Grêmio."""
    if jogo["gf"] > jogo["ga"]:
        return "V"
    if jogo["gf"] == jogo["ga"]:
        return "E"
    return "D"


# Preenche o campo resultado em cada jogo (só necessário para a lista manual;
# os jogos vindos do JSON da API já chegam com o campo "resultado" pronto)
for _j in JOGOS:
    _j["resultado"] = resultado(_j)


# CARREGA JOGOS ATUALIZADOS VIA API (se "atualizar_dados.py" já foi rodado)

if os.path.exists(_ARQ_JOGOS_JSON):
    with open(_ARQ_JOGOS_JSON, encoding="utf-8") as _f:
        JOGOS = json.load(_f)
    print(f"[dados.py] Usando jogos atualizados via API ({len(JOGOS)} jogos) -> {os.path.basename(_ARQ_JOGOS_JSON)}")
else:
    print("[dados.py] Usando snapshot manual (até 20/09/2026). Rode 'python atualizar_dados.py' para buscar dados novos via API.")

# Ordena por data cronológica real (útil para "jogo a jogo" e sequência/forma)
JOGOS_CRONOLOGICOS = sorted(
    JOGOS,
    key=lambda j: tuple(reversed(j["data"].split("/")))  # AAAA-MM-DD para ordenar
)

# TABELA GERAL DO BRASILEIRÃO 2026 — 28ª RODADA (atualizada em 20/09/2026)
# Fonte: aquiesportes.com.br / ESPN
TABELA_GERAL_POS_GREMIO = 17
TABELA_GERAL = {
    "pontos": 29, "jogos": 28, "vitorias": 7, "empates": 8, "derrotas": 13,
    "gp": 30, "gc": 38, "sg": -8, "aproveitamento": 35,
}
PRIMEIRO_TIME_FORA_Z4 = {"time": "Vasco da Gama", "pontos": 31}

# CARREGA TABELA ATUALIZADA VIA API (se "atualizar_dados.py" já foi rodado)
if os.path.exists(_ARQ_TABELA_JSON):
    with open(_ARQ_TABELA_JSON, encoding="utf-8") as _f:
        _tabela_api = json.load(_f)
    TABELA_GERAL_POS_GREMIO = _tabela_api["posicao"]
    TABELA_GERAL = {
        "pontos": _tabela_api["pontos"], "jogos": _tabela_api["jogos"],
        "vitorias": _tabela_api["vitorias"], "empates": _tabela_api["empates"],
        "derrotas": _tabela_api["derrotas"], "gp": _tabela_api["gp"],
        "gc": _tabela_api["gc"], "sg": _tabela_api["sg"],
        "aproveitamento": _tabela_api["aproveitamento"],
    }
    if _tabela_api.get("primeiro_fora_z4"):
        PRIMEIRO_TIME_FORA_Z4 = {
            "time": _tabela_api["primeiro_fora_z4"]["time"],
            "pontos": _tabela_api["primeiro_fora_z4"]["pontos"],
        }
    print(f"[dados.py] Usando tabela/classificação atualizada via API -> {os.path.basename(_ARQ_TABELA_JSON)}")

# CAMPANHA GERAL 2026 (todas as competições) — ge.globo, atualizado 20/09/2026
CAMPANHA_GERAL_2026 = {
    "jogos": 53, "vitorias": 19, "empates": 16, "derrotas": 18,
    "gp": 71, "gc": 56, "aproveitamento": 45.9,
    "competicoes": {
        "Gauchão": "Campeão 2026",
        "Copa do Brasil": "Semifinal (em andamento)",
        "Brasileirão": "Em andamento",
        "Sul-Americana": "Eliminado no playoff (Bolívar)",
    },
}

# ARTILHARIA E ASSISTÊNCIAS — Grêmio, todas as competições 2026 (ge.globo)
ARTILHEIROS_GERAL = [
    {"jogador": "Carlos Vinícius", "gols": 20},
    {"jogador": "Amuzu",           "gols": 8},
    {"jogador": "Braithwaite",     "gols": 4},
    {"jogador": "Tetê",            "gols": 4},
    {"jogador": "Pavón",           "gols": 4},
    {"jogador": "Gustavo Martins", "gols": 4},
    {"jogador": "Gabriel Mec",     "gols": 3},
    {"jogador": "Edenilson",       "gols": 3},
]

ASSISTENCIAS_GERAL = [
    {"jogador": "Amuzu",           "assistencias": 6},
    {"jogador": "Enamorado",       "assistencias": 4},
    {"jogador": "Pavón",           "assistencias": 4},
    {"jogador": "Noriega",         "assistencias": 3},
    {"jogador": "Tetê",            "assistencias": 3},
]

# Artilheiro do Grêmio só no Brasileirão (ge.globo — ranking geral da competição)
ARTILHEIRO_BRASILEIRAO_GREMIO = {"jogador": "Carlos Vinícius", "gols": 10, "posicao_ranking_geral": 4}

# DESTAQUE DA RODADA 28 — Grêmio 0x0 Palmeiras (20/09/2026)
# Estreia de Renato Gaúcho (5ª passagem) no comando técnico
DESTAQUE_RODADA_28 = {
    "resultado": "Grêmio 0 x 0 Palmeiras",
    "local": "Arena do Grêmio, Porto Alegre",
    "publico_destaque": "mais de 50 mil presentes",
    "homem_do_jogo": "Weverton (Grêmio) — 3 defesas decisivas, inclusive nos acréscimos",
    "treinador_estreante": "Renato Gaúcho (5ª passagem como técnico do Grêmio)",
    "estrategia": "Postura mais cautelosa, priorizando contra-ataques e organização defensiva",
    "posse_de_bola": {"Grêmio": 28, "Palmeiras": 72},
    "finalizacoes": {"Grêmio": 7, "Palmeiras": 31},
    "gols_esperados_xg": {"Grêmio": 0.92, "Palmeiras": 2.49},
    "contexto_tabela": "Grêmio segue na 17ª posição (Z-4), 2 pontos atrás do Vasco (1º fora do rebaixamento)",
}
