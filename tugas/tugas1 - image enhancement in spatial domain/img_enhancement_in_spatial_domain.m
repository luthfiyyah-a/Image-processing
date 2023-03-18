% Tugas 1 - Image Enhancement in spatial domain
% Pengolahan Citra Digital
% 20 Februari 2023
% Luthfiyyah hanifah amari (5025201090_
% Selfira Ayu

% membaca gambar
I = imread('xray.jpg');
figure('Name', 'Gambar Asli')
imshow(I)
title('X-ray Asli')


% HISTOGRAM
% memproses gambar menggunakan histogram
I_hist = histeq(I);
figure('Name', 'Histogram Equalization')
imshow(I_hist)
title('X-ray setelah histogram equalization')
% menyimpan gambar hasil proses histogram
imwrite(I_hist, 'xray_hist.jpg');

% PROSES NEGATIF
% memproses gambar dengan proses negatif
L = 255;
% L adalah nilai tertinggi. dalam hal ini, kita memakai 255 (karena
% grayscale)
I_neg = L - I;
figure('Name', 'Proses negatif')
imshow(I_neg)
% menyimpan gambar hasil proses
imwrite(I_neg, 'xray_neg.jpg');

% ADJUST: CLIPPING
I_clipped = imadjust(I, [0.2 0.8]);
figure('Name', 'Adjust: CLIPPING')
imshow(I_clipped)
% menyimpan gambar hasil proses
imwrite(I_clipped, 'xray_clip.jpg');
% clipping ke 2 ini sebagai contoh perbandingan
I_clipped2 = imadjust(I, [0.4 0.6]);
figure('Name', 'Adjust: CLIPPING-2')
imshow(I_clipped2)
imwrite(I_clipped2, 'xray_clip2.jpg');