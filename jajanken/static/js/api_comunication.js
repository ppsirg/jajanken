
const baseURL = 'http://localhost:9000';
// const baseURL = 'http://192.168.0.13:9000';
const apiURL = '/api/';
const crsfRegExp = /value=".+"/g;

const playerAPIURL = baseURL+apiURL+'players/';
const matchAPIURL = baseURL+apiURL+'matches/';
const matchRoundAPIURL = baseURL+apiURL+'match-rounds/';
const matchEventAPIURL = baseURL+apiURL+'match-events/';


async function createPlayer(playerName) {
  // create a player or get created player with a given playerName
  try {
    const response = await axios.get(playerAPIURL)
    // handle success
    var found = keyInArray(playerName.toUpperCase(), response);
    if (!found) {
      console.log('need to create '+playerName.toUpperCase());
      try {
        const creationResponse = await axios.post(playerAPIURL,{
          name: playerName.toUpperCase(),
          csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
        });
        return creationResponse.data;
      } catch (e) {
        console.log(e);
      }
    } else {
      return found;
    }
  } catch (e) {
    console.log(e);
  }
}

async function createMatch(redPlayer, bluePlayer) {
// create a match given a redPlayer and bluePlayer
try {
  const response = await axios.post(matchAPIURL, {
    blue_player:playerAPIURL+bluePlayer+'/',
    red_player:playerAPIURL+redPlayer+'/',
    csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
  });
  return response.data;
} catch (e) {
  console.log(e);
}
}

async function createMatchRound(match) {
  // create match_round given its match
try {
  const response = await axios.post(matchRoundAPIURL, {
    match: matchAPIURL+match+'/',
    csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
  });
  return response.data;
} catch (e) {
  console.log(e);
}
}

async function createMatchEvent(player, choice, match_round) {
  // create match event
  try {
    const response = await axios.post(matchEventAPIURL, {
      player: playerAPIURL+player+'/',
      choice: choice,
      match_round: matchRoundAPIURL+match_round+'/',
      csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
    });
    return response.data;
  } catch (e) {
    console.log(e);
  }
}

function getWinner(match) {
axios.get(baseURL+'/winner/'+match)
.then(function (response) {
  console.log(response.data);
  return response.data
}).catch(function (error) {
  console.log(error);
})
}
