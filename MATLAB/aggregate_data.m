coin_types = {'ETH','XRP','BCH','LTC','EOS','ADA','NEO','XLM','BCD','VEN','IOT','XMR','TRX','DASH','XEM','ETC','QTUM','BNB','LSK','MAID','SC','STORJ'};
json_types = {'_recent.json','_popular.json','_mixed.json'};
json_type_to_use = 3;


% make sure to run the predict function over the JSONS first, so they have
% a sentiment field
if true
    for i = 1:length(coin_types)
        for j = 1:length(json_types)
            temp_file_identifier = fopen(['../twitter_data/',coin_types{i},json_types{j}],'r');
            temp_text_data = fscanf(temp_file_identifier,'%c');
            temp_json = jsondecode(temp_text_data); %jsons{i}{j}
            for k = 1:length(temp_json.statuses)
                try
                    temp_status = temp_json.statuses{k};
                catch e
                    temp_status = temp_json.statuses(k);
                end

                temp_datetime = datetime(temp_status.created_at,...
                    'inputFormat','eee MMM d H:mm:ss xxxx yyyy',...
                    'TimeZone','UTC');
                temp_unixtime = posixtime(temp_datetime);
                temp_followers = temp_status.user.followers_count;

                temp_sent = temp_status.sentiment;

                temp_id = temp_status.id_str;

                tweets{i}{j}{k,1} = temp_unixtime;
                tweets{i}{j}{k,2} = temp_followers;
                tweets{i}{j}{k,3} = temp_sent;
                tweets{i}{j}{k,4} = temp_id;
            end
            tweets{i}{j} = sortrows(tweets{i}{j}, 1);
        end
    end
end

for i=1:length(coin_types)
    price_data{i} = csvread(['../cryptocompare_data/', coin_types{i}, '.csv']);
    price_data{i} = transpose(sortrows(transpose(price_data{i}), 1));
    min_time = min(price_data{i}(1,:));
    k = 1;
    search_type = 3;
    error_acc = 0;
    error = [];
    
    temp_k = size(tweets{i}{search_type});
    max_k = temp_k(1);
    for j = 1:length(price_data{i})
        temp_tweets = 0;
        temp_followers = 0;
        temp_weighted_sent = 0;
        while(k <= max_k && tweets{i}{search_type}{k,1} <= price_data{i}(1,j))
            if(tweets{i}{search_type}{k,1} > price_data{i}(1,j) - 60)
                temp_followers = temp_followers + tweets{i}{search_type}{k,2};
                temp_tweets = temp_tweets + 1;
                temp_weighted_sent = temp_weighted_sent + tweets{i}{search_type}{k,2} *  tweets{i}{search_type}{k,3};
            else
                error_acc = error_acc + 1;
            end              
            k = k + 1;
        end
        price_data{i}(5,j) = temp_tweets;
        price_data{i}(6,j) = temp_followers;
        price_data{i}(7,j) = temp_weighted_sent;
    end
    error(i) = error_acc;
end

XS = price_data{1}(3,:);
YS = price_data{1}(2,:);
testx = price_data{3}(3:7,:);
testy = price_data{3}(2,:);

% for i = 2:length(price_data{1}(2,:))
%     YS(i) = sign(price_data{1}(2,i) - price_data{1}(2,i-1));
% end
% YS(1) = 0;