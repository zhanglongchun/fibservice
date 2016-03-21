easy_install virtualenv

mkdir restapi_test
cd restapi_test
virtualenv venv

. ./venv/bin/activate

pip install Flask

pip install pytest

pip install flask-httpauth

