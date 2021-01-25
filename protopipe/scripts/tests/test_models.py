"""Test the model building script for different cases."""

from os import system
from pkg_resources import resource_filename
import pytest
from protopipe.scripts import build_model

# PATH TO TEST DATA TO BE DEFINED

# - 1 GAMMA TABLE for energy model
# - 1 GAMMA TABLE for classification model
# - 1 PROTON TABLE for classification model

# min events 100000 (conservative estimate)

# config files should be dedicated to tests, with data path local to the script
# they should probably be stored in the test folder and not in aux/example_config_files
# each model should be also tested for GridSearchCV usage


def test_RandomForestRegressor():
    """Launch protopipe.scripts.build_model for a RandomForestRegressor."""

    # configuration file
    config = resource_filename("protopipe", "aux/example_config_files/RandomForestRegressor.yaml")

    exit_status = system(
        f"python {build_model.__file__}\
        --config_file {config}\
        --max_events 100000"
    )
    assert exit_status == 0


def test_RandomForestClassifier():
    """Launch protopipe.scripts.build_model for a RandomForestRegressor."""

    # configuration file
    config = resource_filename("protopipe", "aux/example_config_files/RandomForestClassifier.yaml")

    exit_status = system(
        f"python {build_model.__file__}\
        --config_file {config}\
        --max_events 100000"
    )
    assert exit_status == 0


@pytest.mark.skip(reason="Work In Progress")
def test_AdaBoost_DecisionTreeClassifier():

    # configuration file
    config = resource_filename("protopipe", "aux/example_config_files/AdaBoost_DecisionTreeClassifier.yaml")

    return None


@pytest.mark.skip(reason="Work In Progress")
def test_AdaBoost_DecisionTreeRegressor():

    # configuration file
    config = resource_filename("protopipe", "aux/example_config_files/AdaBoost_DecisionTreeRegressor.yaml")

    return None
