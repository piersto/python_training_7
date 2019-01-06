# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
