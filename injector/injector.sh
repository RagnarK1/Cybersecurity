#!/bin/bash

# Check if enough arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <bin> <helloworld> <custom_bin_word> <custom_helloworld_message>"
    exit 1
fi

# Original binary names
bin="./$1"   
helloworld="./$2"
custom_bin_word="$3"
custom_helloworld_message="$4"

# Check if bin and helloworld exist and are executable
if [ ! -x "$bin" ]; then
    echo "Error: $bin is not an executable file."
    exit 1
fi

if [ ! -x "$helloworld" ]; then
    echo "Error: $helloworld is not an executable file."
    exit 1
fi

# Define a function to inject custom messages into bin and helloworld
inject_and_execute() {
    # Create a new script to combine the outputs
    temp_bin="temp_bin.sh"
    echo "#!/bin/bash" > $temp_bin
    echo "$bin $custom_bin_word" >> $temp_bin
    echo "$helloworld \"$custom_helloworld_message\"" >> $temp_bin

    # Make the new script executable
    chmod +x $temp_bin

    # Execute the new script
    ./$temp_bin

    # Optionally remove the temp script after execution
    rm $temp_bin
}

# Run the injection and execution function with the provided arguments
inject_and_execute
