library("Rsubread")
files <- list.files("./bam/", full.names = TRUE)
files
features <- featureCounts(list.files("./bam/", full.names = TRUE), annot.inbuilt = "hg38", nthreads = 18)
counts <- features$counts

library("org.Hs.eg.db")
library("annotate")

rownames(counts) <- getSYMBOL(rownames(counts), data="org.Hs.eg")