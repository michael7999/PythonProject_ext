from git import Repo
class Git():
    def __init__(self, file):
        self.file = file
        self.repo = Repo('C:\\RepoClone\\PythonProject_ext')
        self.commit = "Python script dat automatisch de code, bestanden naar de repo doorstuurd."
        self.remote_repo_url = 'https://github.com/michael7999/PythonProject_ext.git'
    def git_add_origin(self):
        try:
            origin = self.repo.create_remote('origin', self.remote_repo_url)
        except Exception as e:
            print('There was an error while adding the remote.')
            print(e)

    def git_pull(self):
        try:
            origin = self.repo.remote(name='origin')
            origin.pull()
        except Exception as e:
            print('There was an error while pulling the code from the repo.')
            print(e)

    def git_push(self):
        try:
            self.repo.git.add(self.file)
            self.repo.index.commit(self.commit)
            origin = self.repo.remote(name='origin')
            origin.push()
        except Exception as e:
            print('There was an error while pushing the code to the repo:')
            print(e)
    