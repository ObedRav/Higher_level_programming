$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(character) {
  $('#character').text(character.name);
});