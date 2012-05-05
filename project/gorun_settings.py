# Note! Order matters which makes it possible to run particular
# command if a file changes in a directory and another command for all
# other files in that directory.

DIRECTORIES = (
    ('./', './manage.py test'),
)
