from datetime import datetime

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
    session_date: datetime = None,
) -> MovieSession:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = queryset.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> None:
    update_data = {}

    if show_time:
        update_data["show_time"] = show_time

    if movie_id:
        update_data["movie_id"] = movie_id

    if cinema_hall_id:
        update_data["cinema_hall_id"] = cinema_hall_id

    if update_data:
        MovieSession.objects.filter(id=session_id).update(**update_data)


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()