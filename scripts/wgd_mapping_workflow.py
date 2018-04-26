import os, sys, shutil


main_folder = sys.argv[1]
target_folder = os.path.join(main_folder, "01_mapping")
script = os.path.join(main_folder, "scripts", "mapping.sh")

genes = os.listdir(target_folder)

def get_path_exon(gene):
    gene_path = os.path.join(target_folder, gene)
    con_fldr = os.path.join(gene_path, "consensus")
    files = os.listdir(con_fldr)
    paths = [os.path.join(con_fldr, e) for e in files]
    exons = [e.replace(".fasta", "") for e in files]
    return zip(paths, exons)           
            
def get_species(gene):
    gene_path = os.path.join(target_folder, gene)
    fldr = os.listdir(gene_path)
    return [e for e in fldr if e != 'consensus'] 
            
def main():
    for gene in genes:
        gene_path = os.path.join(target_folder, gene)
        paths_exons = get_path_exon(gene)
        spp = get_species(gene)
        for sp in spp:
            for path, exon in paths_exons:
                output_folder = os.path.join(gene_path, sp)
                os.chdir(output_folder)
                os.system("{0} {1} {2} {3}".format(script, sp, exon, path))


main()