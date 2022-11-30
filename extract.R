# apt install libgdal-dev libcurl4-openssl-dev libssl-dev
# install.packages("lingtypology")

# https://github.com/ropensci/lingtypology
# https://ropensci.github.io/lingtypology/lingtypology_db_API.html
# https://agricolamz.github.io/2018_Areal_Patterns/1_day.html
# https://github.com/autotyp/autotyp-data
# https://gitlab.inria.fr/ud-greenberg/ranlp-2021
# https://clld.org/datasets.html

library(lingtypology)

df <- wals.feature(c('81a', '82a', '83a'))

# Learn more R ...
#df_macroarea <- area.lang(df$language)
#merge(df, df_macroarea, by="Area")

write.table(df, "wals.tsv", fileEncoding="UTF-8", sep="\t")



