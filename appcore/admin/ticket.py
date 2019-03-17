from django import forms
from django.contrib import admin

from appcore.models import Ticket


class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'status',)

    def save(self, commit=True):
        ticket = super(TicketCreationForm, self).save(commit=False)
        ticket.user_id = self.current_user.id
        if commit:
            ticket.save()
        return ticket


class Admin(admin.ModelAdmin):
    add_form_template = 'admin/ticket/add_form.html'
    add_form = TicketCreationForm

    fields = ('title', 'description', 'status',)
    list_display = ('title', 'description', 'status', 'user', 'date_created',)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        form = super(Admin, self).get_form(request, obj, **defaults)
        form.current_user = request.user
        return form
