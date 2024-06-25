import pytest
from pyicu_slugify.slugify import pyicu_slugify

def test_basic_slugify():
    assert pyicu_slugify("Hello World!") == "hello-world"

def test_german_slugify():
    assert pyicu_slugify("Über den Wölken", "de") == "uber-den-wolken"

# Add more tests as needed