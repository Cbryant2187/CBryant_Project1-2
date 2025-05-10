def vote_menu():
    print('----------------------------------')
    print('VOTE MENU')
    print('----------------------------------')
    print('v: Vote')
    print('x: Exit')
    user_choice = input('Option: ').lower()
    while user_choice != 'v' and user_choice != 'x':
        user_choice = input('Invalid (v/x): ').lower()

    return user_choice


def candidate_menu():
    print('----------------------------------')
    print('CANDIDATE MENU')
    print('----------------------------------')
    print('1: Bianca')
    print('2: Edward')
    print('3: Felicia')
    user_num = input('candidate: ').lower()
    while user_num != '1' and user_num != '2' and user_num != '3':
        user_num = input('Invalid (1/2/3): ')

    return int(user_num)


def main():
    can1 = 0
    can2 = 0
    can3 = 0

    user_path = vote_menu()

    while user_path != 'x':
        user_vote = candidate_menu()
        if user_vote == 1:
            can1 = can1 + 1
            print('Voted for Bianca')
        elif user_vote == 2:
            can2 = can2 + 1
            print('voted for Edward')
        elif user_vote == 3:
            can3 = can3 + 1
            print('Voted for Felicia')
        user_path = vote_menu()

    print('-------------------------------------------------------')
    print(f'Bianca – {can1}, Edward – {can2}, Felicia – {can3}, Total – {can1 + can2 + can3}')
    print('-------------------------------------------------------')


if __name__ == '__main__':
    main()