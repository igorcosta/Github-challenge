# Github API challenge!

## Overview

This is a simple PoC webhook handler app written in Python 3.7+ and Flask framework as part of the Github API challenge.

### Features:

- Listens to events from a Github organization when a new repository has been created.
- Protects your master branch from pull requests without a minimum of 5 reviews.
- It creates an Issue ticket with @mention to your username, highlighting what changes were made in the repository.

### Requirements

- [Download](https://git-scm.com/) and install Git 2.x on your machine
- Python 3.7+ installed in your machine
- A code editor, for example [Atom](https://atom.io)
- [A Github account](https://github.com)
- An Github Organisation. _you can [create one for free](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)_
- [A free Ngrok account](https://ngrok.com/)

### Getting started

### Setup your Github

1. [Create a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

  > This solution depends on it.

### Local setup

1. Download and install the required software.
2. Fork and clone this repository into your local machine.
3. Open the terminal and start ngrok server.

  > _this will be used to create a tunnel between your local machine the internet, allowing you to reach GitHub API._

```bash
./ngrok http 5000
```

> **Note** _ngrok and Flask require to run on the same port number 5000, so ngrok will works as a proxy for your flask app._

Expected output:

![Alt text](/img/ngrok_example.png?raw=true "ngrok terminal output")

After your ngrok is running you will see in your terminal a unique url, copy the url, you will need to setup a webhook.

> **Tip**: _Every time you restart the ngrok you will need to update the url in your Github Webhook, you only need to do that if you're developing locally._

Once you have your ngrok tunnel running, you will need to start the **server.py** server, ngrok will point to this local server to accept Github requests.

#### Setup Flask to run

1. Open a new terminal window and type the following commands.

```bash
pip3 install -r requirements.txt
export FLASK_APP=server.py
export FLASK_ENV=development
export GITHUB_TOKEN= REPLACE_WITH_YOUR_ACCESS_TOKEN_HERE
export DEFAULT_USER= REPLACE_WITH_YOUR_GITHUB_USER
pyton3 -m flask run
```

If you see the output below, you're all set to go to the next step.

```bash
 * Serving Flask app 'server.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

2\. Now, let's go back to Github.

In this step you will need to setup the Webhook in your Github Organisation, pointing to your ngrok url, you copied previously..

> [Creating a Webhook on Github Organisation](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks#setting-up-a-webhook) pointing to the Ngrok URL you copied previously.

### Testing

Let's test our solution, open a new browser tab/window at

```bash
http://localhost:4040/inspect/http
```

Now create a new repository in your Github organisation:

```bash
https://github.com/organizations/your-awsome-little-inc/repositories/new
```

Replace the value: 'your-awesome-little-inc', with your organisation's name.

### Final step:

Congratulations, if you followed the steps so far until here. You will be able to see a new issue with @mention in your repo or any new repo you create under your organisation.

![Alt text](/img/repo-created.png?raw=true "ngrok terminal output")

And with issues alerting you that some security changes were applied by default:

![Alt text](/img/issue-created.png?raw=true "ngrok terminal output")

### Contributing

Long-term discussion and bug reports are limited only during the interview with Github Inc. Code reviews are possible, as long are done via Github Pull requests.

#### License

This project is licensed under the Apache 2.0 License.
