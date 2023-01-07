# from faker import Faker
# from model_bakery import baker
# import pytest
# from django.urls import reverse_lazy, reverse
#
# from apps.product.models.category import Category
#
#
# @pytest.mark.django_db
# class TestCategoryView:
#     @pytest.fixture
#     def url(self):
#         return reverse_lazy('apps:models-category')
#
#     def test_category_list_api(self, client, url):
#         response = client.get(url)
#         assert response.status_code == 200
#         assert len(response.data) == 2
#
#     def test_category_create_api(self, client, url):
#         url = reverse_lazy('category-list')
#         data = {
#             'name' : self.category.name
#         }
#         response = client.post(url, data)
#         assert response.status_code == 200
#
#
#     def test_category_update_api(self, client, category):
#         category= Category.objects.first()
#         url = reverse_lazy('category-detail', args=(category.pk,))
#         data = {
#             'name': self.category.name
#         }
#         response = client.patch(url, data, content_type='application/json')
#         assert response.status_code == 200
#         assert response.data['name'] == data['name']
#         assert response.data['id'] == str(category.pk)
#
#     def test_category_filter_api(self, client, products):
#         category = Category.objects.first()
#         url = reverse_lazy('category-list')
#         data = {
#             'name': self.caregory.name
#         }
#         response = client.get(url, data, content_type='application/json')
#         assert response.status_code == 200
#         assert response.data[0]['name'] == data['name']
#         assert response.data[0]['id'] == str(category.pk)
#         assert len(response.data) == 1
#
#     def test_product_wrong_filter_api(self, client, products):
#         product = Category.objects.first()
#         url = reverse_lazy('product-list')
#         data = {
#             'name': self.category.name
#         }
#         response = client.get(url, data, content_type='application/json')
#         assert response.status_code == 200
#         assert len(response.data) == 0
