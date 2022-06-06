<div id="top"></div>

<br />
<div align="center">
  <a href="https://www.velo-antwerpen.be/">
    <img src="../_site/images/velo.png" alt="Logo" width="300" height="150">
  </a>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-it-works">How it works</a></li>
    <li><a href="#reflection">Reflection</a></li>
  </ol>
</details>

## About the project

Dit project is een minimalistische versie van het Velo platform van de provincie Antwerpen

Het project probeert zo goed mogelijk het echte platform van Velo na te bootsen door zo veel mogelijk functies in te bouwen zoals:
* Het ontlenen en terugbrengen van Fietsen door gewone gebruikers
* Het verplaatsen van verschillende fietsen in volle stations naar minder bezette stations door fietstransporteurs

### Built With

Het project bestaat volledig uit deze technologieën en gebruikt volgende python modules:

* [python3](https://python.org/)
* [SQLite3](https://sqlite.org/)
* [Jinja2](https://jinja.palletsprojects.com/)
* [shortuuid](https://pypi.org/project/shortuuid/)

## Getting Started

### Prerequisites

* pip
  1. Change directory to Downloads
  ```sh
  cd Downloads
  ```
  2. Download <a href="https://bootstrap.pypa.io/get-pip.py">pip.py</a> or use wget
  ```sh
  wget http://www.domain.com/filename.zip
  ```
  3. Run install script
  ```sh
  python get-pip.py
  ```

### Installation

1. Clone deze repo
   ```sh
   git clone https://github.com/iniasdb/velo.git
   ```
2. Create virtual environment
   ```sh
   cd velo
   ```
   ```sh
   python -m venv venv
   ```
3. Start virtual environment
   ```sh
   cd venv/Scripts
   ```
   ```sh
   activate.bat
   ```
   ```sh
   cd ../../
   ```
4. Install python modules
   ```sh
   pip install -r requirements.txt
   ```
5. Deactive virtual environment (na het runnen van het script)
   ```sh
   deactivate
   ```

## Usage

Het programma kan gestart worden door `app.py` uit te voeren via de cli
   ```sh
   python app.py
   ```

Het is ook mogelijk het programma te starten met de `-s` parameter, het programma zal dan in simulatiemodus gestart worden.
   ```sh
   python app.py -s
   ```

Het programma zal u dan een menu tonen waar u kunt kiezen om oude data uit de database te laden, of om nieuwe data te genereren en onmiddelijk naar de database te schrijven.

Wanneer u het programma voor de 1e keer start, zal u slechts enkel de optie krijgen om nieuwe data te genereren.

Nadien komt u bij het hoofdmenu, hier zal u een keuze kunnen maken tussen de verschillende features:

* Manueel fiets ontlenen door gebruiker
* Manueel fiets terugbrengen door gebruiker
* Manueel fiets ontlenen door transporteur
* manueel fiets terugbrengen door transporteur
* Simulatie starten
* Station gebruikers interface laden
* Webpagina genereren
* Excel bestand creëren met alle transacties die in runtime gebeurd zijn
  * Worksheet wordt in velo map gecreëerd

Indien u kiest voor een webpagina te generen krijgt u een keuzemenu waar u moet kiezen tussen:

* Fiets infopagina genereren
* Station infopagina genereren
* Gebruiker infopagina genereren

De webpagina zal nadien automatisch in de browser geopend worden.

## Features

* Eigen logging framework
  * logs worden bijgehouden in `logs/velo.log`
  * Er kan gekozen worden tussen verschillende logging levels
  * Er kan geopteerd worden om naar de console, een file of beide te loggen
* Module om random users te genereren uit naam en email datasets
* Alle data wordt snel naar de database geschreven en opgehaald
* Webpagina met info over een bepaalde fiets, gebruiker of station kan gegenereerd worden
* Excel bestand met alle recente verplaatsingen kan gegenereerd worden
* Een GUI kan geopend worden om het ontlenen en terugbrengen van fietsen in een station te vergemakkelijken

## How it works

Het project maakt gebruik van OOP, waardoor de klassen reusable zijn en de code compact blijft.

Wanneer een user een fiets wilt lenen, zal die de loan_bike() method moeten aanspreken van een station. Hierop zal het station dan een slot met een fiets zoeken en deze toekennen aan de user.

Wanneer de user de fiest wilt terugbrengen, zal deze de return_bike() method van een station aanspreken. Hierop wordt er een leeg slot gevonden en de fiets aan dit slot toegekend.

Een transporter is een subklasse van een user, het enige verschil is dat hij een lijst van fietsen heeft en dus ook meerdere fietsen kan opnemen.

Wanneer er een fiets ontleent wordt zal er een Relocation object aangemaakt worden met de fiets, user en beginstation in kwestie.
Wanneer de fiets dan teruggebracht wordt, wordt dit object vervoledigd door het eindstation.<br>
Deze objecten worden dan opgeslagen in een lijst en wanneer nodig naar de database of een excel bestand geschreven.

## Reflection

Het project verliep vrij tot zeer goed bij mij, het enige grootste minpunt was mijn tijdsverdeling. <br>
Ik had de grootte van dit project zwaar onderschat en had mogelijks dit project niet op de oorspronkelijke deadline afgekregen.

Door het verlaten van de deadline kon ik echter wel enkele extra functies toevoegen die mijn python kennis in het algemeen enorm vergroot hebben.

Doorheen de ontwikkeling van dit programma ben ik nooit echt op een "roadblock" tegengekomen op één keer na.<br> 
In het begin toen ik data naar de database schreef, commit'te ik elke na een SQL query uit te voeren. Hierdoor werd het wachten op het schrijven naar de database extreem lang.<br>
Door dit te vermijden en slechts enkele keren te committen na grote stukken SQL code. Hierdoor werd de snelheid tussen het programma en de database drastisch verhoogd.

Mijn keuze om een database te gebruiken in plaats van een andere optie zoals txt fo JSON files was grotendeels door mijn ervaring met het werken in SQL.<br>
Zo heb ik bijvoorbeeld tijdens mijn stage en vorige studies steeds gebruik moeten maken van PostgreSQL en MySQL, waardoor de stap naar SQLite3 minder groot was.<br>
Of deze keuze uiteindelijk de juiste was weet ik niet.

De volledige 'roadmap' van het project kan u vinden op [github](https://github.com/iniasdb/velo/commits)