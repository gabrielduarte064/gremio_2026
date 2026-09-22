CSS = """
:root {
  --azul-gremio: #0039a6;
  --azul-claro: #2e6bd4;
  --preto: #0a0c10;
  --preto-card: #14181f;
  --branco: #ffffff;
  --cinza: #9aa4b2;
  --verde: #2ecc71;
  --amarelo: #f1c40f;
  --vermelho: #e74c3c;
  --borda: #232936;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
  background: linear-gradient(180deg, #05070a 0%, #0a0c10 100%);
  color: var(--branco);
  min-height: 100vh;
}

/* ---------- HEADER ---------- */
.header {
  background: linear-gradient(120deg, var(--preto) 0%, var(--azul-gremio) 100%);
  padding: 28px 32px 22px 32px;
  border-bottom: 4px solid var(--azul-claro);
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.badge {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: repeating-linear-gradient(
      180deg, var(--azul-gremio) 0px, var(--azul-gremio) 8px,
      var(--preto) 8px, var(--preto) 16px, var(--branco) 16px, var(--branco) 20px
  );
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 20px;
  color: var(--branco);
  border: 3px solid var(--branco);
  flex-shrink: 0;
  text-shadow: 0 0 4px #000;
}

.header-text h1 {
  margin: 0;
  font-size: 26px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.header-text p {
  margin: 4px 0 0 0;
  color: #cfd8e8;
  font-size: 14px;
}

/* ---------- MENU ---------- */
.menu {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  background: var(--preto);
  padding: 10px 20px;
  border-bottom: 1px solid var(--borda);
  position: sticky;
  top: 0;
  z-index: 50;
}

.menu button {
  background: transparent;
  color: var(--cinza);
  border: 1px solid var(--borda);
  padding: 10px 18px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.3px;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.menu button:hover {
  border-color: var(--azul-claro);
  color: var(--branco);
}

.menu button.active {
  background: var(--azul-gremio);
  color: var(--branco);
  border-color: var(--azul-claro);
  box-shadow: 0 0 12px rgba(46, 107, 212, 0.6);
}

/* ---------- MAIN ---------- */
.container {
  padding: 26px 32px 60px 32px;
  max-width: 1300px;
  margin: 0 auto;
}

.tab { display: none; animation: fadeIn 0.35s ease; }
.tab.active { display: block; }

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.section-title {
  font-size: 20px;
  font-weight: 700;
  margin: 30px 0 14px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--azul-gremio);
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-title:first-child { margin-top: 0; }

.faixa {
  background: linear-gradient(90deg, var(--preto) 0%, var(--azul-gremio) 100%);
  color: var(--branco);
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 1px;
  padding: 10px 18px;
  border-radius: 6px;
  margin: 24px 0 16px 0;
  font-size: 14px;
}

/* ---------- CARDS / KPI ---------- */
.grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 14px;
  margin-bottom: 20px;
}

.card {
  background: var(--preto-card);
  border: 1px solid var(--borda);
  border-radius: 12px;
  padding: 18px;
  text-align: center;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.card:hover {
  transform: translateY(-3px);
  border-color: var(--azul-claro);
}

.card .valor {
  font-size: 28px;
  font-weight: 800;
  color: var(--branco);
}

.card .valor.pos { color: var(--verde); }
.card .valor.neg { color: var(--vermelho); }
.card .valor.warn { color: var(--amarelo); }

.card .rotulo {
  margin-top: 6px;
  font-size: 12px;
  color: var(--cinza);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* ---------- TABELAS ---------- */
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--preto-card);
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 22px;
}

thead th {
  background: rgb(128,128,128);
  color: var(--branco);
  font-weight: 700;
  padding: 10px 12px;
  font-size: 12px;
  text-transform: uppercase;
  text-align: left;
}

tbody td {
  padding: 9px 12px;
  font-size: 13px;
  border-bottom: 1px solid var(--borda);
  color: #e6e9ee;
}

tbody tr:hover { background: rgba(46, 107, 212, 0.08); }
tbody tr:last-child td { border-bottom: none; }

.tag {
  display: inline-block;
  width: 26px;
  height: 26px;
  line-height: 26px;
  text-align: center;
  border-radius: 50%;
  font-weight: 800;
  font-size: 12px;
  color: #fff;
}
.tag.V { background: var(--verde); }
.tag.E { background: var(--amarelo); color: #202020; }
.tag.D { background: var(--vermelho); }

.forma-seq { display: flex; gap: 6px; flex-wrap: wrap; }

/* ---------- BARRAS COMPARATIVAS ---------- */
.bar-row { margin-bottom: 14px; }
.bar-label {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  margin-bottom: 4px;
  color: var(--cinza);
}
.bar-bg {
  background: #1c212b;
  border-radius: 8px;
  height: 20px;
  overflow: hidden;
  display: flex;
}
.bar-fill {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
  font-size: 11px;
  font-weight: 700;
  color: white;
}
.bar-fill.turno1 { background: linear-gradient(90deg, #12306e, var(--azul-gremio)); }
.bar-fill.turno2 { background: linear-gradient(90deg, #7a1f1f, var(--vermelho)); }
.bar-fill.casa { background: linear-gradient(90deg, #0d5c2f, var(--verde)); }
.bar-fill.fora { background: linear-gradient(90deg, #7a5c00, var(--amarelo)); }

/* ---------- DESTAQUE / CALLOUT ---------- */
.callout {
  background: var(--preto-card);
  border-left: 4px solid var(--azul-claro);
  border-radius: 8px;
  padding: 18px 20px;
  margin-bottom: 20px;
}
.callout h3 { margin: 0 0 8px 0; font-size: 16px; color: var(--branco); }
.callout p { margin: 4px 0; font-size: 13.5px; color: #cdd4de; line-height: 1.5; }
.callout .stat-inline { color: var(--azul-claro); font-weight: 700; }

.footer-note {
  text-align: center;
  color: var(--cinza);
  font-size: 12px;
  margin-top: 40px;
  padding-top: 16px;
  border-top: 1px solid var(--borda);
}

/* ---------- RESPONSIVO ---------- */
@media (max-width: 700px) {
  .header { padding: 18px; }
  .header-text h1 { font-size: 19px; }
  .container { padding: 16px; }
  .menu { padding: 8px 10px; overflow-x: auto; flex-wrap: nowrap; }
  table { font-size: 11px; }
  thead th, tbody td { padding: 6px 8px; }
}
"""
