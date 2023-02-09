from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'is_active',)
    available_fields = ()
    hidden_fields = ('is_active',)

    def get_form(self, request, obj, **kwargs):
        if request.user.has_perm('users.set_status'):
            self.fields = self.hidden_fields + self.available_fields
        else:
            self.fields = self.available_fields

        return super().get_form(request, obj, **kwargs)











