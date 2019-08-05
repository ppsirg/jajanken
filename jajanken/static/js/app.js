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
			this.$emit('swap_color', this);
		}
	},
	template: `#player-form-name-template`,
})

Vue.component('match-control',{
	delimiters: ['[[', ']]'],
	props: [
    'scissors',
		'rock',
		'paper',
		'color',
		'header_label',
		'button_label',
  ],
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
	},
	methods: {
		color_aware_url: function (url, color) {
			let red_pattern = /.+-red\.svg/;
			let current_color = red_pattern.test(url) ? '-red.' : '-blue.';
			let new_color = '-' + color + '.';
			return url.replace(current_color, new_color);
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
	delimiters: ['[[', ']]'],
	template: '#scores-bar-template'
})

Vue.component('score-button', {
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
	},
	methods: {
		on_swap_color: function (current_obj) {
			let new_color = current_obj.key_color == 'red' ? "blue": "red";
			this.color_name = new_color;
			current_obj.$forceUpdate();
		},
		on_swap_component: function (current_obj) {
			if (this.initial_component) {
				this.initial_component = false;
				this.name_component_shown = true;
			} else if (this.name_component_shown) {
				this.name_component_shown = false;
				this.move_component_shown = true;
			}
		}
	},
	})
// }
