#!/bin/bash

i=0

for file in ./bam/*; do
	acc="${file##*/}"
	acc="${acc%%.*}"
	if (( i >= 15 )); then
		wait
		i=0
	fi
	if [ ! -f "./loom/$acc.loom" ]; then
	velocyto run-smartseq2 -v -o loom -m mm10_rmsk.gtf -e $acc $file Homo_sapiens.GRCh38.84.gtf &
	((i++))
	fi
done
wait
