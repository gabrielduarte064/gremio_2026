import os
import json
import requests

FOOTBALL_DATA_KEY = os.environ.get("FOOTBALL_DATA_KEY", "")
FOOTBALL_DATA_URL = "https://api.football-data.org/v4"
BRASILEIRAO_ID = "BSA"
NOME_GREMIO = "Grêmio"  # usado para reconhecer o time nas respostas da API

HEADERS = {"X-Auth-Token": FOOTBALL_DATA_KEY}

ARQ_JOGOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_jogos.json")
ARQ_TABELA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados_tabela.json")


# FUNÇÕES DE APOIO

def _get(endpoint, params=None):
    """Faz um GET autenticado na API football-data.org."""
    url = f"{FOOTBALL_DATA_URL}{endpoint}"
    resp = requests.get(url, headers=HEADERS, params=params or {}, timeout=20)
    resp.raise_for_status()
    return resp.json()


def _eh_gremio(nome_time):
    return NOME_GREMIO.lower() in (nome_time or "").lower()


def _resultado(gf, ga):
    if gf > ga:
        return "V"
    if gf == ga:
        return "E"
    return "D"


# BUSCA DE JOGOS

def buscar_jogos():
    print("Buscando partidas do Brasileirão 2026 na API football-data.org ...")
    dados = _get(f"/competitions/{BRASILEIRAO_ID}/matches")
    partidas = dados.get("matches", [])

    jogos = []
    for p in partidas:
        if p.get("status") != "FINISHED":
            continue  # só processa jogos já disputados/encerrados

        home = p["homeTeam"]["name"]
        away = p["awayTeam"]["name"]

        if not (_eh_gremio(home) or _eh_gremio(away)):
            continue  # não é jogo do Grêmio

        mandante = _eh_gremio(home)
        adversario = away if mandante else home
        gf = p["score"]["fullTime"]["home"] if mandante else p["score"]["fullTime"]["away"]
        ga = p["score"]["fullTime"]["away"] if mandante else p["score"]["fullTime"]["home"]
        rodada = p.get("matchday") or 0
        data_iso = (p.get("utcDate") or "")[:10]  # AAAA-MM-DD
        data_br = "/".join(reversed(data_iso.split("-"))) if data_iso else ""
        turno = 1 if rodada <= 19 else 2

        jogos.append({
            "rodada": rodada,
            "data": data_br,
            "mandante": mandante,
            "adversario": adversario,
            "gf": gf,
            "ga": ga,
            "turno": turno,
            "resultado": _resultado(gf, ga),
        })

    jogos.sort(key=lambda j: j["rodada"])
    print(f"  {len(jogos)} jogo(s) do Grêmio encontrados e processados.")
    return jogos


# BUSCA DE TABELA / CLASSIFICAÇÃO

def buscar_tabela():
    print("Buscando classificação atual do Brasileirão ...")
    dados = _get(f"/competitions/{BRASILEIRAO_ID}/standings")
    tabelas = dados.get("standings", [])
    tabela_total = next((t["table"] for t in tabelas if t.get("type") == "TOTAL"), [])

    linha_gremio = next(
        (linha for linha in tabela_total if _eh_gremio(linha["team"]["name"])),
        None,
    )
    if not linha_gremio:
        print("  Aviso: Grêmio não encontrado na tabela retornada pela API.")
        return None

    jogos = linha_gremio["playedGames"]
    pontos = linha_gremio["points"]
    aproveitamento = round((pontos / (jogos * 3)) * 100, 1) if jogos else 0

    resultado = {
        "posicao": linha_gremio["position"],
        "pontos": pontos,
        "jogos": jogos,
        "vitorias": linha_gremio["won"],
        "empates": linha_gremio["draw"],
        "derrotas": linha_gremio["lost"],
        "gp": linha_gremio["goalsFor"],
        "gc": linha_gremio["goalsAgainst"],
        "sg": linha_gremio["goalDifference"],
        "aproveitamento": aproveitamento,
    }

    # Time na posição 17 (1º time fora do Z-4), usado para calcular distância na tabela
    time_z4 = next((l for l in tabela_total if l["position"] == 17), None)
    if time_z4:
        resultado["primeiro_fora_z4"] = {
            "time": time_z4["team"]["name"],
            "pontos": time_z4["points"],
        }

    print(f"  Grêmio em {resultado['posicao']}º lugar, com {resultado['pontos']} pontos.")
    return resultado

# MAIN

def main():
    if not FOOTBALL_DATA_KEY:
        print("ERRO: variável de ambiente FOOTBALL_DATA_KEY não definida.")
        print("Gere uma chave gratuita em https://www.football-data.org/client/register")
        print("e defina a variável antes de rodar este script. Exemplos:")
        print('  Windows (CMD):        set FOOTBALL_DATA_KEY=sua_chave_aqui')
        print('  Windows (PowerShell): $env:FOOTBALL_DATA_KEY="sua_chave_aqui"')
        print('  Linux/Mac:            export FOOTBALL_DATA_KEY="sua_chave_aqui"')
        return

    jogos = buscar_jogos()
    tabela = buscar_tabela()

    with open(ARQ_JOGOS, "w", encoding="utf-8") as f:
        json.dump(jogos, f, ensure_ascii=False, indent=2)
    print(f"Arquivo '{os.path.basename(ARQ_JOGOS)}' atualizado com {len(jogos)} jogos.")

    if tabela:
        with open(ARQ_TABELA, "w", encoding="utf-8") as f:
            json.dump(tabela, f, ensure_ascii=False, indent=2)
        print(f"Arquivo '{os.path.basename(ARQ_TABELA)}' atualizado.")

    print("\nPronto! Agora rode: python main.py")


if __name__ == "__main__":
    main()
