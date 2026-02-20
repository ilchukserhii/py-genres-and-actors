import init_django_orm  # noqa: F401
from db.models import Actors, Genre
from django.db.models import QuerySet


def main() -> QuerySet:
    list_of_genres = ["Western", "Action", "Dramma"]
    list_of_actors = [
        ("George", "Klooney"), ("Kianu", "Reaves"), ("Scarlett", "Keegan"),
        ("Will", "Smith"), ("Jaden", "Smith"), ("Scarlett", "Johansson")
    ]
    for genre in list_of_genres:
        Genre.objects.create(
            name=genre,
        )
    for first_name, last_name in list_of_actors:
        Actors.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    Genre.objects.filter(name="Dramma").update(
        name="Drama",
    )
    Actors.objects.filter(last_name="Klooney").update(
        last_name="Clooney",
    )
    Actors.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu", last_name="Reeves"
    )
    Genre.objects.filter(name="Action").delete()
    Actors.objects.filter(first_name="Scarlett").delete()
    return Actors.objects.filter(last_name="Smith").order_by("first_name")
