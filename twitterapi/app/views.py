from django.conf import settings
from django.views.generic.base import TemplateView
from twython import Twython


# Create your views here.
class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        action_names = ['Andela', 'Andela_Nigeria', 'Andela_Kenya']
        action_mapping = {
            'all': action_names,
            'andela': action_names[0:1],
            'andela_nigeria': action_names[1:2],
            'andela_kenya': action_names[2:]
        }
        action = kwargs.get('action', 'all')
        self.refresh_tweets(action_mapping[action])

        context['andela_global'] = self.request.session['Andela']
        context['andela_nigeria'] = self.request.session['Andela_Nigeria']
        context['andela_kenya'] = self.request.session['Andela_Kenya']
        return context

    def refresh_tweets(self, *args):
        '''refresh tweets of users supplied via args and add to session'''
        twitter = Twython(settings.APP_KEY, settings.APP_SECRET,
                          settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
        if twitter.verify_credentials():
            for user_handle in args[0]:
                self.request.session[user_handle] = twitter.get_user_timeline(
                    screen_name=user_handle)
        return self
