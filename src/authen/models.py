from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import uuid


# Create your models here.

GENDER_CHOICES = {
    'M': "Male",
    'F': "Female",
    'O': 'Others'
}

USER_TYPE = {
    'ADMIN': 'admin',
    'TEAM_LEAD': 'teamlead',
    'EMP': 'employee',
}


class UUIDModel(models.Model):
    """
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return "{}, {}, {} - {}".format(self.line1, self.line2,
                                        self.city, self.state, self.zipcode)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=120, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=120, blank=True)
    # E-Mail is the username for accounts
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    username = models.CharField(max_length=60, unique=True, db_index=True)

    github_handle = models.CharField(max_length=60)
    is_admin = models.BooleanField(default=False)
    is_organization_mail = models.BooleanField(default=False)

    phone = models.CharField(max_length=10, null=True, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES.items(), default='M')
    address = models.OneToOneField(Address, null=True, blank=True)
    profile_image_url = models.URLField()

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined', )

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name.strip()

    def add_to_group(self, grp):
        try:
            g = Group.objects.get(name=USER_TYPE[grp])
        except Exception as e:
            print e
            return False

        self.groups.add(g)
        self.save()
        return True
