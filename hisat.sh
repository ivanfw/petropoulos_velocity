for file in /media/mdehsfs4/Data/yicheng/trimmed/*; do
	accession="${file##*/}"
	accession="${accession%.*}"
	accession="${accession%.*}"
	if [ ! -f "./loom/$accession.loom" ]; then
		hisat2 -f -t -p 18 -U "$file" -x grch38/genome -S "./bam/$accession.sam"
		samtools view -bS "./bam/$accession.sam" | samtools sort > "./bam/$accession.bam"
		rm "./bam/$accession.sam"
	fi
done
