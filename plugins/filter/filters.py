#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
        }

    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable
