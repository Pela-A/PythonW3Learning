# Python allows you to create virtual environments.

# These are isolated environments to run and test python projects. You can isolate project specific dependencies and libraries to a specific project and not affect your original python installation

# Each python virtual environment contains its own python interpreter, and packages.

# We can prevent version conflicting wiht projects which allows them to be more portable. It also allows us to test different python versions if we want.


#*
# python -m venv myfirstproject
#
# myfirstproject\Scripts\activate
#
# INSTALL PACKAGES
#
# Run python commands/files
#
# WHEN DONE RUN deactivate

# Remove virutal environment
# rmdir /s /q myfirstproject


# This code will only run with the myProject venv active because of dependency on cowsay package

import cowsay

cowsay.cow("Good Mooooorning!")