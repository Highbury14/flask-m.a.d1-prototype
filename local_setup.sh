#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".env" ];
then
  echo ".env folder exists. Installing dependant libraries using pip."
else
  echo "Creating .env and installing dependant libraries using pip."
  python3.7 -m venv .env
fi

# Activate virtual env.
. .env/bin/activate

# Upgrade PIP packages.
pip install --upgrade pip
pip install -r requirements.txt
# Deactivate virtual env.
deactivate
