% 원본 데이터의 샘플링 주파수와 목표 샘플링 주파수 설정
original_fs = 250;  % 원본 데이터의 샘플링 주파수
target_fs = 512;    % 목표 샘플링 주파수

% 원본 데이터 추출
original_data = EEG_1.EEG.data;

% 데이터 크기 계산
[num_channels, num_samples] = size(original_data);

% 원본 데이터와 목표 샘플링 주파수를 사용하여 샘플링 비율 계산
resample_ratio = target_fs / original_fs;

% 변경된 데이터의 크기 계산
num_upsampled_samples = round(num_samples * resample_ratio);

% 변경된 데이터 생성
upsampled_data = zeros(num_channels, num_upsampled_samples, 'single');
for ch = 1:num_channels
    upsampled_data(ch, :) = interp1(1:num_samples, original_data(ch, :), linspace(1, num_samples, num_upsampled_samples), 'linear');
end

% 시간 축 생성
original_time = (0:num_samples-1) / original_fs;
upsampled_time = (0:num_upsampled_samples-1) / target_fs;

% 원본 데이터와 변경된 데이터 비교 플롯
figure;
subplot(2, 1, 1);
plot(original_time, original_data(1, :));
title('Original Data');
xlabel('Time (s)');
ylabel('Amplitude');
subplot(2, 1, 2);
plot(upsampled_time, upsampled_data(1, :));
title('Upsampled Data');
xlabel('Time (s)');
ylabel('Amplitude');