import numpy
import sys
from matplotlib import pyplot as plt


prob = float(sys.argv[1])
COLS = int(sys.argv[2])
ROWS = int(sys.argv[3])
generations = int(sys.argv[4])
prob = 0.7
COLS = 20
ROWS = 19
generations = 100

N=numpy.random.binomial(1,prob,size=(ROWS+2)*COLS)
M=numpy.reshape(N,(ROWS+2,COLS))

M[0,:] = 0
M[ROWS+1,:] = 0
M[:,0] = 0
M[:,COLS-1] = 0

initM = numpy.copy(M)
#print initM
print("First Generation")

plt.imshow(initM, interpolation='nearest')
plt.show()

generation = 0
for i in range(generations):
        generation = generation + 1
 #       print ("Generation = ",generation)
        intermediateM = numpy.copy(M)
        for ROWelem in range(1,ROWS+1):
                for COLelem in range(1,COLS-1):
                        sum = ( M[ROWelem-1,COLelem-1]+M[ROWelem-1,COLelem]+M[ROWelem-1,COLelem+1]
                            +M[ROWelem,COLelem-1]+M[ROWelem,COLelem+1]
                            +M[ROWelem+1,COLelem-1]+M[ROWelem+1,COLelem]+M[ROWelem+1,COLelem+1] )
        #               print(ROWelem," ",COLelem," ",sum)
                        if M[ROWelem,COLelem] == 1:
                                if sum < 2:
                                        intermediateM[ROWelem,COLelem] = 0
                                elif sum > 3:
                                        intermediateM[ROWelem,COLelem] = 0
                                else:
                                        intermediateM[ROWelem,COLelem] = 1
                        if M[ROWelem,COLelem] == 0:
                                if sum == 3:
                                        intermediateM[ROWelem,COLelem] = 1
                                else:
                                        intermediateM[ROWelem,COLelem] = 0
        M = numpy.copy(intermediateM)
        plt.imshow(M, interpolation='nearest')
        plt.show()
        if numpy.sum(M) == 0:
                print("Extinction Occurs at generation = ",generation)
      #          plt.imshow(M, interpolation='nearest')
      #          plt.show()
                break
      #  print(" ")
      #  print M

#print(" ")
#print(" ")
#print("First Generation")
#print initM

#print(" ")
print("Present Generation")
#print M
plt.imshow(M, interpolation='nearest')
plt.show()
