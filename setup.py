from setuptools import setup

setup(
    name='lektor-github-repos',
    description='Fetches your GitHub repos for display in Lektor templates',
    version='0.1',
    author=u'Mark Steve Samson',
    author_email='hello@marksteve.com',
    license='MIT',
    py_modules=['lektor_github_repos'],
    install_requires=['requests'],
    entry_points={
        'lektor.plugins': [
            'github-repos = lektor_github_repos:GithubReposPlugin',
        ]
    },
    url='https://github.com/marksteve/lektor-github-pages',
)
