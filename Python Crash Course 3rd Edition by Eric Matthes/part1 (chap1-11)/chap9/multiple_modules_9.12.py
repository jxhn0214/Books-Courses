import admin_privilege_module

admin_user =admin_privilege_module.Admin('john', 'doe', '987-573-9973', 'johndoe@gmail.com')
admin_user.privileges.show_privileges()