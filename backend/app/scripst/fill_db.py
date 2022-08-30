from plane.models import Plane
from user.models import User


def create_planes(count: int = 10):
    planes = [Plane() for _ in range(count + 1)]
    Plane.objects.bulk_create(planes)


def create_admin():
    try:
        User.objects.get(username='mac')
    except User.DoesNotExist:
        admin = User.objects.create_superuser(username='mac')
        admin.set_password('mac')
        admin.save()


def fill_db(planes: bool = 10, admin: bool = True):
    if planes and Plane.objects.all().count() < 10:
        create_planes(planes)

    if admin:
        create_admin()
