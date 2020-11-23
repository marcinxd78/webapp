from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser

from .models import Position


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'fname', 'lname',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Hasła rozbieżne")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=("Hasło"),
                                         help_text=("Jeśli użytkownik zapomniał hasła skorzystaj z  "
                                                    "formularza "
                                                    " <a href=\"../password\">Reset hasła</a>."))
    class Meta:
        model = MyUser
        fields = ('email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances




    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'fname', 'lname', 'position', 'departy', 'is_staff', )
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', )}),

        ('Informacje o pracowniku',
         {'fields': ('fname', 'lname', 'position', 'departy', 'brygadier', 'companyName', 'companyIn', 'contact',)}),
        ('Uprawnienia', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Reset hasła', {'fields': ('password',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fname', 'lname', 'password1', 'password2')}
        ),


    )
    search_fields = ('email', 'is_staff',)

    ordering = ('email',)
    filter_horizontal = ('user_permissions', 'groups', )

# Now register the new UserAdmin...

admin.site.register(MyUser,UserAdmin)


admin.site.register(Position)

