# Going Down the EECS Stack DeCal Repo

## Setup Instructions
Step 1. Clone this repo to home
```bash
cd ~
git clone https://github.com/HKNDecal/Fall2017.git
```
Step 2. Run setup script in the setup directory
```bash
cd Fall2017/setup
source decal_setup.sh
```

And you're done! When the script finishes running you should see "(decal_env)" appended to the terminal.

## Creating New Sessions
Create a branch starting from the master branch titled `session-N`, where _N_ is the number of your
session. You'll then use `session-N` to develop the material for session _N_. The rest of the class
stays on the master branch while the session _N_ material is under development. When the material for
session _N_ is complete, merge the `session-N` branch back into master.
