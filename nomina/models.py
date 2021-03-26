# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=240)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(unique=True, max_length=250)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=90)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class CfBanco(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'cf_banco'
    def __unicode__(self):
        return self.nombre

class CfBancoCuenta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    cuenta = models.CharField(max_length=90, blank=True)
    cf_banco_id = models.IntegerField()
    class Meta:
        db_table = u'cf_banco_cuenta'

class CfCargo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'cf_cargo'

class CfDepartamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'cf_departamento'

class CfEmpleado(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=30)
    sexo = models.CharField(max_length=3)
    nombres = models.CharField(max_length=135, blank=True)
    apellidos = models.CharField(max_length=135, blank=True)
    cedula = models.IntegerField(null=True, blank=True)
    rif = models.CharField(max_length=60, blank=True)
    tlf_hab = models.CharField(max_length=135, blank=True)
    tlf_cel = models.CharField(max_length=135, blank=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=1500, blank=True)
    direccion2 = models.CharField(max_length=1500, blank=True)
    email = models.CharField(max_length=150, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    cuenta_banco = models.CharField(max_length=90, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    fecha_egreso = models.DateField(null=True, blank=True)
    ruta_foto = models.CharField(max_length=750, blank=True)
    cf_cargo_id = models.IntegerField()
    cf_empleado_tipo_id = models.IntegerField()
    cf_departamento_id = models.IntegerField()
    cf_nomina_tipo_id = models.IntegerField()
    cf_banco_id = models.IntegerField()
    class Meta:
        db_table = u'cf_empleado'

class CfEmpleadoTipo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300)
    class Meta:
        db_table = u'cf_empleado_tipo'

class CfEmpresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    razon_social = models.CharField(max_length=300, blank=True)
    rif = models.CharField(max_length=60, blank=True)
    nit = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=135, blank=True)
    tlf = models.CharField(max_length=135, blank=True)
    fax = models.CharField(max_length=135, blank=True)
    ruta_foto = models.CharField(max_length=600, blank=True)
    class Meta:
        db_table = u'cf_empresa'

class CfNominaTipo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300)
    dias_pago = models.IntegerField()
    nro_periodos = models.IntegerField()
    class Meta:
        db_table = u'cf_nomina_tipo'

class CfSueldo(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_desde = models.DateField()
    mensual = models.FloatField()
    semanal = models.FloatField()
    diario = models.FloatField()
    cf_empleado_id = models.IntegerField()
    class Meta:
        db_table = u'cf_sueldo'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(unique=True, max_length=250)
    model = models.CharField(unique=True, max_length=250)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class NominaNomina(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'nomina_nomina'

