# ~/.bash_profile
# in order to delete all pyc pyo files and __pycache__ dir when you switch
# branches or move the directories, you need to clean up the compiled files manually.
#
# PYTHONDONTWRITEBYTECODE=1 if you want to disable wirte bytecode files
alias delpyc='
find . -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete'