"""Login Testcase"""
from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check


class LoginTestCase(TestCase):
    """Login tests"""

    def test_it_sends_link(self):
        """Tests sending login link to mail"""
        check = Check()
        check.save()

        session = self.client.session
        session["welcome_code"] = str(check.code)
        session.save()

        form = {"email": "alice@example.org"}

        result = self.client.post("/accounts/login/", form)
        assert result.status_code == 302

        ### Assert that a user was created
        assert User.objects.select_related('profile').get(email=form['email'])

        # And email sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Log in to healthchecks.io')

        ### Assert contents of the email body
        self.assertIn(
            "To log into healthchecks.io, please open the link below:", mail.outbox[0].body)

        ### Assert that check is associated with the new user
        new_user = User.objects.get(email="alice@example.org")
        check.refresh_from_db()
        self.assertEqual(check.user, new_user)

    def test_bad_link_from_session(self):
        """Checks bad link from session"""
        self.client.session["bad_link"] = True
        self.client.get("/accounts/login/")
        assert "bad_link" not in self.client.session

        ### Any other tests?
