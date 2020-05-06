# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train_model.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ppicavez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/06 10:47:01 by ppicavez          #+#    #+#              #
#    Updated: 2020/03/06 11:34:23 by ppicavez         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #


import csv

def saveResults(thetas,fileName):
    fileOut = open(fileName,'w')
    fileOut.write(str(thetas[0]))
    fileOut.write('\n')
    fileOut.write(str(thetas[1]))
    fileOut.close()

thetas = []
thetas.append(0.0)
thetas.append(-1.1)
saveResults(thetas,'test')

def main():
    mileages =[]
    prices =[]

    with open('data.csv', 'r') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        firstLine = True;
        try:
            for row in dataReader:
                if firstLine:
                    firstLine = False
                else:
                    mileages.append(float(row[0]))
                    prices.append(float(row[1]))

        except csv.error as e:
            sys.exit('file {}, line {}: {}'.format(fileName, dataReader.line_num, e))

if __name__ == '__main__':
    main()
