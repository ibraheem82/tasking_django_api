# ** Custom permission class in Django Rest Framework (DRF).**
'''
The permission class allows all requests to access the view, but only allows the owner of an object to view it if the request method is safe (i.e., ‘GET’, ‘OPTIONS’, or ‘HEAD’). All other request methods are denied. This is useful for scenarios where you want to restrict who can view certain data based on the user and the type of request.
'''

from rest_framework import permissions # This module contains a set of pre-defined permission classes that you can use in your views.

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission): # This is a custom permission class.
    
    def has_permission(self, request, view): # This method is called before the view function is executed. It checks if the request should be granted permission to the view. In this case, it always returns True, meaning all requests have permission to access the view.
        return True
    
    def has_object_permission(self, request, view, obj): # This method is called for every instance in a queryset when a list of objects is retrieved, and for any object-level operations (retrieve, update, delete). It checks if the request should be granted permission to operate on the obj instance.
        if request.method in permissions.SAFE_METHODS: # This line checks if the HTTP method used in the request is in SAFE_METHODS (which is a tuple containing ‘GET’, ‘OPTIONS’ and ‘HEAD’). If it is, it checks if the user making the request is the same as the user associated with the obj instance. If both conditions are met, it returns True, granting permission. Otherwise, it returns False, denying permission.
            return request.user == obj
        return False