# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from rest_framework import status
# from rest_framework.test import APIClient
# from review.models import Review  # 게시글 모델 import

# class PostTestCase(TestCase):
#     def setUp(self):
#         # 테스트를 위한 사용자 및 게시글 작성
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             password='testpassword',
#             google_id = 'ekdlsdl0@hufs.ac.kr',
#             nickname = 'test',
#             country = 'korea'
#         )
#         self.client = APIClient()

#     def test_post_creation_with_google_token(self):
#         # 구글 로그인 토큰 얻기 (이미 가지고 있다고 가정)
#         google_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNzI2NzI1LCJpYXQiOjE3MDE0MzA3MjUsImp0aSI6Ijk5NzIzYjQ3MTVjODQ2OGJiMjFmZjNiOWZiMjE0MWI4IiwidXNlcl9pZCI6MX0.NEQyF6uwL6L3Jde6XvIaOwgUn83A4XfVLKmHMmHpvRA'

#         # 게시글을 포스트하는 API 엔드포인트 URL
#         url = reverse('review_creation_view')

#         # 로그인한 사용자로 토큰을 사용하여 POST 요청 보내기
#         response = self.client.post(url, {'title': 'Test Post', 'content': 'Test Content'}, HTTP_AUTHORIZATION=f'Bearer {google_token}')

#         # 테스트 결과 확인
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
