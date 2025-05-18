from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('core', 'User')
    superuser = User.objects.create(
        username='admin',
        email='admin@example.com',
        password=make_password('Admin123!'),
        is_staff=True,
        is_superuser=True,
        role='superadmin',
        is_active=True
    )
    superuser.save()

def reverse_create_superuser(apps, schema_editor):
    User = apps.get_model('core', 'User')
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_remove_partenaire_type_commandeclient_nom_and_more'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_create_superuser),
    ] 