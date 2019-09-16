const color_equivalences = {
	red: '#800000',
	blue: '#000080'
}


Vue.component('player-form-name',{
  // ask a player its name and associate with a player
  name: 'playerformname',
	delimiters: ['[[', ']]'],
	props: [
		'color',
	],
  data: function () {
    return {
      playerName: '',
      players: {
        red: {},
        blue: {},
      }
    };
  },
	computed: {
		real_color: function () {
			return color_equivalences[this.key_color];
		},
		key_color: function () {
			let red_pattern = /.*red.*/;
			return red_pattern.test(this.color) ? 'red':'blue';
		},
	},
	methods: {
		swap_color: function (event) {
			event.preventDefault();
      let playerName = document.getElementsByName('playerName')[0].value;
      console.log(playerName);
      axios.post(playerAPIURL, {
        name: playerName.toUpperCase(),
        csrfmiddlewaretoken: csrfmiddlewaretoken_dj,
      })
      .then(player_obj => (this.next_step(player_obj.data)))
      .catch(err => this.find_player())
		},
    find_player: function () {
      axios.get(playerAPIURL)
      .then(resp => (this.next_step(resp.data)))
      .catch(err => (console.log(err)));
    },
    next_step: function (player_obj) {
      this.players[this.color]['id'] = player_obj['id'];
      this.players[this.color]['name'] = player_obj['name'];
      this.$emit('swap_color', this);
    }
	},
	template: `#player-form-name-template`,
})


Vue.component('match-control',{
  // form with options of game, color change
  name: 'matchcontrol',
	delimiters: ['[[', ']]'],
	props: [
    'scissors',
		'rock',
		'paper',
		'color',
		'form_enabled',
		'header_label',
		'button_label',
    'action_url',
  ],
	data: function () {
		return {
			choice: 2,
		}
	},
	computed: {
		real_color: function () {
			return color_equivalences[this.key_color];
		},
		key_color: function () {
			let red_pattern = /.*red.*/;
			return red_pattern.test(this.color) ? 'red':'blue';
		},
		scissors_link: function() {
			return this.color_aware_url(this.scissors, this.key_color);
		},
		rock_link: function() {
			return this.color_aware_url(this.rock, this.key_color);
		},
		paper_link: function() {
			return this.color_aware_url(this.paper, this.key_color);
		},
		is_form: function () {
			return this.form_enabled == 'yes';
		},
		is_landing: function () {
			return this.form_enabled == 'no';
		},
	},
	methods: {
		color_aware_url: function (url, color) {
			let red_pattern = /.+-red\.svg/;
			let current_color = red_pattern.test(url) ? '-red.' : '-blue.';
			let new_color = '-' + color + '.';
			return url.replace(current_color, new_color);
		},
		choice_handler: function (event) {
			console.log(event.target.value);
		},
		swap_state: function (event) {
			event.preventDefault();
			if (this.button_label == 'START!!') {
				this.$emit('swap_component', this);
			} else {
				this.$emit('swap_color', this);
			}
		}
	},
	template: `#match-control-template`,
})


Vue.component('scores-bar', {
  // show the scores of players
  name: 'scoresbar',
	delimiters: ['[[', ']]'],
	template: '#scores-bar-template'
})

Vue.component('score-button', {
  name: 'scorebutton',
	delimiters: ['[[', ']]'],
	props: [
		'img_url'
	],
	computed: {
		color: function () {
			let red_pattern = /.*red.*/;
			return red_pattern.test(this.img_url) ? 'red':'blue';
		}
	},
	template: '#score-button-template'
})
