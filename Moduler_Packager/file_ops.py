def create_file(filename):
    f = open(filename, "w")
    f.close()

def write_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()

def read_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

def append_file(filename, data):
    f = open(filename, "a")
    f.write("\n" + data)
    f.close()
