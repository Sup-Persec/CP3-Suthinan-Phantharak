from tkinter import *
import math

def leftclick(event):
    bmi = round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2),2)
    if bmi <= 18.5:
        bmiResult = "ผอมเกินไป"
    elif bmi <= 18.6 and bmi <= 22.9:
        bmiResult = "น้ำหนักปกติ"
    elif bmi <= 23 and bmi <= 24.9:
        bmiResult = "น้ำหนักเกิน"
    elif bmi <= 25 and bmi <= 29.9:
        bmiResult = "อ้วน"
    elif bmi >= 30:
        bmiResult = "อ้วนมาก"
    else:
        print("โปรดกรอกข้อมูลใหม่")

    labelResult.configure(text="ผลประเมิน : " + bmiResult)


MainWindow = Tk()

labelHight = Label(MainWindow,text="ส่วนสูง(cm.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก(kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftclick)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()