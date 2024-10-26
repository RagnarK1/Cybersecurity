import argparse
from PIL import Image
import exifread

def extract_metadata(image_path):
    # Open the image file for reading in binary mode
    with open(image_path, 'rb') as f:
        # Read the metadata using exifread
        tags = exifread.process_file(f)

        # Check if GPSInfo is in the metadata
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            # Extract latitude
            latitude = tags['GPS GPSLatitude']
            lat_degrees = latitude.values[0].num / latitude.values[0].den
            lat_minutes = latitude.values[1].num / latitude.values[1].den
            lat_seconds = latitude.values[2].num / latitude.values[2].den
            lat_direction = str(tags['GPS GPSLatitudeRef'])

            # Convert latitude to decimal degrees
            latitude_decimal = lat_degrees + lat_minutes / 60 + lat_seconds / 3600
            if lat_direction == 'S':
                latitude_decimal *= -1

            # Extract longitude
            longitude = tags['GPS GPSLongitude']
            lon_degrees = longitude.values[0].num / longitude.values[0].den
            lon_minutes = longitude.values[1].num / longitude.values[1].den
            lon_seconds = longitude.values[2].num / longitude.values[2].den
            lon_direction = str(tags['GPS GPSLongitudeRef'])

            # Convert longitude to decimal degrees
            longitude_decimal = lon_degrees + lon_minutes / 60 + lon_seconds / 3600
            if lon_direction == 'W':
                longitude_decimal *= -1

            # Convert latitude and longitude to integers
            latitude_int = int(latitude_decimal)
            longitude_int = int(longitude_decimal)

            return latitude_int, longitude_int
        else:
            return None, None

def detect_steganography(image):
    # Extract pixel values
    pixels = image.getdata()

    # Check the LSB (Least Significant Bit) of each color channel for every pixel
    for pixel in pixels:
        for value in pixel:
            # If any LSB is non-zero, steganography may be present
            if value & 1:
                return True

    # If all LSBs are zero, steganography is unlikely
    return False

def decode_steganography(image):
    # Extract pixel values
    pixels = image.getdata()

    # Initialize an empty list to store the binary data
    binary_data = []

    # Iterate through each pixel
    for pixel in pixels:
        # Iterate through each color channel value (R, G, B)
        for value in pixel:
            # Extract the LSB (Least Significant Bit) from each value
            lsb = value & 1
            # Append the LSB to the binary data list
            binary_data.append(str(lsb))

    # Convert the binary data list to a string
    binary_string = ''.join(binary_data)

    # Convert the binary string to ASCII characters
    message = ''
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        message += chr(int(byte, 2))

    # Construct PGP public key block
    pgp_key_block = "-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
    pgp_key_block += message + "\n"
    pgp_key_block += "-----END PGP PUBLIC KEY BLOCK-----"

    return pgp_key_block

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Inspector Image')

    # Add positional argument for the image file
    parser.add_argument('image', type=str, help='Path to the image')

    # Add optional arguments for -map and -steg
    parser.add_argument('-map', action='store_true', help='Show the location where the photo was taken')
    parser.add_argument('-steg', action='store_true', help='Show the hidden message in the image')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Open the image
    image = Image.open(args.image)

    # If -map option is provided, extract and display metadata
    if args.map:
        latitude, longitude = extract_metadata(args.image)
        if latitude is not None and longitude is not None:
            print(f"Lat/Lon:\t({latitude}) / ({longitude})")
        else:
            print("Location information not found in metadata.")

    # If -steg option is provided, detect and decode steganography
    if args.steg:
        if detect_steganography(image):
            hidden_message = decode_steganography(image)
            if hidden_message:
                print(hidden_message)
            else:
                print("No hidden message found in the image.")
        else:
            print("No steganography detected in the image.")

if __name__ == "__main__":
    main()