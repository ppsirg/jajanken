const color_equivalences = {
	red: '#800000',
	blue: '#000080'
}

Vue.component('player-form-name',{
	delimiters: ['[[', ']]'],
	props: [
		'color',
	],
	computed: {
		player_color: function () {
			let real_color = this.get_true_color();
			return 'color: ' + real_color + ';';
		},
		player_border: function () {
			let real_color = this.get_true_color();
			return 'border: 3px solid ' + real_color + '; color: '+real_color+';';
		}
	},
	methods: {
		get_true_color: function () {
			let real_color = color_equivalences[this.color];
			return real_color;
		}
	},
	template: `
	<div id="player-form-name" class="game-description">
		<form class="" method="post">
			<div class="player-form-name-title" v-bind:style="player_color">introduce your name</div>
			<input type="text" name="playerName" v-bind:style='player_border' value="">
			<button type="submit" name="save-user-button" v-bind:style="player_color">Ready!!</button>
		</form>
	</div>
	`
})
Vue.component('roundSelector',{
	delimiters: ['[[', ']]'],
	template: `
	<div>
	</div>
	`
})
Vue.component('match-control',{
	delimiters: ['[[', ']]'],
	props: [
    'scissors',
		'rock',
		'paper',
		'color',
		'header_label',
		'button_label'
  ],
	data: function(){
  	return {
    	players_color: 'color: [[this.color]];',
    }
  },
	computed: {
		player_color: function () {
			let real_color = color_equivalences[this.color];
			return 'color: ' + real_color + ';';
		}
	},
	template: `
	<div>
	<div class="game-description" v-bind:style="player_color">
		[[header_label]]
	</div>
	<div class="landing-options">
		<img v-bind:src="scissors" alt="scissors">
		<img v-bind:src="rock" alt="rock">
		<img v-bind:src="paper" alt="paper">
	</div>
	<div class="action-buttons">
		<button id="initial_start_button" type="button" name="initial_start_button">[[button_label]]</button>
	</div>
	</div>
	`
})
Vue.component('matchEnder',{
	delimiters: ['[[', ']]'],
	template: `
	<div>
	</div>
	`
})



window.onload = function () {
	var app = new Vue({
	el: '#app',
	delimiters: ['[[', ']]'],
	})
}
