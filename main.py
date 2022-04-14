import pandas as pd
import numpy as np

def regresion_madera():
  path = "regre.xlsx"
  nombreHoja = "madera"

  df = pd.read_excel(path, sheet_name=nombreHoja) #leer el archivo excel


  df['x*y'] = df['Año']*df['Cantidad_madera'] #crear una nueva columna llamada x*y la cual contendrá el producto entre x e y
  df['x^2'] = df['Año']*df['Año'] #crear una nueva columna llamada x^2 la cual contendrá los cuadrados de la variable x
  df['x^3'] = pow(df['Año'],3)#crear una nueva columna llamada x^3 la cual contendrá los cubos de la variable x
  df['x^4'] = pow(df['Año'],4)#crear una nueva columna llamada x^4 la cual contendrá las cuartas potencias de la variable x
  df['x^2*y'] = df['x^2']*df['Cantidad_madera']#crear una nueva columna llamada x^2 la cual contendrá los cuadrados de la variable x multiplicado por cada una de las varibales y


  n = len(df.index) #n: numero total de datos
  sumx = df['Año'].sum() #sumatoria de las x
  sumy = df['Cantidad_madera'].sum()#sumatoria de las y
  sumxy = df['x*y'].sum()#sumatoria de las x*y
  sumx_2 = pow(sumx,2)#sumatoria de las (x)^2
  sumx2 = df['x^2'].sum()# sumatoria de las x^2
  sumx3 = df['x^3'].sum()#sumatoria de las x^3
  sumx4 = df['x^4'].sum()#sumatoria de las x^4
  sumx2y = df['x^2*y'].sum()#sumatoria de las x^2*y

  a1 = ((n*sumxy) - (sumx*sumy)) / ((n*sumx2) - (sumx_2))#coeficente a1 con base a las sumatorias anteriores
  a0 = ((sumy*sumx2) - (sumx*sumxy)) / ((n*sumx2)- sumx_2)#coeficiente a0 con base a las sumatorias anteriores


#método de resolución de sistémas de ecuaciones a partir de la librería numpy
  a = np.array([[n,sumx,sumx2],[sumx,sumx2,sumx3],[sumx2,sumx3,sumx4]])#matriz de coeficientes
  b = np.array([sumy,sumxy,sumx2y])#vector de terminos independientes
  x = np.linalg.solve(a,b)#solucuión del sistema (un vector solución)
  r = np.corrcoef(df['Año'], df['Cantidad_madera'])#coeficiente de correlación lienal de pearson

  df['e(y-y^)^2'] = pow(df['Cantidad_madera'] - (x[2]*pow(df['Año'],2) + x[1]*df['Año'] +   x[0]),2)#errores (y_real - y_calculado_con_polinomio_grado_dos) al cuadrado
  df['SCT'] = pow(df['Cantidad_madera'] - (sumy/n),2)#cuadrados totales (necesarios para calcular el coeficiente de correlación en el polinomio y así calcular el coeficiente de determinación)

  SCE = df['e(y-y^)^2'].sum()#suma de los cuadrados de los errores
  SCT = df['SCT'].sum()#suma de los cuadrados totales

  r2_pol = (SCT-SCE)/SCT #coeficiente de determinación polinomial con base en los errores
  r_pol = np.sqrt(r2_pol)#coeficiente de correlación polinomial con base en los errores

  print(df)

  print("\n")

  print("y = "+str(a1)+"x + "+str(a0)+"\n")
  print("El coeficiente de correlación lineal de pearson r es: ", r[1][0])
  print("El coeficiente de determinación lineal R^2 es: ", pow(r[1][0],2))

  print("\n")

  print("y = "+str(x[2])+"x^2 + "+str(x[1])+"x + "+str(x[0])+"\n")
  print("El coeficiente de correlación polinomial r es: ", r_pol)
  print("El coeficiente de determinación polinomial R^2 es: ", r2_pol)

  print("\n")

  print("la cantidad de madera en el año 10 usando el ajuste lineal será de: ", a1*10 + a0)
  print("\n")
  print("la cantidad de madera en el año 10 usando el ajuste polinomial será de: ", x[2]*pow(10,2) + x[1]*10 + x[0])
  print("\n")


def regresion_finanzas():
  path = "regre.xlsx"
  nombreHoja = "finanzas"

  df = pd.read_excel(path, sheet_name=nombreHoja) #leer el archivo excel


  df['x*y'] = df['Riesgo X']*df['Rendimiento Y(%)'] #crear una nueva columna llamada x*y la cual contendrá el producto entre x e y
  df['x^2'] = df['Riesgo X']*df['Riesgo X'] #crear una nueva columna llamada x^2 la cual contendrá los cuadrados de la variable x
  df['x^3'] = pow(df['Riesgo X'],3)#crear una nueva columna llamada x^3 la cual contendrá los cubos de la variable x
  df['x^4'] = pow(df['Riesgo X'],4)#crear una nueva columna llamada x^4 la cual contendrá las cuartas potencias de la variable x
  df['x^2*y'] = df['x^2']*df['Rendimiento Y(%)']#crear una nueva columna llamada x^2 la cual contendrá los cuadrados de la variable x multiplicado por cada una de las varibales y


  n = len(df.index) #n: numero total de datos
  sumx = df['Riesgo X'].sum() #sumatoria de las x
  sumy = df['Rendimiento Y(%)'].sum()#sumatoria de las y
  sumxy = df['x*y'].sum()#sumatoria de las x*y
  sumx_2 = pow(sumx,2)#sumatoria de las (x)^2
  sumx2 = df['x^2'].sum()# sumatoria de las x^2
  sumx3 = df['x^3'].sum()#sumatoria de las x^3
  sumx4 = df['x^4'].sum()#sumatoria de las x^4
  sumx2y = df['x^2*y'].sum()#sumatoria de las x^2*y

  a1 = ((n*sumxy) - (sumx*sumy)) / ((n*sumx2) - (sumx_2))#coeficente a1 con base a las sumatorias anteriores
  a0 = ((sumy*sumx2) - (sumx*sumxy)) / ((n*sumx2)- sumx_2)#coeficiente a0 con base a las sumatorias anteriores


#método de resolución de sistémas de ecuaciones a partir de la librería numpy
  a = np.array([[n,sumx,sumx2],[sumx,sumx2,sumx3],[sumx2,sumx3,sumx4]])#matriz de coeficientes
  b = np.array([sumy,sumxy,sumx2y])#vector de terminos independientes
  x = np.linalg.solve(a,b)#solucuión del sistema (un vector solución)
  r = np.corrcoef(df['Riesgo X'], df['Rendimiento Y(%)'])#coeficiente de correlación lienal de pearson

  df['e(y-y^)^2'] = pow(df['Rendimiento Y(%)'] - (x[2]*pow(df['Riesgo X'],2) + x[1]*df['Riesgo X'] +   x[0]),2)#errores (y_real - y_calculado_con_polinomio_grado_dos) al cuadrado
  df['SCT'] = pow(df['Rendimiento Y(%)'] - (sumy/n),2)#cuadrados totales (necesarios para calcular el coeficiente de correlación en el polinomio y así calcular el coeficiente de determinación)

  SCE = df['e(y-y^)^2'].sum()#suma de los cuadrados de los errores
  SCT = df['SCT'].sum()#suma de los cuadrados totales

  r2_pol = (SCT-SCE)/SCT #coeficiente de determinación polinomial con base en los errores
  r_pol = np.sqrt(r2_pol)#coeficiente de correlación polinomial con base en los errores

  print(df)

  print("\n")

  print("y = "+str(a1)+"x + "+str(a0)+"\n")
  print("El coeficiente de correlación lineal de pearson r es: ", r[1][0])
  print("El coeficiente de determinación lineal R^2 es: ", pow(r[1][0],2))

  print("\n")

  print("y = "+str(x[2])+"x^2 + "+str(x[1])+"x + "+str(x[0])+"\n")
  print("El coeficiente de correlación polinomial r es: ", r_pol)
  print("El coeficiente de determinación polinomial R^2 es: ", r2_pol)
  print("\n")

r = 0

while(r != 3):
  print("Menú")
  print("1. Regresión polinomial y lineal de Año vs catidad_madera")
  print("2. Regresión lineal y polinomial Riesgo vs Rendimiento")
  print("3. Salir")
  r = int(input("Digite la opción: "))
  if(r == 1):
    regresion_madera()
  if(r == 2):
    regresion_finanzas()

