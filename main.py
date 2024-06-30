import typer
from typing_extensions import Annotated
import requests
from bs4 import BeautifulSoup, Tag
from rich.table import Table
from rich.console import Console

league_help_text = """Mulige argumenter (ligaer): \n
- 'sl': Superligaen \n
- 'pl': Premier League \n
- 'll': La Liga \n
- 'bl': Bundesligaen \n
- 'sa': Serie A"""


def main(
    league: Annotated[
        str,
        typer.Argument(help=league_help_text),
    ] = "sl"
):
    """
    Hent stillinger fra fodboldligaer fra bold.dk
    """
    markup = fetch_league_markup(league)
    data = extract_ranking_data(markup)
    print_standing(data)


def fetch_league_markup(league):
    url = "https://bold.dk/fodbold/stillinger/"

    match league:
        case "sl":
            url += "superligaen"
        case "pl":
            url += "premier-league"
        case "ll":
            url += "spanien-la-liga"
        case "bl":
            url += "tyskland-1-bundesliga"
        case "sa":
            url += "italien-serie-a"

    return requests.get(url).text


def extract_ranking_data(markup):
    soup = BeautifulSoup(markup, "html.parser")

    table = soup.find("table")

    thead = extract_table_headers(table)
    tbody = extract_table_rows_data(table)

    return {"headers": thead, "rows": tbody}


def extract_table_headers(table: Tag) -> list[str]:
    thead = table.find("thead")

    ths = thead.find_all("th")

    headers = ["#"]
    for th in ths:
        headers.append(th.span.text.strip())

    return headers


def extract_table_rows_data(table: Tag) -> dict:
    tbody = table.find("tbody")

    trs = tbody.find_all("tr")

    table_rows = []

    for tr in trs:
        tds = tr.find_all("td")

        row = []

        row.append(tds[0].div.span.text)
        row.append(tds[0].div.a.span.text)

        for td in tds[1:]:
            # team_data["data"].)
            row.append(td.div.span.text)

        table_rows.append(row)

    return table_rows


def print_standing(data: dict):
    table = Table()

    headers = data["headers"]
    for header in headers:
        table.add_column(header)

    rows = data["rows"]
    for row in rows:
        table.add_row(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )

    console = Console()
    console.print(table)


if __name__ == "__main__":
    typer.run(main)
