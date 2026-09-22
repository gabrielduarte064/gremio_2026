from css_template import CSS

RESULTADO_LABEL = {"V": "Vitória", "E": "Empate", "D": "Derrota"}


def _linha_jogo(j, mostrar_turno=False):
    mando = "Casa" if j["mandante"] else "Fora"
    placar = f'{j["gf"]} x {j["ga"]}'
    turno_col = f'<td>{j["turno"]}º</td>' if mostrar_turno else ""
    return f"""
    <tr>
      <td>{j['rodada']}ª</td>
      <td>{j['data']}</td>
      {turno_col}
      <td>{j['adversario']}</td>
      <td>{mando}</td>
      <td>{placar}</td>
      <td><span class="tag {j['resultado']}">{j['resultado']}</span></td>
    </tr>"""


def _tabela_jogos(jogos, mostrar_turno=False):
    turno_header = "<th>Turno</th>" if mostrar_turno else ""
    linhas = "".join(_linha_jogo(j, mostrar_turno) for j in jogos)
    return f"""
    <table>
      <thead>
        <tr>
          <th>Rodada</th><th>Data</th>{turno_header}<th>Adversário</th>
          <th>Mando</th><th>Placar</th><th>Res.</th>
        </tr>
      </thead>
      <tbody>{linhas}</tbody>
    </table>"""


def _card(valor, rotulo, classe=""):
    return f"""
    <div class="card">
      <div class="valor {classe}">{valor}</div>
      <div class="rotulo">{rotulo}</div>
    </div>"""


def _barra_comparativa(label_a, valor_a, label_b, valor_b, max_valor, classe_a, classe_b, sufixo=""):
    pct_a = max(6, round((valor_a / max_valor) * 100)) if max_valor else 0
    pct_b = max(6, round((valor_b / max_valor) * 100)) if max_valor else 0
    return f"""
    <div class="bar-row">
      <div class="bar-label"><span>{label_a}</span><span>{valor_a}{sufixo}</span></div>
      <div class="bar-bg"><div class="bar-fill {classe_a}" style="width:{pct_a}%">{valor_a}{sufixo}</div></div>
    </div>
    <div class="bar-row">
      <div class="bar-label"><span>{label_b}</span><span>{valor_b}{sufixo}</span></div>
      <div class="bar-bg"><div class="bar-fill {classe_b}" style="width:{pct_b}%">{valor_b}{sufixo}</div></div>
    </div>"""


def _forma_visual(forma_lista):
    bolhas = "".join(
        f'<span class="tag {j["resultado"]}" title="R{j["rodada"]} vs {j["adversario"]} ({j["gf"]}x{j["ga"]})">{j["resultado"]}</span>'
        for j in forma_lista
    )
    return f'<div class="forma-seq">{bolhas}</div>'


# SEÇÕES

def secao_visao_geral(insights):
    tg = insights["tabela_geral"]
    camp = insights["campanha_geral_2026"]
    dest = insights["destaque_rodada_28"]
    seq = insights["sequencia_atual"]
    comp_html = "".join(
        f'<li><strong>{c}:</strong> {v}</li>' for c, v in camp["competicoes"].items()
    )

    return f"""
    <div id="visao-geral" class="tab active">
      <div class="section-title"> Visão Geral — Brasileirão 2026</div>
      <div class="grid-cards">
        {_card(f'{insights["posicao"]}º', 'Posição atual', 'warn')}
        {_card(tg['pontos'], 'Pontos')}
        {_card(f"{tg['vitorias']}V {tg['empates']}E {tg['derrotas']}D", 'Aproveitamento (jogos)')}
        {_card(f"{tg['gp']}-{tg['gc']}", 'Gols pró-contra')}
        {_card(tg['sg'], 'Saldo de gols', 'neg' if tg['sg'] < 0 else 'pos')}
        {_card(f"{tg['aproveitamento']}%", 'Aproveitamento %')}
      </div>

      <div class="callout">
        <h3> Situação na tabela</h3>
        <p>O Grêmio ocupa a <span class="stat-inline">{insights['posicao']}ª posição</span>,
        dentro do Z-4 (zona de rebaixamento), com <span class="stat-inline">{tg['pontos']} pontos</span>
        em {tg['jogos']} rodadas disputadas.</p>
        <p>Está <span class="stat-inline">{insights['rebaixamento']['distancia_pontos']} ponto(s)</span> atrás do
        {insights['rebaixamento']['referencia']} ({insights['rebaixamento']['pontos_referencia']} pts),
        primeiro time fora da degola. Restam <span class="stat-inline">{insights['rebaixamento']['jogos_restantes']} jogos</span>
        até o fim da temporada.</p>
      </div>

      <div class="section-title">🇪 Campanha geral 2026 (todas as competições)</div>
      <div class="grid-cards">
        {_card(camp['jogos'], 'Jogos')}
        {_card(camp['vitorias'], 'Vitórias', 'pos')}
        {_card(camp['empates'], 'Empates', 'warn')}
        {_card(camp['derrotas'], 'Derrotas', 'neg')}
        {_card(f"{camp['gp']}-{camp['gc']}", 'Gols pró-contra')}
        {_card(f"{camp['aproveitamento']}%", 'Aproveitamento %')}
      </div>
      <div class="callout">
        <h3> Competições da temporada</h3>
        <ul>{comp_html}</ul>
      </div>

      <div class="section-title"> Forma recente (últimos 5 jogos)</div>
      {_forma_visual(insights['forma_recente'])}
      <p style="color:#9aa4b2;font-size:13px;margin-top:10px;">
        {seq['jogos_sem_vencer']} jogo(s) sem vencer · {seq['jogos_invicto']} jogo(s) de invencibilidade seguida.
      </p>

      <div class="faixa"> Destaque da 28ª rodada — Grêmio 0x0 Palmeiras</div>
      <div class="callout">
        <h3>{dest['resultado']} — {dest['local']}</h3>
        <p><strong>Homem do jogo:</strong> {dest['homem_do_jogo']}</p>
        <p><strong>Estreia:</strong> {dest['treinador_estreante']} — {dest['estrategia']}</p>
        <p><strong>Posse de bola:</strong> Grêmio {dest['posse_de_bola']['Grêmio']}% x
           {dest['posse_de_bola']['Palmeiras']}% Palmeiras</p>
        <p><strong>Finalizações:</strong> Grêmio {dest['finalizacoes']['Grêmio']} x
           {dest['finalizacoes']['Palmeiras']} Palmeiras</p>
        <p><strong>xG (gols esperados):</strong> Grêmio {dest['gols_esperados_xg']['Grêmio']} x
           {dest['gols_esperados_xg']['Palmeiras']} Palmeiras</p>
        <p><strong>Público:</strong> {dest['publico_destaque']}</p>
        <p>{dest['contexto_tabela']}</p>
      </div>
    </div>"""


def secao_turno(insights, numero):
    t = insights[f"turno_{numero}"]
    jogos = insights[f"jogos_turno_{numero}"]
    titulo = "1º Turno (Rodadas 1 a 19)" if numero == 1 else "2º Turno — até Grêmio 0x0 Palmeiras (Rodadas 20 a 28)"
    return f"""
    <div id="turno{numero}" class="tab">
      <div class="section-title"> {titulo}</div>
      <div class="grid-cards">
        {_card(t['jogos'], 'Jogos')}
        {_card(t['vitorias'], 'Vitórias', 'pos')}
        {_card(t['empates'], 'Empates', 'warn')}
        {_card(t['derrotas'], 'Derrotas', 'neg')}
        {_card(t['pontos'], 'Pontos')}
        {_card(f"{t['aproveitamento']}%", 'Aproveitamento')}
        {_card(f"{t['gf']}-{t['ga']}", 'Gols pró-contra')}
        {_card(t['sg'], 'Saldo de gols', 'neg' if t['sg'] < 0 else 'pos')}
      </div>
      <div class="section-title"> Jogo a jogo — {titulo}</div>
      {_tabela_jogos(jogos)}
    </div>"""


def secao_comparativo(insights):
    ct = insights["comparativo_turnos"]
    mv = insights["mandante_visitante"]
    t1, t2 = ct["turno_1"], ct["turno_2"]
    seta = "🔻" if not ct["melhorou"] else "🔺"
    cor_var = "neg" if not ct["melhorou"] else "pos"

    return f"""
    <div id="comparativo" class="tab">
      <div class="section-title"> Comparativo 1º Turno x 2º Turno</div>
      <div class="grid-cards">
        {_card(f"{t1['aproveitamento']}%", '1º Turno — Aproveitamento')}
        {_card(f"{t2['aproveitamento']}%", '2º Turno — Aproveitamento')}
        {_card(f"{seta} {abs(ct['variacao_aproveitamento'])} p.p.", 'Variação de aproveitamento', cor_var)}
      </div>
      {_barra_comparativa('1º Turno — Aproveitamento', t1['aproveitamento'], '2º Turno — Aproveitamento', t2['aproveitamento'], 100, 'turno1', 'turno2', '%')}
      {_barra_comparativa('1º Turno — Média de gols marcados', t1['media_gols_marcados'], '2º Turno — Média de gols marcados', t2['media_gols_marcados'], 2.5, 'turno1', 'turno2')}
      {_barra_comparativa('1º Turno — Média de gols sofridos', t1['media_gols_sofridos'], '2º Turno — Média de gols sofridos', t2['media_gols_sofridos'], 2.5, 'turno1', 'turno2')}

      <div class="callout">
        <h3>🔎 Leitura do comparativo</h3>
        <p>O aproveitamento do Grêmio caiu de <span class="stat-inline">{t1['aproveitamento']}%</span> no 1º turno
        para <span class="stat-inline">{t2['aproveitamento']}%</span> no returno — uma queda de
        <span class="stat-inline">{abs(ct['variacao_aproveitamento'])} pontos percentuais</span>.</p>
        <p>A média de gols sofridos por jogo subiu de {t1['media_gols_sofridos']} para {t2['media_gols_sofridos']},
        enquanto a média de gols marcados caiu de {t1['media_gols_marcados']} para {t2['media_gols_marcados']}.</p>
      </div>

      <div class="section-title"> Mandante x Visitante (temporada completa)</div>
      <div class="grid-cards">
        {_card(f"{mv['casa']['aproveitamento']}%", 'Aproveitamento em casa', 'pos')}
        {_card(f"{mv['fora']['aproveitamento']}%", 'Aproveitamento fora', 'neg')}
      </div>
      {_barra_comparativa('Em casa — Aproveitamento', mv['casa']['aproveitamento'], 'Fora de casa — Aproveitamento', mv['fora']['aproveitamento'], 100, 'casa', 'fora', '%')}
      <div class="callout">
        <h3> Casa x  Fora</h3>
        <p><strong>Casa:</strong> {mv['casa']['jogos']} jogos — {mv['casa']['vitorias']}V {mv['casa']['empates']}E {mv['casa']['derrotas']}D
        · {mv['casa']['gf']}-{mv['casa']['ga']} gols · saldo {mv['casa']['sg']}</p>
        <p><strong>Fora:</strong> {mv['fora']['jogos']} jogos — {mv['fora']['vitorias']}V {mv['fora']['empates']}E {mv['fora']['derrotas']}D
        · {mv['fora']['gf']}-{mv['fora']['ga']} gols · saldo {mv['fora']['sg']}</p>
      </div>
    </div>"""


def secao_artilharia(insights):
    art = insights["artilheiros_geral"]
    assis = insights["assistencias_geral"]
    art_bras = insights["artilheiro_brasileirao"]

    linhas_art = "".join(
        f"<tr><td>{i+1}º</td><td>{a['jogador']}</td><td>{a['gols']}</td></tr>"
        for i, a in enumerate(art)
    )
    linhas_assis = "".join(
        f"<tr><td>{i+1}º</td><td>{a['jogador']}</td><td>{a['assistencias']}</td></tr>"
        for i, a in enumerate(assis)
    )

    return f"""
    <div id="artilharia" class="tab">
      <div class="section-title"> Artilharia e Assistências — Temporada 2026 (todas as competições)</div>
      <div class="callout">
        <h3> Artilheiro do Grêmio no Brasileirão</h3>
        <p><span class="stat-inline">{art_bras['jogador']}</span> — {art_bras['gols']} gols,
        {art_bras['posicao_ranking_geral']}º do ranking geral de artilheiros da competição.</p>
      </div>
      <div style="display:flex; gap:20px; flex-wrap:wrap;">
        <div style="flex:1; min-width:280px;">
          <table>
            <thead><tr><th>#</th><th>Artilheiro</th><th>Gols</th></tr></thead>
            <tbody>{linhas_art}</tbody>
          </table>
        </div>
        <div style="flex:1; min-width:280px;">
          <table>
            <thead><tr><th>#</th><th>Garçom</th><th>Assist.</th></tr></thead>
            <tbody>{linhas_assis}</tbody>
          </table>
        </div>
      </div>
    </div>"""


def secao_jogo_a_jogo(insights):
    jogos = insights["jogos_cronologicos"]
    goleadas = insights["goleadas"]
    mv = goleadas["maior_vitoria"]
    md = goleadas["maior_derrota"]
    return f"""
    <div id="jogoajogo" class="tab">
      <div class="section-title"> Todos os jogos do Grêmio no Brasileirão 2026 (cronológico)</div>
      <div class="grid-cards">
        {_card(f"{mv['gf']}x{mv['ga']} vs {mv['adversario']}", 'Maior vitória', 'pos') if mv else ''}
        {_card(f"{md['gf']}x{md['ga']} vs {md['adversario']}", 'Maior derrota', 'neg') if md else ''}
      </div>
      {_tabela_jogos(jogos, mostrar_turno=True)}
    </div>"""


def montar_html(insights):
    menu_botoes = [
        ("visao-geral", " Visão Geral"),
        ("turno1", " 1º Turno"),
        ("turno2", " 2º Turno"),
        ("comparativo", " Comparativo"),
        ("artilharia", " Artilharia"),
        ("jogoajogo", " Jogo a Jogo"),
    ]
    menu_html = "".join(
        f'<button data-tab="{tid}" onclick="mostrarTab(\'{tid}\', this)"{" class=\'active\'" if i == 0 else ""}>{label}</button>'
        for i, (tid, label) in enumerate(menu_botoes)
    )

    corpo = (
        secao_visao_geral(insights)
        + secao_turno(insights, 1)
        + secao_turno(insights, 2)
        + secao_comparativo(insights)
        + secao_artilharia(insights)
        + secao_jogo_a_jogo(insights)
    )

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Grêmio 2026 — Painel de Análise</title>
<style>{CSS}</style>
</head>
<body>

<div class="header">
  <div class="badge">GRE</div>
  <div class="header-text">
    <h1>Grêmio Foot-Ball Porto Alegrense</h1>
    <p>Painel de Análise — Brasileirão Série A 2026 · 1º e 2º Turno · atualizado até a 28ª rodada (20/09/2026, Grêmio 0x0 Palmeiras)</p>
  </div>
</div>

<div class="menu">{menu_html}</div>

<div class="container">
  {corpo}
  <div class="footer-note">
    Painel gerado automaticamente a partir de dados públicos (ESPN, ge.globo, ogol.com.br, UOL, Bolavip).
    Projeto Python — módulos: dados.py · analise.py · html_builder.py · main.py
  </div>
</div>

<script>
function mostrarTab(id, btn) {{
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.menu button').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
  window.scrollTo({{top: 0, behavior: 'smooth'}});
}}
</script>

</body>
</html>"""
    return html
