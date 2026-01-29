from git import Repo
import os
import shutil
import stat

def force_remove(func, path, exc_info):
    """
    Handle Windows permission errors when deleting files
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(repo_url, dest="repos/temp"):
    if os.path.exists(dest):
        shutil.rmtree(dest, onerror=force_remove)

    Repo.clone_from(repo_url, dest)
    return dest
