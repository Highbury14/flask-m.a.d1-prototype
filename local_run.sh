#! /bin/sh
echo "======================================================================"
echo "Welcome to to the application-run shell-script. This will run the application."
echo "Before running this shell-script, you have to first setup the local virtual environment using the setup shell-script."
echo "And then it will also load all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".env" ];
then
  echo "Enabling virtual env."
else
  echo "No virtual env. exists. Please run local_setup.sh first."
  exit N
fi

# Activate virtual env.
. .env/bin/activate
export ENV=development
python main.py
deactivate
