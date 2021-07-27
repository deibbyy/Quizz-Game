from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import Conexion_bd
import random
from time import sleep

numero=0
puntaje = 0
numeroPregunta=[]

# Funcion para los botones
def iniciar():
    global puntaje
    global numeroPregunta
    if validacion():
        return False
    numeroPregunta.clear()

    objeto=Conexion_bd.preguntas() # Objeto para preguntas
    preg=objeto.leerPreguntas() # Metodo leerPreguntas

    nom=ventana.Nombre.text()#lectura del nombre puesto el el linetext
    ventana.lblNombre.setText(nom)#etiqueta para mostrar el nombre
    
    llenar(preg) # Funcion para llenar los espacios de las preguntas
    ventana.btnSel.setEnabled(True)
    ventana.btnSiguiente.setEnabled(False)
    ventana.btnIniciar.setEnabled(False)

def siguiente():
    global puntaje
    #funcion para el boton siguiente
    objeto=Conexion_bd.preguntas() # Objeto para preguntas
    preg=objeto.leerPreguntas() # Metodo leerPreguntas
    llenar(preg)
    ventana.btnSel.setEnabled(True)
    ventana.btnSiguiente.setEnabled(False)

def seleccion():
    #funcion para leer el espacio seleccionado en la tabla de opciones 
    sel=ventana.tblOpciones.selectedIndexes()[0].data()
    #ventana.brrProgreso.setValue(0)
    ventana.btnIniciar.setEnabled(False)
    
    #print(sel)

def aceptar():
    global puntaje
    objeto=Conexion_bd.preguntas() # Objeto para preguntas
    preg=objeto.leerPreguntas() # Metodo leerPreguntas
    try:
        sel=ventana.tblOpciones.selectedIndexes()[0].data()
        p=preg[numero] # Guardar la tupla correstondiente al numero random en variable
        A=p[2].split(sep='-')
        B=p[3].split(sep='-')
        C=p[4].split(sep='-')
        D=p[5].split(sep='-')
        if sel==A[0] and A[1]=='#':
            aux='correcto'
            progresbar()
            mensaje(aux)
            puntaje=puntaje+20
            ventana.Puntaje.setText(str(puntaje))
            #print("Respuesta correcta")
        elif sel==B[0] and B[1]=='#':
            aux='correcto'
            progresbar()
            mensaje(aux)
            puntaje=puntaje+20
            ventana.Puntaje.setText(str(puntaje))
            #print("Respuesta correcta")
        elif sel==C[0] and C[1]=='#':
            aux='correcto'
            progresbar()
            mensaje(aux)
            puntaje=puntaje+20
            ventana.Puntaje.setText(str(puntaje))
            #print("Respuesta correcta")
        elif sel==D[0] and D[1]=='#':
            aux='correcto'
            progresbar()
            mensaje(aux)
            puntaje=puntaje+20
            ventana.Puntaje.setText(str(puntaje))
            #print("Respuesta correcta")
        else:
            aux='incorrecto'
            progresbar()
            mensaje(aux)
            #print("respuesta incorecta")

        n=ventana.numeroPreguntas.value()
        n-=1
        ventana.numeroPreguntas.setValue(n)


        if n==0:
            final=QMessageBox()
            final.setText("GENIAL!!!  TU PUNTAJE: "+str(puntaje))
            final.setIcon(QMessageBox.Information)
            final.setWindowTitle("RESULTADOS")
            final.exec()
            puntaje=0
            ventana.Puntaje.setText(str(puntaje))
            ventana.lblNombre.setText("")#etiqueta para mostrar el nombre
            ventana.Nombre.setText("")
            ventana.btnIniciar.setEnabled(True)
            ventana.btnSiguiente.setEnabled(False)
            ventana.btnSel.setEnabled(False)
        else:
            ventana.btnIniciar.setEnabled(False)
            ventana.btnSiguiente.setEnabled(True)
            ventana.btnSel.setEnabled(False)
    except IndexError:
        print("error")

def progresbar():
    f =100
    ventana.brrProgreso.setMinimum(0)
    ventana.brrProgreso.setMaximum(f)
    for i in range(f):
        sleep(0.01)
        ventana.brrProgreso.setValue(i+1)
    
def llenar(preg):
    global numero
    global numeroPregunta
    aux=0
    
    # Verificar que la pregunta no se halla presentado ya 
    while aux==0:
        num=random.randint(0,len(preg)-1) # pregunta random
        if num in numeroPregunta:
            num=random.randint(0,len(preg)-1) # pregunta random
            #print("ya esta")
        else:
            numeroPregunta.append(num)
            p=preg[num] # Guardar la tupla correstondiente al numero random en variable
            #print(num)
            numero = num
            aux=1

    ventana.Pregunta.setPlainText(p[1])

    A=p[2].split(sep='-')
    ventana.tblOpciones.setItem(0, 0, QTableWidgetItem(A[0]))
    B=p[3].split(sep='-')
    ventana.tblOpciones.setItem(1, 0, QTableWidgetItem(B[0]))
    C=p[4].split(sep='-')
    ventana.tblOpciones.setItem(2, 0, QTableWidgetItem(C[0]))
    D=p[5].split(sep='-')
    ventana.tblOpciones.setItem(3, 0, QTableWidgetItem(D[0]))

def mensaje(aux):
    #Mensaje cuando se seleccione una respuesta
    if aux=='correcto':
        dlg = QDialog() # Crear una ventana de dialogo
        dlg.setGeometry(400, 400, 80, 150)#configurar tamaño y posicion donde aparecera
        b1 = QLabel("CORRECTO!!!",dlg)#Mensaje a mostrar en una etiqueta
        b1.move(10,10)#posicion de la etiqueta 1
        b1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))#configurar fuente y tamaño
        b2=QLabel(dlg)#crear etiqueta 2 en la ventana dlg
        b2.setPixmap(QtGui.QPixmap('bien.jpg')) # ponerimagen en etiqueta b2
        b2.move(10, 30)#posicionar imagen
        b2.setStyleSheet("border-radius: 5px;border: 5px solid black;")#bordes en la imagen
        dlg.setWindowTitle("!") #9. PyQt5 — QDialog Class
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()
    elif aux=='incorrecto':
        dlg = QDialog()
        dlg.setGeometry(400, 400, 100, 150)
        b1 = QLabel("INCORRECTO!!!",dlg)
        b1.move(10,10)
        b1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        b2=QLabel(dlg)
        b2.setPixmap(QtGui.QPixmap('mal.jpg'))
        b2.move(10, 30)
        b2.setStyleSheet("border-radius: 5px;border: 5px solid black;")
        dlg.setWindowTitle("!") #9. PyQt5 — QDialog Class
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_() 

def validacion():
    # validacion de si ingresa el nombre para iniciar 
    if ventana.Nombre.text()=="" or ventana.numeroPreguntas.value()<=0 :# la condicion es si el espacio para el nombre esta vacio
        alerta=QMessageBox() # Mensaje de alerta en caja de mensajes
        alerta.setText("Debes de ingresar un nickname o aumentar el numero de preguntas")# Texto en QMessageBox
        alerta.setIcon(QMessageBox.Information)# icono en QMessageBox
        alerta.exec()#ejecucion de la QMessageBox
        return True #retornar True si esta vacio


# Interfaz grafica de la aplicacion
Aplicacion = QtWidgets.QApplication([]) # Crear el objeto Aplicacion
ventana = uic.loadUi("Quiz_g.ui") #cargar la interfaz grafica 
ventana.show() # mostrar la ventana 

#ventana.setStyleSheet("QMainWindow {background-color: black;}")
# desactivar botones jugar y siguiente
ventana.btnSel.setEnabled(False)
ventana.btnSiguiente.setEnabled(False)

ventana.tblOpciones.cellClicked.connect(seleccion)#conexion cuando el cursor esta sobre un espacion de la tabla

# Configuracion de los botones
ventana.btnSel.clicked.connect(aceptar)
ventana.btnSiguiente.clicked.connect(siguiente)
ventana.btnIniciar.clicked.connect(iniciar)

sys.exit(Aplicacion.exec()) # Cerrar aplicacion