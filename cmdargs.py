# Python program to demonstrate
# command line arguments


import argparse


class CmdArgs:

    def __init__(self, pm=None):
        self.pm = pm
        # initializing the parser
        self.parser = argparse.ArgumentParser()

        # adding the optional arguments to the parser
        # i is for inserting/adding new password to the database
        self.parser.add_argument('-i', '--insert', metavar='', nargs=3, type=str,
                                 help="format: -i <site> <username> <password>")

        # v is for viewing* the passwords in the database
        self.parser.add_argument('-v', '--view', metavar='', nargs=1,
                                 type=str, help="format: -i <site>")
        # u is for changing the password of any site-user combo already in database
        self.parser.add_argument('-u', '--update', metavar='', nargs=3, type=str,
                                 help="format: -i <site> <username> <new password>")

        # d is for deleting a particular site-user combo from the database
        self.parser.add_argument('-d', '--delete', metavar='', nargs=2,
                                 type=str, help="format: -i <site> <username>")
        self.parser.add_argument('-mk', '--maskey', metavar='', nargs=2,
                                 type=str, help="format: -i <old> <new>")

        # calling the parse args method and storing the namespace containing arguments
        self.args = self.parser.parse_args()

        # maintains a set of the non default arguments currently part of the program
        self.set_args = {'-i', '-v', '-u', '-d', '-mk'}

    # action handles the task to be executed based on the arguments specified
    def action(self):
        if self.args.insert:
            self.pm.insert()

        if self.args.update:
            self.pm.update()

        if self.args.delete:
            self.pm.delete()

        if self.args.view:
            self.pm.show()

        if self.args.maskey:
            self.pm.change_master_key()


if __name__ == "__main__":
    argparser = CmdArgs()
