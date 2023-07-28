'''This file contains the code to provide permissions to the user as per the method'''
# import the function 
from rest_framework import permissions


# Cresting a class to give permissions based on user action 
class ActionBasedPermissions(permissions.BasePermission):
    ''' 
    Grand or deny access to a view , based on mapping in view .action_permissions
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and str(request.user.user_profile) == 'Admin')