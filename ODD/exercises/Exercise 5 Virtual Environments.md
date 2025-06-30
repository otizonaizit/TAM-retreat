## Exercise 5a: Virtual Environments

#### Goal

Create a virtual environment + install a package + see that that package was installed only in environment

#### Tasks

We will use `venv` as our environment manager - while commands might differ, the principles apply to all other package managers as well.

1. Check which Python you are currently using, and which packages are installed. Also check which folders are in the folder you are installing the environment into.
3. Create and activate a new environment.
4. Check again which Python you are using and which packages are installed - are they different?
5. Install a specific version of a package using pip e.g. pandas=1.5.3
6. See that dependencies are also installed (more packages than only pandas appear)
7. Deactivate and delete the environment
8. Check the packages that are installed when no environment is active again (as step 1). Have they changed?


#### Commands in case you get stuck (not in correct order):

```bash
% investigate Python and packages
> which python
> pip freeze
> pip install <package-name>
> pip install <package-name>==0.0.1

% create an environment option 1 (create folder called venv_folder for files related to virtual environment, feel free to change the name)
> cd <path-to-project_folder>
> mkdir venv_folder
> python3 -m venv venv_folder
> source venv_folder/bin/activate

% create an environment option 2
> python3 -m venv <path-to-folder-for-venv>
> source <path-to-folder-for-venv>/bin/activate

% deactivate and delete a venv environment
> deactivate
> rm -rf venv_folder
```
