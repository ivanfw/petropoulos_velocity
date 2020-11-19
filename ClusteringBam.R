library(Rsubread)

bam.files <- list.files(path = "/media/mdehsfs4/Scratch/yicheng/bam/", pattern = ".bam$", full.names = TRUE)
bam.files


fc <- featureCounts(bam.files, annot.inbuilt="hg38", nthreads = 12)
names(fc)
fc$stat
dim(fc$counts)
head(fc$counts)
head(fc$annotation)