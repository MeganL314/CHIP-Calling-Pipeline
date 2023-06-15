## Set up for Mutect2

tar_info = read.csv("/path/to/BamIDs.csv", header=TRUE)
length(tar_info[,1])

write("#$ -cwd", file="tarCommands_Bai.sh")
write("#$ -cwd", file="tarCommands_Bam.sh")


write("cd /path/to/bams", file="tarCommands_Bai.sh", append=T)
write("cd /path/to/bams", file="tarCommands_Bam.sh", append=T)


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






