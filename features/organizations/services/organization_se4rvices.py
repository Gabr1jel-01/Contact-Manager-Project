from ..models import Organization


def get_all_organizations():
    print('Pozdrav iz get_all_organizations() funkcije')
    

def get_organization():
    try:
        with open('data\\txt_files\\organizations.txt', 'r') as file_reader:
            return file_reader.read()
    
    except Exception as ex:
        print(f'Dogodila se greska {ex}')
    

def save_organization(organization: Organization) -> None:
    try:
        with open('data\\txt_files\\organizations.txt', 'a') as file_writer:
            file_writer.write(str(organization) + '\n')
    
    except Exception as ex:
        print(f'Dogodila se greska {ex}')
        
    
    
    
    
    