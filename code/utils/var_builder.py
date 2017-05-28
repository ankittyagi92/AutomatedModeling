import json
import os

class VarMap(object):
    vars_set = False
    groups_set = False

    @classmethod
    def set_vars(cls, var_map):
        if cls.vars_set:
            raise Exception('Variable overwrite not allowed')
        cls.vars_set = True
        for name, value in var_map.items():
            setattr(cls, name, value)

    @classmethod
    def set_groups(cls, group_map):
        if cls.groups_set:
            raise Exception('Variable groups overwrite not allowed')
        cls.groups_set = True
        for name, value in group_map.items():
            if hasattr(cls, name):
                raise Exception('Group name cannot share keys with Variable name')
            rev_list = cls.create_group_value(value)
            setattr(cls, name, rev_list)

    @classmethod
    def create_group_value(cls, value):
        rev_list = []
        for att_name in value:
            addition = getattr(cls, att_name)
            if isinstance(addition, list):
                rev_list.extend(addition)
            else:
                rev_list.append(addition)
        return rev_list

def set_from_file(json_file):
    with open(json_file, 'r') as infile:
        json_vars = json.load(infile)
    var_map = json_vars['VariableMapping']
    group_map = json_vars['VariableGroups']
    VarMap.set_vars(var_map)
    VarMap.set_groups(group_map)


if 'VARFILE' in os.environ:
    var_file = os.environ['VARFILE']
    set_from_file(var_file)