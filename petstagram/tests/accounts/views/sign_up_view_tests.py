from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user4526',
        'email': 'test_user@testmail.com',
        'password1': 'passw3845',
        'password2': 'passw3845',
    }

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
            follow=True,
        )

        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)
