

// window.onload = function () {
	var app = new Vue({
	el: '#app',
	delimiters: ['[[', ']]'],
	data: {
		color_name: 'red',
		scores: {red:0, blue:0},
		initial_component: true,
		scores_enabled: false,
		name_component_shown: false,
		move_component_shown: false,
		players: {
			red: {},
			blue: {},
		},
		match: {},
		rounds: [],
		events: [],
		current_event: 0,
		current_round: 0,
	},
	methods: {
		on_swap_color_form_name: function (current_obj) {
			this.players[current_obj.color]['id'] = current_obj.players[current_obj.color]['id'];
      this.players[current_obj.color]['name'] = current_obj.players[current_obj.color]['name'];
			let new_color = current_obj.key_color == 'red' ? "blue": "red";
			this.color_name = new_color;
			let done_red = Object.getOwnPropertyNames(this.players.red);
			let done_blue = Object.getOwnPropertyNames(this.players.blue);
			if (done_red.includes("id") && done_blue.includes("id")) {
				console.log('done');
				this.on_swap_component(current_obj);
			} else {
				console.log('not yet');
				current_obj.$forceUpdate();
			}
		},
		on_swap_color_control: function (current_obj) {
			axios.post(matchEventAPIURL, {
	      player: playerAPIURL+this.players[current_obj.key_color]['id']+'/',
	      choice: current_obj.choice,
	      match_round: matchRoundAPIURL+this.rounds[this.current_round]['id']+'/',
	      csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
	    })
			this.on_swap_color(current_obj);
			if (this.current_event == 0) {
				this.current_event +=1;
			} else {
				this.current_event = 0;
				if (this.current_round == 2) {
					this.on_swap_component(current_obj);
				} else {
					axios.get(baseURL+'/winner_round/'+this.rounds[this.current_round]['id'])
					.then(response => (this.update_score_bar(response.data)))
					.catch(err => (this.show_error(err)));
					this.current_round += 1;
				}
			}
		},
		on_swap_color: function (current_obj) {
			let new_color = current_obj.key_color == 'red' ? "blue": "red";
			this.color_name = new_color;
			current_obj.$forceUpdate();
		},
		on_swap_component: function (current_obj) {
			if (this.initial_component) {
				// change initial widget for form that asks user name
				this.initial_component = false;
				this.name_component_shown = true;
			} else if (this.name_component_shown) {
				// switch form for user creation into moves widget
				this.name_component_shown = false;
				this.move_component_shown = true;
				this.scores_enabled = true;
				this.create_match();
			} else if (this.move_component_shown) {
				// change game to ending component
				axios.get(baseURL+'/winner/'+this.match.id)
				.then(resp => (this.show_winner(resp.data)))
				.catch(err => (this.show_error(err)));
			}
		},
		create_match: function () {
			// create match in backend
			return axios.post(matchAPIURL, {
		    blue_player:playerAPIURL+this.players.blue.id+'/',
		    red_player:playerAPIURL+this.players.red.id+'/',
		    csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
		  })
			.then(response => (this.create_rounds(response.data, 3)))
			.catch(err => (this.show_error(err)));
		},
		create_rounds: function (match_obj, number_rounds) {
			// save match information in front and create rounds in backend
			this.match.id = match_obj.id;
			this.match.blue_player = match_obj.blue_player;
			this.match.red_player = match_obj.red_player;
			for (var i = 0; i < number_rounds; i++) {
				axios.post(matchRoundAPIURL, {
			    match: matchAPIURL+match_obj.id+'/',
			    csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
			  })
				.then(response => (this.rounds.push(response.data)))
				.catch(err => (this.show_error(err)));
			}
		},
		show_winner: function (winner_obj) {
			console.log(winner_obj);
			if (winner_obj['winner']) {
				var winner_name = winner_obj.winner == this.players.red ? this.players.red.name : this.players.blue.name
				alert('El ganador es '+winner_name);
			} else {
				alert('hubo un empate entre '+this.players.red.name+' y '+this.players.blue.name);
			}
			location.reload();
		},
		show_error: function (err) {
			console.log(err);
			alert('se ha prresentado un inconveniente, es necesario re-iniciar la partida');
			location.reload();
		},
		update_score_bar: function (winner_obj) {
			console.log(winner_obj);
			if (winner_obj.winner == this.players.red.id) {
				this.scores['red'] +=1;
				console.log('red won');
			} else if (winner_obj.winner == this.players.blue.id) {
				this.scores['blue'] +=1;
				console.log('blue won');
			}
		}
	},

	})
// }
