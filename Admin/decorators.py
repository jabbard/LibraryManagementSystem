from django.core.exceptions import PermissionDenied

def admin_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, *kwargs)
        else:
            raise PermissionDenied
    return wrap

def staff_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap