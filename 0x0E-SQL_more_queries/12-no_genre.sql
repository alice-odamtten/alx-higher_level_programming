-- a script that lists all shows contained in database that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
