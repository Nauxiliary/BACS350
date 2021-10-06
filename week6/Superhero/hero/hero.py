from .models import Hero


def add_hero(hero_name, hero_id):
    return Hero.objects.create(name=hero_name, description=hero_id)


def list_heroes():
    return Hero.objects.all()


def get_hero(pk):
    return Hero.objects.get(pk=pk)


def get_identity(id):
    return Hero.objects.get(description=id)


def get_hero_name(supername):
    return Hero.objects.get(name=supername)


def set_hero_id(pk, id):
    w = get_hero(pk)
    w.description = id
    w.save()


def set_hero_name(pk, name):
    w = get_hero(pk)
    w.name = name
    w.save()


def delete_hero(pk):
    Hero.objects.get(pk=pk).delete()
