class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def check_if_user_exists(user, group):
    """
       This helper function is used to check whether the user exist in the list of users for
       the particular group.
       It's more efficient to keep this as a function as it can be called easily from
       other helper function and main function
    """
    for users in group.get_users():
        if users == user:
            return True
    return False


def check_inside_group(user, group):
    """
       This is a recursive helper function.
       1. It goes inside the group and check for available groups first.
       2. If a subgroup is not having further groups then it checks for user in subgroup.
    """
    for groups in group.get_groups():
        if check_if_user_exists(user, groups):
            return True
        else:
            if check_inside_group(user, groups):
                return True

    return False


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # First checking if group exists. If it doesn't exist then inform user about it.
    try:
        group.get_users()
    except:
        return "The given group object doesn't exist\n"

    # Checking for the user in the group in question:
    if check_if_user_exists(user, group):
        return 'The user {} exists in group {}'.format(user, group.name)

    # Check Groups and the user inside those groups:
    if check_inside_group(user, group):
        return 'The user {} exists in group {}'.format(user, group.name)

    return 'User {} does not exist in group {}'.format(user, group.name)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

parent.add_user('kris')

## Test Case 1

our_user = sub_child_user
our_group = parent

print(is_user_in_group(our_user, our_group))
print('\n')

## Test Case 2

our_user = 'kris'
our_group = child

print(is_user_in_group(our_user, our_group))
print('\n')

## Test Case 3

our_user = 'kris'
our_group = 'grandparent'
print(is_user_in_group(our_user, our_group))