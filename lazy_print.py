import sys, os, subprocess
from pdf2image import convert_from_path # pip install pdf2image

def convert_to_images(pdf_path):
    pages = convert_from_path(pdf_path, 500)

    if os.name == 'posix':
        cont = raw_input('Do you want to print {0} pages (y/n): '.format(len(pages)))
        if cont.lower() == 'y' or cont.lower() == 'yes':
            print("Watch out, we're printing!")

            for x, page in enumerate(convert_from_path(pdf_path)):
                new_path = "{0}{1}.jpg".format(pdf_path.split('.')[0], x)
                page.save(new_path, 'JPEG')
                os.system('lp {0}'.format(new_path))
        else:
            print "Fine then loser, you don't deserve to print anyway."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SyntaxError("Improper arguments.")
    else:
        convert_to_images(sys.argv[1])
