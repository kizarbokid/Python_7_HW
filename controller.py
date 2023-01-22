import view
import module


def start():
    user_input=0
    while user_input!=8:
        user_input = view.show_menu()
        match user_input:
            case 1:
                phone_book=module.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                module.open_phone_book()
                view.load_success()
            case 3:
                module.save_phone_book()
                view.save_success()
            case 4:
                new=list(view.create_new_contact())
                module.update_phone_book(new)
                view.update_success()
            case 5:
                print(f'Пункт {user_input} выбран')
            case 6:
                print(f'Пункт {user_input} выбран')
            case 7:
                search=view.find_what()
                result=module.search_contact(search)
                view.show_contacts(result)
    else:
        view.goodbye()

    