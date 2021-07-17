
# Password Change

## General
- This project uses **Python3** while working inside a **virtualenv** (https://docs.python.org/3/tutorial/venv.html)
- The code contains two main components, each with its own test suite:
    - `password_validator`
        - Performs the actual password validation
        - Raises appropriate exception in case validation fails
        - Validation logic based on a configuration file (e.g. `password_configuration.json`)
        - Other Validators can inherit this class to override the validation logic
        - For our purpose we use `strict_password_validator`
    - `password_manager`
        - Exposes the `change_password` functionality
        - Uses a type of `password_validator` to determine if change is valid
        - Would only change password if validation pass
        - Returns `True` if change occurred otherwise `False`


## Installation

```bash

# downloading the the project to your local machine
$ mkdir password_change
$ cd password_change

# download via git clone
$ git clone https://github.com/gilav115/password_change
# (alternatively, download the zip file and extract the code to the project's folder)

# creating the virtual environment named 'venv' in the project's directory
$ python3 -m venv venv

# activating the virtual environment
$ source venv/bin/activate

# your console should now be ready and should look something like this:
#(venv) ➜  password_change git:(main)

# installing dependencies
$ pip install -r requirements.txt

# once done executing tests (see Usage part below), deactivating the virtual environment
$ deactivate
```




## Usage

```bash
# execute all tests
$ pytest

# execute all tests with output
$ pytest -v

# execute a test suite
# pytest [-v] <path_to_suite>
$ pytest -v tests_suites/managers_tests/password_manager_test.py 

# execute a specific test
# pytest <path_to_suite> -k "<test_name>"
$ pytest -v tests_suites/managers_tests/password_manager_test.py -k "test_change_invalid_password_fail"

```
