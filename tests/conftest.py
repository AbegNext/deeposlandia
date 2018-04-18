"""Test config setup for training dataset handling
"""

import json
import os
import pytest


@pytest.fixture
def mapillary_image_size():
    return 22


@pytest.fixture
def mapillary_sample_dir():
    return "tests/data/mapillary/sample"


@pytest.fixture
def mapillary_nb_images(mapillary_sample_dir):
    return len(os.listdir(os.path.join(mapillary_sample_dir, "images")))


@pytest.fixture
def mapillary_input_config():
    return "tests/data/mapillary/config_aggregate.json"


@pytest.fixture
def mapillary_nb_labels(mapillary_input_config):
    with open(mapillary_input_config) as fobj:
        config = json.load(fobj)
    return len(config["labels"])

@pytest.fixture
def mapillary_config(tmpdir_factory):
    return tmpdir_factory.getbasetemp().join('mapillary.json')


@pytest.fixture(scope='session')
def mapillary_training_data(tmpdir_factory):
    mapillary_subdir = tmpdir_factory.mktemp('mapillary', numbered=False)
    tmpdir_factory.mktemp('mapillary/images', numbered=False)
    tmpdir_factory.mktemp('mapillary/labels', numbered=False)
    return mapillary_subdir


@pytest.fixture
def shapes_image_size():
    return 64


@pytest.fixture
def shapes_nb_images():
    return 20


@pytest.fixture
def shapes_nb_labels():
    return 4


@pytest.fixture
def shapes_config(tmpdir_factory):
    return tmpdir_factory.getbasetemp().join('shapes.json')


@pytest.fixture(scope='session')
def shapes_training_data(tmpdir_factory):
    shapes_subdir = tmpdir_factory.mktemp('shapes', numbered=False)
    tmpdir_factory.mktemp('shapes/images', numbered=False)
    tmpdir_factory.mktemp('shapes/labels', numbered=False)
    return shapes_subdir
