class password:

    def __init__(self, instance: tuple = None):
        # pm.auth()
        # self.pm = pm
        self.password: str = ""
        self.username: str = ""
        self.site: str = ""
        # self.date_time: str = ""
        # self.choice = 698547

        if instance:
            self.instance_to_pass(instance)

    def instance_to_pass(self, instance):
        self.site = instance[0]
        self.username = instance[1]
        self.password = instance[2]

    #
    # def menu(self):
    #     print("\nPlease choose the option you want to pursue.", end="\n")
    #     print("1. View saved password.", end="\n")
    #     print("2. Edit a saved password.", end="\n")
    #     print("3. Remove a saved password.", end="\n")
    #     print("4. Add a new password.", end="\n")
    #
    #     self.choice = int(input())
    #     if self.choice == 1:
    #         site = input("Please enter the site you want to access password for: ")  # make it lowercase and no spaces
    #         # row = self._load_from_saved(site)
    #         self.pm.show(site)
    #         # self.show() #to be created
    #
    #     elif self.choice == 2:
    #         self.site = input("Please enter the site you want to access password for: ")  # make it lowercase and no spaces
    #         # row = self._load_from_saved(site)
    #         self.password = input("Enter the new password: ")
    #         self._update()
    #     elif self.choice == 3:
    #         site = input("Please enter the site you want to access password for: ")  # make it lowercase and no spaces
    #         self.site = site
    #         self._delete()
    #     elif self.choice == 4:
    #         print("Enter the site, username  and password in order.", end="\n")
    #         self.site = input("site: ")
    #         self.username = input("username: ")
    #         self.password = input("password: ")
    #         self.insert()
    #     else:
    #         print("Invalid choice\n")

    # def _update(self):
    #     self.pm.update(self)
    #
    # def _load_from_saved(self, site: str):
    #     pass
    #     # self._load_vars(row)
    #
    # def _load_vars(self):
    #     pass
    #
    # def _delete(self):
    #     self.pm.delete(self)
    #
    # def show(self):
    #     pass
    #
    # def insert(self, list_args:list = None):
    #     if list_args:
    #         self.site = list_args[0]
    #         self.username = list_args[1]
    #         self.password = list_args[2]
    #
    #         self.pm.insert(self)
