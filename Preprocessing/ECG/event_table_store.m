bin_folder_path = '/Users/sh_oh/Library/CloudStorage/Dropbox/Data/2023-1/BDP/ECSMP_Dataset/ECG_experiment';  % .bin 파일이 있는 폴더 경로

sub_folders = dir(bin_folder_path);  % 하위 폴더 목록 가져오기

for i = 1:numel(sub_folders)
    sub_folder = sub_folders(i).name;
    
    % 현재 폴더가 상위 폴더 '.' 또는 '..'인 경우 제외
    if strcmp(sub_folder, '.') || strcmp(sub_folder, '..')
        continue;
    end
    
    % 하위 폴더 경로 생성
    sub_folder_path = fullfile(bin_folder_path, sub_folder);
    
    % CSV 파일 경로 생성
    csv_file_path = fullfile(sub_folder_path, strcat(sub_folder, '.csv'));
    
    % CSV 파일이 존재하는지 확인
    if exist(csv_file_path, 'file') == 2
        % .bin 파일 목록 가져오기
        bin_files = dir(fullfile(sub_folder_path, '*.bin'));
        
        % .bin 파일이 존재하는지 확인
        if numel(bin_files) == 1
            % .bin 파일 경로 생성
            bin_file_path = fullfile(sub_folder_path, bin_files(1).name);
            
            % CSV 파일 읽기
            csv_data = readtable(csv_file_path);
            
            % 데이터 추출
            data = csv_data{2:21, 2};
            
            % .bin 파일에 데이터 저장
            try
                save(bin_file_path, 'data', '-append');
                disp(['Data saved for ' sub_folder]);
            catch ME
                disp(['Error saving data for ' sub_folder]);
            end
        else
            disp(['No .bin file found for ' sub_folder]);
        end
    else
        disp(['CSV file not found for ' sub_folder]);
    end
end
