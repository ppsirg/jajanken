from django.shortcuts import render

from django.views.generic import TemplateView, ListView


class JajankenView(TemplateView):
    template_name = 'app_template.html'


class ScoresView(TemplateView):
    template_name = 'score_list_template.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['player_stats'] = [
            {'rank': 1, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 2, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 3, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
            {'rank': 4, 'name': 'lol', 'won_matches': 12, 'lost_matches': 1},
        ]
        return context
