class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXECTYPE: ', exc_type)
        print('EXECVALUE: ', exc_val)
        print('TRACEBACK: ', exc_tb)
        print('Exiting...')
        if self.file:
            self.file.close()


with ManagedFile('test.txt') as f:
    f.write("hello, world!sdkhjfbkhfgoyuqerfgoalgsdfg;eagfeqr;ifhq'egf"
            "dfgdfkjgbqelug;\niqufh'qerg"
            "qfghgh;qiehf'oqefrj'qeijfqer"
            "qeg;ehrpgqeguqe[rgu[erghwer")
