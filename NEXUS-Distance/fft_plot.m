function fft_plot(to_plot, Fs)
    [~, samples] = read_samples_file(to_plot);
    N = length(samples);
    df = Fs/N;
    f = -Fs/2:df:Fs/2-df;
    Y = fftshift(abs(fft(samples)));
    figure(1);
    name=[to_plot(1:end-4),'all'];
    subplot(121);
    plot(f, Y);
    title(name);
    subplot(122);
    nfft = 128;
    spectrogram(samples(:,2), hanning(nfft), round(nfft*0.9), nfft, Fs);
    title(name);
    %saveas(figure(1),[name,'-fft'],'jpg');
    f = gcf;
    exportgraphics(f,strcat(name,'.jpg'),'Resolution',600)
end
