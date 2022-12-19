#! /bin/sh
echo "======================================================================"
echo "Welcome to to the application-testing shell-script. This will run all the application py-tests after loading the local virtual env." 
echo "And it will also load all the required python libraries."
echo "Before running this shell-script, the setup shell-script must be run first."
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
export ENV=testing
pytest --verbose --disable-warnings -s
deactivate
