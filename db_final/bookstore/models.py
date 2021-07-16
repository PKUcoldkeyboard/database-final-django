from django.db import models

# Create your models here.
class BmsBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    category = models.ForeignKey('BmsCategory', models.DO_NOTHING)
    description = models.CharField(max_length=1000, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, blank=True, null=True)
    author = models.CharField(max_length=100)
    press = models.CharField(max_length=30)
    language = models.CharField(max_length=10, blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bms_book'


class BmsBookDiscount(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.OneToOneField(BmsBook, models.DO_NOTHING)
    count = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bms_book_discount'


class BmsBookFullReduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.OneToOneField(BmsBook, models.DO_NOTHING)
    full_price = models.ForeignKey(BmsBook, models.DO_NOTHING, db_column='full_price', related_name = 'book_full_price')
    reduce_price = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bms_book_full_reduction'


class BmsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'bms_category'


class BmsComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.OneToOneField(BmsBook, models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField(unique=True)
    star = models.PositiveIntegerField()
    read_count = models.PositiveIntegerField()
    collect_count = models.PositiveIntegerField()
    picture = models.CharField(max_length=1000)
    reply_count = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    show_status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bms_comment'


class BmsCommentReply(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.OneToOneField(BmsComment, models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField(unique=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bms_comment_reply'


class BmsCommentReplyContent(models.Model):
    reply = models.OneToOneField(BmsCommentReply, models.DO_NOTHING, primary_key=True)
    reply_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'bms_comment_reply_content'


class BmsConmmntContent(models.Model):
    comment = models.OneToOneField(BmsComment, models.DO_NOTHING, primary_key=True)
    comment_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'bms_conmmnt_content'

class OmsCartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(BmsBook, models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oms_cart_item'
        unique_together = (('user', 'book'), ('user', 'book'), ('user', 'book'),)


class OmsOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.CharField(unique=True, max_length=64)
    user_id = models.PositiveBigIntegerField(unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    freight_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_status = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    delete_status = models.PositiveIntegerField()
    note = models.CharField(max_length=500)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    receive_time = models.DateTimeField()
    pay_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oms_order'


class Role(models.Model):
    role_id = models.PositiveIntegerField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'role'


class UmsUserEmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=100)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ums_user_email'


class UmsUserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING)
    nick_name = models.CharField(unique=True, max_length=64)
    icon = models.CharField(max_length=255)
    gender = models.PositiveIntegerField()
    birthday = models.DateTimeField()
    city = models.CharField(max_length=64)
    job = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ums_user_info'


class UmsUserReceiveInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING)
    receiver_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=64)
    post_code = models.CharField(max_length=6)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=128)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ums_user_receive_info'


class UmsUserStatisticsInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField('User', models.DO_NOTHING)
    consume_amount = models.DecimalField(max_digits=10, decimal_places=2)
    login_count = models.PositiveIntegerField()
    order_count = models.PositiveIntegerField()
    coupon_count = models.PositiveIntegerField()
    collect_book_count = models.PositiveIntegerField()
    collect_comment_count = models.PositiveIntegerField()
    recent_order_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ums_user_statistics_info'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20, db_collation='utf8mb4_general_ci')
    password = models.CharField(max_length=60, db_collation='utf8mb4_general_ci')

    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'