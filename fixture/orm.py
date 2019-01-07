from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        """address = Optional(str, column='address')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        secondaryphone = Optional(str, column='phone2')"""

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    def convert_group_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_group_list(self):
        return self.convert_group_to_model(select(g for g in ORMFixture.ORMGroup))
