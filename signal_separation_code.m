filepath = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/ECG_experiment/폴더이름';

bin_files = dir(fullfile(filepath, '*.bin')); % 폴더 내의 모든 .bin 파일 가져오기

filename = {bin_files.name}; % 파일 이름 추출

disp(filename);

[start_time, stop_time, fs, ECG] = readbindata(filepath, filename{1});

last_chars = filepath(end-2:end);

% CSV 파일 경로 설정
csv_file_path = fullfile(filepath, [last_chars '.csv']);

% CSV 파일 읽기
csv_data = readtable(csv_file_path);

% event 필드 초기화
event = zeros(21, 1);

% 2열 2행부터 21행까지의 값을 event 필드에 저장
event(2:21) = csv_data{1:20, 2};

bin_file_path = fullfile(filepath, filename{1}); % .bin 파일의 경로 생성

% event 필드에서 1행부터 21행까지의 값 가져오기
event_values = event(1:21);

% 데이터 저장을 위한 셀 배열 초기화
segmented_data = cell(21, 1);

% 수직선 사이의 데이터 끊어서 저장
for i = 1:numel(event_values)-1
    start_idx = round(event_values(i));  % 현재 수직선까지
    end_idx = round(event_values(i+1));  % 다음 수직선까지
    segmented_data{i} = ECG(start_idx+1:end_idx);
end

% 데이터 저장을 위한 변수 초기화
selected_data = struct();

% 수직선 사이의 데이터 추출 및 저장
selected_indices = [4, 7, 10, 13, 16, 19];
for i = 1:numel(selected_indices)
    start_idx = selected_indices(i);
    segment_data = segmented_data{start_idx};
    field_name = sprintf('Segment%d', i);
    selected_data.(field_name) = segment_data;
end

% 새로운 .mat 파일에 데이터 저장
output_file_path = fullfile(filepath,  'selected_data.mat');

try
    save(output_file_path, '-struct', 'selected_data');
    disp('Segmented data saved to .mat file.');
catch ME
    disp('Error saving segmented data to .mat file.');
end;