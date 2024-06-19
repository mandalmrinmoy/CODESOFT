import json
def load_todo():
    try:
        with open('todo.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_todo_helper(todo):
    with open('todo.txt','w') as file:
        return json.dump(todo,file)
def all_list_todo(todo):
    print('\n')
    print('*' * 70)
    for index,name in enumerate(todo,start=1):
        print(f"{index}. {name['topic']} , Time: {name['time']} ")
        save_todo_helper(todo)
    print('\n')
    print('*' * 70)
def create_todo(todo):
    topic=input('Enter the topic name: ')
    time=input('Enter the time: ')
    todo.append({'topic':topic , 'time':time})
    save_todo_helper(todo)
def update_todo(todo):
    all_list_todo(todo)
    index=int(input('Enter the index to be updated: '))
    if 1<= index >=len(todo):
        topic=input('Enter the Updated topic name: ')
        time=input('Enter the Updated time: ')
        todo[index-1]={'topic':topic, 'time':time}
        save_todo_helper(todo)
    else:
        print("Invalid Index")
def delete_todo(todo):
    all_list_todo(todo)
    index=int(input('Enter the index to be deleted: '))
    if 1<=index>=len(todo):
        del todo[index-1]
        save_todo_helper(todo)
    else:
        print("Invalid Index")
def main():
    while True:
        todo=load_todo()
        print('\n To Do List')
        print('*' * 13)
        print('1. List of task')
        print('2. Create task')
        print('3. Update task')
        print('4. Delete task')
        print('5. Exit')
        choice=input('Enter the number of index: ')
        match choice:
            case '1':
                all_list_todo(todo)
            case '2':
                create_todo(todo)
            case '3':
                update_todo(todo)
            case '4':
                delete_todo(todo)
            case '5':
                break
            case _:
                    print('invalid Index')


if __name__==("__main__"):
    main()
