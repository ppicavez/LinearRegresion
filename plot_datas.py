# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot_datas.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/05 15:55:53 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/05 16:44:20 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np
import  estimate

thetas =[]
if estimate.verifyFile("parameters",thetas) :
    plt.title('Results of training')
    theta1 = float(thetas[0]) 
    theta0 = float(thetas[1])
    data = np.genfromtxt('./data.csv', delimiter=',')[1:]
    mileage = data[:, 0]
    price = data[:, 1]
    plt.scatter(mileage, price)
    plt.xlabel("mileage")
    plt.ylabel("price")

    x = np.linspace(8000, 250000, 10)
    y = theta1*x + theta0
    plt.plot(x, y, '-r')
    plt.show()

    
