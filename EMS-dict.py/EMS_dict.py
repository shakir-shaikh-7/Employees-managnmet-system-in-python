from db import employee_dict

printing=["Emp_ID","First_Name","Last_Name","Salary","Age","Dept"] 

def employee_table_format():
    print(f"{'-'*125}")
    print(f'\n{"Emp_ID"}\t\t{"First_Name"}\t\t{"Last_Name"}   \t{"Salary"}\t\t{"Age"}\t\t{"Dept"}')
    print(f"{'-'*125}")




def  add_employee():
    employee_ID=int(input('Enter Employee ID: '))
    first_name=(input('Enter first name of Employee: ').lower())
    last_name=(input('Enter last name of Employee: ').lower())
    Salary=int(input('Enter salary of Employee: '))
    Age=int(input('Enter age of Employee: '))
    Dept=(input('Enter department of Employee: '))
    

    emp_ID={}
    emp_ID['employee_ID']=employee_ID
    emp_ID['fname']=first_name
    emp_ID['lname']=last_name
    emp_ID['Salary']=Salary
    emp_ID['Age']=Age
    emp_ID['Dept']=Dept
    
    employee_dict[employee_ID]=emp_ID
    employee_dict.update({employee_ID:emp_ID})
    employee_table_format()

    print(f"{'-'*120}")


def Display_employee():

    name_to_display=int(input('Emp_ID of the employee you want to display[0 for db]: '))
    employee_table_format()


    if name_to_display ==0:                #loop for databases
        for i,j in employee_dict.items():
                sr=0
                for k,l in j.items():
                    printing[sr]=l
                    sr+=1           
                print(f'  \n{printing[0]}   \t\t{printing[1]:<7.10} \t\t{printing[2]:<7.10} \t{printing[3]}\t\t{printing[4]:}\t\t{printing[5]:<7.10}')
                print(f"{'-'*125}")

    else:            #loop for individual
        for i,j in employee_dict.items():
            if i==name_to_display:
                sr=0
                for k,l in j.items():
                    printing[sr]=l
                    sr+=1
                print(f'  \n{printing[0]}   \t\t{printing[1]:<7.10} \t\t{printing[2]:<7.10} \t{printing[3]}\t\t{printing[4]:}\t\t{printing[5]:<7.10}')
                print(f"{'-'*125}")
    if employee_dict=={}:
        print()
        print('Database is emty')
        print()
    print(f"{'-'*125}")





def Update_employee_data():
    emp_id_to_update=int(input('emp_ id of employee you want to Update data: '))
    db_keys_to_update=(input('dict keys of the employee you want to Update[emp-_id,fname,lname,salary,age,dept]: ')).lower()
    db_values_to_update=(input('dict values of the employee you want to Update: '))
    employee_dict[emp_id_to_update][db_keys_to_update]=db_values_to_update
    Display_employee()


def Remove_employee():
    emp_id_to_delete=int(input('emp id of the employee or (0 for database) you want to Delete: '))
    if emp_id_to_delete==0:
        employee_dict.clear()
        print('database deleted')
    else: 
        employee_dict.pop(emp_id_to_delete)
        # print(db)
        if employee_dict=={}:
            print('All data deleted and database is emty')
    print(f"{'-'*120}")
    Display_employee()





def trial():
    print(employee_dict[1])






while True:
    option=eval(input('what you want to do in this process[1:Add, 2:Read/Display, 3:Update 4:Delete]: '))

    if option==1:
        add_employee()
    elif option==00:
         trial()
        
    elif option==2:
         Display_employee()


    elif option==3:
         Update_employee_data()
        
    elif option==4:
         
         Remove_employee()

    else:
        print('invilide input')

    choice=input('do you want to continue [y/n]: ')
    if choice !='y':
        print('Thank you')
        break
