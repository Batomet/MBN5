import arxiv
import fitz
import io
import time
def dowonload_pdfs(query):
    
    searchIEEE11 = arxiv.Search(
        query,
        max_results=30
    )
    i = 0
    for result in searchIEEE11.results():
        result.download_pdf(dirpath="D:\MBN\PDFY1", filename="paper{}.pdf".format(i))
        i+=1
    print("Success")



def scan_for_img():
    num_paper = 0
    for k in range(4):
        num_img = 0
        for num_paper in range(30):
            file = f"D:\MBN\PDFY{k + 1}\paper{num_paper}.pdf"
            x = 0
            pdf_file = fitz.open(file)
            for page_index in range(len(pdf_file)):
                page = pdf_file[page_index]
                image_list = page.get_images()
                if image_list:
                    x += len(image_list)
            num_img+=x
            num_paper += 1
        print(f"Znaleziono: {num_img} obrazków w plikach pdf{k+1}")
        print(f"Średnia obrazków: {num_img/30} w pdfy{k+1}\n")
        f = open("D:\MBN\iloscObrazkow.txt", "a")
        f.write(f"Znaleziono: {num_img} obrazki w plikach pdfy{k+1}\n")
        f.write(f"Średnia obrazków: {num_img/30} w pdfy{k+1}\n")
        f.close()

def main():
    start_time = time.time()
    dowonload_pdfs("IEEE 2011")
    scan_for_img()
    print("--- Czas wykonywania: {} sekund ---".format(round(time.time() - start_time,2)))


if __name__=='__main__':
    main()
