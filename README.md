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
- TBD

Installing project dependencies
- Run `pip install -r requirements.txt`
- Should not see any errors. Fix them if you see any of them. Most likely postgres related



# Running the server
- Run `make`
- Server should be on localhost:8000

# Running the console
- Run `make shell`
