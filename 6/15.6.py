def print_msg(msg):
    def printer():
        print(msg)
another = print_msg("Hello")
another()