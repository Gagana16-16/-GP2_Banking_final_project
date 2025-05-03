from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from bank_account.forms import RegisterForm
from bank_account.forms import WithdrawForm
class RegisterFormTest(TestCase):

    def test_form_valid_data(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertTrue(form.is_valid())

    def test_form_password_mismatch(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'password1': 'StrongPass123',
            'password2': 'WrongPass123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_form_missing_fields(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_duplicate_username(self):
        User.objects.create_user(username='testuser', password='testpass123')
        form = RegisterForm(data={
            'username': 'testuser',
            'password1': 'NewPass123',
            'password2': 'NewPass123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

from bank_account.forms import DepositForm

class DepositFormTest(TestCase):
    def test_form_valid_data(self):
        form = DepositForm(data={'amount': 100.00})
        self.assertTrue(form.is_valid())

    def test_form_invalid_amount_too_low(self):
        form = DepositForm(data={'amount': 0.50})
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)



class WithdrawFormTest(TestCase):

    def test_form_valid_amount(self):
        form = WithdrawForm(data={'amount': 100})
        self.assertTrue(form.is_valid())

    def test_form_amount_zero(self):
        form = WithdrawForm(data={'amount': 0})
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(
            form.errors['amount'],
            ['Ensure this value is greater than or equal to 1.']
        )

    def test_form_amount_negative(self):
        form = WithdrawForm(data={'amount': -50})
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(
            form.errors['amount'],
            ['Ensure this value is greater than or equal to 1.']
        )

    def test_form_amount_missing(self):
        form = WithdrawForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(
            form.errors['amount'],
            ['This field is required.']
        )
