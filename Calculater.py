from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current=result['text']
    new=current + str(digit)
    result.config(text=new)



def clear():
    result.config(text='')



def get_operator(op):
    global first_number,operator

    first_number = int(result['text'])
    operator = op
    result.config(text='')

def get_result():
    global first_number,second_number,operator

    second_number = int(result['text'])

    if operator == '+':
        result.config(text=str(first_number+second_number))
    elif operator == '-':
        result.config(text=str(first_number - second_number))
    elif operator == '*':
        result.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result.config(text='Error')
        else:
            result.config(text=str(round(first_number / second_number,2)))


root=Tk()
root.title('Calculater')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='Black')
#code by Yash Patle
result=Label(root,text='',fg='white',bg='Black')
result.grid(row=0,column=0,columnspan=5,sticky='w',pady=(30,25))
result.config(font=('verdana',30))

btn7=Button(root,text='7',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14,'bold'))

btn8=Button(root,text='8',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14,'bold'))

btn9=Button(root,text='9',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14,'bold'))

btn_add=Button(root,text='+',fg='white',bg='green',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14,'bold'))


btn4=Button(root,text='4',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14,'bold'))

btn5=Button(root,text='5',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14,'bold'))

btn6=Button(root,text='6',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14,'bold'))

btn_sub=Button(root,text='-',fg='white',bg='green',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14,'bold'))


btn1=Button(root,text='1',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14,'bold'))

btn2=Button(root,text='2',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14,'bold'))

btn3=Button(root,text='3',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14,'bold'))

btn_mul=Button(root,text='*',fg='white',bg='green',width=5,height=2,command=lambda :get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14,'bold'))



btn_clr=Button(root,text='C',fg='white',bg='green',width=5,height=2,command=clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14,'bold'))

btn0=Button(root,text='0',fg='white',bg='green',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14,'bold'))

btn_equals=Button(root,text='=',fg='white',bg='green',width=5,height=2,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('verdana',14,'bold'))

btn_div=Button(root,text='/',fg='white',bg='green',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14,'bold'))


root.mainloop()

