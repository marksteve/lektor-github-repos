# -*- coding: utf-8 -*-
import requests
from lektor.pluginsystem import Plugin


class GithubReposPlugin(Plugin):
    name = u'GitHub Repos'
    description = u'Fetches your GitHub repos for display in Lektor templates'

    def on_process_template_context(self, context, **extra):
        context['get_github_repos'] = self.get_github_repos
        context['get_top_github_repos'] = self.get_top_github_repos

    def get_github_repos(self, **params):
        config = self.get_config()
        token = config.get('github-repos.token')
        params.setdefault('per_page', 100)
        resp = requests.get(
            'https://api.github.com/user/repos',
            headers={'Authorization': 'token ' + token},
            params=params,
        )
        return resp.json()

    def get_top_github_repos(self, **params):
        count = params.pop('count', None)
        repos = self.get_github_repos(**params)
        return sorted(
            repos,
            key=lambda repo: repo['stargazers_count'],
            reverse=True,
        )[:count]

