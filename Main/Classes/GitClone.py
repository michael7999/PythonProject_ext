from git import Repo

class GitCloner:
    @staticmethod
    def git_clone():
        try:
            # Binnenhalen van de repo en op de C schijf plaatsen
            Repo.clone_from('https://github.com/michael7999/PythonProject_ext.git', 'C:/RepoClone') 
        except Exception as e:
            print('There was an error while cloning the repo.')
            print(e)

# Gebruik de klasse en roep de methode aan
#cloner = GitCloner()
#cloner.git_clone()

# Men kan de klasse ook rechtstreeks aanroepen
# GitCloner.git_clone()




