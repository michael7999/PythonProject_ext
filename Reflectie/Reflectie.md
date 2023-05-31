# Project Python: Trojan
# Samenvatting
- Het project bestaat uit verschillende klassen/modules. (Fictieve situatie: wanneer de gebruiker via een mail de code triggert worden de volgende stappen uitgevoerd.)
1) Eerst wordt de code gecloned van de repository en weggeschreven naar een opgegeven locatie op de target pc, in dit geval C:/RepoClone.
2) Vervolgens wordt de systeeminfo weggeschreven naar een bestand. Dit bestand wordt naar een nieuwe repository gepusht die vooraf werd aangemaakt. (Voor het project wordt er gebruik gemaakt van dezelfde repository.)
3) Het programma blijft de oorspronkelijke repository controleren en "pullen" om het uur. Indien er een wijziging is van het bestand trigger.txt, m.a.w. wanneer de letters "e" "encrypt" , "s" van "song" en/of "k" van "keylogger" worden toegevoegd, zal de desbetreffende module worden geactiveerd.
4) Wanneer de "e" wordt toegevoegd worden de encrypt modules getriggerd. Deze zorgen ervoor dat een folder "te_versleutelen_folder" en alle bestanden die aanwezig zijn in de folder worden geëncrypteerd. Het is mogelijk om de path aan te passen naar de volledige C-schijf, waardoor deze dan wordt geëncrypteerd. In de eerste plaats wordt er een sleutel gegenereerd. Deze wordt in een bestand opgeslagen. Dan treedt de encryptie in werking. Uiteindelijk wordt de key naar de repo doorgestuurd en de inhoud van het bestand wordt gewist.
5) De "s" van "song" zorgt ervoor dat het nummer "sympathy for the devil" in een loop wordt afgespeeld tot de gebruiker het getal "666" invoert.
6) De "k" van "keylogger" gaat alle toetsaanslagen van de gebruiker wegschrijven naar een bestand dat eveneens wordt doorgestuurd naar de repository.
   
   

## Geïnstalleerde modules
Deze kunnen worden teruggevonden in de requirements.txt

# Bestanden

## GitHub

### Repo.py
- Deze code definieert een klasse genaamd Git die functionaliteiten biedt om met een Git-repository te communiceren en wijzigingen te pushen, pullen en origin toe te voegen.
- Maak een instantie van Git en geef het bestand op dat moet worden toe gevoegd aan de Git-repository. Vervolgens kan men de methoden git_add_origin, git_pull en git_push aanroepen om de gewenste Git-acties uit te voeren. 

### GitClone.py

- Deze code definieert een klasse genaamd GitCloner met een statische methode git_clone() die verantwoordelijk is voor het klonen (clonen) van een Git-repository naar een specifieke locatie op de C-schijf.
- Om deze klasse te gebruiken, hoeft men geen instantie van de GitCloner-klasse te maken. Men kan rechtstreeks de statische methode git_clone() aanroepen.

## Attack

### SystemInfo.py
- De SystemInfoLogger-klasse heeft als doel om systeeminformatie te verzamelen en op te slaan in een tekstbestand.
- Er dient een instantie van SystemInfoLogger worden aangemaakt. Men kan een optioneel argument output_file opgeven om de naam en locatie van het uitvoerbestand aan te passen. Vervolgens kan men de write_to_file-methode aanroepen om de systeeminformatie op te slaan in het aangegeven bestand. De modules platform en os moeten geïnstalleerd worden om de klasse te kunnen gebruiken.

### GenerateKey.py
- Deze code heeft tot doel een sleutel te genereren met behulp van de Fernet-klasse uit het cryptography.fernet-pakket. De gegenereerde sleutel wordt vervolgens opgeslagen in een bestand met de naam "Key.txt".

### WriteKeys.py
- Het doel van deze code is het maken van een keylogger-functionaliteit met behulp van de pynput.keyboard-module. De Listener-klasse uit deze module wordt gebruikt om toetsaanslagen te monitoren en de Keywriter-klasse wordt gebruikt om deze toetsaanslagen naar een logbestand te schrijven.
- Windows defender verwijdert automatisch een bestand met de naam keylogger.py, daarom werd het bestand WriteKeys.py genoemd.

### Encrypt.py
- Hierin bevindt zich de klasse FileEncryptor. 
- Deze klasse heeft als doel het versleutelen van bestanden en mappen met behulp van de Fernet-coderingsbibliotheek uit de cryptography-module.
- Om deze klasse te gebruiken, moet je eerst een instantie van FileEncryptor maken en het pad naar het bestand met de sleutel (Key.txt) opgeven bij het initialiseren. Daarna kun je de methoden encrypt_file of encrypt_folder aanroepen om de gewenste versleutelingsbewerking uit te voeren.
-  Zorg ervoor dat de vereiste modules worden geïmporteert, zoals os en cryptography.fernet.

### Trigger_Encrypt_.py
- De FolderEncryptor-klasse heeft als doel om bestanden in een opgegeven map  te versleutelen met behulp van de FileEncryptor-klasse. (Normaal gezien de C-schijf, deze is voor testdoeleinden vervangen door de map: te_versleutelen_folder.)
- Om deze klasse te gebruiken, moet er een instantie van FolderEncryptor worden gemaakt met de gewenste map en het pad naar het sleutelbestand. Daarna kun je de encrypt_folder-methode aanroepen om alle bestanden in die map te versleutelen. 
### PerfectDay.py

- Het doel van deze code is om een eenvoudige muziekspeler te implementeren met behulp van de Pygame-bibliotheek. 

- Het maakt een object van de klasse met een specifiek muziekbestand, roept de functie play_music aan om het nummer "sympathy for the devil" af te spelen en stopt het afspelen wanneer de gebruiker "666" invoert.



## Decrypt
### Decrypt.py (Bevindt zich in de folder Decrypt.)
- Het doel van deze code is om een bestand of een hele map met bestanden te decrypteren. 
- Deze module dient niet aan de (aanvals)repo toegevoegd te worden die op de target-pc wordt gecloned. 
- Ze wordt gebruikt om de C-schijf te decrypteren wanneer deze eerst is geëncrypteerd. 
- Voor deze actie zal een fictief bedrag moeten worden overgemaakt door het slachtoffer alvorens de code met de sleutel (die door de klasse Keygenerator wordt aangemaakt, doorgestuurd en verwijderd) wordt overhandigd.

### Trigger_Decrypt.py
- Deze code heeft als doel om een map te ontsleutelen met behulp van de functie decrypt_folder die geïmporteerd wordt uit een module genaamd "Decrypt".


## Trigger
### Check_cfg_file.py
- Deze code definieert een klasse genaamd WordChecker die verschillende acties uitvoert op basis van de letters die worden aangetroffen in een tekstbestand genaamd "trigger.txt". Hier is een overzicht van de functionaliteit:
- De functie check_trigger_file controleert het bestand "trigger.txt" in het opgegeven repositorypad.

- Het pad naar het "trigger.txt"-bestand wordt samengesteld door self.repo_path te combineren met "/trigger.txt".


- Er wordt een lus uitgevoerd over elke letter in de inhoud van het bestand. Oorspronkelijk was het de bedoeling om met woorden te werken, maar uiteindelijk vond ik het meer comfortabel om met letters te werken (e, s, k)
- Als de letter "e" wordt gevonden, worden de volgende acties uitgevoerd:
  a. Een object key_generator van de klasse KeyGenerator wordt gemaakt.

  - De functie generate_and_save_key("Key.txt") wordt aangeroepen op key_generator om een sleutel te genereren en op te slaan in een bestand genaamd "Key.txt".

  - De paden naar de te versleutelen map en het sleutelbestand worden ingesteld.

  - Een object encryptor van de klasse FolderEncryptor wordt gemaakt, met de bovengenoemde paden als argumenten.

  - De functie encrypt_folder() wordt aangeroepen op encryptor om de map te versleutelen.

  - Een object push_key van de klasse Git wordt gemaakt, met het pad naar het bestand "Key.txt" als argument.

  - De functie git_push() wordt aangeroepen op push_key om het "Key.txt"-bestand naar het repository te pushen.

  - De functie clear_key_file() wordt aangeroepen op key_generator om het "Key.txt"-bestand te verwijderen.

  - De boodschap "Alles is succesvol versleuteld." wordt afgedrukt.
  
- Als de letter "s" wordt gevonden, worden de volgende acties uitgevoerd:

  - De naam van het muziekbestand wordt ingesteld op "sympathy_for_the_devil.mp3".



  - De functie play_music() wordt aangeroepen op player om de muziek af te spelen.

  - Er wordt een while-lus gestart waarin gebruikersinvoer wordt gevraagd. De lus wordt herhaald totdat de gebruiker "666" invoert.

  - Wanneer de gebruiker "666" heeft ingevoerd wordt de functie stop_music() aangeroepen.
  - 
- Als de letter "k" wordt gevonden, worden de volgende acties uitgevoerd:

  - De naam van het logbestand wordt ingesteld op "keylogs.txt".

  - Een object write van de klasse Keywriter wordt gemaakt, met het logbestand als argument.

  - De functie start_logging() wordt aangeroepen op write om het loggen te starten.

## Main

### main.py

- Deze code zorgt ervoor dat bepaalde taken, zoals het ophalen van de laatste versie van een repository, het controleren van het bestand "trigger.txt" op wijzigingen en het uitvoeren van specifieke acties, systematisch worden uitgevoerd op basis van een tijdschema.
- In de while True-lus wordt schedule.run_pending() aangeroepen om de geplande taken uit te voeren. Het programma blijft in deze lus draaien totdat het wordt gestopt. De time.sleep(59)-regel voorkomt dat de lus te intensief wordt uitgevoerd door een korte pauze van 59 seconde tussen elke iteratie in te voegen.

## Moeilijkheden
- Alle modules zijn afzonderlijk getest en werken. Het enige wat problemen opleverde, was ervoor te zorgen dat de taken die in de main.py met de schedule module werden uitgevoerd effectief om het uur werden getriggerd. De twee functies die hier werden ondergebracht maakten gebruik van het Repo.py bestand met Git-klasse en Check_cfg_file.py met de WordChecker-klasse. De Git-klasse zorgt voor een pull van de repository waarna de WordChecker-klasse gaat kijken of er specifieke letters aan het "trigger.txt" bestand werden toegevoegd en vervolgens de initiële aanval te triggeren. 





