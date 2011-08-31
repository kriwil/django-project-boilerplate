from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ModelDeletedFlagMixin(object):

    def get_queryset(self):
        queryset = super(ModelDeletedFlagMixin, self).get_queryset()
        return queryset.filter(user=self.request.user, deleted=False)


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class FormUserInitMixin(object):

    # pass the request.user to the form
    def get_form_kwargs(self):
        kwargs = super(FormUserInitMixin, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


