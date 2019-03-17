from django.contrib import admin
from django.contrib.auth.models import Group

from appcore import models as model
from appcore.admin import (
    user,
    role,
    ticket
)

# REGISTER

admin.site.register(model.User, user.Admin)
admin.site.register(model.Role, role.Admin)
admin.site.register(model.Ticket, ticket.Admin)

# UN REGISTER
admin.site.unregister(Group)
