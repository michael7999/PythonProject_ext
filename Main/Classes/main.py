
from GitClone import GitCloner
from SystemInfo import SystemInfoLogger
from Repo import Git
import schedule
import time
from Check_cfg_file import WordChecker



# Clone de repository naar de juiste locatie

GitCloner.git_clone()

# Verzamel de system data en sla deze op in het bestand "SystemData.txt"
logger = SystemInfoLogger()
logger.write_to_file()

# Push het bestand naar de repository

push_system_info = Git("C:/RepoClone/PythonProject_ext/Project_def/Main/Classes/SystemData.txt")
push_system_info.git_push()


# Hier worden de objecten aangemaakt van de verschillende klassen die verder in de code worden gebruikt
word_checker = WordChecker("C:/RepoClone/PythonProject_ext/Project_def/Main/Classes/")
git = Git("C:/RepoClone/PythonProject_ext/Project_def/Main/Classes/SystemData.txt")

# Pull de repository naar de juiste locatie om de laatste wijzigingen van het bestand trigger.txt te controleren  
# Gitpull: pull de laatste versie van de repository

def git_pull_job():
      
    git.git_pull()

def letters_search_job():
    
    word_checker.check_trigger_file()

# Om het uur de git_pull_job() functie uitvoeren
schedule.every().hour.do(git_pull_job)

# Om het uur de letters_search_job() functie uitvoeren om te kijken of het trigger.txt bestand is gewijzigd
schedule.every().hour.do(letters_search_job)


# Blijft de taak uitvoeren totdat het programma wordt gestopt
while True:
    schedule.run_pending()

    time.sleep(59)






