% 폴더 경로
folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/EEG';

% 폴더 내부의 .mat 파일 목록 가져오기
mat_files = dir(fullfile(folder_path, '*.mat'));

for file_idx = 1:numel(mat_files)
    % .mat 파일 경로
    mat_file_path = fullfile(folder_path, mat_files(file_idx).name);
    
    % .mat 파일 로드
    loaded_data = load(mat_file_path);

    % 필요한 필드만 유지
    fields_to_keep = {'Segment_3', 'Segment_6', 'Segment_9', 'Segment_12', 'Segment_15', 'Segment_18'};
    fields_to_delete = setdiff(fieldnames(loaded_data), fields_to_keep);
    loaded_data = rmfield(loaded_data, fields_to_delete);

    % .mat 파일 덮어쓰기
    save(mat_file_path, '-struct', 'loaded_data');
    
    disp(['Processed file ' num2str(file_idx) ' of ' num2str(numel(mat_files))])
end
