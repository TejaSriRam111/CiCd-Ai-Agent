from git import Repo
import os
import shutil

def clone_repo(repo_url, dest="repos/temp"):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    Repo.clone_from(repo_url, dest)
    return dest
 
