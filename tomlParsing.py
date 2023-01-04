import toml



def reading_toml_file(filepath: str)->dict:
    f=open(filepath,'r')
    print(f.read())


def parsing_toml_file(filepath: str)->dict:
    f=open(filepath,'r')
    toml_data=f.read()
    toml_dict=toml.loads(toml_data) 
    return toml_dict



#reading_toml_file("test.toml")
check=parsing_toml_file("test.toml")
print(check)