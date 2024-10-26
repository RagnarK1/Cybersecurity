import sys
from elftools.elf.elffile import ELFFile

def merge_elf(bin1_filename, bin2_filename, output_filename):
    with open(bin1_filename, 'rb') as bin1_file, \
        open(bin2_filename, 'rb') as bin2_file:
        
        elf1 = ELFFile(bin1_file)
        elf2 = ELFFile(bin2_file)
        
        # Check that both files are ELF binaries
        if not elf1.has_dwarf_info() or not elf2.has_dwarf_info():
            print("Error: Input files are not valid ELF binaries.")
            return
        
        # Assuming bin1 entry point will be used for the merged binary
        entry_point = elf1.header['e_entry']
        
        # Start constructing the merged ELF file
        with open(output_filename, 'wb') as output_file:
            # Write ELF header and program headers of bin1
            output_file.write(bin1_file.read(elf1.header['e_phoff']))
            
            # Merge program headers from both ELF files
            # For simplicity, just use program headers from the first ELF file
            output_file.write(bin1_file.read(elf1.header['e_phentsize'] * elf1.header['e_phnum']))
            
            # Merge section headers from both ELF files
            # Skip section headers of the first ELF file
            bin1_file.seek(elf1.header['e_shoff'] + elf1.header['e_shentsize'] * elf1.header['e_shnum'])
            output_file.write(bin1_file.read())
            
            # Merge sections from both ELF files
            for section in elf1.iter_sections():
                if section.header['sh_type'] == 'SHT_NULL':
                    continue
                bin1_file.seek(section.header['sh_offset'])
                output_file.write(bin1_file.read(section.header['sh_size']))
            
            for section in elf2.iter_sections():
                if section.header['sh_type'] == 'SHT_NULL':
                    continue
                bin2_file.seek(section.header['sh_offset'])
                output_file.write(bin2_file.read(section.header['sh_size']))
            
            # Set the entry point for the merged binary
            output_file.seek(24)  # Assuming e_entry offset in ELF header
            output_file.write(entry_point.to_bytes(8, byteorder='little'))  # 64-bit entry point
            
            print(f"Merged binary saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python injector.py bin1 bin2 output")
        sys.exit(1)
    
    bin1_filename = sys.argv[1]
    bin2_filename = sys.argv[2]
    output_filename = sys.argv[3]
    
    merge_elf(bin1_filename, bin2_filename, output_filename)
