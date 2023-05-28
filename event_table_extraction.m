save_folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/Event_marker';  % 저장할 폴더 경로

mat_files = dir('EEG_downsample/*.mat');  % .mat 파일 목록 가져오기

for i = 1:numel(mat_files)
    mat_file = mat_files(i).name;
    file_name = erase(mat_file, '.mat');  % 파일 이름에서 '.mat' 제거
    save_name = file_name(end-2:end);  % 뒤에서부터 3글자 가져오기
    
    save_path = fullfile(save_folder_path, strcat(save_name, '.csv'));
    
    mat_data = load(fullfile('EEG_downsample', mat_file));  % .mat 파일 읽기
    event_table = mat_data.EEG.event;  % 필드에서 table 가져오기
    values = event_table(:, 2);  % 모든 값 추출
    
    % 값이 20개 이상인 경우에만 저장
    if size(values, 1) >= 20
        % 추출한 값을 CSV 파일로 저장
        writetable(values(1:20, :), save_path);
    end
end