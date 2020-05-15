$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp) {
    $.each(resp.results, function (key, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
