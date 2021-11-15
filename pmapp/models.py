from django.contrib.auth.models import User
from django.db import models


class Server(models.Model):
    DATASERVER = '数据服务器'
    APPSERVER = '应用服务器'
    INSERVER = '综合服务器'
    WINDOWS = 'WINDOWS'
    LINUX = 'LINUX'
    COMPANY = '公司'
    PCU = '省联社'
    OTHER = '其他'
    server_type_choice = [
        (DATASERVER, '数据服务器'),
        (APPSERVER, '应用服务器'),
        (INSERVER, '综合服务器')
    ]
    server_system_choice = [
        (WINDOWS, 'WINDOWS'),
        (LINUX, 'LINUX'),
    ]
    server_belong_choice = [
        (COMPANY, '公司'),
        (PCU, '省联社'),
        (OTHER, '其他'),
    ]
    server_name = models.CharField(max_length=255, null=False)
    server_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    server_domain = models.CharField(max_length=255, null=False)
    server_belong = models.CharField(max_length=255, null=False, choices=server_belong_choice)
    server_type = models.CharField(max_length=255, null=False, choices=server_type_choice)
    server_system = models.CharField(max_length=255, null=False, choices=server_system_choice)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器管理'
    #     managed = False
    #     db_table = 'pm_server'

    def __str__(self):
        return self.server_name


class Project(models.Model):
    APPR = '立项'
    GOINGALINE = '上线'
    OFFLINE = '下线'
    COLLECTION_ING = '收款中'
    RECEIVED = '已收款'
    FOR_COLLECTION = '待收款'
    TO_EXPIRE = '即将过期'
    HAVE_EXPIRED = '已过期'
    NOT_OUT_OF_DATE = '质保中'

    project_status_choice = [
        (APPR, '立项'),
        (GOINGALINE, '上线'),
        (OFFLINE, '下线'),
    ]
    payment_status_choice = [
        (COLLECTION_ING, '收款中'),
        (RECEIVED, '已收款'),
        (FOR_COLLECTION, '待收款'),
    ]
    quality_status_choice = [
        (TO_EXPIRE, '即将过期'),
        (HAVE_EXPIRED, '已过期'),
        (NOT_OUT_OF_DATE, '质保中'),
    ]
    project_name = models.CharField(max_length=255, null=False)
    bank = models.CharField(max_length=255, null=False)
    project_time = models.DateField(null=False)
    ex_online_time = models.DateField(null=False)
    ac_online_time = models.DateField(null=False)
    sales_price = models.DecimalField(max_digits=24, decimal_places=6, null=False)
    development_cost = models.DecimalField(max_digits=24, decimal_places=6, null=False)
    project_status = models.CharField(max_length=32, null=False, choices=project_status_choice)
    quality_status = models.CharField(max_length=255, null=False, choices=quality_status_choice,
                                      default=NOT_OUT_OF_DATE)
    payment_status = models.CharField(max_length=255, null=False, choices=payment_status_choice,
                                      default=FOR_COLLECTION)
    amount_collected = models.IntegerField(null=False, default=0)
    amount_uncollected = models.IntegerField(null=False, default=0)
    payment_process = models.IntegerField(null=False, default=0)
    server = models.ManyToManyField(Server)
    project_user = models.ManyToManyField(User)

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目管理'
    #     managed = False
    #     db_table = 'pm_project'

    def __str__(self):
        return self.project_name


class CollectionRecord(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, null=False)
    payment_periods = models.IntegerField(null=False)
    payee = models.ForeignKey(User, models.DO_NOTHING, null=False)
    current_collection = models.DecimalField(max_digits=24, decimal_places=6, null=False)
    receipt_date = models.DateField(null=False)

    class Meta:
        verbose_name = '收款记录'
        verbose_name_plural = '收款记录管理'
    #     managed = False
    #     db_table = 'pm_collection_record'

    def __str__(self):
        return u'%s收款记录第%s期' % (self.project, self.payment_periods)


class QualityRecord(models.Model):
    project = models.ForeignKey('Project', models.DO_NOTHING, null=False)
    guarantee_period = models.CharField(max_length=255, null=False)
    quality_people = models.ForeignKey(User, models.DO_NOTHING, null=False)
    quality_money = models.IntegerField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    class Meta:
        verbose_name = '质保记录'
        verbose_name_plural = '质保记录管理'
    #     managed = False
    #     db_table = 'pm_quality_record'

    def __str__(self):
        return u'%s质保记录第%s期' % (self.project, self.guarantee_period)
