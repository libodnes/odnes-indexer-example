# odnes-indexer-example

Tento projekt slouží jako šablona pro vytvoření nového datového zdroje pro nástroj **ODNES**. Díky modulární architektuře je rozšíření systému o vlastní datasource snadné a nevyžaduje žádné zásahy do jádra aplikace.

## Požadavky

- Python 3.9+
- [Poetry](https://python-poetry.org/) pro správu balíčků a závislostí

## Postup přidání nového zdroje

### 1. Přejmenujte šablonu

V adresáři `src/odnes/datasources/` se nachází ukázkový soubor `example.py`. Tento soubor slouží jako výchozí šablona. Přejmenujte jej podle vašeho zdroje, např.:

```bash
mv src/odnes/datasources/example.py src/odnes/datasources/dnsdb.py
```

### 2. Přejmenujte třídu

Uvnitř nového souboru přejmenujte třídu `Example` na název odpovídající vašemu zdroji, např. `DNSDB`. Třída musí dědit ze základní třídy `Datasource` a implementovat metodu:

```python
async def search(self, domain: str) -> list[DatasourceObject]:
    ...
```

### 3. Upravte `pyproject.toml`

Pokud chcete nový datasource distribuovat jako samostatný balíček, upravte v souboru `pyproject.toml` název projektu, například:

```toml
name = "odnes-indexer-dnsdb"
```

Doporučuje se aktualizovat i popis, autora, verzi atd.

### 4. Instalace balíčku

Pomocí Poetry můžete balíček sestavit a nainstalovat:

```bash
poetry build -f wheel
pip install dist/odnes_indexer_dnsdb-*.whl
```

Alternativně lze balíček nainstalovat přímo ze zdrojového adresáře:

```bash
pip install .
```

## Automatická registrace

ODNES při spuštění automaticky načte všechny třídy dědící z `Datasource` — není tedy nutné upravovat žádný registr ani konfiguraci. Název třídy slouží jako identifikátor zdroje (např. pro CLI přepínač `-D DNSDB`).

## Poznámka

Každý nový datasource může využívat vlastní závislosti definované v `pyproject.toml`, a být distribuován jako samostatný plugin. Tím je zajištěna čistá oddělenost jednotlivých komponent.
