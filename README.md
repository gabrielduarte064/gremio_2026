Para ver o relatório, baixe o arquivo .html,
que provavelmente vai estar atualizado até a data de 21/09/2026.



#  Painel Grêmio 2026 — Brasileirão Série A

Projeto em Python que gera um relatório HTML com menu de navegação e insights
de análise do Grêmio no Campeonato Brasileiro Série A 2026 (1º e 2º turno),
com **atualização automática via API** — ou seja, quando o Grêmio jogar de novo,
basta rodar um comando e o painel já reflete o novo jogo.

---

  Estrutura do projeto

```
gremio_2026/
├── dados.py              # Base de dados (snapshot manual + carregamento automático via API)
├── analise.py            # Cálculos: aproveitamento, comparativo de turnos, forma, etc.
├── css_template.py       # Estilo visual (tema escuro nas cores do Grêmio)
├── html_builder.py       # Monta o HTML final (menu + seções)
├── main.py               # Ponto de entrada — gera o gremio_2026_painel.html
├── atualizar_dados.py    # Busca dados novos na API football-data.org
└── README.md             # Este arquivo
```

Depois de rodar `atualizar_dados.py` pela primeira vez, dois arquivos novos
aparecem na pasta (não vêm no ZIP, são gerados por você):

```
dados_jogos.json    # jogos do Grêmio buscados na API (substitui o snapshot manual)
dados_tabela.json   # posição, pontos e saldo atuais na tabela do Brasileirão
```

---

#  Como usar

# 1) Gerar o painel com os dados que já vêm prontos (snapshot até 20/09/2026)

Não precisa de API nem chave para isso — já funciona direto:

```bash
python main.py
```

Isso gera o arquivo **`gremio_2026_painel.html`**. Basta abrir no navegador.

# 2) Atualizar os dados automaticamente via API (recomendado a cada rodada nova)

O projeto usa a **football-data.org** — a mesma API que você já usa no seu
`cartola_extractor.py` (variável `FOOTBALL_DATA_KEY`, `BRASILEIRAO_ID = "BSA"`).

**Passo 1 — Pegue uma chave gratuita (leva 1 minuto):**
Acesse [football-data.org/client/register](https://www.football-data.org/client/register),
crie uma conta grátis e copie sua API Key.

**Passo 2 — Configure a variável de ambiente com a chave:**

| Sistema               | Comando                                      |
|------------------------|-----------------------------------------------|
| Windows (CMD)          | `set FOOTBALL_DATA_KEY=sua_chave_aqui`        |
| Windows (PowerShell)   | `$env:FOOTBALL_DATA_KEY="sua_chave_aqui"`     |
| Linux / Mac            | `export FOOTBALL_DATA_KEY="sua_chave_aqui"`   |

**Passo 3 — Rode os dois scripts nessa ordem:**

```bash
python atualizar_dados.py
python main.py
```

Pronto! O `atualizar_dados.py` busca todos os jogos já disputados do Grêmio no
Brasileirão 2026 e a classificação atual, salva em `dados_jogos.json` e
`dados_tabela.json`, e o `main.py` já usa esses dados automaticamente na
próxima geração — sem precisar mexer em nenhum código.

>  **Toda vez que o Grêmio jogar de novo**, é só repetir o passo 3
> (`atualizar_dados.py` + `main.py`) que o painel já vem com o jogo mais recente,
> a posição atualizada na tabela e o novo aproveitamento do 2º turno recalculado.

---

  Como funciona a atualização automática

O `dados.py` foi construído para **preferir dados automáticos quando disponíveis**:

```python
if os.path.exists("dados_jogos.json"):
    JOGOS = json.load(...)      # usa dados da API
else:
    JOGOS = [...]               # usa o snapshot manual (fallback)
```

Ou seja, o snapshot manual dentro de `dados.py` nunca é apagado — ele continua
funcionando como uma base de segurança caso você não tenha (ou não queira usar)
uma chave de API. O projeto sempre roda, com ou sem internet.

---

 O que o painel mostra

| Aba              | Conteúdo                                                                 |
|-------------------|---------------------------------------------------------------------------|
|  Visão Geral    | Posição na tabela, campanha geral 2026, forma recente, destaque do último jogo |
|  1º Turno       | Estatísticas e jogo a jogo das rodadas 1–19                              |
|  2º Turno       | Estatísticas e jogo a jogo das rodadas 20 em diante                      |
|  Comparativo    | 1º x 2º turno e mandante x visitante, com barras comparativas            |
|  Artilharia      | Artilheiros e assistências da temporada                                  |
|  Jogo a Jogo    | Todos os jogos em ordem cronológica, com selo V/E/D                      |

---

  Sobre a API football-data.org

- **Plano gratuito**: acesso às principais competições (inclui Brasileirão Série A / código `BSA`), com limite de requisições por minuto.
- Se a chave não estiver definida, `atualizar_dados.py` avisa no terminal e não quebra nada — o `main.py` continua funcionando com o snapshot manual.
- Se a API retornar erro (ex: limite de requisições excedido), rode novamente após alguns segundos.

---

  Requisitos

- Python 3.8+
- Biblioteca `requests` (apenas necessária para `atualizar_dados.py`):
  ```bash
  pip install requests
  ```

---

  Fontes dos dados do snapshot manual (até 20/09/2026)

ESPN, ge.globo, ogol.com.br, UOL, Bolavip e aquiesportes.com.br.
