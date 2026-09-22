from analise import gerar_todos_insights
from html_builder import montar_html

SAIDA = "gremio_2026_painel.html"


def main():
    print("Calculando insights a partir de dados.py ...")
    insights = gerar_todos_insights()

    print("Montando o HTML final (menu + seções) ...")
    html = montar_html(insights)

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Concluído! Relatório salvo em: {SAIDA}")


if __name__ == "__main__":
    main()
