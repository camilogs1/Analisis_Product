library(margaret)
library(tidyverse)

groups <- read_csv("https://docs.google.com/spreadsheets/d/1OFg9Jzypg_uwsmFxyXFSgtdfXfgsN9AG/export?format=csv&gid=808772593")
researchers  <-  read_csv("https://docs.google.com/spreadsheets/d/1mpwR15wHbrFbO1s8DWsDdLta_aou7gHD/export?format=csv&gid=2102359855")

margaret_updated <-
  getting_data(groups, researchers)

