import git

def reset_commits(repo_path):
    try:
        repo = git.Repo(repo_path)
        repo.git.reset("--hard", "HEAD~")
    except git.exc.GitCommandError as e:
        print("Une erreur est survenue lors de la suppression des commits :", e)

# Utilisation de la fonction pour supprimer les commits
reset_commits("C:\\Users\\Louis\\Desktop\\EvoDict\\tests\\.evodict_repo")


