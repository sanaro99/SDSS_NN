from tkinter import *
from tensorflow.keras.models import load_model
import numpy as np
from numpy import transpose

window=Tk()

l1=Label(window, text="u : ", font="15").grid(row = 1, column=1)
e1=Entry(window, bd =5)
e1.grid(row = 1, column=2)

e2=Entry(window, bd=5)
e2.grid(row = 3, column=2)
l2=Label(window, text="g : ", font="15").grid(row = 3, column=1)

e3=Entry(window, bd=5)
e3.grid(row = 5, column=2)
l3=Label(window, text="r : ", font="15").grid(row = 5, column=1)

e4=Entry(window, bd=5)
e4.grid(row = 1, column=5)
l4=Label(window, text="i : ", font="15").grid(row = 1, column=4)

e5=Entry(window, bd=5)
e5.grid(row = 3, column=5)
l5=Label(window, text="z : ", font="15").grid(row = 3, column=4)

e6=Entry(window, bd=5)
e6.grid(row = 5, column=5)
l6=Label(window, text="redshift : ", font="15").grid(row = 5, column=4)

def geta():
      return float(e1.get())

def getb():
      return float(e2.get())


def getc():
    return float(e3.get())


def getd():
    return float(e4.get())


def gete():
    return float(e5.get())


def getf():
    return float(e6.get())


v=StringVar()

l3=Label(window, textvariable=v, font="Callibri 25").grid(row = 2, column=3)

def label():
      global v
      v.set("Prediction : " + str(result))

def predict():
      global result
      a=geta()
      b=getb()
      c=getc()
      d=getd()
      e=gete()
      f=getf()

      arr = np.array([a, b, c, d, e, f])
      #arr = [17.55025, 16.26342, 16.43869, 16.55492, 16.61326, 269.00000]
      #arr = [0.697177, 0.901458, 0.693378, 0.501851, 0.418186, 0.072878]

      mean = [18.61566737, 17.36477853, 16.83154414, 16.57064002, 16.41133206, 0.14426812]
      sd = [0.82679535, 0.94359545, 1.06548846, 1.1286817, 1.19400876, 0.39036527]
      arr = (arr - mean)/sd
      x_predict = np.array([arr])
      model = load_model("sloanModel.h5")
      predictions = {0: "Star", 1: "Galaxy", 2: "Quasar"}
      i = np.asscalar(model.predict_classes(x_predict))
      result=predictions[i]
      label()


b1=Button(window, text="submit", fg="orange", command=predict, padx=4, pady=4, font="12", borderwidth=4).grid(row = 7, column = 2)



window.mainloop()
