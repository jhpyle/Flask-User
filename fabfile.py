from fabric.operations import local
from fabric.api import cd, env, task, prefix, run
from contextlib import contextmanager

@task
def runserver():
    local('python runserver.py')

@task
def test():
    # Requires "pip install pytest"
    local('py.test docassemble_flask_user/tests/')

@task
def coverage():
    # Requires "pip install pytest-coverage"
    local('py.test --cov docassemble_flask_user --cov-report term-missing --cov-config docassemble_flask_user/tests/.coveragerc docassemble_flask_user/tests/')

@task
def update_babel():
    local('pybabel extract -F docassemble_flask_user/translations/babel.cfg -k lazy_gettext -c NOTE -o docassemble_flask_user/translations/flask_user.pot docassemble_flask_user docassemble_flask_user')
    for code in ('de', 'en', 'es', 'fa', 'fi', 'fr', 'it', 'nl', 'ru', 'sv', 'tr', 'zh'):
        local('pybabel update -i docassemble_flask_user/translations/flask_user.pot --domain=docassemble_flask_user --output-dir docassemble_flask_user/translations -l '+code)
    local('pybabel compile -f --domain=flask_user --directory docassemble_flask_user/translations')

@task
def docs():
    local('cp example_apps/*_app.py docs/source/includes/.')
    local('sphinx-build -b html docs/source ../builds/flask_user/docs')
    local('cd ../builds/flask_user/docs && zip -u -r flask_user_docs *')

@task
def rebuild_docs():
    local('rm -fr ../builds/flask_user/docs')
    docs()

# PyEnv: https://gist.github.com/Bouke/11261620
# PyEnv and Tox: https://www.holger-peters.de/using-pyenv-and-tox.html
# Available Python versions: pyenv install --list
@task
def setup_tox():
    versions_str = '2.6.9 2.7.13 3.3.6 3.4.6 3.5.3 3.6.2'
    versions = versions_str.split()
    for version in versions:
        local('pyenv install --skip-existing '+version)
    local('pyenv global '+versions_str)

@task
def tox():
    local('tox')

@task
def build_dist():
    local('rm dist/*.tar.gz')
    local('python setup.py sdist')

@task
def upload_to_pypi():
    build_dist()
    local('twine upload dist/*')

