import frappe

def filter_project(user):
    user=frappe.get_user().doc
    username=user.name
    email = user.email
    return "_assign LIKE '%{}%'".format(username) + " OR owner LIKE '%{}%'".format(email)
    

def filter_task(user):
    user=frappe.get_user().doc
    username=user.name
    email = user.email
    return "_assign LIKE '%{}%'".format(username) + " OR owner LIKE '%{}%'".format(email)
  