from fate_arch.abc import AddressABC


class StandaloneAddress(AddressABC):
    def __init__(self, name, namespace, storage_type):
        self.name = name
        self.namespace = namespace
        self.storage_type = storage_type


class EggRollAddress(AddressABC):
    def __init__(self, name, namespace, storage_type):
        self.name = name
        self.namespace = namespace
        self.storage_type = storage_type


class HDFSAddress(AddressABC):
    def __init__(self, path):
        self.path = path


class MysqlAddress(AddressABC):
    def __init__(self, user, passwd, host, port, db, name):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.db = db
        self.name = name


class FileAddress(AddressABC):
    def __init__(self, path, path_type):
        self.path = path
        self.path_type = path_type
