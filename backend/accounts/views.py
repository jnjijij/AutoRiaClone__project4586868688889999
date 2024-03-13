from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import CreateView

from models import CustomUser


class SignUpView(CreateView):
    model = CustomUser
    template_name = 'signup.html'
    fields = ['username', 'password', 'email']

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_premium = True if self.request.POST.get('account_type') == 'premium' else False
        user.save()
        return HttpResponseRedirect('/login')


def user_passes_test():
    pass


@login_required
def manage_users(request):

    return render(request, 'manage_users.html', {})
@login_required
def upgrade_account(request):

    return render(request, 'upgrade_account.html', {})

@login_required
def view_statistics(request):
    if request.user.account_type == 'premium':

        return render(request, 'statistics.html', {})
    else:
        return HttpResponseForbidden("You do not have permission to view statistics")
