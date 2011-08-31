from django.core.urlresolvers import reverse


class AuthenticationMixin(object):

    def _unauthenticated(self, target):
        response = self.client.get(target)
        login_url = "%s?next=%s" % (reverse("login"), target)
        self.assertRedirects(response, login_url, 302)

    def _authenticated(self, target):
        response = self.client.get(target)
        self.assertEqual(response.status_code, 200)


class AuthorizationMixin(object):

    def _unauthorized(self, target):
        response = self.client.get(target)
        self.assertEqual(response.status_code, 404)

    def _authorized(self, target):
        response = self.client.get(target)
        self.assertEqual(response.status_code, 200)
