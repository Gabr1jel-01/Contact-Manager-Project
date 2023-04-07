from features import (Organization,
                       get_all_organizations,
                       get_organization,
                       save_organization)


def start_app():
    print('Print iz start_app() funkcije')
    org = Organization('Algebra d.o.o', '123456535684679')
    save_organization(org)
    
    
    get_all_organizations()
    organization_from_file = get_organization()
    print('\nOrganizacija iz datoteke')
    print(organization_from_file)
    print()
    

if __name__ == '__main__':
    start_app()
    