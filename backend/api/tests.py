from django.test import TestCase
from django.urls import reverse


class ListTweetTest(TestCase):

    def setUp(self):
        url             = reverse('tweet-list-create')
        self.response   = self.client.get(url)

    def test_list_tweet(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.request['REQUEST_METHOD'], 'GET')


class CreateTweetTest(TestCase):

    def setUp(self):
        url     = reverse('tweet-list-create')
        data    = {
            'name': 'Walter White',
            'text': 'Just cooking!',
        }

        self.response = self.client.post(url, data)

    def test_create_tweet(self):
        self.assertEqual(self.response.status_code, 201)
        self.assertEqual(self.response.request['REQUEST_METHOD'], 'POST')
        self.assertEqual(self.response.data['name'], 'Walter White')
        self.assertEqual(self.response.data['text'], 'Just cooking!')
        self.assertNotEqual(self.response.data['datetime'], None)
        self.assertNotEqual(self.response.data['datetime'], '')

