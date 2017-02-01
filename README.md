# PetJungle


# Installation instructions
## For windows:
Getting python 2.7
- Install python 2.7.13 from [here](https://www.python.org/downloads/)
- Run Windows PowerShell, it should be already pre-installed with every Windows 10??
- Download [this gist](https://gist.github.com/KenLSM/4322c05132a7d1fa17483fd1fabaa516#file-helloworld-py) as `helloworld.py` and run `python helloworld.py`. You should see `Hello World` printed out on your powershell.

Updating your pip
- Run `pip install --upgrade pip` to update your pip. Pip is the package manager for python libraries. Synonymous to `npm` for `node.js`.

Clone this repo
- `git clone https://github.com/cs2102jan17g11/PetJungle.git` to a folder of your liking, be sure to `cd` to that folder first!

Installing postgres
- Get it [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows)
- I recommend setting the password to `postgres` so that you dont forget it.
- Leave the port number to be at `5432`
- pgAdmin comes with it, whoo!

Get `virtualenv` and `virtualenvwrapper`
- Run `pip install virtualenv virtualenvwrapper`. These are helpers to isolate our python environments.
- Run `mkvirtualenv cs2102`. We are creating an environment called `cs2102`
- Run `workon cs2102`. This command will allow our current session to use the targeted python environment, `cs2102` to be exact.

Installing project dependencies
- Run `pip install -r requirements.txt`
- Should not see any errors. Fix them if you see any of them. Most likely postgres related


# Running the server
- Run `make`
- Server should be on localhost:8000

# Running the console
- Run `make shell`
