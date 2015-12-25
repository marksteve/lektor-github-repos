# lektor-github-pages

Fetches your GitHub repos for display in Lektor templates

## Enabling the plugin

To enable the plugin add this to your project file:

```
[packages]
lektor-github-repos = 0.1
```

## Generate a personal access token

If you're only accessing public repos, the GitHub API allows you
to only make 60 unauthenticated requests per hour. But that goes up
to 5,000 requests per hour with authentication and it's not that hard to do:

Go to https://github.com/settings/tokens/new and generate a token. You
can untick all scopes to get public access.

## Create the config file

Create `configs/github-repos.ini` with the following content:

```
[github-repos]
token = <your personal access token>
```

## Use in your templates

The plugin adds `get_github_repos()` and `get_top_github_repos()` to the template
context. Both accepts the same parameters as with the user repos API call
(https://developer.github.com/v3/repos/#list-your-repositories).
`get_top_github_repos` also sorts repos by stargazers and accepts an additional
param `count`.

### Get latest pushed repositories

```
<ul>
{% for repo in get_github_repos(sort="pushed") %}
  <li>
    <strong>{{ repo.name }}</strong>
    {{ repo.description }}
  </li>
{% endfor %}
</ul>
```

### Get 10 latest updated repositories sorted by stargazers

```
<ul>
{% for repo in get_top_github_repos(type="owner", sort="updated", count=10) %}
  <li>
    [{{ repo.stargazers_count }} stars]
    <strong>{{ repo.name }}</strong>
    {{ repo.description }}
  </li>
{% endfor %}
</ul>
```
