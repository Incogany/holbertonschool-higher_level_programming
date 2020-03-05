-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.title, tv_genres.name FROM tv_genres RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id ORDER BY tv_shows.title, tv_genres.name ASC;
