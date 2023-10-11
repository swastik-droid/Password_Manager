import sys

from database import Database
from cmdargs import CmdArgs
from aes import AESCipher
import clipboard
from sys import argv, exit


class PM:
    def __init__(self):
        self.cipher = None
        # print(argv, end='\n')
        self.argparser = CmdArgs(self)
        self.arg = self.argparser.args
        # print("Action not yet called")

        self.database = Database()

        self.auth()
        # print("action have been called")
        self.argparser.action()

    def auth(self):
        if len(self.argparser.set_args) + len(argv) == \
                len(set(argv).union(self.argparser.set_args)):
            print(f"No arguments from {self.argparser.set_args} entered")
            print("Use 'pm -h' for help")
            exit()

        key = input("Enter the master key: ")
        self.cipher = AESCipher(key)

    def delete(self):
        command = "DELETE FROM passw WHERE site='{0}' AND username = '{1}'" \
            .format(self.arg.delete[0], self.arg.delete[1])
        self.database.execute(command, commit=1)

    def update(self):

        new_password = self.cipher.encrypt(self.arg.update[2])
        command = f"UPDATE passw SET password = \"{new_password}\" WHERE site =" \
                  f" '{self.arg.update[0]}' AND username ='{self.arg.update[1]}'"
        self.database.execute(
            command, commit=1)

    def update(self, new_pass: list):

        # new_password = self.cipher.encrypt(self.arg.update[2])
        command = f"UPDATE passw SET password = \"{new_pass[2]}\" WHERE site =" \
                  f" '{new_pass[0]}' AND username ='{new_pass[1]}'"
        self.database.execute(
            command, commit=1)

    def insert(self):
        password = self.cipher.encrypt(self.arg.insert[2])
        command = "INSERT INTO passw (site, username, password) VALUES" + \
                  f"('{self.arg.insert[0]}', '{self.arg.insert[1]}', \"{password}\")"
        # print(command)
        self.database.execute(command, 1)

    def show(self):
        """
        This function prints the data as per the query in a tabular form


        :return: none
        """
        if self.arg.view[0] != "*":
            print(f"Passwords for {self.arg.view[0]}:\n")
            command = f"SELECT * FROM passw WHERE site = '{self.arg.view[0]}'"
        else:
            command = f"SELECT * FROM passw"

        self.database.cursor.execute(command)

        fetched = self.database.cursor.fetchall()

        if not fetched:
            print("No Entries were found.")
            return
        self._print_tabular_and_clipboard(fetched)
        # print(fetched)
        # for f in fetched:
        #     print(self.cipher.decrypt(f[2]))

    def _print_tabular_and_clipboard(self, fetched):
        """
        This function prints the data in the tabular form
        It also decides the password to be copied to clipboard as per the user choice

        param fetched: list of lists containing the password fetched from the database
        :return: none
        """
        # printing the head of the table
        print(" " + "_" * 95)
        print("|{0:3}|{1:^30}|{2:^30}|{3:^30}|".format("#", "Application", "Username", "Password"))
        print("|" + "_" * 95 + "|")

        # printing the body of the table
        for i, fetch in zip(range(len(fetched)), fetched):
            print("|{0:^3}|{1:^30}|{2:^30}|{3:^30}|".format(i + 1, fetch[0], fetch[1], "**********"))
            # print("|{0:^3}|{1:^30}|{2:^30}|{3:^30}|".format(i + 1, fetch[0], fetch[1], self.cipher.decrypt(fetch[2])))

            print(" " + "_" * 95)

        # asking user to choose the password to copy to clipboard
        sno = int(input("Enter S.NO of password you want to access: "))

        # validating sno
        if sno > len(fetched):
            print("Please Enter valid S.NO")
            return

        # copy to clipboard and inform the user the
        clipboard.copy(self.cipher.decrypt(fetched[sno - 1][2]))
        print(f"!! Password for {fetched[sno - 1][0]} {fetched[sno - 1][1]} copied to the clipboard.")

    def change_master_key(self):
        old_cipher = AESCipher(self.arg.maskey[0])

        new_cipher = AESCipher(self.arg.maskey[1])
        self.database.execute("SELECT * FROM passw")
        fetched = self.database.cursor.fetchall()

        for fetch in fetched:
            new_pass = new_cipher.encrypt(old_cipher.decrypt(fetch[2]))
            if old_cipher.decrypt(fetch[2]):
                newinstance = fetch[0:2] + tuple([new_pass]) + tuple([fetch[3]])
                self.update(newinstance)
            else:
                print(f'masterkey for {fetch[0]} {fetch[1]} could not be updated.\n')


if __name__ == "__main__":
    pm = PM()
