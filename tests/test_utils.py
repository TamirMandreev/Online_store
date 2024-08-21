import pytest
from src.classes.Category import Category
from src.classes.Product import Product

from src.utils import load_categories_from_json



def test_utils():
    assert isinstance(load_categories_from_json('../src/products.json')[0], Category)
    assert isinstance(load_categories_from_json('../src/products.json'), list)