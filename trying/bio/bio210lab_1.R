library(ggplot2)
ggplot(iris,aes(x = Sepal.Length)) + geom_histograph(bins=10)