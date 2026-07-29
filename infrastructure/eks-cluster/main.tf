provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "a3-i3-super-cluster"
  cluster_version = "1.30"
  
  vpc_id                   = module.vpc.vpc_id
  subnet_ids               = module.vpc.private_subnets
  control_plane_subnet_ids = module.vpc.intra_subnets

  eks_managed_node_groups = {
    ai_quantum_nodes = {
      desired_size = 2
      min_size     = 1
      max_size     = 5

      instance_types = ["g4dn.xlarge"]
      ami_type       = "AL2_x86_64_GPU" 
      
      labels = {
        workload = "a3-i3-core"
        hardware = "nvidia-cuda"
      }
    }
  }
}
