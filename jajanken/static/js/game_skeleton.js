
async function main_game() {
  var nameRed = 'julia';
  var nameBlue = 'estefania';

  // create red player
  var redPlayer = await createPlayer(nameRed);
  // create blue player
  var bluePlayer = await createPlayer(nameBlue);
  // create match
  var current_match = await createMatch(redPlayer.id, bluePlayer.id);
  console.log(current_match);
  // for 3 times
  for (var i = 0; i < 3; i++) {
    //   create match round
    var current_round = await createMatchRound(current_match.id);
    //   create match event for player red
    var red_event = await createMatchEvent(redPlayer.id, 1, current_round.id);
    //   create match event for player blue
    var blue_event = await createMatchEvent(bluePlayer.id, 2, current_round.id);
  }
  // calculate winner
  var winner = getWinner(current_match.id);
}
main_game();
