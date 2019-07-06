# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core import validators


class AllDiamondUrls(models.Model):
    diamond_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'all_diamond_urls'


class AllDiamonds(models.Model):
    good_name = models.CharField(max_length=255)
    good_price = models.IntegerField()
    sell_number = models.IntegerField()
    comment_number = models.IntegerField()
    belong_name = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    good_size = models.CharField(max_length=255)
    main_diamond = models.CharField(max_length=255, blank=True, null=True)
    assitant_diamond = models.CharField(max_length=255, blank=True, null=True)
    send_date = models.CharField(max_length=255, blank=True, null=True)
    good_exists = models.CharField(max_length=255, blank=True, null=True)
    detail_img = models.TextField()
    type_name = models.CharField(max_length=255, blank=True, null=True)
    good_img = models.TextField()

    class Meta:
        managed = False
        db_table = 'all_diamonds'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderForms(models.Model):
    sender_name = models.CharField(max_length=255)
    sender_phone = models.CharField(max_length=11,validators=[validators.MinLengthValidator(11,message='sssss')])
    sender_address = models.CharField(max_length=255)
    sender_post = models.CharField(max_length=255)
    sender_postcode = models.IntegerField(validators=[validators.MinLengthValidator(6),validators.MaxLengthValidator(6)])
    receiver_name = models.CharField(max_length=255)
    receiver_phone = models.CharField(max_length=11,validators=[validators.MinLengthValidator(11)])
    receiver_address = models.CharField(max_length=255)
    receiver_postcode = models.IntegerField(validators=[validators.MinLengthValidator(6),validators.MaxLengthValidator(6)])
    shop_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_forms'


class Shoppings(models.Model):
    good_name = models.CharField(max_length=255)
    main_diamond = models.CharField(max_length=255, blank=True, null=True)
    assitant_diamond = models.CharField(max_length=255, blank=True, null=True)
    good_size = models.CharField(max_length=255)
    good_number = models.IntegerField()
    good_price = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    first_price = models.IntegerField()
    good_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shoppings'


class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'
