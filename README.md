# Github API challenge named API!

## Overview

This is a simple web app written in Python 3.7+, and uses Flask framework (Python web framework).

### Features:

- Listen to events from an organisation when a new repository has been created.
- When a repository is created under the organization, triggers an automated process to protect the master branch of the repository using a minimum number of pull reviews.
- Then notify your Github user account with an @mention using Github issue within the repository, highlights the details of what protection was added to the branch.

### Requirements

- [Download](https://git-scm.com/) and install Git 2.x on your machine
- Python 3.7+ installed in your machine
- A code editor, for example [Atom](https://atom.io)
- [A Github account](https://github.com)
- An Github Organisation. _you can create one from your free Github account_
- [A free Ngrok account](https://ngrok.com/)

### Getting started

It's super simple web application, doesn't use docker or anything like that, the idea is you can host this Flask app anywhere with not a specific virtualization platform.

### Setup

1. Download and install the required software.
2. Fork and clone this repository into your local machine.
3. Open the terminal and start ngrok server, __this will be used to create a tunnel between your local machine the internet, allowing you to reach GitHub API.

```bash
./ngrok http 5000
```

--------------------------------------------------------------------------------

**NOTE** _ngrok and Flask needs to run on the same port number 5000, so ngrok will works as a proxy for your flask app._

--------------------------------------------------------------------------------

1. Once you have your ngrok tunnel running, you will need to start the **server.py** server, which is the main component here that receives webhook requests from Github.

Open a new terminal window and typ the following commands.

```bash
pip3 install -r requirements.txt
export FLASK_APP=server.py
export FLASK_ENV=development
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

### Testing

Now that you completed the setup, let's test our solution.

Open the browser tab at

```bash
http://localhost:4040/inspect/http
```

Now create a new repository in your github organisation:

```bash
https://github.com/organizations/your-awsome-little-inc/repositories/new
```

### Contributing

Long-term discussion and bug reports are limited only during the interview with Github. Code reviews are possible, as long are done via Github Pull requests.

#### License

This project is licensed under the Apache 2.0 License.
