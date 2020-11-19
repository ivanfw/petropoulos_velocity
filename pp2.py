import numpy as np
import pandas as pd

avital_time_points = {0: "T0", 2: "T2.5", 4: "T4", 8: "T8"}


def is_mouse_gene(gene_name):
    return gene_name.startswith("N")


def is_salmonella_gene(gene_name):
    return gene_name.startswith("S")


def classify_gene_organism(gene_name):
    if is_mouse_gene(gene_name):
        return "mouse"
    if is_salmonella_gene(gene_name):
        return "salmonella"
    return np.nan


def is_coding_gene(gene_name):
    if is_mouse_gene(gene_name):
        if gene_name.startswith("NM_"):
            return True  # e.g. NM_001001130
        return False  # e.g. NR_024324
    if is_salmonella_gene(gene_name):
        if gene_name.startswith("SL1344_P"):
            return True  # e.g. SL1344_P2_0022
        if len(gene_name) == 11:
            return True  # SL1344_0479
        return False  # e.g. SL1344_tRNA0086
    return np.nan  # e.g. GFP


def annotate_cells(dataframe):
    dataframe.index.name = "cell"
    dataframe["time"] = dataframe.index.str.slice(1, 2).astype(np.int)
    dataframe["time_name"] = dataframe.time.map(avital_time_points)
    dataframe["exposed"] = dataframe.time > 0


def annotate_genes(dataframe):
    dataframe.index.name = "gene"
    dataframe["organism"] = dataframe.index.map(classify_gene_organism)
    dataframe["coding"] = dataframe.index.map(is_coding_gene)


def join_gene_info(dataframe):
    gene_info_df = pd.read_csv("mouse_genes_RefSeq.csv", index_col=0)
    new_df = dataframe.merge(gene_info_df,
                             left_index=True,
                             right_index=True,
                             how="left",
                             validate="1:1")
    new_df["name_or_id"] = new_df.name
    new_df.name_or_id.loc[new_df.name.isna()] = new_df.index[new_df.name.isna()]
    return new_df
