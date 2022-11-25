from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login

from petstagram.accounts.forms import UserCreateForm

UserModel = get_user_model()


# def login_user(request):
#     return render(request, 'accounts/login-page.html') # model-operation-page.html


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        login(request, self.object)

        return response


# def register_user(request):
#     return render(request, 'accounts/register-page.html')

class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    photos_paginate_by = 2

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()

        photos = self.object.photo_set \
            .order_by('-publication_date')

        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set \
            .prefetch_related('photolike_set') # \
            # .select_related('user')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        context['photos'] = self.get_paginated_photos()
        context['pets'] = self.object.pet_set.all()

        return context
# n+1 query problem - select_related

# def details_user(request, pk):
#     return render(request, 'accounts/profile-details-page.html')

class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


# def edit_user(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')

class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')


# def delete_user(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')





