from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import UserSchema
from blog.models.database import db
from blog.models import User
from blog.permissions.user import UserListPermission, UserPatchPermission

class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserListPermission],
    }

class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserListPermission],
        "permission_patch": [UserPatchPermission],
        
    }