## Set up for Mutect2

tar_info = read.csv("/Users/meganlynch/Dropbox/Mac/Documents/CHIP/GeneSTAR_WES_manifest_plates1to11_02032023_long.csv", header=TRUE)
length(tar_info[,1])


### Which files do we need?
### Which files are the 'panel of norms'

# Somatic variant calling pipeline to detect CHIP (GATK ToolKit). Uses local haplotype assembly and Bayesian modelling to detect SNPs
# and small indels.

# Limit scan for putative CHIP variants to those contained in Supplemental Table 1.
# canonical CHIP driver variants


#    tar -xvf /dcl01/mathias1/data/Becker_WES/2002UNHS-0345/30402/30402.tar 30402.recal.bam.bai
#    tar -xvf /dcl01/mathias1/data/Becker_WES/2002UNHS-0345/30402/30402.tar 30402.recal.bam

write("#$ -cwd", file="tarCommands_Bai.sh")
write("#$ -cwd", file="tarCommands_Bam.sh")


write("cd /dcs04/mathias/data/mlynch/9_CHIP/bams", file="tarCommands_Bai.sh", append=T)
write("cd /dcs04/mathias/data/mlynch/9_CHIP/bams", file="tarCommands_Bam.sh", append=T)


#i=7
clustersite_fix <- c()
for (i in 1:length(tar_info$clustersite))
{
  if (endsWith(tar_info$clustersite[i], '/')) ## check that it ends with '/'
  {
    clustersite_fix <- c(clustersite_fix, tar_info$clustersite[i])
    
  }
  else 
  {
    fixed <- paste(tar_info$clustersite[i], '/', collapse="", sep="")
    ## add / then append
    clustersite_fix <- c(clustersite_fix, fixed)
  }
}



#m=3
for (m in 1:length(tar_info[,1]))
{
  bai_line <- paste("tar -xvf ", clustersite_fix[m], tar_info$sample[m], "/", tar_info$sample[m], ".tar ", tar_info$sample[m],".recal.bam.bai", collapse="", sep="")
  write(bai_line, file="tarCommands_Bai.sh", append=T)
  bam_line <- paste("tar -xvf ", clustersite_fix[m], tar_info$sample[m], "/", tar_info$sample[m], ".tar ", tar_info$sample[m],".recal.bam", collapse="", sep="")
  write(bam_line, file="tarCommands_Bam.sh", append=T)
}
