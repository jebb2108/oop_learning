class Stack():

    def __init__(self, starting_stack_as_list):
        if starting_stack_as_list is None:
            self.data_list = [ ]
        else:
            self.data_list = starting_stack_as_list

    def push(self, item):
        self.data_list.append(item)

    def pop(self):
        if len(self.data_list) == 0:
            return None
        else:
            return self.data_list.pop()

    def peek(self):
        item = self.data_list[-1]
        return item

    def get_size(self):
        n_elements = len(self.data_list)
        return n_elements

    def show(self):
        print('Stack is:')
        for value in reversed(self.data_list):
            print(' ', value)
