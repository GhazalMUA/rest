from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):      #in the first step you should create a class that inheritance from basepermission class. in fact you rare overwriting basepermission class. as you can see in the basepermission definition it contains two methods has perm.. and object.. override these two . first has perm for checking if a user is authenticated so can go to the view and check the second condition which is hasobjectpermisssion here we check if a user is the owner of that post or item to CRUD on  that.
    message='permission denied, you are not the owner'
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user



#The following is an example of a permission class that checks the incoming request's IP address against a blocklist, and denies the request if the IP has been blocked.

# from rest_framework import permissions

# class BlocklistPermission(permissions.BasePermission):
#     """
#     Global permission check for blocked IPs.
#     """

#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked