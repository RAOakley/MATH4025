coin_types = {'ETH','XRP','BCH','LTC','EOS','ADA','NEO','XLM','BCD','VEN','IOT','XMR','TRX','DASH','XEM','ETC','QTUM','BNB','LSK','MAID','SC','STORJ'};
json_types = {'_recent.json','_popular.json','_mixed.json'};
json_type_to_use = 3;

for i = 1:length(coin_types)
    for j = 1:length(json_types)
        temp_file_identifier = fopen(['../twitter_data/',coin_types{i},json_types{j}],'r');
        temp_text_data = fscanf(temp_file_identifier,'%c');
        temp_json = jsondecode(temp_text_data); %jsons{i}{j}
        for k = 1:length(temp_json.statuses)
            temp_status = temp_json.statuses{k,1};
            temp_datetime = datetime(temp_status.created_at,...
                'inputFormat','eee MMM d H:mm:ss xxxx yyyy',...
                'TimeZone','UTC');
            temp_unixtime = posixtime(temp_datetime);
            temp_followers = temp_status.user.followers_count;
            
            %tweets{i}{j}[k,1] = temp_unixtime;
            %tweets{i}{j}[k,2] = temp_followers;            
        end
    end
end

for i=1:length(coin_types)
    price_data{i} = csvread(['../cryptocompare_data/', coin_types{i}, '.csv']);
    
    
end

