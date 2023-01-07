import random
from uuid import UUID

import pytest
from django.urls import reverse_lazy

from apps.product.models import Product

from django.test import TestCase




class TestProductView:
    def test_create_model_product(self):
        product = Product.objects.create(name='Samsung S22', price=random.randint(1, 10))
        count = Product.objects.count()
        assert isinstance(product.pk, UUID)
        assert product.name == 'Samsung S22'
        assert count == 1

    def test_create_product_api(self, client):
        url = reverse_lazy('product-list')
        data = {
            "name": "p1",
            "price": 12.00,
        }
        response = client.post(url, data)
        assert response.status_code == 201
        assert response.data['name'] == data['name']
        assert len(response.data['id']) == 36

    @pytest.fixture()
    def products(self):
        Product.objects.create(name='Samsung S22', price=random.randint(1, 10))
        Product.objects.create(name='Macbook Pro', price=random.randint(1, 10))

    def test_product_list_api(self, client, products):
        url = reverse_lazy('products-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_product_update_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
        url = reverse_lazy('product-detail', args=(product.pk,))
        data = {
            'name': 'Samsung S22'
        }
        response = client.patch(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(product.pk)

    def test_product_filter_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product?name=Samsung+S22'
        url = reverse_lazy('product-list')
        data = {
            "id": "8ac39cfa-e7c4-4445-af73-e3599234a439",
            "name": "Samsung S22",
        }
        response = client.get

    def products(self):
        Product.objects.create(name='Samsung S22', price=random.randint(1, 10))
        Product.objects.create(name='Macbook Pro', price=random.randint(1, 10))

    def test_product_list_api(self, client, products):
        url = reverse_lazy('product-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_product_update_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
        url = reverse_lazy('product-detail', args=(product.pk,))
        data = {
            'name': 'Samsung S22'
        }
        response = client.patch(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(product.pk)

    def test_product_filter_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product?name=Samsung+S22'
        url = reverse_lazy('product-list')
        data = {
            "id": "8ac39cfa-e7c4-4445-af73-e3599234a439",
            "name": "Samsung S22",
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data[0]['name'] == data['name']
        assert response.data[0]['id'] == str(product.pk)
        assert len(response.data) == 2
