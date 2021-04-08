from zipfile import ZipFile
import os

INFOLDER = ["LogFiles40^0", "LogFiles40^10", "LogFiles40^20", "LogFiles60^0", "LogFiles60^10", "LogFiles60^20", "full^10"]
data_info = ["ch120-160.txt", "ch420-480.txt", "ch50-100.txt", "80.txt",
             "120.txt", "180.txt", "280.txt", "320.txt", "120-160.txt", "130-200.txt"]


def extract_gyro(infile, outfile):
    f = open(infile, "r",encoding="utf8")
    f_out = open(outfile, "w")
    line = f.readline().split(';')
    t = []
    x = []
    y = []
    z = []
    lenght = 0
    while line:
        if line[0] == 'GYRO':
            t.append(line[2])
            x.append(line[3])
            y.append(line[4])
            z.append(line[5])
            lenght += 1
        elif line[0] == '':
            break
        line = f.readline().split(';')

    for i in range(lenght):
        f_out.write(t[i])
        f_out.write(' ')
        f_out.write(x[i])
        f_out.write(' ')
        f_out.write(y[i])
        f_out.write(' ')
        f_out.write(z[i])
        f_out.write('\n')
    f_out.close()


def trans_files(FOLDER):
    for folder in FOLDER:
        files = os.listdir(folder)
        gyro_path = folder+"\\"+folder+"_GYRO"
        exist_fol = os.path.exists(gyro_path)
        if not exist_fol:
            os.makedirs(gyro_path)
        i = 0
        files.sort()
        print(files)
        for f in files:
            if not f.endswith('.txt'):
                continue
            in_path = folder + '\\' + f
            print(files.index(f))
            out_path = gyro_path+"\\"+data_info[i]
            extract_gyro(in_path, out_path)
            i = i+1


if __name__ == "__main__":
    trans_files(INFOLDER)
