# 'footy': et CLI til fodboldstillinger
Dette script bruges som et CLI til nemmere at hente fodboldstillinger fra https://bold.dk/, i stedet for at bruges hjemmesidens egen navigationsmuligheder til samme.

## Baggrund
Baggrunden for at have lavet dette CLI er, at man - hvis man er fodboldinteresseret og følger med stillingerne fra de europæiske ligaer - på bold.dk's hjemmeside hele tiden skal bruge fx hjemmesidens navigationsbar til at kunne se stillingerne, hvilket er (rimelig) irriterende og langsommeligt, når blot man gerne vil se stillingen fra en anden liga.

### Eksempel
Hvis man er gået ind for at se stillingen for den danske Superliga, og dernæst gerne vil se stillingen for den engelske Premier League, så skal man enten:
1. Først op i bold.dk's navigationsmenu, vælge "Stillinger" drop-down listen og så først der vælge "Premier League", eller
2. Vælge det undseelige lige link i øverste venstre med teksten "Alle turneringer", og dernæst vælge "Premier League" fra den fremkomne liste, når man trykket på linket

Her er et eksempel der viser den "langsommelige" proces man skal igennem for at gå siden med stillingen fra danske Superliga til siden stillingen med stillingen for Premier League:

<img width="672" alt="Screenshot 2024-08-20 at 10 18 06" src="https://github.com/user-attachments/assets/1c458e16-f1fc-43de-9b59-4a2b9699b722">

## CLI'et
Det CLI'et løser er således at man blot ved enten at køre det - eller evt. give det argument for den liga man gerne vil se en stilling fra (fx 'pl' for Premier Leagu, 'll' for La Liga osv. - kan få fodboldstillinger hurtigt vist i sin terminal, uden at man behøver bruge bold.dk's langsommelige proces for at se samme.

### Forudsætninger for at bruge CLI'et
For at kunne bruge CLI'et, så forudsættes følgende:

#### Have Python installeret
Først og fremmest skal man have [Python](https://www.python.org/) installeret. Har man ikke det, så følg linket til https://www.python.org/ for at downloade og installere Python.

#### Installere 'Typer', 'BeautifulSoup' og 'Rich'
Når man har Python installeret, så kræver CLI'et at man henter følgende pakker:
* [Typer](https://typer.tiangolo.com/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Rich](https://rich.readthedocs.io/en/latest/)

Nemmeste måde at installere disse Python pakker er dog heldigvis blot at køre denne kommando, da den vil installere alle de nødvendige pakker, uden at man skal gøre noget selv:
```bash
pip install -r requirements.txt
```

### Hvordan man bruger CLI'et
I dette nedenstående gennemgås, hvordan man bruger CLI'et på følgende måder:
1. Uden brug af argumenter
2. Med brug af argumenter
3. Får hjælp til brug af CLI'et

#### Brug uden argumenter
CLI'et er sat op til vise stillingen for den danske Superliga som standard. Så hvis man kører CLI'et uden brug af argumenter, så vises stillingen for Superligaen.

Dette gøres ved at køre denne kommando:
```bash
typer main.py run
```

Når denne kommando køres, så fremkommer stillingen for den danske Superliga (her indhentet d. 20. august 2024) sådan her i terminalen:
<img width="495" alt="cli-superliga-2024-08-20" src="https://github.com/user-attachments/assets/6b00d6da-75b8-456f-8b62-19e010932d1f">

### Brug med argumenter
Hvis man gerne vil se stillingen for en anden liga - pt. er mulighederne uderover Superligaen at se stillinger for Premier League, La Liga, Bundesligaen og Seria A - så skal blot efter ovenstående kommando tilføje en af følgende argumenter:
- pl (for Premier League)
- ll (for La Liga)
- bl (for Bundesligaen)
- sa (for Seria A)

Vil man således gerne se stillingen for Premier League, så er kommandoen for det følgende:
```bash
typer main.py run pl
```

Ved kørsel af denne kommando vil stillingen for Premier League i ens terminal se ud som følger (her indhentet for d. 20. august 2024):

<img width="542" alt="cli-pl" src="https://github.com/user-attachments/assets/8ec9c2fb-d59a-474d-9a24-3287a4138b52">

Vil man i stedet se en af de andre ligaers stillinger, som udskiftes 'pl' i ens kommando bare med en af argumenterne fra ovenstående liste.

### Få hjælp til brugen af CLI'et
Hvis man vil se, hvordan man får hjælp til brugen af CLI'et, så tilføjer man bare 'flaget' ```--help``` på følgende måde:
```bash
typer main.py run --help
```

Gøres dette, så fremkommer følgende hjælp i terminalen:
<img width="618" alt="cli-help" src="https://github.com/user-attachments/assets/d84ed941-105a-4bb8-a079-2c3a8848aa40">

