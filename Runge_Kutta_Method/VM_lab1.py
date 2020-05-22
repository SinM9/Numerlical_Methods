import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

def fx(x, y):
    return float(x - x * x * x / 3. - y)

def fy(x, a):
    E = 0.05
    return float(E * (x + a))

#############################################################################
def Runge_Kutt(x0,y0,t,h):
    x.append(x0)
    y.append(y0)
    t0 = 0.
    i = 0
    yt = 0
    xt = 0
    while(t0<t):

        k1_x = fx(x[i], y[i])
        k2_x = fx(x[i] + h / 2, y[i] + h * k1_x / 2)
        k3_x = fx(x[i] + h / 2, y[i] + h * k2_x / 2)
        k4_x = fx(x[i] + h, y[i] + h * k3_x)
        xt=x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6 * h   
        x.append(xt)

        k1_y = fy(x[i], a)
        k2_y = fy(x[i] + h / 2, a)
        k3_y = fy(x[i] + h / 2, a)
        k4_y = fy(x[i] + h, a)
        yt=y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6 * h
        y.append(yt)

        t0+=h
        i+=1

#############################################################################
def addGraphPhase(graph_axes, x, y):
     graph_axes.plot(x, y)
     plt.draw()

if __name__ == '__main__':
    x = list()
    y = list()

    #############################################################################
    def onButtonAddClicked(event):
        global graph_axes, x, y
        global x0, y0, t, h, a
        Runge_Kutt(x0,y0,t,h)
        addGraphPhase(graph_axes, x, y)
        x = []
        y = []

    #############################################################################
    def onButtonClearClicked(event):
        global graph_axes
        graph_axes.clear()
        graph_axes.grid()
        plt.draw()

    #############################################################################
    def submitA(text):
        global a
        a = float(text)

    def submitH(text):
        global h
        h = float(text)

    def submitX0(text):
        global x0
        x0 = float(text)

    def submitY0(text):
        global y0
        y0 = float(text)

    def submitN(text):
        global t
        t = float(text)

    #####______Create graph__________________________#############################
    fig, graph_axes = plt.subplots()
    graph_axes.grid()
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    ######______#Create add button___________________#############################
    axes_button_add = plt.axes([0.55, 0.05, 0.4, 0.075])
    button_add = Button(axes_button_add, 'Добавить')
    button_add.on_clicked(onButtonAddClicked)

    ######______Create clear buttin___________________############################
    axes_button_clear = plt.axes([0.05, 0.05, 0.4, 0.075])
    button_clear = Button(axes_button_clear, 'Очистить')
    button_clear.on_clicked(onButtonClearClicked)

    #######_____Create textbox for h, t, x0, y0, a____#############################
    axbox = plt.axes([0.14, 0.25, 0.15, 0.075])
    h_box = TextBox(axbox, 'Шаг h =', initial="0.01")
    h=0.01
    h_box.on_submit(submitH)

    axbox = plt.axes([0.55, 0.25, 0.15, 0.075])
    x0_box = TextBox(axbox, 'Задача Коши x0 =', initial="0")
    x0=0
    x0_box.on_submit(submitX0)

    axbox = plt.axes([0.8, 0.25, 0.15, 0.075])
    y0_box = TextBox(axbox, 'y0 =', initial= "0")
    y0=0
    y0_box.on_submit(submitY0)

    axbox = plt.axes([0.30, 0.15, 0.15, 0.075])
    n_box = TextBox(axbox, 'Количество точек n =', initial="100")
    t=100
    n_box.on_submit(submitN)

    axbox = plt.axes([0.8, 0.15, 0.15, 0.075])
    a_box = TextBox(axbox, 'Параметр a =', initial= "2")
    a=2
    a_box.on_submit(submitA)

    plt.show()

