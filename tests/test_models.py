# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test cases for Product Model

Test cases can be run with:
    nosetests
    coverage report -m

While debugging just these tests it's convenient to use this:
    nosetests --stop tests/test_models.py:TestProductModel

"""
import os
import logging
import unittest
from decimal import Decimal
from service.models import Product, Category, db
from service import app
from tests.factories import ProductFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)


######################################################################
#  P R O D U C T   M O D E L   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
class TestProductModel(unittest.TestCase):
    """Test Cases for Product Model"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Product.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        db.session.close()

    def setUp(self):
        """This runs before each test"""
        db.session.query(Product).delete()  # clean up the last tests
        db.session.commit()

    def tearDown(self):
        """This runs after each test"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_a_product(self):
        """It should Create a product and assert that it exists"""
        product = Product(name="Fedora", description="A red hat", price=12.50, available=True, category=Category.CLOTHS)
        self.assertEqual(str(product), "<Product Fedora id=[None]>")
        self.assertTrue(product is not None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.name, "Fedora")
        self.assertEqual(product.description, "A red hat")
        self.assertEqual(product.available, True)
        self.assertEqual(product.price, 12.50)
        self.assertEqual(product.category, Category.CLOTHS)

    def test_add_a_product(self):
        """It should Create a product and add it to the database"""
        products = Product.all()
        self.assertEqual(products, [])
        product = ProductFactory()
        product.id = None
        product.create()
        # Assert that it was assigned an id and shows up in the database
        self.assertIsNotNone(product.id)
        products = Product.all()
        self.assertEqual(len(products), 1)
        # Check that it matches the original product
        new_product = products[0]
        self.assertEqual(new_product.name, product.name)
        self.assertEqual(new_product.description, product.description)
        self.assertEqual(Decimal(new_product.price), product.price)
        self.assertEqual(new_product.available, product.available)
        self.assertEqual(new_product.category, product.category)
    def test_read_a_product(self):
        """It should Read a Product"""
        product = ProductFactory()
        # Set the ID of the product object to None and then call the create() method on the product.
        # Assert that the ID of the product object is not None after calling the create() method.
        # Fetch the product back from the system using the product ID and store it in found_product
        # Assert that the properties of the found_product match with the properties of the original product object, such as id, name, description and price.
    def test_delete_a_product(self):
        """It should Delete a Product"""
        product = ProductFactory()
        # Call the create() method on the product to save it to the database.
        # Assert  if the length of the list returned by Product.all() is equal to 1, to verify that after creating a product and saving it to the database, there is only one product in the system.
        # Call the delete() method on the product object, to remove the product from the database.
        # Assert if the length of the list returned by Product.all() is now equal to 0, indicating that the product has been successfully deleted from the database.
    def test_list_all_products(self):
        """It should List all Products in the database"""
        products = Product.all()
        # Assert if the products list is empty, indicating that there are no products in the database at the beginning of the test case.
        # Use for loop to create five Product objects using a ProductFactory() and call the create() method on each product to save them to the database.
        # Fetch all products from the database again using product.all()
        # Assert if the length of the products list is equal to 5, to verify that the five products created in the previous step have been successfully added to the database.
    def test_find_by_name(self):
        """It should Find a Product by Name"""
        products = ProductFactory.create_batch(5)
        # Use a for loop to iterate over the products list and call the create() method on each product to save them to the database.
        # Retrieve the name of the first product in the products list.
        # Use a list comprehension to filter the products based on their name and then use len() to calculate the length of the filtered list, and use the variable called count to hold the number of products that match the name.
        # Call the find_by_name() method on the Product class to retrieve products from the database that have the specified name.
        # Assert if the count of the found products matches the expected count.
        # Use a for loop to iterate over the found products and assert that each product's name matches the expected name, to ensure that all the retrieved products have the correct name.
    def test_find_by_availability(self):
        """It should Find Products by Availability"""
        products = ProductFactory.create_batch(10)
        # Use a for loop to iterate over the products list and call the create() method on each product to save them to the database.
        # Retrieve the availability of the first product in the products list.
        # Use a list comprehension to filter the products based on their availability and then use len() to calculate the length of the filtered list, and use the variable called count to hold the number of products that have the specified availability.
        # Call the find_by_availability() method on the Product class to retrieve products from the database that have the specified availability.
        # Assert if the count of the found products matches the expected count.
        # Use a for loop to iterate over the found products and assert that each product's availability matches the expected availability, to ensure that all the retrieved products have the correct availability.
    def test_find_by_availability(self):
        """It should Find Products by Category"""
        products = ProductFactory.create_batch(10)
        # Use a for loop to iterate over the products list and call the create() method on each product to save them to the database.
        # Retrieve the category of the first product in the products list.
        # Use a list comprehension to filter the products based on their category and then use len() to calculate the length of the filtered list, and use the variable called count to hold the number of products that have the specified category.
        # Call the find_by_category() method on the Product class to retrieve products from the database that have the specified category.
        # Assert if the count of the found products matches the expected count.
        # Use a for loop to iterate over the found products and assert that each product's category matches the expected category, to ensure that all the retrieved products have the correct category.
    #
    # ADD YOUR TEST CASES HERE
    #
