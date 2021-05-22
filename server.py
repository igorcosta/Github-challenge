from flask import Flask, request, Response
from github import Github
from flask import request
import requests
import json
import os

app = Flask(__name__)

git_token = os.environ['GITHUB_TOKEN']
repo_name = ''
default_branch =''
default_user = os.environ['DEFAULT_USER']

issue_Template = """

 Hi @{}, the security settings for your main branch has been changed!
 This will keep your repository safe and maintain a high standards.
 We included the following changes automatically:

**Changes**:

 - Admin branch protection: You have absolute control over this branch.
 - Pull request protection: Auto approval of pull requests, requires at least 5 approving reviews.

""".format(default_user)



@app.route('/webhook', methods=['POST'])
def respond():
    git_data = request.json;
    if 'action' in git_data:
        if git_data['action'] == 'created':
            if git_data['repository']:
                repo_name = git_data['repository']['full_name'];
                default_branch = git_data['repository']['default_branch']
                createGitHubIssue(repo_name, 'Updated branch protection', issue_Template, default_user, 'enhancement');
            createBranchProtection(git_data['repository']['owner']['login'],git_data['repository']['name'], default_branch)
    return Response(status=200)

def createBranchProtection(owner,repo,branch,review_number=5):
    '''This is still in preview mode'''
    url = 'https://api.github.com/repos/{}/{}/branches/{}/protection'.format(owner,repo, branch)
    headers = {"Authorization": "token {}".format(git_token), "Accept": "application/vnd.github.luke-cage-preview+json"}
    data = {
  "required_status_checks": {
    "strict": True,
    "contexts": [
      "trevis-baby"
    ]
  },
  "enforce_admins": True,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {
      "users": [
        "users"
      ],
      "teams": [
        "teams"
      ]
    },
    "dismiss_stale_reviews": True,
    "require_code_owner_reviews": True,
    "required_approving_review_count": review_number
  },
  "restrictions": {
    "users": [
      'users'
    ],
    "teams": [
      'teams'
    ],
    "apps": [
      'apps'
    ]
  }
}
    r = requests.put(url, headers=headers, data=json.dumps(data))
    return


def createGitHubIssue(repoName, title, body=None, assignee=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    client = Github(git_token)
    repo = client.get_repo("%s" % (repoName))
    issue = repo.create_issue(
        title= title,
        body= body,
        assignee= assignee,
        labels=[
        repo.get_label(labels)
    ]
)
