# Virtual Enviroment setup 
# Virtual enviroment create an isolated environment for python projects.Its allow you to manage dependencies and packages for each project separately without affecting the global ptyhon interpreter

# Step 1:
# cd my_project    -> reason because virtual enviroment should be created inside the project folder
# Step 2:
# python -m venv env -> this command will create a virtual enviroment named env inside the my_project folder. -m means run this library built-in module as a script. venv is the module that creates virtual enviroment and env is the name of the virtual enviroment you want to create.
# Step 3:
# source env\Scripts\activate -> this command will activate the virtual enviroment. After activating the virtual enviroment, you will see the name of the virtual enviroment in the terminal prompt. This indicates that you are now working inside the virtual enviroment.
# Step 4:
# pip install package_name -> this command will install the package inside the virtual enviroment. You can install any package you want without affecting the global python interpreter.
# Step 5:
# pip freeze > requirements.txt -> this command will create a requirements.txt file that contains all the packages and their versions that are installed in the virtual enviroment. This file can be used to recreate the same environment in another machine or for deployment. > means redirect the output of the pip freeze command to the requirements.txt file. You can also use pip list to see the list of installed packages in the virtual enviroment.
# Step 6:
# deactivate -> this command will deactivate the virtual enviroment and return you to the global python interpreter. You can reactivate the virtual enviroment anytime by running the source env\Scripts\activate command again.
# Step 7:
# pip install -r requirements.txt -> this command will install all the packages and their versions that are listed in the requirements.txt file. This is useful when you want to set up the same environment on another machine or for deployment. -r means read the packages from the requirements.txt file.