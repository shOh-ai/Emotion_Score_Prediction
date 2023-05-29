% EEG_downsample 폴더 경로
folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/EEG_downsample';

% EEG_downsample 폴더 내부의 .mat 파일 목록 가져오기
mat_files = dir(fullfile(folder_path, '*.mat'));

for file_idx = 1:numel(mat_files)
    % .mat 파일 경로
    mat_file_path = fullfile(folder_path, mat_files(file_idx).name);
    
    % .mat 파일 로드
    EEG = load(mat_file_path);

    % 데이터 자를 기준이 되는 event 필드의 2열 1행부터 20행까지의 값을 추출
    event_data = EEG.EEG.event;
    if size(event_data, 1) < 20
        disp(['Event data does not satisfy the required format for file ' num2str(file_idx) '. Skipping to the next file.'])
        continue;
    end
    event_values = event_data{1:20, 2};

    % Segment 데이터를 저장할 새로운 .mat 파일 경로 생성
    [~, mat_file_name] = fileparts(mat_files(file_idx).name);
    output_file_name = mat_file_name(end-2:end);
    output_file_path = fullfile('/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/EEG', [output_file_name '.mat']);
    
    output_data = struct();

    % EEG.EEG.data를 배열로 변환 (만약 이미 배열 형태라면 생략 가능)
    data_array = EEG.EEG.data;

    for i = 1:numel(event_values) - 1
        start_idx = int64(event_values(i));
        end_idx = int64(event_values(i + 1)) - 1;

        % 각 구간의 데이터 추출
        segment_data = data_array(:, start_idx:end_idx);

        % 필드 이름 생성 및 데이터 저장
        field_name = sprintf('Segment_%d', i);
        output_data.(field_name) = segment_data;
    end

    % .mat 파일에 데이터 저장
    save(output_file_path, '-struct', 'output_data');
    
    disp(['File ' num2str(file_idx) ' processed.'])
end