# This code is to learn how To parameterize the code so that it accepts parameters from the command line,
# you can modify the script to take the source folder (~/Afolder), 
# destination folder (~/Bfolder), and the filename (a.txt) as command-line arguments.

if [ "$#" -lt 3] # this checks if the number of command line arguments passed are less than 3
then
    echo "Usage: $0 <source_folder> <destination_folder> <filename>"
    exit 1
fi

source_folder="$!"
destination_folder="$2"
filename="$3"

find "$source_folder" -name '.*txt' -exec cp {} "$destination_folder"/ \;
cd "$destination_folder"

if [ -f "$filename"]
then
   echo "filename $filename exists"
else
   echo "filename $filename does not exist"
fi

# execute this script by passing the "./project.sh ~/Afolder ~/Bfolder a.txt" through command line

