import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()


prob = 0.70
COLS = 200
ROWS = 98
generations = 100

N=numpy.random.binomial(1,prob,size=(ROWS+2)*COLS)
M=numpy.reshape(N,(ROWS+2,COLS))

M[0,:] = 0
M[ROWS+1,:] = 0
M[:,0] = 0
M[:,COLS-1] = 0

initM = numpy.copy(M)
print("First Generation")

generation = 0
ims=[]
for i in xrange(generations):
        generation = generation + 1
        intermediateM = numpy.copy(M)
        for ROWelem in xrange(1,ROWS+1):
                for COLelem in xrange(1,COLS-1):
                        sum = ( M[ROWelem-1,COLelem-1]+M[ROWelem-1,COLelem]+M[ROWelem-1,COLelem+1]
                            +M[ROWelem,COLelem-1]+M[ROWelem,COLelem+1]
                            +M[ROWelem+1,COLelem-1]+M[ROWelem+1,COLelem]+M[ROWelem+1,COLelem+1] )
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
        im=plt.imshow(M, animated=True,interpolation='None')
        ims.append([im])
        if numpy.sum(M) == 0:
                print("Extinction Occurs at generation = ",generation)
                break

print("Present Generation = %d" %(generation))
ani = animation.ArtistAnimation(fig, ims, interval=250, blit=True,repeat_delay=500)
ani.save('game_of_life.mp4')

plt.show()
