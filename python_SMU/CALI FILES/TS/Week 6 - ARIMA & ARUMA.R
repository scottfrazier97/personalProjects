library(tswge)
library(ggplot2)
library(tidyverse)

# From ASYNC
x = gen.arima.wge(200, phi=c(.6, -.8), d=2, var = 1)
acf(x)

firstDiff = artrans.wge(x,2)
parzen.wge(firstDiff)
aic5.wge(firstDiff)

#What is the system frequency for the complex root?
ar = mult.wge(fac1 = c(.6, -.8), fac2 = 1, fac3 = 1)
factor.wge(ar$model.coef)

#Generate a realization of size 500, with seed 37. What is the biggest
# peak in the spectral density?
x2 = gen.arima.wge(500, phi=c(.6, -.8), d=2, var = 1, sn=35)
diff = artrans.wge(x2, 1)
parzen.wge(diff)

#Generate a realization of size 500, with seed 35. and then take the 
# second differences. Use aic5 to get the top five autocorrelations
# structure of the second differenced data. What is favored by AIC?

secondDiff = artrans.wge(diff, 1)
parzen.wge(secondDiff)
aic5.wge(secondDiff)


#Seasonal Model with s = 7
seas = gen.aruma.wge(n=80, s=7, sn=6)
plotts.sample.wge(seas)

seas2 = gen.aruma.wge(n=80, phi=c(.6,-.8), s = 7, theta=.5, sn=6)
plotts.sample.wge(seas2)
factor.wge(seas2)

#ASYNC Example
x3 = gen.aruma.wge(n=80, phi = c(.6,-.94), s = 6, theta = -.3, sn=19)
plotts.sample.wge(x3)

x4 = gen.aruma.wge(n=500, phi = c(.6, -.8), s= 12, theta = c(.3, -.7), sn = 35)
diffx4 = artrans.wge(x4,c(rep(0,11),1))
aic5.wge(diffx4)

#FLS models
x5 = gen.aruma.wge(n=80, phi=c(.6, -.8), s= 4, theta = c(-.3))
diffx5 = artrans.wge(x5,c(0,0,0,1))
aic5.wge(diffx5)

x6 = gen.aruma.wge(n=80, phi=c(.6, -.8), s= 4, theta = c(-.3))
diffx6 = artrans.wge(x6,c(0,0,0,1))
aic5.wge(diffx6)

x7 = gen.aruma.wge(n=80, phi=c(.6, -.8), s= 4, theta = c(-.3))
diffx7 = artrans.wge(x7,c(0,0,0,1))
aic5.wge(diffx7)

AAL = read.csv(file.choose(), header = T)
diffAAL = artrans.wge(AAL$close, 1)
aic5.wge(diffAAL)
