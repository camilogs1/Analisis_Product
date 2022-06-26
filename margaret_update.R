library(margaret)
library(tidyverse)

groups <- read_csv("https://docs.google.com/spreadsheets/d/1gBaXHFp1NTUTeXodb4JyHqY-P-AWV5yN5-p4L1O09gk/export?format=csv&gid=0")
researchers  <-  read_csv("https://docs.google.com/spreadsheets/d/1gBaXHFp1NTUTeXodb4JyHqY-P-AWV5yN5-p4L1O09gk/export?format=csv&gid=347194763")

margaret_updated <-
  getting_data(groups, researchers)

