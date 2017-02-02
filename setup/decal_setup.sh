pip install --user virtualenv
mkdir ~/envs
python -m virtualenv ~/envs/decal_env

source ~/envs/decal_env/bin/activate

pip install -r requirements.txt

echo "source ~/envs/decal_env/bin/activate" >> ~/.bashrc
