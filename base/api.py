import provider as Provider
import sys
import db


if __name__ == '__main__':
    if sys.argv[1] == 'init':
        print(db.init())
        sys.stdout.flush()
    elif sys.argv[1] == 'get_projects':
        print(Provider.get_projects())
        sys.stdout.flush()
    elif sys.argv[1] == 'get_project':
        data = [sys.argv[2]]
        print(Provider.get_project(data))
        sys.stdout.flush()
    elif sys.argv[1] == 'create_project':
        data = [sys.argv[2], sys.argv[3], sys.argv[4]]
        print(Provider.create_project(data))
        sys.stdout.flush()
    elif sys.argv[1] == 'delete_project':
        id = [sys.argv[2]]
        print(Provider.delete_project(id))
        sys.stdout.flush()
