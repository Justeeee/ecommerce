from uuid import UUID

import pytest
from django.urls import reverse_lazy

from product.models.product import Product


@pytest.mark.django_db
class TestProductView:
    def test_create_model_region(self):
        product = Product.objects.create(name='Iphone 14 pro max')
        count = Product.objects.count()
        assert isinstance(product.pk, UUID)
        assert product.name == 'Iphone 14 pro max'
        assert count == 1

    def test_create_product_api(self, client):
        url = reverse_lazy('product-list')
        data = {
            'name': 'Iphone 14 pro max'
        }
        response = client.post(url, data)
        assert response.status_code == 201
        assert response.data['name'] == data['name']
        assert len(response.data['id']) == 36

    @pytest.fixture()
    def products(self):
        Product.objects.create(name='Iphone 14 pro max')
        Product.objects.create(name='Macbook Pro')

    def test_product_list_api(self, client, products):
        url = reverse_lazy('region-list')
        # url = '/api/v1/product/'
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_product_update_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
        url = reverse_lazy('product-detail', args=(product.pk,))
        data = {
            'name': 'Samsung Galaxy S22'
        }
        response = client.patch(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(product.pk)

    def test_product_filter_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/region?name=Samsung+Galaxy+S22'
        url = reverse_lazy('product-list')
        data = {
            'name': 'Iphone 14 pro max'
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data[0]['name'] == data['name']
        assert response.data[0]['id'] == str(product.pk)
        assert len(response.data) == 1

    def test_region_wrong_filter_api(self, client, products):
        product = Product.objects.first()
        '/api/v1/product?name=Macbook+Air'
        url = reverse_lazy('product-list')
        data = {
            'name': 'Macbook Air'
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == 0