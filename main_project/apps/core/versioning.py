import subprocess
from datetime import datetime


def get_git_changeset_timestamp(absolute_path):
    """
    The get_git_changeset_timestamp() function takes the absolute_path directory as a
parameter and calls the git log shell command with the parameters to show the Unix
timestamp of the HEAD revision in the directory. We pass BASE_DIR to the function, as we
are sure that it is under version control. The timestamp is parsed, converted to a string
consisting of the year, month, day, hour, minutes, and seconds returned, and is then
included in the definition of the STATIC_URL.
    :param absolute_path:
    :return timestamp:
    """
    repo_dir = absolute_path
    git_log = subprocess.Popen("git log --pretty=format:%ct --quiet -1 HEAD",
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True,
                               cwd=repo_dir,
                               universal_newlines=True,
                               )
    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.utcfromtimestamp(int(timestamp))
    except ValueError:
        # Fallback to current timestamp
        return datetime.now().strftime('%Y%m%d%H%M%S')
    changeset_timestamp = timestamp.strftime('%Y%m%d%H%M%S')
    return changeset_timestamp
