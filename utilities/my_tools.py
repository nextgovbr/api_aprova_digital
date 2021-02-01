from .connect import gen_db

class MyFlag:
    '''Just a flag so I can manage default args better'''


class FlexKeyDict(dict):
    '''Extends dict to define get method for multiple keys
    that returns a my_dict as default so you can chain the method'''

    def recursive_conversion(self, item):

        if type(item) is dict:
            return FlexKeyDict(item)

        elif type(item) is list or type(item) is tuple:
            parsed_list = []
            for i in item:
                i = self.recursive_conversion(i)
                parsed_list.append(i)
            return parsed_list
        else:
            return item

    def get_m(self, keys, not_found=MyFlag, verbose=True):

        for key in keys:
            resp = self.get(key)
            if resp is not None:
                return self.recursive_conversion(resp)
        else:
            if not_found is MyFlag:
                not_found = FlexKeyDict()
            if verbose:
                print(f'{keys} not found in {repr(self)}')
            return not_found

#####################################__Other Tools__#########################################

def b_resp(label, desc, value):
    '''Buils API resp on system specific format'''

    return {'label': label,
            'description': desc,
            'value': value}


def get_proc_aleatorio():
    '''Gets a random process data for testing and prototyping'''

    db = gen_db()
    p = list(db.process.aggregate([{'$sample': {'size': 1}}]))[0]

    p = FlexKeyDict(p)

    return p