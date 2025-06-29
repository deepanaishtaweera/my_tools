#!/usr/bin/env python3
"""
PDF Combiner Script

This script takes all PDF files from a specified folder and combines them into a single PDF file.
The files are combined in alphabetical order by filename.

Usage:
    python pdf_combiner.py input_folder output_file.pdf
"""

import os
import sys
import glob
import argparse
from pathlib import Path
from PyPDF2 import PdfMerger


def combine_pdfs(input_folder, output_file):
    """
    Combine all PDF files from the input folder into a single PDF file.

    Args:
        input_folder (str): Path to the folder containing PDF files
        output_file (str): Path for the output combined PDF file
    """
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return False

    # Find all PDF files in the input folder
    pdf_pattern = os.path.join(input_folder, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)

    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'")
        return False

    # Sort files alphabetically
    pdf_files.sort()

    print(f"Found {len(pdf_files)} PDF files:")
    for pdf_file in pdf_files:
        print(f"  - {os.path.basename(pdf_file)}")

    try:
        # Create a PDF merger object
        merger = PdfMerger()

        # Add each PDF file to the merger
        for pdf_file in pdf_files:
            print(f"Adding: {os.path.basename(pdf_file)}")
            merger.append(pdf_file)

        # Write the combined PDF to the output file
        print(f"Combining PDFs into: {output_file}")
        merger.write(output_file)
        merger.close()

        print(f"Successfully combined {len(pdf_files)} PDF files into '{output_file}'")
        return True

    except Exception as e:
        print(f"Error combining PDF files: {str(e)}")
        return False


def parse_arguments():
    """Parse command line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Combine multiple PDF files from a folder into a single PDF file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdf_combiner.py ./documents combined.pdf
  python pdf_combiner.py /path/to/pdfs final_report.pdf
  python pdf_combiner.py ./reports output  # Will create output.pdf
        """,
    )

    parser.add_argument(
        "input_folder", help="Path to the folder containing PDF files to combine",
    )

    parser.add_argument(
        "output_file",
        help="Path for the output combined PDF file (will add .pdf extension if not provided)",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    parser.add_argument("--version", action="version", version="PDF Combiner v1.0")

    return parser.parse_args()


def main():
    """Main function to handle command line arguments and execute the PDF combination."""
    args = parse_arguments()

    input_folder = args.input_folder
    output_file = args.output_file

    # Ensure output file has .pdf extension
    if not output_file.lower().endswith(".pdf"):
        output_file += ".pdf"

    # Validate input folder
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a directory.")
        sys.exit(1)

    print("PDF Combiner")
    print("=" * 50)
    print(f"Input folder: {input_folder}")
    print(f"Output file: {output_file}")
    if args.verbose:
        print(f"Verbose mode: enabled")
    print("=" * 50)

    success = combine_pdfs(input_folder, output_file)

    if success:
        print("\n✅ PDF combination completed successfully!")
    else:
        print("\n❌ PDF combination failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
