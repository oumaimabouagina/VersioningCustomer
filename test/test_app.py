import os
import sys
import pytest
from flask import Flask
from pytest import fixture

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask app and ValuePredictor from the main application file
from app import app, ValuePredictor

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/index')
    assert b'Customer Segmentation' in response.data


def test_result_page():
    # Create a test client using Flask's test_client method
    client = app.test_client()

    # Send a POST request to the result page with valid input
    response = client.post('/result', data={'param1': '19', 'param2': '39'})

    # Check if the response contains the expected content
    assert b'Customers with low annual income and low annual spending score' in response.data

