import utils.var_builder as vb

def call_funcs(row_dict):

    func_list = {add_null_column,
                 #test_var_builder
                 }
    for func in func_list:
        row_dict = func(row_dict)

    return row_dict

def add_null_column(row_dict):
    row_dict['null_column'] = None
    return row_dict

def test_var_builder(row_dict):
    row_dict['fake_column'] = 'FAKE_NEWS' if row_dict[vb.VarMap.policy_coverage] != '' else 'TRUE_NEWS'
    return row_dict