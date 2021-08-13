###############################################################################
#
#   Create conda virtual environment for bindz (dev)
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: maciej.bak@unibas.ch
#   CREATED: 04-07-2020
#   LICENSE: Apache_2.0
#   USAGE: bash create-conda-environment-dev.sh
#
###############################################################################

CWD="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
conda env create --file "$CWD"/../envs/dev.yml
