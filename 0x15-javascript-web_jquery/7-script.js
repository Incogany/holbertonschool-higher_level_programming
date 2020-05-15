$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (resp) {
    $('DIV#character').text(resp.name);
  });
});
