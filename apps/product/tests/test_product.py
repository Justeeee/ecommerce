from uuid import UUID

from faker import Faker
from model_bakery import baker
import pytest
from django.urls import reverse_lazy, reverse

from apps.product.models.product import Product


@pytest.mark.django_db
class TestProductView:
    @pytest.fixture()
    def product(self):
        fake = Faker()
        product = baker.make(
            Product,
            name = fake.random.choice(Product.Type.choices),
        )

        return product

    @pytest.fixture
    def url(self):
        return reverse_lazy('apps:models-product')

    def test_product_list_api(self, client, url):
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_product_create_api(self, client, url):
        url = reverse_lazy('product-list')
        data = {
            'name' : self.product.name
        }
        response = client.post(url, data)
        assert response.status_code == 200


    def test_product_update_api(self, client, products):
        product = Product.objects.first()
        url = reverse_lazy('product-detail', args=(product.pk,))
        data = {
            'name': self.product.name
        }
        response = client.patch(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['name'] == data['name']
        assert response.data['id'] == str(product.pk)

    def test_product_filter_api(self, client, products):
        product = Product.objects.first()
        url = reverse_lazy('product-list')
        data = {
            'name': self.product.name
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert response.data[0]['name'] == data['name']
        assert response.data[0]['id'] == str(product.pk)
        assert len(response.data) == 1

    def test_product_wrong_filter_api(self, client, products):
        product = Product.objects.first()
        url = reverse_lazy('product-list')
        data = {
            'name': self.product.name
        }
        response = client.get(url, data, content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == 0


