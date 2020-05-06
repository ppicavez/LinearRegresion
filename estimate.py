# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    estimate.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 10:26:31 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 14:15:50 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import os.path
import sys
import re

def verifyFile(fileName,thetas):
    ret = True
    thetas.append(0.0);
    thetas.append(0.0);

    if os.path.exists(fileName) == False :
        print ('Error : parameters file doesnt exists !!')
        ret = False
    else :
        try:
          parametersFile = open(fileName,'r')
        except:
            print("Error : cannot open file parameters !!")  
            ret = False
        try:
            lines = parametersFile.readlines()
        except:
            parametersFile.close()
            print("Error : file parametres is empty !!")  
            ret = False
        
        parametersFile.close()
        if len(lines) != 2 :
            print ('Error : file parameter must have 2 lines. First for theta0 and second for theta1 !!');
        else:    
            try:
                thetas[0] = float(lines[0])
            except:
                print("Error :  parameter theta0 is not a real number !!")  
                ret = False
            try:
                thetas[1] = float(lines[1])
            except:
                print("Error :  parameter theta1 is not a real number !!")  
                ret = False
        return ret

def main():
    thetas = [] 
    mileage = 0
    if verifyFile("parameters",thetas) :
        if len(sys.argv) != 2 :
            print ('Usage : python estimate.py mileage')
        else :
            try:
                mileage = int(sys.argv[1])
            except:
                print("Mileage must be an integer value !")
                return


            if mileage <= 0 :
                print("Mileage must > 0 !")
            else :
                carPrice = thetas[0] * mileage + thetas[1] 
                print("Using theta0 = %f, theta1 =%f" % (theta[0], theta[1]))
                print('A car with '+str(mileage)+' mile(s) have an evaluated price of '+str(carPrice))
    return 0

if __name__ == '__main__' :
	main()	 
# calculate and print the estimated price
