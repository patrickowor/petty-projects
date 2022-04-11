# this is the list everything will be saved in
solvent_lists=[]

def value():
    # this will take the input values if you have more please add
    solvent_name = input('enter your solvent name here: ')
    solvent_wg = int(input('enter your solvent weight here: '))
    solvent_vol = int(input('enter your solvent volume here: '))
    # if you have any calculation to do do it here or call the function that will do it pass it the value and ask the function to return the value here but advice you do it here it is easier.
    # here I created the dictionary variable that will take your values 
    solvent_dic = {'name': solvent_name, 'volume': solvent_vol, 'weight': solvent_wg}
    # here I append those values to the global list 
    solvent_lists.append(solvent_dic)
    print('')
    
def view():
    print('your result')
    # here I loop through the list
    for solvent_list in solvent_lists:
        # this first print serve as a demarcation 
        print('###########################l')
        print('name is ' + str(solvent_list['name']))
        print('volume is ' + str(solvent_list['volume']))
        print('weight is ' + str(solvent_list['weight']))
        print('')
    
        
        
def main():  
    while True:
        choice = input('welcome enter "a" to add new data,  "v" to view list and click any other to exit  ')
        if choice == 'a':
            value()
        elif choice == 'v':
            view() 
        else:
            break
main()