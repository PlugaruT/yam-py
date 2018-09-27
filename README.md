yam-py
==========================
Simple CLI interface for https://news.yam.md/

## Usage

 1. Clone the repo
    ```
    git clone git@github.com:PlugaruT/yam-py.git
    ```
 2. Nagivate inside the folder and install the module
    ```
    python setup.py install
    ```
 3. Enjoy 🌟


## Help
```
$ yam-py --help
Usage: yam-py [OPTIONS]

  CLI interface for https://news.yam.md/

Options:
  --source TEXT      Source of the article used for article filtering.
  --pages INTEGER    Number of pages to fetch. Each page represents 30 more
                     articles.
  --lang [ro|ru|en]  Language to be used when fetching list of articles.
  --help             Show this message and exit.
```


### Sample Output
```
$ yam-py
14:10 <Concurs ecologic la Ungheni (FOTO) # Provincial> https://news.yam.md/ro/s/8047573
14:10 <Școli și grădinițe din Moldova, fără specialiști # National4> https://news.yam.md/ro/s/8047591
14:10 <Singapore, a treia țară atinsă de isteria acelor din căpșune. Mai nou, oamenii găsesc și bucăți de metal în fructe # UNIMEDIA> https://news.yam.md/ro/s/8047595
14:10 <Fotografia zilei: Ca în politică… # Observatorul de Nord> https://news.yam.md/ro/s/8047596
14:10 <Expertiza legislației electorale va fi prezentată până la 31 octombrie curent # Parlament.md> https://news.yam.md/ro/s/8047597
14:10 <Expertiza legislației electorale va fi prezentată până la 31 octombrie curent # Parlament.md> https://news.yam.md/ro/s/8047598
14:10 <Măsurile luate de MSMPS în urma decesului bărbatului de pe str. Lech Kaczyński # Cotidianul> https://news.yam.md/ro/s/8047599
14:10 <(FOTO) Efectele încălzirii globale: Prima navă port container a trecut cu succes prin ruta arctică # Cotidianul> https://news.yam.md/ro/s/8047600
14:10 <La Tiraspol a avut loc ședința grupurilor de lucru pentru dezvoltarea transportului auto și infrastructurii drumurilor # Moldpres> https://news.yam.md/ro/s/8047601
14:10 <Un pasager a intrat in cabina pilotilor, fiindca voia sa-si incarce telefonul # ProTV.md> https://news.yam.md/ro/s/8047602
14:10 <Producătorii de struguri vor beneficia de suport în identificarea noilor piețe de desfacere # Moldpres> https://news.yam.md/ro/s/8047603
14:10 <Atentie soferi. O portiune din strada Columna va fi inchisa de maine pana luni. Cum va circula transportul public # ProTV.md> https://news.yam.md/ro/s/8047604
14:10 <Theresa May a discutat cu Donald Trump un acord comercial post-Brexit # Jurnal TV> https://news.yam.md/ro/s/8047605
14:10 <Leul moldovenesc - a zecea valută tranzacționată la casele de schimb ale Băncii Transilvania # Timpul> https://news.yam.md/ro/s/8047606
14:10 <Angajații Agenției Naționale pentru Sănătate Publică își vor primi salariile începând cu ziua de luni # Moldova.org> https://news.yam.md/ro/s/8047607
14:15 <„Nu transformați cortegiile oficiale în cortegii funerare!” Asociația Tineri pentru dreptul la viață au lansat o petiție # #diez> https://news.yam.md/ro/s/8047616

```