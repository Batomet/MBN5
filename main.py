import arxiv
import fitz
import io
from PIL import Image

# searchIEEE11 = arxiv.Search(
#     query="IEEE 2011",
#     max_results=30
# )
# i = 0
# for result in searchIEEE11.results():
#     result.download_pdf(dirpath="D:\MBN\PDFY1", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")
#
# searchIEEE21 = arxiv.Search(
#     query="IEEE 2021",
#     max_results=30
# )
# i = 0
# for result in searchIEEE21.results():
#     result.download_pdf(dirpath="D:\MBN\PDFY2", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")
#
# searchSD11 = arxiv.Search(
#     query="ScienceDirect 2011",
#     max_results=30
# )
# i = 0
# for result in searchSD11.results():
#     result.download_pdf(dirpath="D:\MBN\PDFY3", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")
#
# searchSD21 = arxiv.Search(
#     query="ScienceDirect 2021",
#     max_results=30
# )
# i = 0
# for result in searchSD21.results():
#     result.download_pdf(dirpath="D:\MBN\PDFY4", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")

j = 0
k = 0

for k in range(4):
    m = 0
    for j in range(30):
        file = f"D:\MBN\PDFY{k + 1}\paper{j}.pdf"
        x = 0
        # open the file
        pdf_file = fitz.open(file)
        for page_index in range(len(pdf_file)):
            # get the page itself
            page = pdf_file[page_index]
            image_list = page.get_images()
            # printing number of images found in this page
            if image_list:
                x += len(image_list)
        m+=x
        # print(f"Znaleziono: {x} obrazki w pliku pdf{j}")
        j += 1
    print(f"Znaleziono: {m} obrazków w plikach pdf{k+1}")
    print(f"Średnia obrazków: {m/30} w pdfy{k+1}\n")
    f = open("D:\MBN\iloscObrazkow.txt", "a")
    f.write(f"Znaleziono: {m} obrazki w plikach pdfy{k+1}\n")
    f.write(f"Średnia obrazków: {m/30} w pdfy{k+1}\n")
    f.close()
