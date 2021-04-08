path_list = dir('*.txt');   %组合成一个完整的绝对路径，这里会定义顺序
file_num = length(path_list);          %找出文件夹内有多少个文件
fprintf('%d\n',file_num)
if file_num > 0
    for j = 1:file_num
        file=path_list(j).name;
        fft_plot(file, 200);
        close all;
        plot_spectrums(file,200);
        close all;
    end
end
